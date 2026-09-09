# Resumen — Intro a grafos

## Grafo no dirigido

**Intuición.** Un grafo modela objetos y una relación entre ellos: los objetos
son los **vértices** (o nodos), y cada par de objetos relacionados se une con
una **arista** (la línea que los conecta). "No dirigido" quiere decir que la
relación es **simétrica**: si $u$ está conectado con $v$, entonces $v$ está
conectado con $u$; la arista no tiene sentido, es una calle de doble mano.

Ejemplos de relación simétrica: "son amigos en una red social", "hay un cable
entre estas dos computadoras", "estas dos ciudades están unidas por una ruta".

**Definición formal.** Un grafo es $G = (V, E)$ donde $V$ es el conjunto de
vértices y $E$ el conjunto de aristas. En un grafo no dirigido una arista se
escribe como un **conjunto de dos elementos**:

$$e = \{u, v\} \qquad \text{(o abreviado } uv\text{)}$$

Como es un conjunto, no hay orden: $\{u, v\}$ y $\{v, u\}$ son la misma arista.
$u$ y $v$ son los **extremos** de $e$, y se dice que $e$ **incide** en $u$ y en
$v$. Notación de adyacencia:

$$u \sim v \iff uv \in E(G)$$

("$u$ es adyacente a $v$ si y solo si existe la arista $uv$").

**Contraste: digrafo (grafo dirigido).** Si la relación **no** es simétrica
—"$u$ sigue a $v$" en Twitter, "el vuelo va de $u$ a $v$", "la tarea $u$ debe
hacerse antes que $v$"— se usa un **digrafo** $D = (V, A)$, donde cada **arco**
es un **par ordenado**:

$$(u, v) \in A(D), \qquad (u, v) \neq (v, u)$$

Ahí sí importa el sentido: la flecha va de $u$ a $v$ y no al revés.

| | Grafo no dirigido | Digrafo (dirigido) |
|---|---|---|
| Elemento que conecta | arista $\{u,v\}$ | arco $(u,v)$ |
| ¿Tiene sentido? | no (doble mano) | sí (flecha) |
| $uv$ vs $vu$ | son la misma | son distintos |
| Notación del grafo | $G = (V, E)$ | $D = (V, A)$ |

**Error clásico.** Confundir "grafo orientado" con "digrafo". Un grafo
orientado se obtiene de un grafo no dirigido eligiendo **una** dirección para
cada arista, así que nunca tiene los dos arcos $(u,v)$ y $(v,u)$ a la vez. Un
digrafo sí puede tener ambos.

## Fuentes

- `context/teoria/intro-grafos/temas/16-aristas-no-dirigidas.md` (L11, L22, L24) — arista como conjunto $\{u,v\}$, extremos, incidencia, notación $u \sim v$
- `context/teoria/intro-grafos/temas/22-definici-n.md` (L11-15, L28) — digrafo $D=(V,A)$, arco como par ordenado $(u,v) \neq (v,u)$
- `context/teoria/intro-grafos/temas/42-orientaciones-de-un-grafo.md` (L3) — grafo orientado = elegir dirección para cada arista
- `context/teoria/intro-grafos/temas/02-redes-de-transporte.md` (L19) — cuándo conviene no dirigido vs digrafo
