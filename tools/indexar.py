#!/usr/bin/env python3
"""
Regenera el INDICE.md de una carpeta de teoria con senal suficiente para que
Claude pueda rutear sin abrir los archivos.

Todo se extrae localmente del propio markdown: cero llamadas a un modelo,
cero tokens. Corre en menos de un segundo sobre cientos de archivos.

Agrega respecto de un indice de solo titulos:
  - resumen  : primera oracion util del archivo
  - terminos : conceptos detectados (negritas, subtitulos, codigo inline)
  - tamano   : lineas, para decidir si conviene abrirlo entero
  - mapa de conceptos: indice invertido concepto -> archivos

Uso:
    python tools/indexar.py context/teoria/u1
    python tools/indexar.py context/teoria/*          # todas las unidades
"""

from __future__ import annotations

import glob
import os
import re
import sys
from collections import Counter, defaultdict

# Palabras que aparecen en negrita pero no son conceptos de la materia.
STOP = {
    "nota", "importante", "ojo", "atencion", "atención", "ejemplo", "ejercicio",
    "definicion", "definición", "observacion", "observación", "esto", "esta",
    "este", "no", "si", "sí", "pero", "ver", "cuidado", "resumen", "aclaracion",
    "aclaración", "recordar", "clave", "idea",
}

MAX_TERMINOS = 6
MAX_RESUMEN = 110


def _slug_a_titulo(nombre: str) -> str:
    base = re.sub(r"^\d+[-_]", "", nombre.removesuffix(".md"))
    return base.replace("-", " ").replace("_", " ").strip().capitalize()


def _normalizar(t: str) -> str:
    return re.sub(r"\s+", " ", t).strip(" .,:;·-–—")


# Descarta expresiones de codigo: son ruido como "concepto".
_CODIGO = re.compile(r"[=(){}\[\]<>|]|->|::|\+\+|\d\s*[*+/-]")


def _es_concepto(t: str) -> bool:
    if _CODIGO.search(t):
        return False
    if t.lower() in STOP or t.isdigit():
        return False
    if not (2 < len(t) < 40):
        return False
    if not re.fullmatch(r"[\w áéíóúüñÁÉÍÓÚÜÑ.'’-]+", t):
        return False
    palabras = t.split()
    if any(p.isdigit() for p in palabras):          # "f 3", "3 2"
        return False
    # al menos una palabra de 3+ letras
    return any(len(p) >= 3 and p.isalpha() for p in palabras)


def analizar(path: str) -> dict:
    with open(path, encoding="utf-8") as f:
        lineas = f.read().splitlines()

    titulo = ""
    resumen = ""
    subtitulos: list[str] = []
    en_codigo = False

    for l in lineas:
        s = l.strip()
        if s.startswith("```"):
            en_codigo = not en_codigo
            continue
        if en_codigo:
            continue
        if s.startswith("# ") and not titulo:
            titulo = s[2:].strip()
        elif re.match(r"^#{2,4} ", s):
            subtitulos.append(re.sub(r"^#+\s*", "", s))
        elif s and not s.startswith(("#", ">", "|", "-", "*", "!", "    ")) and not resumen:
            resumen = s

    texto = "\n".join(lineas)
    # conceptos: negritas, codigo inline y subtitulos cortos
    crudos = re.findall(r"\*\*(.+?)\*\*", texto)
    crudos += re.findall(r"`([^`\n]{2,28})`", texto)
    crudos += [s for s in subtitulos if len(s) < 40]

    conteo: Counter[str] = Counter()
    vistos: dict[str, str] = {}          # clave normalizada -> forma a mostrar
    for c in crudos:
        n = _normalizar(re.sub(r"[*_`]", "", c))
        if not _es_concepto(n):
            continue
        clave = n.lower()
        vistos.setdefault(clave, n)
        conteo[clave] += 1

    # descartar terminos que son subcadena de otro mas especifico
    ordenados = [vistos[t] for t, _ in conteo.most_common(MAX_TERMINOS * 2)]
    terminos: list[str] = []
    for t in ordenados:
        tl = t.lower()
        if any(tl != o.lower() and tl in o.lower() for o in ordenados):
            continue
        terminos.append(t)
        if len(terminos) == MAX_TERMINOS:
            break

    resumen = re.sub(r"[*_`]", "", resumen)
    resumen = re.sub(r"\[(.+?)\]\(.+?\)", r"\1", resumen)
    if len(resumen) > MAX_RESUMEN:
        corte = resumen[:MAX_RESUMEN].rsplit(" ", 1)[0]
        resumen = corte + "…"

    return {
        "archivo": os.path.basename(path),
        "titulo": titulo or _slug_a_titulo(os.path.basename(path)),
        "resumen": resumen,
        "terminos": terminos,
        "subtitulos": subtitulos,
        "lineas": len(lineas),
    }


