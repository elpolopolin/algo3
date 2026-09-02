#!/usr/bin/env python3
"""
Helper para generar diagramas explicativos en SVG.
Sin dependencias: solo stdlib. El objetivo es que un diagrama se describa
en 8-15 lineas de Python en vez de 200 lineas de SVG a mano.

El modulo calcula solo: tamano de cajas, anclaje de flechas al borde
correcto, curvatura, posicion de etiquetas. Vos solo decis QUE conectar.

Uso minimo:

    from diagrama import Diagrama

    d = Diagrama(760, 360, titulo="Ciclo de instruccion")
    d.fila(y=120, ids=["fetch", "decode", "execute"],
           textos=["Fetch", "Decode", "Execute"])
    d.flecha("fetch", "decode")
    d.flecha("decode", "execute")
    d.flecha("execute", "fetch", curva=-0.5, etiqueta="siguiente")
    d.puntero("decode", "aca se lee el opcode", lado="abajo")
    d.guardar("imagenes/ciclo.svg")
"""

from __future__ import annotations

import math
import os
from dataclasses import dataclass, field

# --- estilo -----------------------------------------------------------------

PALETA = {
    "azul":     ("#dbeafe", "#2563eb"),
    "verde":    ("#dcfce7", "#16a34a"),
    "amarillo": ("#fef3c7", "#d97706"),
    "rojo":     ("#fee2e2", "#dc2626"),
    "violeta":  ("#ede9fe", "#7c3aed"),
    "gris":     ("#f1f5f9", "#475569"),
}

FUENTE = "ui-sans-serif, system-ui, 'Segoe UI', Roboto, sans-serif"
CHAR_W = 7.4          # ancho aprox. de caracter a 13px
LINE_H = 17


def _mid(color: str) -> str:
    """Id de marker determinista a partir del color."""
    return "p" + "".join(ch for ch in color if ch.isalnum())


def _esc(t: str) -> str:
    return (str(t).replace("&", "&amp;").replace("<", "&lt;")
            .replace(">", "&gt;").replace('"', "&quot;"))


def _wrap(texto: str, max_chars: int) -> list[str]:
    lineas, actual = [], ""
    for palabra in str(texto).split():
        if actual and len(actual) + 1 + len(palabra) > max_chars:
            lineas.append(actual)
            actual = palabra
        else:
            actual = f"{actual} {palabra}".strip()
    if actual:
        lineas.append(actual)
    return lineas or [""]


# --- primitivas -------------------------------------------------------------

@dataclass
class Caja:
    id: str
    x: float
    y: float
    w: float
    h: float
    lineas: list[str]
    color: str = "azul"
    forma: str = "rect"       # rect | redonda | rombo
    negrita: bool = False

    @property
    def centro(self) -> tuple[float, float]:
        return (self.x + self.w / 2, self.y + self.h / 2)

    def borde(self, hacia: tuple[float, float]) -> tuple[float, float]:
        """Punto del borde en direccion a `hacia`."""
        cx, cy = self.centro
        dx, dy = hacia[0] - cx, hacia[1] - cy
        if dx == 0 and dy == 0:
            return cx, cy
        sx = (self.w / 2) / abs(dx) if dx else math.inf
        sy = (self.h / 2) / abs(dy) if dy else math.inf
        s = min(sx, sy)
        return cx + dx * s, cy + dy * s

    def ancla(self, lado: str) -> tuple[float, float]:
        cx, cy = self.centro
        return {
            "arriba":  (cx, self.y),
            "abajo":   (cx, self.y + self.h),
            "izq":     (self.x, cy),
            "der":     (self.x + self.w, cy),
        }[lado]


# --- diagrama ---------------------------------------------------------------

