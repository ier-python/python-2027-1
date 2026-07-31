# Proyectos de ciencia de datos con Python — temario completo

Semestre 2027-1 · 16 sesiones · 48 horas

---

## Unidad 1 · Introducción a los proyectos de ciencia de datos con Python
> **Objetivo.** Que cada estudiante termine con Python y uv instalados y funcionando, y sea capaz de
> crear un proyecto de ciencia de datos bien formado: con su entorno declarado, su estructura de
> carpetas, y sus libretas y variables nombradas con criterio, bajo las reglas de narrativa
> computacional que se reforzarán durante todo el semestre.

**6 h en el curso**

### 1.1 Qué es un proyecto de ciencia de datos

1. Por qué Python es un lenguaje de programación para ciencia de datos; panorama del semestre.
2. Proyecto frente a script suelto: datos, código, entorno y resultados.

### 1.2 Instalación y espacio de trabajo

1. Instalación: Miniconda en Windows (terminal y Python base); macOS y Linux sin instalación; uv de
   Astral; herramientas a la mano.
2. Terminal: navegación, rutas, crear carpetas.
3. El editor de texto plano: los archivos que no son libretas — `.py`, `.md`, `.gitignore` — se
   editan como texto; VS Code a la mano desde el inicio.
4. Verificación común: `python --version` y `uv --version`.

### 1.3 Entornos virtuales y la primera libreta

1. Qué es un entorno virtual y por qué existe.
2. `uv init`, `uv add`, `uv run`: el primer proyecto.
3. Los paquetes se agregan con `uv add`, nunca con `pip install` desde la libreta: instalar por
   fuera rompe la receta del proyecto sin avisar.
4. `pyproject.toml`, la receta; `uv.lock`, el registro exacto.
5. Borrar el entorno y reconstruirlo con `uv sync`.
6. Jupyter Notebook dentro del proyecto: el kernel es el entorno.

### 1.4 Paseo por la libreta de Jupyter

1. Celdas de código y celdas de Markdown; ejecutar con `Shift+Enter`.
2. Modo edición y modo comando; los atajos que valen la pena (`a`, `b`, `dd`, `m`, `y`).
3. La libreta es su propia documentación: autocompletar con `Tab`, ayuda con `?` y `Shift+Tab`.
4. El kernel: qué significa que esté ocupado, reiniciarlo, y qué sobrevive a un reinicio (el
   archivo) y qué no (las variables).
5. `%whos`: ver las variables vivas en memoria — la evidencia de qué sobrevive al reinicio.
6. El número entre corchetes: el orden de ejecución queda registrado.
7. Guardar, exportar, y qué es realmente el archivo `.ipynb`.

### 1.5 Anatomía de un proyecto

1. Estructura: `data/raw`, `data/processed`, `notebooks/`, `figures/`, y el `README.md` que
   presenta el proyecto.
2. Rutas relativas frente a rutas absolutas.
3. Qué se versiona y qué no.

### 1.6 Nombres

1. Archivos y carpetas: minúsculas, sin espacios ni acentos.
2. Libretas: numeradas por orden de lectura.
3. Variables: `snake_case`, qué contienen y en qué unidades.
4. Fechas en formato ISO.

### 1.7 Narrativa computacional

1. La libreta como documento, no como consola con historial.
2. El orden de ejecución; reiniciar y ejecutar todo antes de compartir.
3. Markdown y sus piezas: encabezados, listas, enlaces, bloques de código y tablas — la
   estructura del relato, qué explicar y qué se explica solo.
4. Una libreta, una pregunta.

### 1.8 Reglas del curso y repositorios

1. Qué es un repositorio: el espacio de trabajo donde vive el proyecto y su historia. Por ahora,
   solo la definición — se usa desde el inicio, se aprende a fondo más adelante.
2. Los datos crudos no se tocan.
3. Todo proyecto declara su entorno.
4. Una libreta corre de arriba abajo, desde cero.
5. Ningún nombre que no diga qué es.
6. Rutas relativas, siempre.
7. Si no está en el repositorio, no existe.

### Ejercicios sugeridos

1. Instalar Python y uv antes de la primera sesión, y llegar con la verificación hecha.
2. Crear un proyecto con uv, agregarle una dependencia y ejecutar un script dentro de él.
3. Hacer correr un programa antiguo que hoy falla, sin modificar una sola línea de su código.
4. Tener dos proyectos con versiones incompatibles de la misma biblioteca, funcionando ambos en la
   misma computadora.
5. Borrar por completo el entorno de un proyecto y reconstruirlo.
6. Diagnosticar una libreta que no encuentra un paquete que sí está instalado en el proyecto.
7. Reorganizar un proyecto desordenado según la estructura de carpetas de la unidad.
8. Renombrar los archivos y variables de una libreta ajena hasta que se entienda sin explicación.
9. Convertir una libreta escrita como consola en una libreta que se lea como documento.
10. Intercambiar proyectos por parejas y reproducir el resultado del compañero en la propia máquina.

### Al terminar la unidad

- Explicar por qué el mismo código puede dar resultados distintos en dos computadoras.
- Abrir una terminal y saber qué Python responde, y por qué.
- Crear un proyecto con uv, agregarle dependencias y ejecutarlo.
- Distinguir `pyproject.toml` de `uv.lock`, y saber cuál duele perder.
- Abrir una libreta con el kernel correcto y diagnosticar cuando no lo es.
- Estructurar y nombrar un proyecto de modo que otra persona lo entienda sin explicación.

---

## Unidad 2 · Sintaxis, herramientas de control y métodos de Python
> **Objetivo.** Que cada estudiante domine el vocabulario básico de Python —tipos, colecciones,
> estructuras de control, cadenas y funciones— y lo use con criterio: primero los datos, luego el
> código que los recorre, siempre dentro de libretas que respeten la narrativa computacional de la
> Unidad 1.

**6 h en el programa oficial**

### 2.1 Sintaxis, tipos de variables, iterables

1. La celda como unidad de ejecución: expresiones, asignación, comentarios.
2. Anatomía del error: el traceback se lee de abajo hacia arriba y la última línea dice el tipo;
   los cinco sospechosos habituales (`NameError`, `TypeError`, `KeyError`, `FileNotFoundError`,
   `ModuleNotFoundError`).
3. El eco de la celda y `print()`: la libreta muestra la última expresión sin pedirlo; `print` es
   para todo lo demás.
