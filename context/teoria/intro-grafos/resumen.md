# Resumen — Introducción a grafos

Tres cosas para llevarse:

- Un grafo es un **par $(V, E)$**, no un dibujo. Dos dibujos distintos pueden ser
  el mismo grafo (isomorfismo), y el mismo dibujo puede engañar.
- Casi toda la unidad son **caracterizaciones**: "X pasa **si y sólo si** Y".
  Cada una es una herramienta para reemplazar una condición difícil de chequear
  por otra fácil.
- Los invariantes (grados, cantidad de aristas, ciclos) sirven para **descartar**
  isomorfismo, nunca para confirmarlo.

---

## 1. Definiciones básicas

Un **grafo** es un par
$$G = (V, E),$$
donde $V = V(G)$ es el conjunto de **vértices** y $E = E(G)$ el de **aristas**.
Una arista representa una relación entre dos vértices.

En un grafo **no dirigido** una arista se escribe $e = \{u,v\}$ o simplemente
$uv$; $u$ y $v$ son los **extremos** y decimos que $e$ **incide** en ellos.
Notación: $u \sim v \iff uv \in E(G)$.

Un **digrafo** es un grafo donde las aristas tienen dirección: $D = (V, A)$, y
cada **arco** es un par **ordenado** $(u,v) \in A(D)$. Ojo:
$(u,v) \neq (v,u)$.

Un **grafo orientado** es un digrafo donde, para cada par $u,v$, **no** aparecen
los dos arcos $u \to v$ y $v \to u$. Es decir: sale de orientar cada arista de un
grafo no dirigido. *Todo grafo orientado es un digrafo; no todo digrafo es un
grafo orientado.*

![Grafo G = (V,E)](imagenes/teo2-intro-grafos.pdf-0011-15.png)

## 2. Isomorfismo: cuándo dos grafos son "el mismo"

$G$ y $H$ son **isomorfos** si existe una **biyección** $f: V(G) \to V(H)$ tal
que para todo par $u, v \in V(G)$:
$$uv \in E(G) \iff f(u)f(v) \in E(H).$$

En criollo: se pueden renombrar los vértices de $G$ para obtener $H$. Un
isomorfismo **preserva la estructura de adyacencias**: $u \sim v \iff f(u) \sim f(v)$.

### Cómo se ataca un ejercicio de isomorfismo

Son dos trabajos distintos según la respuesta:

- **Para decir que SÍ son isomorfos:** hay que **exhibir la biyección** (es un
  $\exists$: elegimos nosotros) y verificar que cada arista de $G$ va a una
  arista de $H$ **y viceversa**. No alcanza con "se ve parecido".
- **Para decir que NO:** alcanza con **un invariante que difiera**. Un invariante
  es cualquier cosa que se preserva por isomorfismo: $n = |V|$, $m = |E|$, la
  secuencia de grados, la cantidad de componentes conexas, la longitud del ciclo
  más corto, si es bipartito.

> **Cuidado con el error clásico:** que coincidan $n$, $m$ y la secuencia de
> grados **no implica** que sean isomorfos. Los invariantes sólo sirven para
> descartar.

## 3. Grados

El **grado** de un vértice $v$ es
$$\deg_G(v) = |\{e \in E(G) : e \text{ incide en } v\}|,$$
o sea, la cantidad de aristas que tienen a $v$ como extremo.

La **secuencia de grados** se obtiene listando los grados de todos los vértices
(típicamente ordenados). Es un **invariante por isomorfismo**.

### Lema del apretón de manos

$$\sum_{v \in V(G)} \deg_G(v) = 2\,|E(G)|.$$

Cada arista aporta 1 al grado de cada uno de sus dos extremos, entonces se cuenta
dos veces. De ahí salen dos corolarios que se usan todo el tiempo:

- No existe un grafo cuya suma de grados sea **impar**.
- **Todo grafo tiene una cantidad par de vértices de grado impar.**

### Dos vértices con el mismo grado (palomar)

> **Todo grafo con al menos dos vértices tiene dos vértices distintos del mismo
> grado.**

