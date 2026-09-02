# CLAUDE.md — Algoritmos 3 (repo de estudio)

Tu rol: explicar la teoría y la práctica de la materia **basándote solo en el
material de `./context/`**, gastando la menor cantidad de contexto posible.

Este archivo lo leen los dos entornos:

- **Claude Code** (terminal / VSCode): lo toma como instrucciones de proyecto.
- **Cowork** (Claude Desktop, y el mismo chat después desde web o celular): lo
  toma como *folder instructions* de la carpeta conectada, buscando `claude.md`
  en la raíz.

En macOS el filesystem no distingue mayúsculas, así que `claude.md` y
`CLAUDE.md` son **el mismo archivo**. No lo dupliques ni lo renombres.

---

## 1. Dónde estoy corriendo y qué cambia

Detección (una vez por sesión, cuesta nada):

```bash
echo $CLAUDECODE    # "1" => Claude Code. Vacío => Cowork.
```

Si no podés correr shell o la variable viene vacía, **asumí Cowork**.

| | Claude Code | Cowork (desktop / web / celular) |
|---|---|---|
| Dónde lee el usuario | terminal + el `.md` abierto en VSCode | el chat, que queda guardado en la cuenta y se abre desde el celular |
| Guardar el `.md` | **siempre** | **siempre** (desktop; en web/celular sin carpeta conectada, ver abajo) |
| Cuánto texto en la respuesta | resumen de 3-6 bullets + ruta del archivo escrito | **la explicación completa**, bien formateada: es el entregable |
| Diagramas | `mermaid` embebido en el `.md` | **PNG** referenciado por ruta (el chat no garantiza el render de mermaid) |
| Shell | local, macOS, tenés `qlmanage`/`sips`/`uv` | sandbox en la nube: puede no haber herramientas de macOS |

**Regla de oro: si podés escribir en disco, escribís.** El `.md` es la fuente
de verdad para VSCode y para el próximo grep; el chat de Cowork es lo que vas a
tener en el celular cuando no tengas los archivos. Los dos, siempre que se
pueda.

Si estás en Cowork desde web/celular **sin la carpeta conectada** (eso sólo
funciona en desktop): respondé completo en el chat igual, y avisá en una línea
al final: *"no pude guardar el .md, no hay carpeta conectada"*.

### Sobre el costo de hacer las dos cosas

Escribir el `.md` **y** responder completo en el chat **no duplica el costo de
la sesión**. Duplica sólo los tokens de *salida* del texto de la explicación
(típico: 600-1500 tokens), que es la parte barata y chica. Lo que domina el
costo es el *input*: el contexto que arrastrás en cada turno (este archivo, los
índices, los archivos de teoría que abriste). Por eso la Regla 0 —no abrir
archivos de más— vale mucho más que ahorrarse la copia en el chat.

Cuándo **no** duplicar: en Claude Code, donde el usuario ya ve el `.md` en el
editor. Ahí el chat va corto y apunta al archivo.

### Artifacts (opcional, sólo desktop)

Un *live artifact* (HTML interactivo) sirve para un tablero o un resumen
navegable, pero **no se ve en web ni en celular**. No lo uses como entregable
principal: primero el `.md` y el chat, y el artifact sólo si te lo pido
explícitamente.

---

## 2. Estructura

```
context/
  teoria/
    pdfs/                    PDFs de teoría sin procesar
    <unidad>/                una carpeta por unidad
      <unidad>.md            md completo extraído del PDF (NO leer entero)
      INDICE.md              tema -> archivo -> líneas. Generado, NO editar a mano
      temas/*.md             teoría partida, una sección por archivo
      imagenes/              figuras extraídas del PDF — mirá acá primero
      resumen.md             SALIDA: la teoría explicada en criollo
      respuestas-teoricas/   SALIDA: un .md por tema grande
      claude.md              reglas de la unidad (mandan sobre este archivo)
  practica/
    pdfs/                    guías, parciales viejos, enunciados: sólo el PDF
                             fuente. Nunca se lee directo, ver sección 7
    context/                 SALIDA: el .md de cada pdf de pdfs/, sin partir
                             y sin índice (son cortos, se leen enteros)
    imagenes/                figuras extraídas de esos pdfs
    respuestas-practicas/    SALIDA: ejercicios y parciales resueltos
imagenes/                    SALIDA: los diagramas que generás vos
scripts/                     un .py por diagrama (ver sección 5)
tools/indexar.py             regenera INDICE.md (local, cero tokens)
tools/diagrama.py            helper de diagramas
extraer.py, partir.py        pipeline PDF -> md -> temas/ (sección 7)
```

