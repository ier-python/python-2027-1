# Proyectos de ciencia de datos con Python — 2027-1

Repositorio del curso del Posgrado en Ingeniería (Energía), UNAM. Este repo es el **libro Quarto**
del curso: el sitio publicado que crece clase a clase.

📖 Sitio: <https://ier-python.github.io/python-2027-1/>

## Flujo de trabajo

Las clases se imparten y desarrollan en una carpeta de trabajo aparte (`curso_python/`), donde cada
clase tiene su propio entorno `uv` y sus libretas. Al terminar una sesión, la carpeta de la clase se
copia a `clases/` de este repo, se registra en `_quarto.yml`, se renderiza y se publica.

> ⚠️ Las libretas de este repo llevan además **celdas markdown de documentación** (título, objetivo,
> narración) agregadas después de la clase. Al copiar desde `curso_python/`, copia **solo clases
> nuevas**: sobrescribir una libreta ya documentada borra esa documentación.

## Estructura

```
.
├── _quarto.yml            # configuración del libro; aquí se registran las clases
├── index.qmd              # portada
├── temario.qmd            # programa oficial (índice temático autogenerado)
├── reglas.qmd             # reglas y acuerdos del curso
├── estilos.scss           # tema visual (claro)
├── estilos-oscuro.scss    # tema visual (oscuro)
├── scripts/
│   └── genera_indice.py   # pre-render: tabla del temario + temario_completo.md
├── unidades/
│   └── unidad-0N.qmd      # las 8 unidades del programa (fuente del índice temático)
├── apendices/
│   └── instalacion.qmd
├── recursos/pdfs/         # material de referencia (se publica en el sitio)
└── clases/
    └── NNN_tema/              # ← una carpeta por clase
        ├── notebooks/         # libretas de la sesión → páginas del libro
        ├── data/              # datos (no se versionan; ver Convenciones)
        │   ├── 001_raw/
        │   └── 002_intermediate/
        ├── pyproject.toml     # dependencias de esta clase (si se copia)
        └── uv.lock
```

**La raíz no es un proyecto Python.** No contiene `pyproject.toml` a propósito: si lo tuviera,
`uv init` dentro de `clases/` convertiría cada clase en miembro de un *workspace* con un entorno
compartido, y se perdería el aislamiento entre sesiones. Nunca ejecutes `uv init` en la raíz.

## Organización del libro

En `_quarto.yml` cada **unidad** del temario es un capítulo numerado (1–8) y las libretas de clase
cuelgan del `part` de su unidad con `{.unnumbered}` en el título de su primera celda (ver
Convenciones). Así los números de capítulo del libro coinciden con la tabla del temario (temas N.M):

```yaml
- part: "Unidad 3 · Importar y limpiar datos"
  chapters:
    - unidades/unidad-03.qmd                             # capítulo 3
    - clases/009_importar_datos/notebooks/001_ETL.ipynb  # {.unnumbered}
```

## Agregar una clase al libro

1. **Guarda las libretas ejecutadas.** *Restart Kernel and Run All Cells* antes de guardar, para que
   las salidas publicadas sean coherentes de arriba a abajo.
2. Copia la carpeta de la clase desde `curso_python/` a `clases/NNN_tema/`.
3. Agrega a cada libreta su celda Raw de título y su celda markdown de entrada (ver Convenciones).
4. Registra las libretas en `_quarto.yml`, dentro del `part` de su unidad.
5. Revisa y publica:

```bash
quarto preview                                  # revisión local
git add -A && git commit -m "Clase NNN: tema"
git push
quarto publish gh-pages
```

## Convenciones que hacen que esto funcione

**Las libretas se versionan con sus salidas.** El libro se construye con `execute: enabled: false`:
no ejecuta nada, publica las salidas guardadas en cada `.ipynb`. Es lo que permite que cada clase
tenga dependencias distintas sin que el libro entre en conflicto. Consecuencia directa: **no
instalar `nbstripout`** — borraría las salidas y dejaría el libro vacío.

**Un entorno por clase.** En la carpeta de trabajo, cada clase tiene su `.venv/` y su `uv.lock`. La
interfaz del curso es **Jupyter Notebook, no JupyterLab** (`uv run jupyter notebook`).