Se prueba con el **principio del palomar**: si distribuimos más de $k$ objetos en
$k$ cajas, alguna caja tiene al menos dos. Equivalente: si $f: A \to B$ es una
función entre conjuntos finitos con $|A| > |B|$, entonces $f$ no es inyectiva, así
que existen $x \neq y$ con $f(x) = f(y)$.

La idea de la prueba: en un grafo de $n$ vértices los grados van de $0$ a $n-1$
($n$ valores posibles para $n$ vértices — todavía no alcanza), pero $0$ y $n-1$
**no pueden convivir**: si alguien tiene grado $n-1$ es vecino de todos, así que
nadie tiene grado 0. Quedan $n-1$ cajas para $n$ vértices.

### En digrafos

$$d_{\text{out}}(v) = |\{(v,w) \in A(D)\}| \qquad d_{\text{in}}(v) = |\{(w,v) \in A(D)\}|$$

y el teorema análogo al apretón de manos:
$$\sum_{v \in V(D)} d_{\text{in}}(v) = \sum_{v \in V(D)} d_{\text{out}}(v) = |A(D)|.$$

Razón: cada arco $(u,v)$ contribuye exactamente 1 al grado de salida de $u$ y 1
al grado de entrada de $v$. **Cada arco se cuenta una vez de cada lado.**

## 4. Caminos, ciclos y conectividad

Un **camino** es una secuencia $P = v_0, v_1, \dots, v_k$ donde cada par
consecutivo es una arista. Es **simple** si no repite vértices.

> **Lema.** Si existe un camino de $u$ a $v$, entonces existe un camino **simple**
> de $u$ a $v$.
>
> *Idea:* si el camino repite un vértice $x$, borramos el tramo cerrado entre dos
> apariciones consecutivas de $x$:
> $$P = u, \dots, x, \underbrace{a, \dots, b, x}_{\text{se borra}}, \dots, v
> \quad\rightsquigarrow\quad P' = u, \dots, x, \dots, v.$$
> Repitiendo, queda un camino sin vértices repetidos.

Este lema es la razón por la que **para estudiar conectividad alcanza con
considerar caminos simples** — se usa constantemente para evitar casos raros.

Un **ciclo** es un camino $C = v_0, v_1, \dots, v_{k-1}, v_k$ con $v_0 = v_k$,
$k \geq 3$, y $v_0, \dots, v_{k-1}$ todos distintos.

$G$ es **conexo** si para todo par $u, v \in V(G)$ existe un camino de $u$ a $v$.
Conectividad significa que el grafo está "en una sola pieza".

La **distancia** $\text{dist}(u,v)$ es la mínima longitud de un camino de $u$ a
$v$, y $\infty$ si no hay ninguno.

## 5. Sacar cosas: $G - v$, $G - e$, subgrafos

| Operación | Vértices | Aristas |
|---|---|---|
| $G - v$ | $V(G) \setminus \{v\}$ | las que **no** inciden en $v$ |
| $G - e$ | $V(G)$ (¡todos!) | $E(G) \setminus \{e\}$ |

Eliminar una arista **no** elimina sus extremos.

- $H$ es **subgrafo** de $G$ si $V(H) \subseteq V(G)$ y $E(H) \subseteq E(G)$
  (sacamos vértices y/o aristas).
- El **subgrafo inducido** por $W \subseteq V(G)$ es $G[W]$ con $V(G[W]) = W$ y
  $E(G[W]) = \{uv \in E(G) : u, v \in W\}$. *En un subgrafo inducido elegimos los
  vértices y las aristas quedan determinadas* — no hay libertad.
- Un subgrafo $H$ es **maximal respecto de una propiedad $P$** si cumple $P$ y no
  es subgrafo propio de ningún otro subgrafo que también cumpla $P$.
- Una **componente conexa** es un subgrafo conexo **maximal**.

## 6. Particiones y cortes

