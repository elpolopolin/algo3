# extraer.py
# Pipeline PDF -> markdown.
#
#   teoria   : pdf -> context/teoria/<unidad>/<unidad>.md -> temas/ -> INDICE.md
#   practica : pdf -> context/practica/context/<nombre>.md  (sin partir, sin indice)
#
# Uso:
#   uv run --with pymupdf4llm python extraer.py            # solo lo que falta
#   uv run --with pymupdf4llm python extraer.py --force    # rehace todo
#   uv run --with pymupdf4llm python extraer.py intro      # solo lo que matchea

import pathlib
import re
import subprocess
import sys

import pymupdf4llm

from partir import partir

DPI = 150

# pdf -> carpeta de la unidad. El .md se llama igual que la carpeta.
TEORIA = {
    "context/teoria/pdfs/teo01-demostraciones.pdf": "context/teoria/demostraciones",
    "context/teoria/pdfs/teo2-intro-grafos.pdf": "context/teoria/intro-grafos",
    "context/teoria/pdfs/Graph Algorithms-03.pdf": "context/teoria/grafos-algoritmos-03",
    "context/teoria/pdfs/teo04-Divide_and_Conquer.pdf": "context/teoria/divide-and-conquer",
}

# pdf -> nombre del .md de salida en context/practica/context/
PRACTICA = {
    "context/practica/pdfs/practica_1_repaso.pdf": "practica_1.md",
    "context/practica/pdfs/practica_2_intro_grafos.pdf": "practica_2.md",
    "context/practica/pdfs/practica_3_algoritmos_grafos.pdf": "practica_3.md",
    "context/practica/pdfs/practica_4_divide_and_conquer.pdf": "practica_4.md",
}

PRACTICA_OUT = pathlib.Path("context/practica/context")
PRACTICA_IMG = pathlib.Path("context/practica/imagenes")


def _extraer(pdf: pathlib.Path, imagenes: pathlib.Path, prefijo: str) -> str:
    """Pasa el pdf a markdown y deja los links de imagen relativos al .md destino."""
    imagenes.mkdir(parents=True, exist_ok=True)
    md = pymupdf4llm.to_markdown(
        str(pdf),
        write_images=True,
        image_path=str(imagenes),
        image_format="png",
        dpi=DPI,
    )
    # pymupdf4llm escribe la ruta tal cual se la pasamos; la recortamos al prefijo
    return re.sub(r"\]\(\S*?/?imagenes/", f"]({prefijo}", md)


def hacer_teoria(pdf: pathlib.Path, carpeta: pathlib.Path, force: bool) -> None:
    destino = carpeta / f"{carpeta.name}.md"
    if destino.exists() and not force:
        print(f"skip  {destino}  (ya existe, --force para rehacer)")
        return

    md = _extraer(pdf, carpeta / "imagenes", "imagenes/")
    carpeta.mkdir(parents=True, exist_ok=True)
    destino.write_text(md, encoding="utf-8")
    print(f"OK -> {destino}  ({len(md.splitlines())} lineas)")

    partir(carpeta)  # temas/ + INDICE.md plano
    # el indice util (resumen, conceptos, lineas, mapa invertido) lo hace indexar.py
    subprocess.run([sys.executable, "tools/indexar.py", str(carpeta)], check=True)


def hacer_practica(pdf: pathlib.Path, nombre: str, force: bool) -> None:
    destino = PRACTICA_OUT / nombre
    if destino.exists() and not force:
        print(f"skip  {destino}  (ya existe, --force para rehacer)")
        return

    md = _extraer(pdf, PRACTICA_IMG, "../imagenes/")
    PRACTICA_OUT.mkdir(parents=True, exist_ok=True)
    destino.write_text(md, encoding="utf-8")
    print(f"OK -> {destino}  ({len(md.splitlines())} lineas)")


def main() -> None:
    args = sys.argv[1:]
    force = "--force" in args
    filtros = [a for a in args if not a.startswith("-")]

    def pasa(ruta: str) -> bool:
        return not filtros or any(f.lower() in ruta.lower() for f in filtros)

    for pdf, carpeta in TEORIA.items():
        if not pasa(pdf) and not pasa(carpeta):
            continue
        ruta = pathlib.Path(pdf)
        if not ruta.exists():
            print(f"FALTA {ruta}")
            continue
        hacer_teoria(ruta, pathlib.Path(carpeta), force)

    for pdf, nombre in PRACTICA.items():
        if not pasa(pdf) and not pasa(nombre):
            continue
        ruta = pathlib.Path(pdf)
        if not ruta.exists():
            print(f"FALTA {ruta}")
            continue
        hacer_practica(ruta, nombre, force)


if __name__ == "__main__":
    main()