4. Tipos básicos: `int`, `float`, `complex`, `str`, `bool`, `None`; `type()` y conversiones entre
   tipos.
5. Colecciones: listas, tuplas, diccionarios y conjuntos — qué dato pide cuál.
6. Desempaquetado de tuplas: `a, b = pareja` — el gesto que el curso repetirá en `fig, ax` y en
   `enumerate`.
7. Iterables sin escribir ciclos: indexado, rebanadas, `len`, `in`, `sum`, `min`, `max`, `sorted`.
8. Mutabilidad y el patrón `objeto.método()`: `lista.append()` como primer método; atributo sin
   paréntesis (un dato que se consulta) frente a método con paréntesis (una acción que se
   ejecuta); qué se modifica en el lugar y qué se reemplaza.
9. Asignar no copia: `b = a` no crea una lista nueva — dos nombres, un solo objeto; el susto que
   volverá en NumPy y en pandas, anunciado desde ahora.

### 2.2 Estructuras de control

1. La sangría como sintaxis: el bloque es lo que está indentado.
2. `if` / `elif` / `else`: comparaciones, operadores lógicos, decisiones sobre datos.
3. `for` sobre un iterable: recorrer listas y diccionarios (`.items()`); `range`, `enumerate` y
   `zip`.
4. `while`: repetir hasta que algo cambie; por qué en datos casi siempre gana `for`.
5. *List comprehensions*: el ciclo que produce una colección nueva.

### 2.3 Cadenas en Python

1. La cadena de 2.1, ahora de cerca: no es un escalar, es un iterable de caracteres; indexado y
   rebanadas, otra vez.
2. Comillas simples y dobles: son equivalentes; elegir una por consistencia, la otra queda para
   anidar (`"it's"`).
3. Inmutabilidad: los métodos devuelven cadenas nuevas.
4. Métodos de limpieza: `lower`, `strip`, `replace`, `split`, `join` — antesala de la limpieza de
   datos de la Unidad 3.
5. Cadenas que son datos: encabezados de columnas, categorías, rutas de archivos.

### 2.4 f-strings

1. *String interpolation*: `f'El valor es: {variable}'` — variables y expresiones dentro del
   texto.
2. Formato de números: decimales, separadores de miles, notación científica.
3. Resultados que se explican solos: cifras con sus unidades y fechas en formato ISO.
4. Construir nombres de archivos y rutas con f-strings.

### 2.5 Funciones

1. `def`, parámetros y `return`: de la celda repetida a la función.
2. Argumentos con nombre y valores por defecto.
3. Docstrings: qué recibe, qué devuelve, en qué unidades.
4. Ámbito de las variables: lo que vive dentro de la función se queda dentro.
5. Funciones en la libreta: definir arriba, usar abajo, sin romper la lectura.

### Ejercicios sugeridos

1. Dado un conjunto de mediciones en una lista, responder preguntas (máximo, mínimo, promedio,
   cuántas superan un umbral) usando solo funciones integradas, sin escribir un solo ciclo.
2. Provocar a propósito los cinco errores clásicos, y escribir en Markdown qué dice la última
   línea de cada traceback y qué lo causó.
3. Elegir la colección correcta —lista, tupla, diccionario o conjunto— para cinco datos reales del
   área de cada estudiante, y defender la elección.
4. Repetir el ejercicio 1 con un `for`, y comparar ambas versiones: cuándo bastan las funciones
   integradas y cuándo hace falta el ciclo.
5. Clasificar una serie de valores en categorías con `if` / `elif` / `else` dentro de un ciclo.
6. Reescribir un ciclo `for` de tres líneas como *list comprehension*, y una *list comprehension*
   ilegible como ciclo de tres líneas.
7. Limpiar una lista de encabezados de columna sucios (mayúsculas, espacios, acentos) usando
   métodos de cadenas, hasta dejarlos en `snake_case`.
8. Producir un reporte de resultados con f-strings: cifras con dos decimales, unidades explícitas
   y fecha en formato ISO.
9. Generar nombres de archivos de salida con f-strings a partir de una fecha y una variable.
10. Extraer una función a partir de dos celdas casi idénticas de una libreta, con docstring y
    valores por defecto.
11. Intercambiar funciones por parejas: usar la función del compañero leyendo solo su docstring,
    sin mirar el código.
12. Ejercicio integrador: representar un conjunto pequeño de mediciones (fecha, valor, sensor)
    como diccionario de listas, y responder preguntas usando toda la unidad — ciclos,
    condicionales, funciones y f-strings. El dolor que quede es exactamente el que la Unidad 3
    viene a quitar.

### Al terminar la unidad

- Elegir la colección adecuada para un dato y explicar por qué.
- Interrogar un iterable con funciones integradas antes de escribir un ciclo.
- Recorrer listas y diccionarios con `for`, y decidir cuándo un `while` se justifica.
- Limpiar texto con métodos de cadenas y reconocer que las cadenas son datos.
- Reportar resultados con f-strings: números formateados, unidades y fechas ISO.
- Convertir código repetido en una función con docstring que otra persona pueda usar sin leerla
  por dentro.

---

## Unidad 3 · Importación y limpieza de datos
> **Objetivo.** Que cada estudiante domine el DataFrame como concepto central del curso: importar
> datos reales con pandas, diagnosticarlos antes de tocarlos, limpiarlos declarando cada decisión,
> y consolidar múltiples archivos crudos en un solo archivo limpio — el flujo completo de
> `data/raw` a `data/processed`.

**10 h en el programa oficial**

### 3.1 Módulos e `import`

1. Recordatorio: los paquetes se instalan en el proyecto con `uv add`, nunca con `pip` desde la
   libreta — instalar no es importar.
2. `import` y su sintaxis: `import math`, `from math import sqrt`, el alias `as`. La biblioteca
   estándar: `math`, `datetime`, `glob` y compañía — instaladas desde siempre, importadas cuando
   hacen falta.
3. La línea que abre la unidad: `import pandas as pd`.

### 3.2 Pair wise data

1. Del diccionario de listas al DataFrame: la tabla del ejercicio integrador ya tenía nombre.
2. `pd.read_csv`: el primer archivo real; la ruta relativa hasta `data/raw`.
3. Anatomía del DataFrame: índice, columnas, `dtypes`; `head`, `info`, `describe` — mirar antes
   de tocar.