**Cada libreta empieza con una celda Raw que declara el título en YAML:**

```yaml
---
title: "# Datos faltantes con `missingno` {.unnumbered}"
---
```

El `#` dentro de la cadena no es opcional: Quarto sólo reconoce `{.unnumbered}` en el título de una
libreta si lo lee con sintaxis de encabezado. Si el título va en una celda markdown
(`# Título {.unnumbered}`), Quarto conserva el texto pero descarta el atributo, la libreta consume un
número de capítulo y descuadra la numeración de las unidades. Sin título aparece el nombre del archivo.

**La segunda celda es markdown y abre con `Clase NNN · NNN_tema ·`**, seguido de dos a cuatro líneas
que dicen qué hace la libreta y qué lugar ocupa en la secuencia. Si la libreta lee archivos que no
viajan en el repo, sigue un `::: {.callout-important title="Datos"}` que dice cuáles son y dónde
colocarlos.

**Una celda markdown antes de cada celda de código**, con encabezado `## ` por paso o por archivo y un
párrafo que dice qué hace la celda, por qué, y qué hay que mirar en la salida. Las celdas que sólo
confirman algo (`head()`) llevan una línea. Cuando aparece un paquete nuevo, el markdown dice que se
instala con `uv add paquete`.

**La documentación vive en celdas markdown, el código no se toca.** Las celdas de código y sus
salidas quedan tal como se ejecutaron en clase (errores intencionales incluidos: son parte de la
narrativa); la explicación se agrega alrededor, en celdas markdown nuevas.

**Figuras embebidas.** Con matplotlib inline las imágenes quedan dentro del `.ipynb` y viajan solas
al sitio. Si usas `savefig()`, asegúrate de que la figura también se muestre en la celda.

**Toda figura publicada lleva opciones `#|` al inicio de su celda**, antes del código y sin tocarlo:

```python
#| label: fig-v1-faltantes
#| fig-cap: "Matriz de datos faltantes de `v1_filas_faltantes.csv`. Los huecos blancos son `NaN`; `p_atm` es la variable con más faltantes."
#| fig-alt: "Matriz de missingno con diez columnas; la columna p_atm tiene un bloque blanco grande al inicio."
msno.matrix(esolmet)
```

`label` empieza con `fig-`, es único en todo el libro y permite citar la figura como
`@fig-v1-faltantes`; `fig-cap` dice qué muestra la figura y cuál es el hallazgo; `fig-alt` la describe
para quien no la ve. Como el libro no ejecuta las libretas, las opciones surten efecto sin volver a
correr la celda y las líneas `#|` no aparecen en el código publicado. La comprobación es el HTML en
`_book/`: título sin número y pie de figura con `Figura N:`.

**Salidas contenidas.** Un DataFrame de miles de filas impreso son megabytes de HTML dentro del
`.ipynb`, en cada commit. `df.head(20)` basta.

**Sólo se publica lo listado en `_quarto.yml`.** Nada más llega al sitio: ni `data/`, ni `.venv/`,
ni las libretas no registradas.

**Datos.** `clases/*/data/` está ignorado por omisión (convención `001_raw/`, `002_intermediate/`).
Los CSV usados en clase se comparten aparte; cada libreta documenta en un callout qué archivo
necesita y dónde colocarlo. Para versionar los datos de una clase concreta, añade su excepción en
`.gitignore`.

**El índice temático se genera solo.** `scripts/genera_indice.py` corre en cada render (pre-render):
lee los `## temas` de `unidades/unidad-0N.qmd`, reescribe la tabla de `temario.qmd` (entre los
marcadores `<!-- indice:inicio -->` y `<!-- indice:fin -->`) y regenera `temario_completo.md`. Las
unidades se editan a mano; la tabla, nunca.

## Publicación

El sitio **solo** se actualiza al correr:

```bash
quarto publish gh-pages
```

(renderiza y empuja a la rama `gh-pages`; GitHub Pages tarda unos minutos). Hacer `git push` a
`main` no cambia el sitio publicado. La primera vez hay que habilitar GitHub Pages en el
repositorio (Settings → Pages) apuntando a la rama `gh-pages`.
