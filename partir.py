# partir.py
# Parte cada markdown de teoria en temas y genera un INDICE.md por carpeta.
import re
import pathlib

BASE = pathlib.Path("context/teoria")


def partir(carpeta: pathlib.Path) -> None:
    fuente = carpeta / f"{carpeta.name}.md"
    if not fuente.exists():
        return

    texto = fuente.read_text(encoding="utf-8")
    partes = re.split(r"^(#{1,2} .+)$", texto, flags=re.M)

    temas = carpeta / "temas"
    temas.mkdir(exist_ok=True)

    indice = [f"# Indice — {carpeta.name}\n"]
    for i in range(1, len(partes), 2):
        titulo = re.sub(r"\*+", "", partes[i]).lstrip("#").strip()
        slug = re.sub(r"[^a-z0-9]+", "-", titulo.lower()).strip("-")[:40]
        nombre = f"{i // 2 + 1:02d}-{slug}.md"
        cuerpo = partes[i] + partes[i + 1]
        # los temas viven un nivel mas abajo que imagenes/
        cuerpo = cuerpo.replace("](imagenes/", "](../imagenes/")
        (temas / nombre).write_text(cuerpo, encoding="utf-8")
        indice.append(f"- `temas/{nombre}` — {titulo}")

    (carpeta / "INDICE.md").write_text("\n".join(indice) + "\n", encoding="utf-8")
    print(f"{carpeta.name}: {(len(partes) - 1) // 2} temas -> {temas}")


if __name__ == "__main__":
    for carpeta in sorted(BASE.iterdir()):
        if carpeta.is_dir():
            partir(carpeta)