4. Cada columna es una Serie; seleccionar columnas, filas y celdas con `[]`, `loc`, `iloc`.
5. Pair wise data: observaciones apareadas (x, y); filtros booleanos para quedarse con las filas
   que cumplen algo — y `.copy()` cuando el resultado va a modificarse, para que el
   `SettingWithCopyWarning` no sorprenda.
6. Operaciones vectorizadas: columnas nuevas a partir de las existentes, sin escribir un solo
   `for`.
7. Fontanería mínima: `rename`, `sort_values`, `set_index` / `reset_index`, `drop` — y
   `df.columns` a `snake_case`, el ejercicio de la Unidad 2 cobrado.

### 3.3 Series temporales

1. La fecha como dato, no como texto: `pd.to_datetime`; las fechas ISO de la Unidad 1 pagan aquí.
2. El módulo `datetime` por dentro: `strptime` / `strftime` y los códigos de formato
   (`%Y-%m-%d %H:%M`), `timedelta` — el idioma que `to_datetime` y su `format=` hablan.
3. El índice temporal: leer con `parse_dates`, poner el tiempo como índice del DataFrame.
4. Los accesores `.dt` y los atributos del `DatetimeIndex`: `.year`, `.month`, `.hour`,
   `.dayofweek` — cada estampa sabe contestar quién es; el insumo de los grupos de la Unidad 7.
5. Seleccionar por fecha y por rango: el índice temporal como herramienta de rebanado.
6. `df.plot()`, la primera mirada gráfica: revisar rápido sin pelear con ejes — la visualización
   de verdad llega en la Unidad 4.
7. Qué hace especial a una serie temporal: orden, frecuencia esperada, huecos — y cómo un
   `plot` los delata (el zigzag del índice desordenado; `sort_index`).
8. Cambiar de frecuencia: `df.resample('D').mean()`, de minutos a días en una línea — primer
   contacto con una idea (agrupar y resumir) que la Unidad 7 desarrolla a fondo.

### 3.4 Data cleaning

1. Archivos que no se dejan leer: encabezados corridos, líneas de más, separadores raros — la
   limpieza empieza en las opciones de `pd.read_csv` (`skiprows`, `header`, `sep`, `decimal`,
   `encoding`). CSV, TXT y EPW son el mismo animal: texto con separador, y `read_csv` los lee
   todos. Antes de pelear, mirar el crudo: abrirlo en el editor o `head` en la terminal.
2. No todo es texto: `read_excel` para los `.xlsx` — `sheet_name` y `skiprows`, la misma
   gramática de opciones sobre otro formato.
3. Cómo vienen los `NaN`: `-999`, `N/A`, `--`, celdas vacías; declararlos con `na_values` desde
   la importación. El `None` de la Unidad 2, con nombre nuevo.
4. Diagnóstico antes de cirugía: `isna`, `value_counts`, `duplicated` y un `df.plot()` rápido —
   cuantificar y *ver* lo que la importación no resolvió.
5. Números que llegaron como texto: los métodos de cadenas cosechan (`strip`, `replace`) y
   `astype` convierte.
6. Fechas que no son fechas: `p. m.` en lugar de `PM`, formatos locales; arreglar el texto antes
   de `to_datetime`, o declararle el `format`.
7. Duplicados y valores imposibles: filtros booleanos para descartar lo que ningún sensor pudo
   medir.
8. La rejilla esperada: `pd.date_range` y `reindex` — comparar el tiempo que llegó contra el que
   debió llegar; `.diff()` sobre el índice censa los huecos.
9. Huecos en el tiempo: detectarlos, y decidir — rellenar, interpolar o dejar el hueco (`fillna`,
   `interpolate`, `dropna`); cada opción es una decisión que se declara, no se esconde.
10. Guardar en `data/processed`: `to_csv` para compartir, `to_parquet` para trabajar — el CSV
   olvida los tipos (las fechas vuelven como texto), parquet los recuerda; limpiar una vez, no
   cada vez. Requiere `uv add pyarrow`: la Unidad 1 en acción.

### 3.5 Importación de múltiples archivos

1. El escenario real: un archivo por día, por mes o por sensor — nadie te da la tabla completa.
2. `glob`: patrones para listar archivos desde Python.
3. Leer en ciclo, acumular en una lista (`append`, otra vez) y unir con `pd.concat`; un `try` /
   `except` mínimo salva el ciclo del archivo corrupto.
4. Unir a lo ancho: `concat(axis=1)` para sensores que comparten el tiempo, `merge` para pegar
   metadatos de estación — la unión vertical tiene hermanas.
5. Verificar el consolidado: tamaño esperado, duplicados en las uniones, continuidad temporal.
6. Los datos no siempre viven en tu disco: `read_csv` también acepta una URL — un archivo
   publicado en la red (Conagua) se lee con la misma línea.
7. Cerrar el flujo: de muchos crudos a un solo archivo limpio en `data/processed`.

### Ejercicios sugeridos

1. Convertir el diccionario de listas del ejercicio integrador de la Unidad 2 en un DataFrame, y
   responder las mismas preguntas — ahora en una línea cada una.
2. Leer un CSV de `data/raw` y producir su ficha en Markdown: cuántas filas, qué columnas, qué
   tipos, cuántos huecos.
3. Quedarse con las filas que cumplen dos condiciones a la vez, usando filtros booleanos.
4. Crear una columna nueva a partir de otras (una conversión de unidades) sin escribir un ciclo.
5. Leer un archivo cuyas fechas llegaron como texto, convertirlas, ponerlas como índice, rebanar
   una semana concreta y graficarla con `df.plot()`.
6. Diagnosticar con `df.plot()` un archivo que "se ve bien" con `head()`: descubrir el índice
   desordenado por el zigzag de la gráfica, y corregirlo con `sort_index`.
7. Importar un archivo hostil: el encabezado en la fila 5, `-999` como dato faltante y fechas
   con `p. m.`; resolver todo lo posible desde `read_csv` y el resto antes de `to_datetime`.
8. Limpiar una columna numérica que llegó como texto: espacios, unidades pegadas al número,
   comas decimales; terminar con `astype`.
9. Detectar los valores que ningún sensor pudo medir, descartarlos, y documentar en Markdown
   cuántos fueron y con qué criterio.
10. Encontrar los huecos de una serie temporal y comparar tres tratamientos: rellenar,
    interpolar y dejar el hueco. Argumentar cuál conviene y por qué.