Una **partición** de $V(G)$ en dos conjuntos es un par $A, B \subseteq V(G)$ con
$A \neq \emptyset$, $B \neq \emptyset$, $A \cap B = \emptyset$ y $A \cup B = V(G)$.
Se escribe $V(G) = A \,\dot\cup\, B$.

Una arista $e = uv$ **cruza** la partición $(A,B)$ si tiene un extremo en $A$ y
el otro en $B$.

> **Teorema.** $G$ es conexo **si y sólo si** para toda partición
> $V(G) = A \,\dot\cup\, B$ existe una arista de $G$ que cruza entre $A$ y $B$.

![Partición sin aristas que crucen](imagenes/teo2-intro-grafos.pdf-0048-06.png)

Interpretación: **un grafo conexo no puede separarse en dos partes sin cortar
alguna arista.** Y al revés, para probar que algo es disconexo alcanza con
exhibir **una** partición sin aristas cruzadas.

Este teorema es exactamente el ejercicio 11b de la práctica 2 — la teórica lo
enuncia y deja la demostración para la guía.

## 7. Puntos de articulación, aristas de corte, biconexión

- $v$ es **punto de articulación** si $G - v$ tiene **más** componentes conexas
  que $G$.
- $e$ es **arista de corte** (o **puente**) si $G - e$ tiene más componentes
  conexas que $G$.

![Punto de articulación](imagenes/teo2-intro-grafos.pdf-0051-06.png)

> **Proposición.** $e$ es arista de corte de $G$ **si y sólo si** $e$ no pertenece
> a ningún ciclo de $G$.

Esta caracterización es clave: convierte "sacar la arista y contar componentes"
(caro) en "¿está en un ciclo?" (que después, con DFS, se chequea en tiempo lineal).

- $G$ es **biconexo** si es conexo y no tiene puntos de articulación.
  Equivalentemente, si $G - v$ sigue siendo conexo para **todo** $v$. Biconexo =
  la conectividad sobrevive a borrar cualquier vértice.
- Una **componente biconexa** (o **bloque**) es un subgrafo biconexo maximal.

> **Proposición.** Si $B_1$ y $B_2$ son bloques distintos, entonces
> $|V(B_1) \cap V(B_2)| \leq 1$. Y si $V(B_1) \cap V(B_2) = \{v\}$, entonces $v$
> es punto de articulación.

Los bloques se pegan entre sí **únicamente a través de puntos de articulación**.

## 8. Árboles

> **Lema.** Todo grafo acíclico con al menos dos vértices tiene al menos **dos
> vértices de grado uno**.

> **Proposición (la de los "dos de tres").** Sea $G$ un grafo con $n$ vértices.
> Cualesquiera **dos** de las siguientes implican la tercera:
>
> 1. $G$ es conexo.
> 2. $G$ es acíclico.
> 3. $G$ tiene $n-1$ aristas.

Un grafo conexo y acíclico se llama **árbol**.

Esta proposición es la herramienta para los ejercicios del tipo "¿cuál de estos
ítems garantiza que $G$ es un árbol?": si el ítem te da **dos** de las tres,
listo; si te da **una sola** (o dos que en realidad son la misma), hay que buscar
**contraejemplo**. Un contraejemplo típico: un triángulo suelto más un camino
aparte tiene $n-1$ aristas y no es árbol.

## 9. Complemento

El **complemento** $\overline{G}$ tiene $V(\overline{G}) = V(G)$ y, para $u \neq v$:
$$uv \in E(\overline{G}) \iff uv \notin E(G).$$

Cambia aristas por no-aristas. Los grados:
$$\deg_G(v) + \deg_{\overline{G}}(v) = n - 1 \quad\Longrightarrow\quad \deg_{\overline{G}}(v) = n - 1 - \deg_G(v).$$

Cada vértice tiene $n-1$ posibles vecinos; los que tiene en $G$ no los tiene en
$\overline{G}$, y viceversa.

## 10. Grafos bipartitos

$G$ es **bipartito** si existe una partición $V(G) = X \,\dot\cup\, Y$ tal que
toda arista tiene un extremo en $X$ y el otro en $Y$ (no hay aristas con ambos
extremos del mismo lado).

