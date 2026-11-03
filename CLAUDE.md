# Libro del curso Proyectos de ciencia de datos con Python (UNAM, 2027-1)

Libro Quarto que publica las libretas de clase tal como se ejecutaron. Las convenciones están en
`README.md` ("Convenciones que hacen que esto funcione"); léelas antes de tocar libretas o
`_quarto.yml`.

## Antes de empezar

- Corre `git pull` primero: el profesor trabaja desde más de una máquina y el formato del libro se
  ha cambiado desde otra sin que esta copia lo supiera. Publicar sin traer `origin/main` pisa el sitio
  con una versión vieja.

## Al formatear una libreta para el libro

- No modifiques código, salidas, `execution_count`, ids ni metadatos de las celdas de código. Lo único
  que se agrega dentro de una celda de código son las opciones `#|` de una figura, al inicio.
- Primera celda Raw con `title: "# Título {.unnumbered}"` (el `#` no es opcional); segunda celda
  markdown que abre con `Clase NNN · NNN_tema ·` y, si hay datos externos, el callout "Datos"; una
  celda markdown antes de cada celda de código.
- Edita el `.ipynb` con un script (JSON con `sort_keys=True, indent=1, ensure_ascii=False`, salto de
  línea final) y comprueba contra el original que el código y las salidas quedaron idénticos.
- Registra la ruta completa (con `notebooks/`) dentro del `part` de su unidad en `_quarto.yml` y corre
  `quarto render`; verifica en `_book/` que el capítulo no tiene número y que cada figura tiene
  `figcaption`.
- `quarto render` corre `scripts/genera_indice.py` (pre-render) y puede reescribir `temario.qmd` y
  `temario_completo.md`; revisa `git status` después.

## Origen de las libretas

Se trabajan en clase en `~/curso_python/NNN_tema/` (un proyecto `uv` por clase) y se copian a
`clases/NNN_tema/notebooks/` sólo cuando son nuevas: las ya documentadas no se sobrescriben. Los datos
(`data/`) no se versionan.