11. El viaje redondo: guardar un DataFrame limpio en CSV y en parquet, releer ambos, y comparar
    qué sobrevivió — tipos, índice temporal, `NaN` — y qué hay que volver a arreglar.
12. Consolidar con `glob` y `pd.concat` una carpeta con un archivo por mes, y verificar el
    resultado: tamaño esperado, sin duplicados, sin saltos de tiempo.
13. Flujo completo por parejas: entregar al compañero una carpeta de crudos sucios y recibir de
    vuelta un `data/processed` con la libreta que lo produce, corriendo de arriba abajo.

### Al terminar la unidad

- Explicar qué es un DataFrame y qué relación tiene con el diccionario de listas y con la Serie.
- Importar archivos que no vienen fáciles — encabezados corridos, `NaN` disfrazados, fechas en
  formato local — resolviendo desde las opciones de `read_csv` lo que se pueda.
- Diagnosticar un archivo real — filas, tipos, huecos, duplicados — antes de tocarlo.
- Seleccionar filas y columnas con `[]`, `loc`, `iloc` y filtros booleanos, y crear columnas
  nuevas sin ciclos.
- Poner el tiempo como índice, rebanar un DataFrame por fechas y rangos, y darle la primera
  mirada con `df.plot()`.
- Limpiar un dataset declarando cada decisión: qué se descartó, qué se rellenó y con qué
  criterio.
- Consolidar una carpeta de archivos crudos en un solo archivo limpio en `data/processed`, con
  una libreta reproducible, y elegir el formato con criterio: CSV para compartir, parquet para
  trabajar.

---

## Unidad 4 · Introducción a la visualización
> **Objetivo.** Que cada estudiante produzca figuras con calidad de tesis: elegir el tipo de
> gráfica según la pregunta, construirla con la API de objetos de matplotlib, componer paneles,
> y exportarla lista para LaTeX sin retoques posteriores — sabiendo además cuándo conviene
> explorar con plotly y por qué se publica con matplotlib.

**8 h en el programa oficial**

### 4.1 El paisaje de las bibliotecas de visualización

1. El ecosistema de graficadores de Python: matplotlib, seaborn, plotly, altair, bokeh y más —
   muchos nombres, un mapa para no perderse.
2. El mapa son capas: `df.plot()` y seaborn le hablan a matplotlib por ti — por eso nunca lo
   importamos en la Unidad 3.
3. Los paradigmas distintos: plotly (interactivo), altair (declarativo) — saber que existen y
   cuándo buscarlos.
4. Por qué el curso se enfoca en matplotlib: es el fondo común de casi todo, y el control fino
   que una tesis exige.
5. La revelación: `df.plot()` devuelve un `Axes` de matplotlib — personalizar la figura de
   pandas es empezar a usar matplotlib.

### 4.2 Anatomía de una figura

1. `Figure`, `Axes`, `Axis`: el lienzo, la gráfica y los ejes — cada elemento con su nombre.
2. Los elementos con los que se habla: título, etiquetas de ejes, leyenda, *ticks*, rejilla,
   colores y estilos de línea.
3. La figura que se explica sola: ejes con unidades, título que dice el hallazgo, leyenda cuando
   hay más de una serie, fechas legibles — las reglas de nombres de la Unidad 1, ahora en tinta.

### 4.3 OOP en matplotlib

1. Las dos APIs: `plt.plot()` (la máquina de estados de los tutoriales y de ChatGPT) frente a
   `fig, ax = plt.subplots()` (la de objetos, el estándar del curso) — nombrarlas para no
   mezclarlas.
2. El patrón del curso: `fig, ax = plt.subplots()`; el `Axes` como el objeto al que se le pide
   todo — `objeto.método()`, otra vez.
3. Los tipos básicos y su pregunta: línea (`ax.plot`, serie temporal), dispersión (`ax.scatter`,
   pair wise data), barras (`ax.bar`, categorías), histograma (`ax.hist`, distribución).
4. Cuándo una figura miente: el eje recortado, los *bins* mal elegidos, la línea que une puntos
   que no son continuos.
5. Varias series en un mismo `Axes`: la leyenda se vuelve obligatoria.
6. La ventana de tiempo configurable: `ax.set_xlim(fecha, fecha + pd.Timedelta("1D"))` — la
   serie larga se grafica una vez y la ventana decide qué se mira.
7. Series densas: miles de puntos minutales piden `alpha` para que la nube respire y
   `markevery` para no sembrar marcadores.

### 4.4 Esquemas complejos con specgrid

1. Varios `Axes` en una `Figure` con el mismo `plt.subplots(nrows, ncols)` de siempre; `sharex`
   para series que comparten el tiempo, `sharey` para paneles que se comparan en la misma
   escala.
2. `GridSpec`: paneles de tamaños distintos — la serie principal con su histograma marginal.
3. Dos unidades en el mismo panel: `twinx` — irradiancia y temperatura sobre el mismo tiempo.
4. Composición con criterio: cuándo superponer, cuándo separar paneles, cuándo hacer dos
   figuras.

### 4.5 Formatos para figura

1. `figures/` se une al proyecto: las figuras se regeneran desde la libreta, nunca se editan a
   mano; nombres que dicen qué muestran.
2. `savefig`: PNG (píxeles y `dpi`) frente a PDF/SVG (vectores) — cuál para la tesis, cuál para
   la presentación, cuál para la web.
3. La figura pensada para LaTeX: el tamaño en pulgadas se decide desde matplotlib para el
   `\textwidth` del documento, con la tipografía al tamaño final — la figura no se escala
   después, se produce a la medida.
4. Matemáticas en las etiquetas: *mathtext* para `$W/m^2$` en cualquier máquina; `usetex`
   cuando la tesis exige la tipografía de LaTeX.

### 4.6 La misma figura, en plotly

1. Rehacer la figura final de la unidad en plotly: zoom, *hover*, exploración sin costo.
2. El precio: cada punto viaja dentro del archivo — HTML y libretas que engordan con datos de
   alta frecuencia; y nada de mathtext ni PDF a la medida para la tesis.
3. El criterio que cierra la unidad: explorar con plotly, publicar con matplotlib.

### Ejercicios sugeridos

1. Capturar el `Axes` que devuelve `df.plot()` y personalizarlo: título, unidades en los ejes,
   leyenda.
2. La misma figura dos veces: con `plt.plot()` a secas y con `fig, ax = plt.subplots()`;
   explicar cuál sobrevive cuando la libreta tiene diez figuras.