class Diagrama:
    def __init__(self, ancho: int = 760, alto: int = 420, titulo: str = ""):
        self.ancho = ancho
        self.alto = alto
        self.titulo = titulo
        self.cajas: dict[str, Caja] = {}
        self._capas: list[str] = []      # se dibuja despues de las cajas
        self._colores: set[str] = set()

    # -- colocacion ----------------------------------------------------------

    def caja(self, id: str, x: float, y: float, texto: str,
             color: str = "azul", ancho: float | None = None,
             forma: str = "rect", negrita: bool = False,
             max_chars: int = 22) -> Caja:
        lineas = _wrap(texto, max_chars)
        w = ancho or max(90, max(len(l) for l in lineas) * CHAR_W + 28)
        h = max(46, len(lineas) * LINE_H + 22)
        c = Caja(id, x, y, w, h, lineas, color, forma, negrita)
        self.cajas[id] = c
        return c

    def fila(self, y: float, ids: list[str], textos: list[str],
             color: str | list[str] = "azul", margen: float = 40,
             ancho: float | None = None) -> None:
        """Distribuye cajas horizontalmente, centradas y equiespaciadas."""
        colores = color if isinstance(color, list) else [color] * len(ids)
        tmp = [self.caja(i, 0, y, t, c, ancho)
               for i, t, c in zip(ids, textos, colores)]
        total = sum(c.w for c in tmp) + margen * (len(tmp) - 1)
        x = (self.ancho - total) / 2
        for c in tmp:
            c.x = x
            x += c.w + margen

    def columna(self, x: float, ids: list[str], textos: list[str],
                y0: float = 60, color: str | list[str] = "azul",
                margen: float = 34, ancho: float | None = None) -> None:
        colores = color if isinstance(color, list) else [color] * len(ids)
        y = y0
        for i, t, c in zip(ids, textos, colores):
            caja = self.caja(i, 0, y, t, c, ancho)
            caja.x = x - caja.w / 2
            y += caja.h + margen

    # -- conexiones ----------------------------------------------------------

    def flecha(self, desde, hasta, etiqueta: str = "", curva: float = 0.0,
               punteada: bool = False, color: str = "#334155",
               lado_desde: str | None = None, lado_hasta: str | None = None):
        """Conecta dos cajas (por id) o dos puntos (x, y).

        curva: 0 = recta. Positivo curva hacia un lado, negativo hacia el otro.
        """
        c1, c2 = self._centro(desde), self._centro(hasta)
        ctrl = None
        if curva:
            ctrl = self._control(c1, c2, curva)
            p1 = self._punto(desde, ctrl, lado_desde)
            p2 = self._punto(hasta, ctrl, lado_hasta)
        else:
            p1 = self._punto(desde, c2, lado_desde)
            p2 = self._punto(hasta, c1, lado_hasta)
        self._trazo(p1, p2, etiqueta, ctrl, punteada, color, 2.0)

    def puntero(self, hacia, texto: str, lado: str = "arriba",
                largo: float = 52, color: str = "#b45309"):
        """Flechita punteada con cartelito que senala una caja.

        lado: arriba | abajo | izq | der
        """
        obj = self.cajas[hacia] if isinstance(hacia, str) else None
        destino = obj.ancla(lado) if obj else hacia
        dx, dy = {"arriba": (0, -1), "abajo": (0, 1),
                  "izq": (-1, 0), "der": (1, 0)}[lado]
        origen = (destino[0] + dx * largo, destino[1] + dy * largo)
        self._trazo(origen, destino, "", None, True, color, 1.6)

        anchor = {"izq": "end", "der": "start"}.get(lado, "middle")
        ty = origen[1] + (-6 if lado == "arriba" else 16 if lado == "abajo" else 4)
        tx = origen[0] + (-6 if lado == "izq" else 6 if lado == "der" else 0)
        self._capas.append(
            f'<text x="{tx:.0f}" y="{ty:.0f}" text-anchor="{anchor}" '
            f'font-size="12.5" font-style="italic" fill="{color}">'
            f'{_esc(texto)}</text>'
        )

    def nota(self, x: float, y: float, texto: str, ancho_max: int = 46):
        for i, l in enumerate(_wrap(texto, ancho_max)):
            self._capas.append(
                f'<text x="{x:.0f}" y="{y + i * 16:.0f}" font-size="12.5" '
                f'fill="#64748b">{_esc(l)}</text>'
            )

    def llave(self, ids: list[str], texto: str, lado: str = "abajo"):
        """Agrupa varias cajas con una llave y una etiqueta."""
        cs = [self.cajas[i] for i in ids]
        x0 = min(c.x for c in cs) - 8
        x1 = max(c.x + c.w for c in cs) + 8
        if lado == "abajo":
            y = max(c.y + c.h for c in cs) + 14
            d = f"M {x0} {y} L {x0} {y+7} L {x1} {y+7} L {x1} {y}"
            ty = y + 24
        else:
            y = min(c.y for c in cs) - 14
            d = f"M {x0} {y} L {x0} {y-7} L {x1} {y-7} L {x1} {y}"
            ty = y - 14
        self._capas.append(
            f'<path d="{d}" fill="none" stroke="#94a3b8" stroke-width="1.4"/>'
            f'<text x="{(x0+x1)/2:.0f}" y="{ty:.0f}" text-anchor="middle" '
            f'font-size="12.5" fill="#64748b">{_esc(texto)}</text>'
        )

    # -- internos ------------------------------------------------------------

    def _centro(self, obj):
        return self.cajas[obj].centro if isinstance(obj, str) else obj

    @staticmethod
    def _control(c1, c2, curva):
        mx, my = (c1[0] + c2[0]) / 2, (c1[1] + c2[1]) / 2
        dx, dy = c2[0] - c1[0], c2[1] - c1[1]
        largo = math.hypot(dx, dy) or 1
        return (mx - dy / largo * curva * largo * 0.5,
                my + dx / largo * curva * largo * 0.5)

    def _punto(self, obj, ref, lado):
        if isinstance(obj, str):
            caja = self.cajas[obj]
            return caja.ancla(lado) if lado else caja.borde(ref)
        return obj

    def _trazo(self, p1, p2, etiqueta, ctrl, punteada, color, grosor):
        if ctrl:
            cx, cy = ctrl
            d = f"M {p1[0]:.0f} {p1[1]:.0f} Q {cx:.0f} {cy:.0f} {p2[0]:.0f} {p2[1]:.0f}"
            lx, ly = (p1[0] + 2 * cx + p2[0]) / 4, (p1[1] + 2 * cy + p2[1]) / 4
        else:
            d = f"M {p1[0]:.0f} {p1[1]:.0f} L {p2[0]:.0f} {p2[1]:.0f}"
            lx, ly = (p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2

        self._colores.add(color)
        dash = ' stroke-dasharray="6 5"' if punteada else ""
        mid = _mid(color)
        self._capas.append(
            f'<path d="{d}" fill="none" stroke="{color}" '
            f'stroke-width="{grosor}"{dash} marker-end="url(#{mid})"/>'
        )
        if etiqueta:
            w = len(etiqueta) * CHAR_W + 10
            self._capas.append(
                f'<rect x="{lx - w/2:.0f}" y="{ly - 10:.0f}" width="{w:.0f}" '
                f'height="19" rx="4" fill="#ffffff" opacity="0.92"/>'
                f'<text x="{lx:.0f}" y="{ly + 4:.0f}" text-anchor="middle" '
                f'font-size="12.5" fill="#475569">{_esc(etiqueta)}</text>'
            )

    def _svg_cajas(self) -> str:
        out = []
        for c in self.cajas.values():
            relleno, borde = PALETA.get(c.color, PALETA["azul"])
            cx, cy = c.centro
            if c.forma == "rombo":
                pts = (f"{cx},{c.y} {c.x + c.w},{cy} {cx},{c.y + c.h} {c.x},{cy}")
                out.append(f'<polygon points="{pts}" fill="{relleno}" '
                           f'stroke="{borde}" stroke-width="2"/>')
            else:
                rx = c.h / 2 if c.forma == "redonda" else 8
                out.append(
                    f'<rect x="{c.x:.0f}" y="{c.y:.0f}" width="{c.w:.0f}" '
                    f'height="{c.h:.0f}" rx="{rx:.0f}" fill="{relleno}" '
                    f'stroke="{borde}" stroke-width="2"/>'
                )
            y0 = cy - (len(c.lineas) - 1) * LINE_H / 2 + 4
            peso = "600" if c.negrita else "500"
            for i, l in enumerate(c.lineas):
                out.append(
                    f'<text x="{cx:.0f}" y="{y0 + i * LINE_H:.0f}" '
                    f'text-anchor="middle" font-size="13" font-weight="{peso}" '
                    f'fill="#1e293b">{_esc(l)}</text>'
                )
        return "\n".join(out)

    def _markers(self) -> str:
        out = []
        for c in sorted(self._colores):
            mid = _mid(c)
            out.append(
                f'<marker id="{mid}" viewBox="0 0 10 10" refX="9" refY="5" '
                f'markerWidth="6" markerHeight="6" orient="auto">'
                f'<path d="M 0 0 L 10 5 L 0 10 z" fill="{c}"/></marker>'
            )
        return "".join(out)

    def svg(self) -> str:
        titulo = ""
        if self.titulo:
            titulo = (f'<text x="{self.ancho/2:.0f}" y="30" text-anchor="middle" '
                      f'font-size="16" font-weight="600" fill="#0f172a">'
                      f'{_esc(self.titulo)}</text>')
        return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {self.ancho} {self.alto}" width="{self.ancho}" height="{self.alto}" font-family="{FUENTE}">
<defs>{self._markers()}</defs>
<rect width="100%" height="100%" fill="#ffffff"/>
{titulo}
{self._svg_cajas()}
{chr(10).join(self._capas)}
</svg>'''

    def guardar(self, path: str) -> str:
        os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
        with open(path, "w", encoding="utf-8") as f:
            f.write(self.svg())
        print(f"OK -> {path}")
        return path


if __name__ == "__main__":
    d = Diagrama(760, 300, titulo="Ejemplo: ciclo de instruccion")
    d.fila(y=120, ids=["f", "d", "e"],
           textos=["Fetch", "Decode", "Execute"],
           color=["azul", "amarillo", "verde"])
    d.flecha("f", "d")
    d.flecha("d", "e")
    d.flecha("e", "f", curva=-0.55, etiqueta="PC + 1")
    d.puntero("f", "arranca aca", lado="izq")
    d.llave(["f", "d", "e"], "una instruccion completa", lado="arriba")
    d.guardar("imagenes/ejemplo.svg")