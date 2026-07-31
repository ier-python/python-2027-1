"""Pre-render de Quarto: regenera el índice temático de temario.qmd (entre los
marcadores <!-- indice:inicio --> / <!-- indice:fin -->) y temario_completo.md,
leyendo los encabezados de sección de unidades/unidad-0*.qmd. La numeración de
los temas es posicional, igual que la que Quarto asigna al renderizar."""

import glob
import re
from pathlib import Path

unidades = []
for f in sorted(glob.glob("unidades/unidad-0*.qmd")):
    numero = int(re.search(r"unidad-0(\d)", f).group(1))
    src = Path(f).read_text(encoding="utf-8")
    titulo = re.search(r'^title: "(.+?)"$', src, re.M).group(1)
    temas = [t for t in re.findall(r"^## (.+?)\s*$", src, re.M)
             if "{.unnumbered}" not in t]
    unidades.append((numero, titulo, temas, src))

# Temas candidatos a sacrificio para acercar el temario a las 48 h de clase;
# se sombrean en la tabla con la clase .sacrificable (ver estilos.scss).
SACRIFICABLES = {
    "La misma figura, en plotly",
    "Creación de mallas",
    "Importar, guardar y el puente con pandas",
    "Profiling",
    "Numba (y Cython, la anécdota)",
}

# ── Índice temático en temario.qmd ────────────────────────────────────────────
filas = ["| Tema | |", "|:---|:---|"]
for numero, titulo, temas, _ in unidades:
    filas.append(f"| | **Unidad {numero} · {titulo}** |")
    for i, tema in enumerate(temas, 1):
        celda = f"[{tema}]{{.sacrificable}}" if tema in SACRIFICABLES else tema
        filas.append(f"| {numero}.{i} | {celda} |")
tabla = "\n".join(filas)

# la tabla se inserta en cualquier .qmd del proyecto que tenga los marcadores
for pagina in Path(".").rglob("*.qmd"):
    if "_book" in pagina.parts:
        continue
    src = pagina.read_text(encoding="utf-8")
    if "<!-- indice:inicio -->" not in src:
        continue
    nuevo = re.sub(
        r"<!-- indice:inicio -->.*?<!-- indice:fin -->",
        lambda m: "<!-- indice:inicio -->\n" + tabla + "\n<!-- indice:fin -->",
        src,
        flags=re.DOTALL,
    )
    if nuevo != src:
        pagina.write_text(nuevo, encoding="utf-8")

# ── temario_completo.md ───────────────────────────────────────────────────────
partes = ["# Proyectos de ciencia de datos con Python — temario completo\n\n"
          "Semestre 2027-1 · 16 sesiones · 48 horas\n"]
for numero, titulo, temas, src in unidades:
    cuerpo = src.split("---\n", 2)[2]
    cuerpo = re.sub(r"::: \{[^}]*\}\n.*?\n:::\n", "", cuerpo, flags=re.DOTALL)
    cuerpo = re.sub(r"\s*·\s*\[Unidad \d del temario\]\([^)]*\)", "", cuerpo)
    contador = [0]

    def transforma(m):
        tema = m.group(1)
        if "{.unnumbered}" in tema:
            return "### " + tema.replace(" {.unnumbered}", "")
        contador[0] += 1
        return f"### {numero}.{contador[0]} {tema}"

    cuerpo = re.sub(r"^## (.+?)$", transforma, cuerpo, flags=re.M)
    partes.append(f"## Unidad {numero} · {titulo}\n{cuerpo.strip()}\n")

Path("temario_completo.md").write_text("\n---\n\n".join(partes) + "\n",
                                       encoding="utf-8")
print(f"genera_indice: {len(unidades)} unidades, "
      f"{sum(len(t) for _, _, t, _ in unidades)} temas")