3. Cuatro preguntas sobre un mismo dataset, cuatro figuras — línea, dispersión, barras,
   histograma — y defender cada elección en una línea de Markdown.
4. Recibir una figura sin etiquetas ni unidades y arreglarla hasta que se entienda sin leer el
   código que la produjo.
5. Construir una figura que miente — eje recortado, *bins* tramposos — y luego corregirla;
   documentar qué cambió.
6. Graficar un mes de datos minutales una sola vez, y recorrer tres días distintos moviendo la
   ventana con `set_xlim` y `pd.Timedelta`; `alpha` y `markevery` para que la nube se deje
   leer.
7. Panel de series apiladas con `sharex`: tres variables del mismo día compartiendo el eje del
   tiempo.
8. Con `GridSpec`, la serie temporal principal acompañada de su histograma marginal.
9. Dos variables con unidades distintas en el mismo panel usando `twinx`, sin que la leyenda se
   pierda.
10. Exportar una figura en PDF a la medida del `\textwidth`, con unidades en mathtext, e
    insertarla en un documento LaTeX sin escalarla.
11. Guardar la misma figura en PNG a varios `dpi` y en PDF; hacer zoom hasta que cada PNG se
    pixele y el PDF no.
12. Rehacer la figura final en plotly con un año de datos minutales, y comparar el tamaño en
    disco y de la libreta contra la versión matplotlib.
13. Borrar la carpeta `figures/` completa y regenerarla ejecutando las libretas de arriba
    abajo.

### Al terminar la unidad

- Explicar qué biblioteca de visualización es capa de cuál, y por qué el curso publica con
  matplotlib.
- Elegir el tipo de figura según la pregunta — y detectar cuándo una figura miente.
- Construir figuras con `fig, ax = plt.subplots()` y distinguir las dos APIs al leer código
  ajeno.
- Producir figuras que se explican solas: unidades, título con hallazgo, leyenda.
- Componer paneles con `subplots`, `GridSpec` y `twinx`, eligiendo la composición con criterio.
- Exportar una figura lista para la tesis — PDF a la medida, tipografía y matemáticas correctas
  — que se regenera desde la libreta.
- Decidir entre matplotlib y plotly con argumentos: explorar frente a publicar, y el costo en
  disco de la interactividad.

---

## Unidad 5 · NumPy
> **Objetivo.** Que cada estudiante entienda NumPy como la capa numérica sobre la que viven
> pandas y matplotlib, y sea capaz de operar arreglos completos sin ciclos: estadística por
> ejes, selección con máscaras, mallas para evaluar funciones, y el criterio de cuándo trabajar
> en NumPy y cuándo en pandas.

**3 h en el programa oficial**

### 5.1 Qué es NumPy

1. La tercera revelación de capas: las columnas del DataFrame y las operaciones vectorizadas de
   la Unidad 3 eran arreglos de NumPy todo el tiempo.
2. Qué es y para qué: arreglos n-dimensionales de números homogéneos; el idioma numérico común
   de pandas, matplotlib y el cómputo científico en Python.
3. El arreglo frente al DataFrame: sin índice, sin nombres de columnas, un solo `dtype` — se
   pierden las etiquetas, se ganan la velocidad y las dimensiones (el DataFrame es tabla; el
   arreglo puede ser cubo).
4. `uv add numpy`, `import numpy as np`: el alias que ya es apellido.
5. Su especialización, medida: `%timeit` — sumar un millón de números con un ciclo y con
   `np.sum`; la promesa de velocidad convertida en dato.

### 5.2 Arrays, size, shape

1. `np.array` desde las listas de la Unidad 2; `dtype`: la homogeneidad es el precio de la
   velocidad.
2. `size`, `shape`, `ndim`: el vector, la matriz, y saber siempre de qué tamaño es lo que se
   tiene.
3. Crear desde cero: `zeros`, `ones`, `arange`, `linspace` — el eje x que matplotlib estaba
   esperando.
4. `reshape`: los mismos números, otra forma — un año de datos horarios como matriz de días por
   horas.

### 5.3 Estadística de arreglos

1. `mean`, `std`, `min`, `max`, `percentile` sobre el arreglo completo.
2. El argumento `axis`: la misma matriz de días por horas responde dos preguntas — el promedio
   de cada día y el de cada hora.
3. Los huecos otra vez: `np.nan` y las versiones que lo perdonan (`nanmean`, `nanstd`).

### 5.4 Slicing y fancy indexing

1. En una dimensión, las rebanadas de la Unidad 2 funcionan igual; en dos, `[fila, columna]`.
2. Máscaras booleanas: los filtros de la Unidad 3, revelados — comparar produce un arreglo de
   `True`/`False` que selecciona.
3. Fancy indexing: seleccionar con un arreglo de posiciones.
4. Rebanada no es copia: modificar la vista modifica el original — el susto anunciado a tiempo.

### 5.5 Creación de mallas

1. El problema: evaluar `f(x, y)` en todo un plano sin escribir un doble ciclo.
2. `np.meshgrid` sobre dos `linspace`: la malla como par de matrices coordenadas.
3. Evaluar la función sobre la malla y verla con `contourf` — el puente hacia los mapas y
   superficies de la Unidad 7.

### 5.6 Importar, guardar y el puente con pandas

1. Texto plano: `np.loadtxt` y `np.savetxt` para arreglos sin etiquetas.
2. Binario: `np.save` y `np.load` (`.npy`, `.npz`) — la lección de parquet otra vez: el texto
   olvida los `dtype`, el binario los recuerda.
3. El puente: `df.to_numpy()` de ida, `pd.DataFrame(arr)` de vuelta — las etiquetas se pierden
   y se recuperan en la frontera.
4. El criterio: etiquetas, fechas y tablas → pandas; números puros, mallas y velocidad → NumPy.

### Ejercicios sugeridos

1. Multiplicar por dos una lista y un arreglo, y explicar en Markdown la diferencia entre lo
   que hizo cada uno.
2. Medir con `%timeit` la suma de un millón de números en ciclo, con `sum` y con `np.sum`;
   reportar los tiempos con f-strings.
3. Convertir un año de datos horarios en una matriz de días por horas con `reshape`, y validar
   con `shape` antes de continuar.
4. Sobre esa matriz, responder con `axis`: qué día acumuló más y qué hora promedia más — sin un
   solo ciclo.
