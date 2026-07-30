# Proyectos de ciencia de datos con Python — 2027-1

Repositorio del curso del Posgrado en Ingeniería (Energía), UNAM. Es dos cosas a la vez:

- **Espacio de trabajo**: una carpeta por clase, cada una con su propio entorno gestionado con `uv`.
- **Libro Quarto**: el sitio publicado que crece clase a clase.

📖 Sitio: <https://ier-python.github.io/python-2027-1/>

## Estructura

```
.
├── _quarto.yml          # configuración del libro; aquí se registran las clases
├── index.qmd            # portada
├── temario.qmd          # programa oficial de la actividad académica
├── estilos.scss         # tema visual
├── apendices/
│   └── instalacion.qmd
├── recursos/pdfs/       # material de referencia (se publica en el sitio)
└── clases/
    └── clase-NN-tema/           # ← una carpeta = una clase = un proyecto uv = una parte del libro
        ├── index.qmd            # introducción de la parte: temas, objetivos, contexto
        ├── pyproject.toml       # dependencias de esta clase
        ├── uv.lock              # versiones exactas (se versiona)
        ├── .venv/               # no se versiona
        ├── data/{raw,processed}
        ├── notebooks/           # libretas de la sesión → capítulos del libro
        └── tareas/
            ├── tarea-NN.ipynb      # enunciado → se publica
            └── _solucion-NN.ipynb  # no se publica
```

**La raíz no es un proyecto Python.** No contiene `pyproject.toml` a propósito: si lo tuviera, `uv init`
dentro de `clases/` convertiría cada clase en miembro de un *workspace* con un entorno compartido, y se
perdería el aislamiento entre sesiones. Nunca ejecutes `uv init` en la raíz.

## Requisitos

[uv](https://docs.astral.sh/uv/) · [Git](https://git-scm.com/) · [Quarto](https://quarto.org/)

No hace falta instalar Python: `uv` lo descarga. El detalle está en
[`apendices/instalacion.qmd`](apendices/instalacion.qmd).

## Uso

### Crear una clase

```bash
cd clases
uv init clase-03-importacion && cd clase-03-importacion
uv add pandas matplotlib                # dependencias del tema
uv add --dev notebook ipykernel         # herramientas (Jupyter Notebook, no Lab)
mkdir -p data/raw data/processed notebooks tareas
```

### Trabajar durante la clase

```bash
cd clases/clase-03-importacion
uv run jupyter notebook
```

El kernel será el `.venv` de esa clase. En VS Code o Positron, selecciona `./.venv/bin/python` de la
carpeta de la clase.

### Agregar la clase al libro (al terminar la sesión)

1. **Guarda las libretas ejecutadas.** *Restart Kernel and Run All Cells* antes de guardar, para que
   las salidas publicadas sean coherentes de arriba a abajo.
2. Escribe `clases/clase-03-importacion/index.qmd` con la introducción de la parte.
3. Registra la clase en `_quarto.yml`:

```yaml
    - part: clases/clase-03-importacion/index.qmd
      chapters:
        - clases/clase-03-importacion/notebooks/01-importacion.ipynb
        - clases/clase-03-importacion/tareas/tarea-03.ipynb
```

4. Revisa y publica:

```bash
quarto preview                                  # revisión local
git add -A && git commit -m "Clase 03: importación y limpieza"
git push
quarto publish gh-pages
```

## Convenciones que hacen que esto funcione

**Las libretas se versionan con sus salidas.** El libro se construye con `execute: enabled: false`: no
ejecuta nada, publica las salidas guardadas en cada `.ipynb`. Es lo que permite que cada clase tenga
dependencias distintas sin que el libro entre en conflicto. Consecuencia directa: **no instalar
`nbstripout`** — borraría las salidas y dejaría el libro vacío.

**Un entorno por clase.** Cada carpeta tiene su `.venv/` y su `uv.lock`. Al cambiar de clase, cambia
también el intérprete en el editor.

**La interfaz del curso es Jupyter Notebook, no JupyterLab.** Cada clase declara el paquete `notebook`
(Notebook 7) como dependencia de desarrollo y se abre con `uv run jupyter notebook`. No agregues
`jupyterlab` a las dependencias.

**Cada libreta empieza con `# Título`** en una celda markdown. Quarto lo usa como título del capítulo;
sin él aparece el nombre del archivo.

**Figuras embebidas.** Con matplotlib inline las imágenes quedan dentro del `.ipynb` y viajan solas al
sitio. Si usas `savefig()`, asegúrate de que la figura también se muestre en la celda.

**Salidas contenidas.** Un DataFrame de miles de filas impreso son megabytes de HTML dentro del
`.ipynb`, en cada commit. `df.head(20)` basta.

**Sólo se publica lo listado en `_quarto.yml`.** Nada más llega al sitio: ni `data/`, ni `.venv/`, ni
las libretas no registradas. Por eso `_solucion-NN.ipynb` no se publica — aunque, si el repo es
público, siga siendo visible navegando los archivos en GitHub.

**Datos.** `data/raw/` y `data/processed/` están ignorados por omisión. Para versionar los de una clase
concreta, añade su excepción en `.gitignore`. Lo pesado se documenta en el `index.qmd` de la clase, con
una libreta `00-descarga.ipynb` que lo reconstruya cuando sea posible.

**Cuando una clase continúa el trabajo de la anterior**: vuelve a declarar sus dependencias (`uv add`,
que resuelve desde caché) y lee los datos previos por ruta relativa
(`../../clase-05-series/data/processed/...`). La continuidad narrativa va en el `index.qmd` nuevo.

## Reproducir una clase

```bash
cd clases/clase-01-introduccion
uv sync          # instala las versiones exactas de uv.lock
uv run jupyter notebook
```

Para comprobar que una clase sigue corriendo con su lock versionado:

```bash
uv run jupyter execute notebooks/*.ipynb
```

## Primera publicación

`quarto publish gh-pages` crea y actualiza la rama `gh-pages`. La primera vez hay que habilitar
GitHub Pages en el repositorio (Settings → Pages) apuntando a esa rama.