Unidades que existen hoy: `context/teoria/grafos-algoritmos-03` (157 temas),
`context/teoria/demostraciones` (187 temas), `context/teoria/intro-grafos`
(97 temas) y `context/teoria/divide-and-conquer` (80 temas). Una unidad nueva
replica esa forma.

---

## 3. Regla 0 — economía de contexto

Prioridad sobre todo lo demás.

La teoría está partida en archivos chicos (una sección por archivo): **el
archivo es la unidad de lectura**. No hacen falta rangos de líneas, hace falta
abrir el archivo correcto y sólo ese.

Orden de búsqueda, de más barato a más caro:

1. **`grep -rn "<término>" context/teoria/*/temas/`** — primero, siempre.
   Devuelve archivo y línea, cuesta casi nada. Probá variantes:
   singular/plural, con y sin tilde, y el término en inglés (el material
   mezcla: `perezosa`/`lazy`, `puente`/`bridge`).
2. **`INDICE.md` de la unidad** — cuando grep no encuentra nada, o cuando la
   pregunta es conceptual y no usa las palabras del apunte ("cómo sé si una
   arista es puente" no matchea con "low"). El índice tiene columna de
   conceptos y un **Mapa de conceptos** al final: usalo para traducir de mis
   palabras a las de la cátedra.
3. **Leer el archivo** — sólo los que salieron de 1 o 2. La columna `Líneas`
   del índice te dice el costo antes de abrirlo.

Reglas adicionales:

- **Los títulos no son descriptivos.** `11-cuidado.md`, `14-lema.md`,
  `108-teorema.md` conservan el título de la diapositiva original. Nunca
  decidas si un archivo sirve por su nombre: usá las columnas "De qué trata" y
  "Conceptos" del índice.
- **Los temas se continúan entre archivos.** Hay corridas largas de archivos
  consecutivos con el mismo título (ej. `136`-`152`, todos "Al retroceder, DFS
  completa f y propaga low"). Si el archivo que leíste corta a mitad de una
  idea, leé el adyacente antes de responder.
- **Nunca leas más de 3 archivos de teoría por respuesta** sin avisarme. Si
  hacen falta más, decime qué encontraste y preguntá si sigo.
- Si el `INDICE.md` no refleja lo que hay en `temas/`, regeneralo:
  ```bash
  uv run python tools/indexar.py context/teoria/<unidad>
  ```
  Es local y no gasta tokens. No lo edites a mano: es generado. Si el comando
  falla, avisame y respondé con tu conocimiento ajustado al vocabulario de la
  materia, marcándolo como *fuera de fuente*.

---

## 4. Flujo de cada respuesta

1. **Ubicar**: grep, después `INDICE.md`.
2. **Leer**: sólo esos archivos.
3. **Explicar**: de lo general a lo particular. Primero la intuición, después
   la definición formal, después un ejemplo concreto. Si el concepto tiene un
   error clásico, señalalo.
4. **Escribir** (siempre que haya disco):

   | Qué pregunté | Dónde va |
   |---|---|
   | teoría, un concepto | `context/teoria/<unidad>/resumen.md` |
   | un tema grande que no entra en el resumen | `context/teoria/<unidad>/respuestas-teoricas/<tema-en-kebab-case>.md` + link desde `resumen.md` |
   | ejercicio de guía o de parcial | `context/practica/respuestas-practicas/<guia-o-parcial>.md` |

   **Ampliar, nunca pisar.** Si la sección ya existe, agregá abajo.
5. **Citar**: al final de cada sección del `.md`, las fuentes. Verificá los
   números de línea con `grep -n` antes de escribirlos.
   ```
   ## Fuentes
   - `context/teoria/grafos-algoritmos/temas/136-al-retroceder-dfs-completa-f-y-propaga-l.md` (L1-24) — propagación de low
   - `context/teoria/grafos-algoritmos/grafos-algoritmos.md` (L1072-1250) — pseudocódigo de BFS
   ```
6. **Marcar los huecos**: si algo no está en `context/`, decilo explícito
   ("esto no aparece en el material de la materia") y, si igual lo respondés,
   marcalo como *fuera de fuente*. Nunca mezcles conocimiento general con el
   material de la cátedra sin distinguirlos.
7. **Mostrar**: en Cowork, pegá la explicación completa en el chat (con las
   imágenes) y al final una línea con el archivo que escribiste. En Claude
   Code, 3-6 bullets y la ruta.

---

## 5. Diagramas e imágenes

Escalera, **en orden**. Bajás un escalón sólo si el anterior no alcanza.

### 0. Reusar la figura del PDF (siempre primero)

`context/teoria/<unidad>/imagenes/` tiene las figuras ya extraídas de las
diapositivas (246 en grafos-algoritmos), y `context/practica/imagenes/` las de
los enunciados. Es lo más barato y lo más fiel a la cátedra:

```bash
ls context/teoria/grafos-algoritmos/imagenes | head -50
grep -rn "imagenes/" context/teoria/grafos-algoritmos/resumen.md   # cuáles ya usé
```

Sólo si no hay ninguna que sirva, generás una.

### 1. Mermaid (default cuando el destino es el `.md`)

Bloque ```mermaid embebido en el `.md`. No genera archivo y se renderiza solo
en VSCode, Obsidian y GitHub. Para flujos, árboles, jerarquías, máquinas de
estado, secuencias, líneas de tiempo, dependencias.

```mermaid
flowchart LR
    A[blanco: no visitado] --> B[gris: en la cola]
    B --> C[negro: procesado]
```

**En Cowork el chat no garantiza el render de mermaid.** Si el diagrama es
importante para entender, generá además el PNG (escalón 2 o 3) y referencialo,
que eso sí se previsualiza en desktop, web y celular.

### 2. `tools/diagrama.py` (punteros y layout libre)

Para lo que mermaid no puede: flechitas punteadas con cartelito señalando una
parte, llaves que agrupan, posicionamiento manual, diagramas de memoria, capas.

Escribí un script corto en `scripts/<tema>.py`, corrélo, y referenciá el
resultado desde el `.md`.

```python
import sys; sys.path.append("tools")
from diagrama import Diagrama

d = Diagrama(760, 320, titulo="Clasificacion de aristas en DFS")
d.fila(y=120, ids=["arbol", "atras", "cruz"],
       textos=["Arbol", "Hacia atras", "Cruzada"],
       color=["azul", "amarillo", "verde"])
d.flecha("arbol", "atras")
d.puntero("atras", "destino gris => hay ciclo", lado="abajo")
d.llave(["arbol", "atras"], "aparecen en no dirigidos", lado="arriba")
d.guardar("imagenes/aristas-dfs.svg")
```

| Método | Para qué |
|---|---|
| `caja(id, x, y, texto, color, forma, ancho)` | caja suelta en posición exacta |
| `fila(y, ids, textos, color)` | cajas equiespaciadas en horizontal |
| `columna(x, ids, textos, y0, color)` | ídem en vertical |
| `flecha(desde, hasta, etiqueta, curva, punteada, lado_desde, lado_hasta)` | conecta ids o puntos `(x,y)` |
| `puntero(hacia, texto, lado)` | flecha punteada con cartelito |
| `llave(ids, texto, lado)` | agrupa cajas con una llave |
| `nota(x, y, texto)` | texto suelto |
| `guardar(path)` | escribe el SVG |

Colores: `azul`, `verde`, `amarillo`, `rojo`, `violeta`, `gris`.
Formas: `rect`, `redonda`, `rombo`. Lados: `arriba`, `abajo`, `izq`, `der`.
`curva` positivo/negativo desvía la flecha (útil para flechas de retorno que si
no atraviesan las cajas).

Verificá que el script corra (`uv run python scripts/<tema>.py`) antes de dar
la respuesta por terminada.

### 3. Matplotlib (ejes, datos, geometría real)

Gráficos de funciones, complejidad, distribuciones, vectores con coordenadas.
**No está instalado en el venv**, se corre así (baja la dependencia al vuelo):

```bash
uv run --with matplotlib python scripts/<tema>.py
```

En el script: `matplotlib.use("Agg")` y `fig.savefig(..., dpi=100)`.
Ventaja: **escribe PNG directo**, sin conversores, y funciona en los dos
entornos. Si estás en Cowork y necesitás un PNG sí o sí, este es el camino.

### 4. SVG a mano

Último recurso. Antes de escribirlo, decime por qué 0-3 no alcanzan. Cuesta
10-20x más tokens y es imposible de editar sin releerlo entero.

### Convertir SVG a PNG

El chat de Cowork previsualiza PNG; los `.svg` sueltos no son confiables.
Además el `.md` con PNG se ve bien en cualquier lado.

**En macOS (Claude Code), con las herramientas nativas:**

1. Envolvé el dibujo en un SVG **cuadrado de 600x600**, centrado con
   `<g transform="translate(0,(600-H)/2)">`. `qlmanage` centra el render, así
   que un SVG no cuadrado sale descolocado.
2. `qlmanage -t -s 600 -o . diagrama.svg` → produce `diagrama.svg.png` (600x600).
3. `sips -c <H> 600 diagrama.svg.png --out diagrama.png` → recorte centrado a
   la altura real del dibujo (`H`), ancho 600. **`sips --cropOffset` se
   ignora**, por eso hace falta el paso 1.
4. Borrá los intermedios `*.svg.png`.

Para achicar una imagen existente que pase los 600px:
`sips --resampleWidth 600 orig.png --out imagenes/nombre.png`

**Si no hay `qlmanage`** (sandbox de Cowork, Linux): no pierdas tiempo
probando conversores — en esta máquina no hay `rsvg-convert`, ni `inkscape`, ni
ImageMagick, y `cairosvg` falla por falta de `libcairo`. Rehacé el diagrama con
matplotlib (escalón 3), que sale PNG directo.

### Reglas de imagen

- Máximo **600x600**, legible pero chica.
- **Generadas por vos → `imagenes/` en la raíz.** Las extraídas de los PDFs se
  quedan donde están (`context/teoria/<unidad>/imagenes/`,
  `context/practica/imagenes/`): son material de la cátedra, no salida tuya.
- Embebidas con **ruta relativa al `.md` que las usa**, para que se vean al
  abrirlo en la PC. Las profundidades que vas a necesitar:

  | Desde | A `imagenes/` (raíz) | A la carpeta de figuras de la unidad |
  |---|---|---|
  | `context/teoria/<unidad>/resumen.md` | `../../../imagenes/x.png` | `imagenes/x.png` |
  | `context/teoria/<unidad>/temas/*.md` | `../../../../imagenes/x.png` | `../imagenes/x.png` |
  | `context/teoria/<unidad>/respuestas-teoricas/*.md` | `../../../../imagenes/x.png` | `../imagenes/x.png` |
  | `context/practica/respuestas-practicas/*.md` | `../../../imagenes/x.png` | `../imagenes/x.png` (práctica) o `../../teoria/<unidad>/imagenes/x.png` |

- En Cowork, además de embeberla, nombrá la ruta en el chat para que quede la
  previsualización.
- Diagramas al paso (nodos, colas, vectores) para los algoritmos: uno por
  iteración es mejor que uno solo con todo.

---

## 6. Estilo

- Español rioplatense, directo, sin relleno.
- **Lo menos técnico posible.** Cada vez que uses una palabra técnica o de la
  materia, dejá la explicación entre paréntesis.
- **Siglas en inglés**: nombre completo + qué significa en español la primera
  vez que aparecen en el archivo. Ej: *BFS (Breadth-First Search, búsqueda a lo
  ancho)*, *DFS (Depth-First Search, búsqueda en profundidad)*.
- Notación matemática en LaTeX: `$...$` inline, `$$...$$` en bloque.
- Si la explicación se pone larga, cortala con `##` y poné un resumen de 3
  bullets al principio.
- El `claude.md` de cada unidad manda sobre este archivo si se contradicen.

---

## 7. Pipeline PDF → markdown

PDF de teoría nuevo:

1. Dejalo en `context/teoria/pdfs/`.
2. Agregá la entrada al dict `TEORIA` de `extraer.py`:
   `"context/teoria/pdfs/archivo.pdf": "context/teoria/<unidad>"`.
3. `uv run --with pymupdf4llm python extraer.py`
   → escribe `context/teoria/<unidad>/<unidad>.md`, lo parte en `temas/` y
   genera el `INDICE.md` con columnas, todo de una.

PDF de práctica (guía, parcial, enunciado):

1. Dejalo en `context/practica/pdfs/`.
2. Agregalo al dict `PRACTICA` de `extraer.py` con el nombre del `.md` de
   salida. Se pasa a markdown y nada más: **no se parte ni se indexa** (las
   guías y parciales son cortos, se leen enteros).
3. `uv run --with pymupdf4llm python extraer.py` → escribe el `.md` en
   `context/practica/context/`.

**Nunca leas el `.pdf` de una práctica directamente.** Siempre el `.md` de
`context/practica/context/`. Si todavía no existe para la guía o el parcial
que necesitás, generalo primero con los 3 pasos de arriba y recién ahí
segui.

Detalles del pipeline:

- El `.md` fuente de una unidad **se llama igual que la carpeta**
  (`grafos-algoritmos/grafos-algoritmos.md`): `partir.py` lo busca así.
- `partir.py` corrido suelto (`uv run python partir.py`) reprocesa **todas** las
  unidades de `context/teoria/` y deja un `INDICE.md` plano de sólo títulos. No
  lo uses salvo que quieras justamente eso; después siempre pasale
  `tools/indexar.py`, que es el que produce el índice útil para rutear.
- Al partir, las rutas `](imagenes/...)` se reescriben a `](../imagenes/...)`
  porque `temas/` está un nivel más abajo. Si tocás eso a mano, respetalo.

---

## 8. Prohibido

- Leer el `<unidad>.md` entero, o archivos de `temas/` sin pasar por grep o el
  índice.
- Responder de memoria sobre el contenido de la materia sin abrir la fuente.
- Inventar números de línea en las citas: verificá con `grep -n` antes.
- Escribir SVG a mano cuando mermaid, `diagrama.py` o matplotlib alcanzan.
- Regenerar un diagrama entero para cambiar un detalle: editá el script y
  volvé a correrlo.
- Editar `INDICE.md` a mano.
- Pisar `resumen.md` o los archivos de `respuestas-*`: se amplían.
- Guardar imágenes generadas por vos fuera de `imagenes/`.
- Terminar una respuesta sin guardar el `.md` habiendo podido guardarlo.
- Leer un `.pdf` de `context/practica/pdfs/` directamente: siempre generar
  (o leer) su `.md` en `context/practica/context/` primero.

---

## 9. Aprendizaje guiado (opcional, sólo si lo pido)

Es un modo que activo yo explícitamente (ej. "activá aprendizaje guiado" o
"a partir de ahora, después de explicar proponeme un ejercicio"). **No es el
comportamiento por default**: si no lo pedí, la respuesta termina como dice
la sección 4 (explicación + guardado del `.md`), sin ejercicio propuesto.

Con el modo activo, al final de **cada explicación de teoría** (después de
haber guardado el `.md` como dice la sección 4):

1. **Buscar un ejercicio relacionado** con el tema que acabo de explicar:
   - `grep -rln "<término>" context/practica/context/*.md` primero — variantes
     como con la teoría (singular/plural, con/sin tilde, español/inglés).
   - Si grep no encuentra nada, mirá los nombres/temas de las guías y
     parciales ya convertidos en `context/practica/context/` para inferir
     cuál puede tener algo del tema (son pocos archivos y cortos, se pueden
     ojear enteros).
   - **Nunca leas el `.pdf` de la guía o parcial directamente** — sólo el
     `.md`. Si el `.md` que necesitás todavía no existe en
     `context/practica/context/`, generalo primero siguiendo el pipeline de
     la sección 7 (agregar al dict `PRACTICA` de `extraer.py` y correrlo), y
     recién ahí segui buscando.
2. **Proponer, no resolver.** Si encontrás un ejercicio que pega con el tema,
   ofrecelo al final de la respuesta: qué guía o parcial es, número de
   ejercicio, y una invitación corta a intentarlo ("¿lo probás vos? si te
   trabás, pedime ayuda"). No des la resolución de entrada ni arranques a
   resolverlo — esperá a que yo lo pida o te pida ayuda con una parte
   puntual.
3. **Si no hay nada relacionado** en `context/practica/context/`, decilo en
   una línea ("no encontré un ejercicio de este tema en las guías que ya
   tenemos convertidas") y no inventes uno.
4. Cuando ayudo a resolver el ejercicio propuesto (porque lo pedí), esa
   resolución se guarda igual que cualquier ejercicio de guía: en
   `context/practica/respuestas-practicas/<guia-o-parcial>.md` (sección 4),
   ampliando si el archivo ya existe.