5. Repetir el cálculo con huecos en los datos: comparar `mean` contra `nanmean` y explicar la
   diferencia.
6. Con una máscara booleana, contar y extraer los valores fuera del rango físico de un sensor —
   el ejercicio de la Unidad 3, ahora sin pandas.
7. Demostrar el susto de la vista: rebanar un arreglo, modificar la rebanada, y descubrir el
   original cambiado; repetir con `.copy()`.
8. Construir una malla con `meshgrid`, evaluar una función de dos variables y graficarla con
   `contourf`, con su barra de color etiquetada.
9. El viaje redondo de NumPy: guardar el mismo arreglo con `savetxt` y con `save`, releer
   ambos, y comparar qué sobrevivió — `dtype`, forma, precisión.
10. Tomar un DataFrame limpio de la Unidad 3, cruzar el puente con `to_numpy()`, calcular en
    NumPy, y regresar el resultado a un DataFrame con sus etiquetas.

### Al terminar la unidad

- Explicar qué es NumPy, qué lugar ocupa debajo de pandas y matplotlib, y qué lo hace rápido.
- Crear arreglos desde listas, desde generadores (`arange`, `linspace`) y con `reshape`, sabiendo
  siempre su `shape`.
- Responder preguntas estadísticas por ejes sobre una matriz, con y sin huecos.
- Seleccionar con rebanadas, máscaras booleanas y fancy indexing — y distinguir vista de copia.
- Evaluar una función sobre una malla y visualizarla, sin escribir ciclos.
- Guardar y cargar arreglos eligiendo formato con criterio, y cruzar el puente entre pandas y
  NumPy en ambas direcciones.

---

## Unidad 6 · Prácticas para el cómputo científico
> **Objetivo.** Que cada estudiante convierta su proyecto en un proyecto de cómputo científico
> serio: versionado con git, con sus funciones graduadas de la libreta a un paquete local,
> optimizado solo donde el perfil lo señala, y con pruebas que vigilan tanto el código como los
> datos.

**8 h en el programa oficial**

### 6.1 Git: el repositorio, ahora de verdad

1. La promesa de la Unidad 1 se cumple: el repositorio deja de ser una definición.
2. `git init`, `git status`, `git add`, `git commit`: la foto del proyecto, cuándo tomarla y
   cómo describirla.
3. `git log`: la historia del proyecto como narrativa — mensajes que dicen qué cambió y por qué.
4. `.gitignore`: la regla "qué se versiona y qué no" de la Unidad 1, por fin ejecutada — fuera
   el entorno, fuera los datos pesados.
5. GitHub: `push`, `clone`; el respaldo y la carta de presentación.
6. La regla del curso, ahora literal: si no está en el repositorio, no existe.

### 6.2 Paquetes

1. La función que se repite entre libretas pide graduarse: de la celda al archivo `.py`.
2. Un paquete local junto a `notebooks/`: la carpeta, el `__init__.py`, y el proyecto que ahora
   tiene código propio importable.
3. `from mipaquete import mi_funcion`: las libretas se adelgazan, el conocimiento se comparte.
4. `%load_ext autoreload`: editar el módulo sin reiniciar el kernel — el magic que faltaba.
5. Los docstrings de la Unidad 2 pagan: el paquete se explora con `?` como cualquier
   biblioteca.

### 6.3 Profiling

1. La regla de oro: medir antes de optimizar — la intuición sobre qué es lento casi siempre
   falla.
2. `%%time` y `%timeit` (de la Unidad 5), ahora sobre funciones propias.
3. `%prun`: el perfil completo — qué función se lleva el tiempo y cuántas veces se llama.
4. Leer un perfil: el cuello de botella casi siempre es una línea, no el programa.

### 6.4 Numba (y Cython, la anécdota)

1. Acelerar Python compilando — pero solo lo que el perfil del tema anterior señaló.
2. numba: `uv add numba` y el decorador `@njit` sobre la función numérica; la primera llamada
   compila, las demás vuelan.
3. El antes y el después, medidos con `%timeit`: la aceleración es un dato, no una promesa.
4. Los límites de numba: habla NumPy y números, no pandas ni cadenas — por eso se compila la
   función, no la libreta.
5. Cython, la anécdota: el pariente anticipado que traduce a C y necesita compilador; así están
   construidos pedazos de pandas y scikit-learn. Se usa al escribir bibliotecas, no al analizar
   datos.

### 6.5 Pruebas unitarias en datos

1. Por qué probar: la función que hoy funciona, mañana alguien la edita.
2. pytest sobre el paquete local: archivos `test_*.py`, funciones `assert`, y el punto verde
   que da permiso de confiar.
3. Casos frontera: la lista vacía, el `NaN`, el valor negativo que no debería existir.
4. Pruebas sobre los datos: rangos físicos, huecos inesperados, columnas que deben existir —
   la validación manual de la Unidad 3, ahora automática y repetible.
5. El ciclo completo: cambiar el paquete, correr las pruebas, hacer commit.

### Ejercicios sugeridos

1. Poner el proyecto del curso bajo git: `init`, `.gitignore` razonado en Markdown, y el primer
   commit con mensaje digno.
2. Reconstruir la historia: hacer cinco cambios pequeños con cinco commits, y leer el `git log`
   como narrativa del proyecto.
3. Subir el proyecto a GitHub, clonarlo en otra carpeta, y reconstruir el entorno con `uv sync`
   — la reproducibilidad completa: código versionado más entorno declarado.
4. Extraer a un paquete local las tres funciones más repetidas en las libretas propias, con
   docstrings, e importarlas desde una libreta limpia.
5. Activar `autoreload`, editar una función del paquete con la libreta abierta, y verificar el
   cambio sin reiniciar el kernel.
6. Perfilar con `%prun` una libreta de limpieza de la Unidad 3 completa, y reportar en Markdown
   dónde vive el cuello de botella.
7. Escribir dos versiones de un cálculo sobre un millón de puntos — ciclo puro y NumPy — y
   perfilar ambas: ¿cuánto explica la vectorización?
8. Acelerar con `@njit` una función numérica que NumPy solo no resuelve (un ciclo con
   dependencia del paso anterior), y medir el antes y el después con `%timeit`.
9. Intentar `@njit` sobre una función con pandas adentro, leer el error con calma, y explicar
   en Markdown por qué numba la rechaza.