Equivalente: **una bipartición es lo mismo que un coloreo propio con dos
colores** (toda arista une colores distintos).

Por qué un ciclo impar falla: al colorear $C_5$ alternando, la última arista
$\{5,1\}$ termina uniendo dos vértices del mismo color.

![Ciclo impar](imagenes/teo2-intro-grafos.pdf-0066-07.png)

> **Teorema (caracterización).** $G$ es bipartito **si y sólo si** no contiene
> ciclos impares.

*Idea de la demostración:*

- **($\Rightarrow$)** Si $G$ es bipartito, todo ciclo alterna entre las dos
  partes, entonces tiene longitud par.
- **($\Leftarrow$)** Si $G$ no tiene ciclos impares: en cada componente conexa
  elegimos un vértice $s$ y agrupamos los vértices según la **paridad de su
  distancia a $s$**.

Esa segunda mitad es la que después se implementa con BFS.

## Fuentes

- `temas/14-definici-n.md` (L1-56), `temas/16-aristas-no-dirigidas.md` (L1-43) — grafo, aristas, extremos
- `temas/22-definici-n.md` (L1-47), `temas/45-grafo-orientado.md` (L1-41) — digrafo y grafo orientado
- `temas/27-definici-n.md` (L1-44) — isomorfismo
- `temas/30-definici-n.md` (L1-45), `temas/31-secuencia-de-grados.md` (L1-33) — grado y secuencia de grados
- `temas/34-lema-del-apret-n-de-manos.md` (L1-34), `temas/35-corolario.md` (L1-32) — apretón de manos y corolarios
- `temas/37-principio-del-palomar.md` (L1-54) — palomar y "dos vértices del mismo grado"
- `temas/38-grado-de-entrada-y-grado-de-salida.md` (L1-54), `temas/41-teorema.md` (L1-48) — grados en digrafos
- `temas/50-definici-n.md` (L1-58), `temas/51-todo-camino-contiene-un-camino-simple.md` (L1-28) — camino simple
- `temas/53-definici-n.md` (L1-44) — ciclo
- `temas/57-definici-n.md` (L1-44), `temas/73-distancia.md` (L1-34) — conexo y distancia
- `temas/58-eliminar-v-rtices.md` (L1-44), `temas/60-eliminar-aristas.md` (L1-42) — $G-v$ y $G-e$
- `temas/62-definici-n.md` (L1-40), `temas/63-subgrafo-inducido.md` (L1-46), `temas/65-definici-n.md` (L1-30), `temas/66-definici-n.md` (L1-34) — subgrafos, inducido, maximal, componente conexa
- `temas/68-particiones-de-v-rtices.md` (L1-32), `temas/70-definici-n.md` (L1-43), `temas/71-conectividad-y-cortes.md` (L1-50), `temas/72-interpretaci-n.md` (L1-33) — particiones, aristas que cruzan, teorema de cortes
- `temas/74-ejemplo-un-punto-de-articulaci-n.md` (L1-36), `temas/77-definici-n.md` (L1-20), `temas/78-proposici-n.md` (L1-36) — articulación, arista de corte, caracterización por ciclos
- `temas/80-lema.md` (L1-16), `temas/81-proposici-n.md` (L1-42) — acíclicos y la proposición de los "dos de tres"
- `temas/83-definici-n.md` (L1-46), `temas/86-definici-n.md` (L1-16), `temas/87-proposici-n.md` (L1-38) — biconexo, bloques
- `temas/88-complemento-de-un-grafo.md` (L1-44), `temas/90-grados-en-el-complemento.md` (L1-46) — complemento
- `temas/91-grafos-bipartitos.md` (L1-44), `temas/93-coloreo-con-dos-colores.md` (L1-31), `temas/95-un-ciclo-impar-no-es-bipartito.md` (L1-35), `temas/96-caracterizaci-n.md` (L1-18), `temas/97-idea-de-la-demostraci-n.md` (L1-24) — bipartitos y ciclos impares