def _desambiguar(entradas: list[dict]) -> None:
    """Titulos repetidos (ej. 08 y 09 'Igualdades por definicion') pasan a
    'Titulo (1/2)' + el subtitulo mas informativo, para que se distingan."""
    grupos: dict[str, list[dict]] = defaultdict(list)
    for e in entradas:
        grupos[e["titulo"].lower()].append(e)
    for grupo in grupos.values():
        if len(grupo) < 2:
            continue
        for i, e in enumerate(grupo, 1):
            detalle = e["subtitulos"][0] if e["subtitulos"] else (e["terminos"][0] if e["terminos"] else "")
            sufijo = f" ({i}/{len(grupo)}" + (f": {detalle}" if detalle else "") + ")"
            e["titulo"] += sufijo


def generar(carpeta: str) -> str:
    temas_dir = os.path.join(carpeta, "temas")
    if not os.path.isdir(temas_dir):
        raise SystemExit(f"no existe {temas_dir}")

    archivos = sorted(glob.glob(os.path.join(temas_dir, "*.md")))
    entradas = [analizar(p) for p in archivos]
    _desambiguar(entradas)

    unidad = os.path.basename(os.path.abspath(carpeta))
    total = sum(e["lineas"] for e in entradas)

    out = [
        f"# Índice — {unidad}",
        "",
        f"{len(entradas)} archivos · {total} líneas en total.",
        "",
        "> Generado por `tools/indexar.py`. No editar a mano: se regenera.",
        "> Para buscar un término literal es más barato `grep -rl \"término\" temas/`",
        "> que leer este índice. Este índice sirve para lo que grep no encuentra.",
        "",
        "| Archivo | Tema | De qué trata | Conceptos | Líneas |",
        "|---|---|---|---|---|",
    ]

    for e in entradas:
        terminos = ", ".join(f"`{t}`" for t in e["terminos"]) or "—"
        resumen = e["resumen"].replace("|", "\\|") or "—"
        out.append(
            f"| `{e['archivo']}` | {e['titulo']} | {resumen} | {terminos} | {e['lineas']} |"
        )

    # indice invertido
    invertido: dict[str, list[str]] = defaultdict(list)
    for e in entradas:
        for t in e["terminos"]:
            invertido[t].append(e["archivo"])

    out += ["", "## Mapa de conceptos", "",
            "Concepto → archivos donde aparece definido o usado.", ""]
    for concepto in sorted(invertido):
        refs = ", ".join(f"`{a}`" for a in invertido[concepto])
        out.append(f"- **{concepto}** → {refs}")

    contenido = "\n".join(out) + "\n"
    destino = os.path.join(carpeta, "INDICE.md")
    with open(destino, "w", encoding="utf-8") as f:
        f.write(contenido)
    print(f"OK -> {destino}  ({len(entradas)} archivos, {len(invertido)} conceptos)")
    return destino


if __name__ == "__main__":
    objetivos = sys.argv[1:] or ["."]
    for o in objetivos:
        if os.path.isdir(os.path.join(o, "temas")):
            generar(o)
        else:
            for sub in sorted(glob.glob(os.path.join(o, "*"))):
                if os.path.isdir(os.path.join(sub, "temas")):
                    generar(sub)