10. Escribir pruebas pytest para una función propia: el caso normal, la lista vacía, el `NaN`.
11. Escribir la prueba de los datos: un `test_datos.py` que valide rangos físicos, columnas
    esperadas y continuidad temporal del `data/processed` del proyecto.
12. Romper una función del paquete a propósito, ver las pruebas fallar, arreglarla, y hacer el
    commit — el ciclo de trabajo completo, vivido una vez.

### Al terminar la unidad

- Versionar un proyecto con git: commits con mensajes que narran, `.gitignore` con criterio, y
  respaldo en GitHub.
- Clonar un proyecto ajeno y dejarlo corriendo con `uv sync` — y explicar por qué eso es
  reproducibilidad.
- Graduar funciones de la libreta a un paquete local importable, y trabajar con `autoreload`.
- Encontrar el cuello de botella con un perfil antes de tocar una sola línea.
- Acelerar una función numérica con numba, saber cuándo no aplica, y decir qué es Cython.
- Proteger el proyecto con pruebas: las del código con pytest, y las de los datos con
  validaciones automáticas.

---

## Unidad 7 · Conceptos avanzados de manipulación de datos y visualización de datos
> **Objetivo.** Que cada estudiante cierre el curso dominando las tres operaciones que el
> análisis serio de series de medición exige — tratar huecos con criterio, cambiar de frecuencia
> respetando la física de la variable, y responder preguntas por grupos — y sea capaz de
> publicar sus resultados en un dashboard de Quarto que se regenera desde los datos.

**10 h en el programa oficial**

### 7.1 Datos faltantes

1. El censo de huecos antes de tratarlos: cuántos, dónde, de qué tamaño — el hueco de cinco
   minutos y el de una semana no se tratan igual.
2. Rellenos con memoria: `ffill` y `bfill`, y su freno (`limit`) — cuándo copiar el pasado es
   razonable y cuándo es inventar.
3. `interpolate` a fondo: lineal, temporal, y el argumento `limit`; la Unidad 3 eligió entre
   tres opciones, ahora se domina cada una.
4. Honestidad gráfica: el dato interpolado se señala en la figura — lo inventado se declara,
   como toda decisión de limpieza en este curso.

### 7.2 Cambio de frecuencia

1. `resample`, la promesa de la Unidad 3 cumplida: la gramática completa — la regla (`'h'`,
   `'D'`, `'ME'`) y la función que resume.
2. La física decide la agregación: la irradiancia se promedia, la energía se suma, la ráfaga
   es un máximo — la misma variable, tres preguntas distintas.
3. Subir la frecuencia: `asfreq` y el reindexado temporal; los `NaN` que aparecen son huecos
   nuevos, y 7.1 ya sabe qué hacer con ellos.
4. Ventanas móviles: `rolling` — suavizar el ruido sin cambiar la frecuencia.

### 7.3 Agrupación de datos

1. `groupby`: la idea anunciada desde la Unidad 3, por fin completa — separar, aplicar,
   combinar.
2. `resample` era un `groupby` con reloj: ahora se agrupa por lo que sea — el mes, el día de
   la semana, el sensor.
3. `agg`: varias estadísticas de un golpe, con columnas resultantes bien nombradas.
4. Ancho y largo: `pivot_table` y `melt` — el heatmap quiere la tabla ancha, seaborn la quiere
   larga; cambiar de forma es cambiar de pregunta.
5. El patrón mental: toda pregunta que empieza con "¿qué mes…?, ¿qué sensor…?" es un `groupby`
   esperando a ser escrito.

### 7.4 Visualizaciones avanzadas: heatmaps, boxplots, histogramas, violin plots

1. Distribuciones: el histograma revisitado, el boxplot, el violin — qué muestra y qué esconde
   cada uno; el bigote tiene definición: cuartiles e IQR.
2. seaborn cosecha su lugar en el mapa de la Unidad 4: las figuras de distribución por
   categoría en una línea, sobre los `Axes` de siempre.
3. El heatmap: la matriz de días por horas de la Unidad 5, ahora como mapa de calor — el año
   entero de un sensor en una sola figura.
4. El calendario anual (calplot): el heatmap que se lee como agenda — el año de un vistazo, en
   el idioma de todo el mundo.
5. La rosa de vientos: el eje polar — cuando la variable es una dirección, el eje recto miente.
6. El joyplot (joypy): las distribuciones mes a mes apiladas como paisaje — lo que el violin
   cuenta, contado como serie.
7. Elegir con criterio, otra vez: cuándo una distribución, cuándo un mapa, cuándo un ángulo —
   y la figura avanzada también se explica sola.

### 7.5 Dashboards con Quarto

1. Qué es Quarto: Markdown y celdas de código que se ejecutan al renderizar — la libreta y el
   `.qmd` son parientes. La revelación final del curso: este sitio está hecho con Quarto.
2. De libreta a documento: `quarto render`, y el análisis se vuelve HTML o PDF que viaja solo.
3. `format: dashboard`: los encabezados se vuelven layout — filas, columnas, tarjetas y *value
   boxes*.
4. Las figuras del curso entran todas: matplotlib para lo que se imprime, plotly donde el
   tablero pide zoom y *hover* — el criterio de la Unidad 4, revisitado.
5. El tablero reproducible: se regenera desde `data/processed` con un comando, como todo lo
   demás en este curso.

### Ejercicios sugeridos

1. Hacer el censo de huecos de un año de datos: cuántos, dónde, de qué duración; reportarlo en
   una tabla con el hueco más largo señalado.
2. Sobre el mismo dataset, tratar un hueco de minutos y uno de días con `ffill`, `interpolate`
   y nada: argumentar en Markdown qué merece cada uno.
3. Producir la figura honesta: la serie con sus tramos interpolados marcados visualmente
   distinto.
4. Bajar la frecuencia de un año de irradiancia de minutos a horas y a días, eligiendo entre
   promedio y suma según la pregunta — y explicar por qué la agregación cambia.
5. Suavizar una serie ruidosa con `rolling` y graficar cruda y suavizada en el mismo `Axes`,
   con la leyenda obligada.
6. Responder tres preguntas con `groupby` y `agg`: el mes más ventoso, el día de la semana con
   más demanda, el sensor con más huecos.
7. El perfil diario promedio de cada mes: un `groupby` doble, pivotado a tabla de meses por
   horas.
8. Convertir esa tabla en heatmap con barra de color etiquetada — el año entero en una figura.
9. Comparar la distribución mensual de una variable con boxplot y con violin: qué enseña el
   violin que el boxplot esconde.
10. Las figuras de la casa: la rosa de vientos del año y el calendario anual de una variable;
    una línea de Markdown por figura diciendo qué pregunta responde.
11. Convertir una libreta de análisis propia en un `.qmd` y renderizarla a HTML con Quarto.
12. Construir el dashboard del proyecto: *value boxes* con las cifras clave, el heatmap anual,
    los perfiles por mes — regenerable con `quarto render`.
13. El cierre del curso: entregar el repositorio completo — crudos intactos, paquete probado,
    `data/processed`, figuras y dashboard — clonable y reproducible de punta a punta por
    cualquiera.

### Al terminar la unidad

- Censar los huecos de una serie y tratarlos con criterio declarado — y señalar en la figura lo
  interpolado.
- Cambiar de frecuencia eligiendo la agregación por la física de la variable, y suavizar con
  ventanas móviles.
- Traducir preguntas por categorías a `groupby` y `agg`, incluyendo agrupaciones dobles.
- Elegir y construir la figura de distribución correcta, y condensar un año de datos en un
  heatmap.
- Explicar qué es Quarto y convertir una libreta en un documento que se renderiza.
- Publicar un dashboard reproducible que se regenera desde `data/processed` con un comando.
- Entregar un proyecto de ciencia de datos completo — versionado, probado, documentado y
  reproducible — que funcione como carta de presentación.

---

## Unidad 8 · Vibe coding con Quarto y Claude: analiza, documenta, itera y escribe tu tesis
> **Objetivo.** Que cada estudiante use asistentes de IA como acelerador sin ceder el criterio:
> analizar datos conversando con Claude, verificar lo generado con las herramientas del curso —
> reproducibilidad, pruebas, figuras honestas —, iterar con historia en git, y montar su tesis
> como proyecto de Quarto donde el texto, el análisis y las figuras viven y se regeneran juntos.

**Adicional al programa oficial**

### 8.1 Qué es vibe coding

1. Programar conversando: describir la intención, leer lo propuesto, decidir — el código se
   negocia, no se dicta.
2. Por qué esta unidad va al final: el criterio se entrenó quince semanas; sin él, el asistente
   maneja y tú vas de pasajero.
3. El panorama: Claude en el chat, Claude Code en la terminal, asistentes dentro del editor —
   la misma conversación en tres lugares.

### 8.2 Analiza: el asistente dentro del proyecto

1. El contexto lo es todo: el proyecto bien formado de la Unidad 1 — estructura, nombres,
   entorno declarado — es exactamente lo que un asistente necesita leer para ayudar de verdad.
2. Pedir bien: la pregunta con sus datos, sus unidades y el resultado esperado; el mismo rigor
   que un docstring.
3. Verificar siempre: lo generado corre desde cero, pasa las pruebas de la Unidad 6, y la
   figura dice lo que dicen los datos.
4. La regla nueva del curso: ningún código que no puedas explicar línea por línea — quien firma
   eres tú, no el asistente.

### 8.3 Documenta e itera

1. La libreta sigue siendo el documento: lo que el asistente aporta se integra a la narrativa
   computacional, no se pega como vino.
2. Los errores como conversación: el traceback se entrega completo, la explicación se lee con
   escepticismo, la corrección se verifica.
3. Iterar con historia: cada vuelta con el asistente termina en commit — git registra qué
   cambió, y el `diff` cuenta qué hizo realmente la "ayuda".

### 8.4 Escribe tu tesis con Quarto

1. La tesis como proyecto de Quarto: capítulos `.qmd`, el `format: book` — el dashboard de la
   Unidad 7 tiene un hermano mayor.
2. Figuras vivas: las figuras del proyecto entran solas y se regeneran si cambian los datos —
   nadie vuelve a pegar una imagen desactualizada.
3. Citas y referencias: BibTeX, referencias cruzadas, números de figura y de tabla que se
   cuidan solos.
4. Congelar capítulos: `freeze: auto` — el capítulo con cómputo pesado no se re-ejecuta en
   cada render, solo cuando cambia; si los datos cambiaron, se descongela tocando el capítulo
   o borrando `_freeze/`. La tesis entera renderiza en segundos.
5. `quarto render` a PDF: el LaTeX de la Unidad 4 paga completo — la tesis sale tipografiada.
6. El cierre del curso: la tesis reproducible — quien la lea puede clonarla, reconstruir el
   entorno y regenerar cada número y cada figura.

### Ejercicios sugeridos

1. Pedirle al asistente una función que ya escribiste en el curso, comparar ambas versiones, y
   quedarte con lo mejor de cada una — explicando por qué.
2. Analizar un dataset nunca visto conversando con Claude, aplicando en cada paso las reglas
   del curso: diagnóstico antes de cirugía, decisiones declaradas, figura honesta.
3. Recibir del asistente una solución con un error sutil (sembrado por el profesor) y cazarlo
   con las pruebas de la Unidad 6 — la moraleja se escribe en Markdown.
4. Entregar un traceback completo al asistente, verificar su corrección propuesta, y
   documentar qué entendió bien y qué no.
5. Iterar una figura con el asistente hasta calidad de tesis: un commit por vuelta, y el
   `git log` como bitácora de la conversación.
6. Montar el esqueleto de la tesis en Quarto: capítulos, bibliografía en BibTeX, y una figura
   viva que se regenera desde `data/processed`.
7. Escribir un capítulo de avance real de la tesis propia, con sus citas y sus referencias
   cruzadas, y renderizarlo a PDF.
8. El examen final silencioso: intercambiar tesis por parejas, clonar la del compañero,
   reconstruir el entorno y regenerar el PDF completo — si compila con sus figuras, el curso
   cumplió.

### Al terminar la unidad

- Conversar con un asistente de IA describiendo intención, contexto y resultado esperado — y
  leer críticamente lo que proponga.
- Verificar código generado con las armas del curso: corre desde cero, pasa las pruebas, la
  figura es honesta.
- Iterar con historia: cada colaboración con el asistente registrada en commits que narran.
- Montar una tesis en Quarto con figuras vivas, citas en BibTeX y referencias cruzadas, y
  renderizarla a PDF.
- Entregar el paquete completo — proyecto y tesis reproducibles — y explicar por qué eso vale
  más que cualquier archivo suelto.

