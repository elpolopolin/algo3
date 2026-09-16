# Selección ⋆ — dos ejercicios por guía (1 a 4)

Ocho ejercicios marcados con ⋆ (el subconjunto mínimo que pide la cátedra), dos
por guía. **No están resueltos a propósito**: de cada uno tenés el enunciado, un
mapa de por dónde entrarle, y el link a la parte del resumen que explica la
técnica. Cuando quieras resolver uno, pedímelo y lo hacemos juntos.

Los resúmenes linkeados:

| Guía | Resumen de teoría |
|---|---|
| 1 — Demostraciones | [`context/teoria/demostraciones/resumen.md`](../../teoria/demostraciones/resumen.md) |
| 2 — Intro a grafos | [`context/teoria/intro-grafos/resumen.md`](../../teoria/intro-grafos/resumen.md) |
| 3 — Algoritmos en grafos | [`context/teoria/grafos-algoritmos-03/resumen.md`](../../teoria/grafos-algoritmos-03/resumen.md) |
| 4 — Divide & Conquer | [`context/teoria/divide-and-conquer/resumen.md`](../../teoria/divide-and-conquer/resumen.md) |

---

## Guía 1 — Demostraciones

### Ejercicio 11 ⋆ — Encontrar el error (y reescribir)

> ¿Cuál es el error en la siguiente demostración? ¿Hay más de uno? Reescribirla
> para que sea correcta.
>
> Queremos ver que si un conjunto compuesto por números enteros no negativos
> tiene por lo menos un número positivo, entonces la suma de todos los elementos
> del conjunto es positiva. Hacemos inducción en el tamaño $n$ del conjunto.
>
> **Caso base ($n=1$):** Si el conjunto tiene un solo número $a$ y este es
> positivo, la suma de todos los elementos es $a$, lo cual es positivo.
>
> **Paso inductivo:** Saquemos un elemento cualquiera $k$ del conjunto,
> quedándonos con un subconjunto $C$ de $n-1$ elementos. Por hipótesis inductiva,
> la suma de los elementos de $C$ es positiva, y por lo tanto agregarle $k$ de
> nuevo, que es un número no negativo, no puede hacer que la suma sea no positiva. □

**Cómo pensarlo.** No busques el error en las cuentas: buscalo en el
**esqueleto**. Andá por esta checklist, en este orden:

1. **¿Está definida $P(n)$?** No aparece por ningún lado. Escribila vos, con
   cuantificadores, antes de seguir. → [Cómo se escribe una demostración por inducción (los 4 pasos)](../../teoria/demostraciones/resumen.md#cómo-se-escribe-los-4-pasos)
2. **¿La inducción es sobre un natural?** Dice "inducción en el tamaño $n$",
   que está bien — pero fijate si $P$ realmente habla del tamaño o del conjunto.
   → [Advertencia: la inducción es sobre naturales](../../teoria/demostraciones/resumen.md#cómo-se-escribe-los-4-pasos)
3. **¿La HI se aplica a un objeto que cumple la hipótesis?** Acá está el error
   grueso: al sacar "un elemento cualquiera $k$", nada garantiza que el
   subconjunto $C$ **siga teniendo** un elemento positivo. Si $k$ era el único
   positivo, $C$ no cumple la premisa y la HI **no se puede usar**.
   → [Checklist, punto 3: decí dónde usás la HI y verificá que el valor cae en el rango donde vale](../../teoria/demostraciones/resumen.md#7-checklist-antes-de-entregar)
4. **¿El caso base cubre todo lo que necesita el paso?** El paso arranca en
   $n \geq 2$; ¿el caso base $n=1$ alcanza? → [¿Cuántos casos base?](../../teoria/demostraciones/resumen.md#cuántos-casos-base)
5. **Para reescribirla:** el arreglo natural es no sacar "un elemento
   cualquiera" sino **el mínimo**, o sacar uno que *no* sea el positivo. Ahí
   entra el otro truco de la unidad. → [El truco del "primer elemento que cumple"](../../teoria/demostraciones/resumen.md#6-el-truco-del-primer-elemento-que-cumple)

**Error clásico a evitar:** "arreglarlo" cambiando la conclusión en vez del
argumento. La proposición es verdadera; lo que está mal es cómo se la prueba.

**Hermanos útiles:** los ejercicios 9 y 10 ⋆ son del mismo tipo (encontrar el
error). El 9 falla por **cuántos casos base**; el 10, por **dónde se aplica la
HI**. Si el 11 te sale, hacé esos dos que son más cortos.

---

<a id="g1-ej18"></a>

### Ejercicio 18 ⋆ — Cambio de fase

> Sea $C$ un conjunto, y $A$ y $B$ dos subconjuntos de $C$ tal que
> $A \cup B = C$. Supongamos que $S := (s_1, \dots, s_n)$ es una secuencia de
> $n \geq 2$ elementos de $C$ donde $s_1 \in A$ y $s_n \in B$. Queremos ver que
> existe un índice $i \in \{1, \dots, n-1\}$ tal que $s_i \in A$ y $s_{i+1} \in B$.
>
> a) Demostrar lo pedido por **inducción en $n$**.
>
> b) Demostrarlo **de forma directa** considerando el primer elemento $s_j$ de
> $S$ que pertenezca a $B$, con $j > 1$. Recordar demostrar que este elemento
> efectivamente existe, es decir, que el conjunto $\{s_j \mid s_j \in B \land j > 1\}$
> no es vacío.

**Por qué este ejercicio.** Es la misma proposición demostrada con **dos técnicas
distintas**, que es exactamente lo que muestra la teórica. Vale el doble.

**Cómo pensar el a).**

1. Antes que nada, **formalizá**: ¿qué es exactamente $P(n)$? Ojo que $A$ y $B$
   **no son disjuntos** ($A \cup B = C$, pero pueden solaparse) — eso importa.
   → [Formalizar la consigna](../../teoria/demostraciones/resumen.md#2-formalizar-la-consigna)
2. Es un $\exists i$ dentro de un $\forall n$: en el paso inductivo, quien elige
   $n$ es Beto, y quien tiene que producir el $i$ sos vos.
   → [La conversación Alicia / Beto](../../teoria/demostraciones/resumen.md#la-conversación-alicia--beto)
3. Para el paso inductivo conviene **partir en casos** según dónde cae
   $s_{n-1}$ (o $s_2$), y ver en cuál de los dos se puede aplicar la HI.
   → [Inducción: los 4 pasos](../../teoria/demostraciones/resumen.md#cómo-se-escribe-los-4-pasos)

**Cómo pensar el b).** Es *literalmente* el truco del mínimo:

- Definí $D = \{j > 1 \mid s_j \in B\}$.
- **Probá que $D \neq \emptyset$** (acá entra $s_n \in B$ y $n \geq 2$). Este es
  el paso que la consigna te avisa explícitamente que no te saltees.
- Tomá $j = \min D$ y mirá $s_{j-1}$: por minimalidad, $s_{j-1} \notin B$; como
  $A \cup B = C$, entonces $s_{j-1} \in A$. Ese $i = j-1$ es el que buscabas.

→ [El truco del "primer elemento que cumple"](../../teoria/demostraciones/resumen.md#6-el-truco-del-primer-elemento-que-cumple)

**Error clásico a evitar:** olvidarte de justificar que el conjunto es no vacío.
Sin eso el "mínimo" no existe y la demostración no vale nada.

---

## Guía 2 — Introducción a grafos

### Ejercicio 6 ⋆ — Doble grado

> Demostrar, **usando la técnica de reducción al absurdo**, que todo grafo no
> trivial tiene al menos dos vértices del mismo grado.

**Cómo pensarlo.** El resultado ya está enunciado en la teórica, pero la
demostración es tuya. La consigna te fija la técnica, así que arrancá diciendo
"supongamos por el absurdo que todos los grados son distintos".

1. **¿Cuántos valores puede tomar un grado?** En un grafo de $n$ vértices,
   $\deg(v) \in \{0, 1, \dots, n-1\}$: son $n$ valores para $n$ vértices, así
   que el palomar **todavía no alcanza**. Hay que afinar.
   → [Grados y secuencia de grados](../../teoria/intro-grafos/resumen.md#3-grados)
2. **La observación que cierra el argumento:** $0$ y $n-1$ no pueden convivir.
   Si alguien tiene grado $n-1$ es vecino de todos, así que nadie puede tener
   grado $0$. Quedan $n-1$ valores posibles para $n$ vértices.
   → [Dos vértices con el mismo grado (palomar)](../../teoria/intro-grafos/resumen.md#dos-vértices-con-el-mismo-grado-palomar)
3. **Rematar con el palomar** y marcar dónde aparece el absurdo.
   → [Principio del palomar (versión de la teórica de demostraciones)](../../teoria/demostraciones/resumen.md#principio-del-palomar)
   y [Contradicción (absurdo)](../../teoria/demostraciones/resumen.md#5-contrarrecíproco-y-absurdo)

**Error clásico a evitar:** decir "hay $n$ vértices y $n-1$ grados posibles" sin
justificar **por qué** son $n-1$. Ese "por qué" es toda la demostración.

**Dato:** el palomar acá se puede usar en su versión "función no inyectiva":
$\deg : V \to \{0, \dots, n-1\}$ con $|V| > |{\rm imagen}|$.

#### Demostración formal

Sea $G$ un grafo simple (sin lazos ni aristas múltiples) **no trivial**, es
decir con $n = |V(G)| \geq 2$.

**Hipótesis del absurdo.** Supongamos que $G$ tiene *menos de dos* vértices del
mismo grado, o sea que **no hay dos vértices distintos con el mismo grado**.
Equivale a decir que la función grado

$$\deg : V(G) \longrightarrow \mathbb{Z}_{\geq 0}, \qquad v \mapsto \deg(v)$$

es **inyectiva** (vértices distintos $\Rightarrow$ grados distintos).

**Paso 1 — acotar el codominio.** En un grafo simple, cada vértice $v$ es
adyacente a lo sumo a los otros $n-1$ vértices, y nunca a sí mismo. Entonces

$$0 \leq \deg(v) \leq n-1 \quad \text{para todo } v \in V(G),$$

así que $\deg$ toma valores en el conjunto $\{0, 1, \dots, n-1\}$, que tiene
exactamente $n$ elementos.

**Paso 2 — de inyectiva a biyectiva.** Tenemos $\deg : V(G) \to \{0,\dots,n-1\}$
inyectiva, con $|V(G)| = n = |\{0,\dots,n-1\}|$. Una función inyectiva entre dos
conjuntos finitos del mismo cardinal es **biyectiva**. Por lo tanto $\deg$ es
sobreyectiva: **todo** valor de $\{0, 1, \dots, n-1\}$ es el grado de algún
vértice. En particular existen

$$u \in V(G) \ \text{con}\ \deg(u) = 0, \qquad
  w \in V(G) \ \text{con}\ \deg(w) = n-1.$$

Además $u \neq w$, porque $n \geq 2$ implica $0 \neq n-1$.

**Paso 3 — el absurdo.** $\deg(w) = n-1$ significa que $w$ es adyacente a los
otros $n-1$ vértices del grafo, es decir a **todos** los vértices salvo él
mismo. En particular $w$ es adyacente a $u$, con lo cual esa arista $uw$ aporta
al grado de $u$ y entonces $\deg(u) \geq 1$.

Pero habíamos obtenido $\deg(u) = 0$. Contradicción: $\deg(u) = 0$ y
$\deg(u) \geq 1$ a la vez.

**Conclusión.** La hipótesis del absurdo es falsa. Luego todo grafo simple no
trivial tiene **al menos dos vértices distintos con el mismo grado**. $\blacksquare$

##### Variante del remate con el palomar (Paso 3 alternativo)

En lugar de usar la biyección, alcanza con esta observación: los valores $0$ y
$n-1$ **no pueden estar los dos** en la imagen de $\deg$. Si algún vértice
tuviera grado $n-1$ sería adyacente a todos, y entonces ningún vértice podría
tener grado $0$; y al revés. Entonces la imagen de $\deg$ está contenida en un
conjunto de a lo sumo $n-1$ valores (o $\{0,\dots,n-2\}$ o $\{1,\dots,n-1\}$).

Tenemos así $\deg : V(G) \to B$ con $|V(G)| = n$ y $|B| \leq n-1$, o sea
$|A| > |B|$. Por el **principio del palomar** (una función entre conjuntos
finitos con $|A| > |B|$ no puede ser inyectiva), existen $x \neq y$ con
$\deg(x) = \deg(y)$. Esto contradice la hipótesis del absurdo, y se concluye
igual.

**Nota sobre "no trivial".** La hipótesis $n \geq 2$ se usa dos veces: para que
$0 \neq n-1$ (y así $u \neq w$), y para que la frase "dos vértices distintos"
tenga sentido. Con $n = 1$ (grafo trivial) el enunciado es falso: un único
vértice no tiene con quién compartir grado.

**Nota sobre "grafo simple" (fuera de fuente).** El enunciado original sólo
dice "todo grafo no trivial", sin aclarar "simple" — lo agrego yo en la
demostración porque **la afirmación es falsa sin esa aclaración**, no por
prolijidad. Dos contraejemplos:

- *Con un lazo:* $V=\{u,v\}$, sin arista $uv$, pero con un lazo en $u$. Con la
  convención de que un lazo suma $2$ al grado, $\deg(u)=2$ y $\deg(v)=0$: son
  $n=2$ vértices con grados distintos. La proposición ya falla en el caso más
  chico posible.
- *Con aristas múltiples (sin lazos):* $V=\{a,b,c\}$, con $0$ aristas $ab$, $1$
  arista $ac$ y $2$ aristas $bc$ (en paralelo). Entonces $\deg(a)=1$,
  $\deg(b)=2$, $\deg(c)=3$: los tres grados son distintos.

En los dos casos se rompe exactamente el **Paso 1** de la demostración
($0 \le \deg(v) \le n-1$): un lazo o una arista repetida hacen que el grado deje
de estar acotado por $n-1$, así que ya no hay "más vértices que valores
posibles de grado" y el palomar no aplica. Por eso "grafo simple" no es una
convención decorativa acá: es lo que hace que el argumento (y la proposición
misma) sea cierto.

#### Fuentes

- `context/practica/context/practica_2.md` (L126-128) — enunciado del Ejercicio 6
- `context/teoria/intro-grafos/temas/37-principio-del-palomar.md` (L11-21) — principio del palomar, versión cajas y versión "función no inyectiva"
- `context/teoria/intro-grafos/temas/37-principio-del-palomar.md` (L31) — proposición: todo grafo con $\geq 2$ vértices tiene dos vértices distintos del mismo grado
- `context/teoria/intro-grafos/temas/31-secuencia-de-grados.md` (L3) — secuencia de grados (lista de $\deg(v)$)

---

### Ejercicio 8 ⋆ — Unicidad digrafo

> Un *grafo orientado* es un digrafo $D$ tal que al menos uno de $v \to w$ y
> $w \to v$ no es arco de $D$, para todo $v, w \in V(D)$. Demostrar que para
> cada $n$ existe un único grafo orientado cuyos vértices tienen todos grados
> de salida distintos.

**Qué pide.** $n$ es la cantidad de **vértices** del grafo orientado (no la
cantidad de aristas). El *grado de salida* $d_{\text{out}}(v)$ de un vértice
es la cantidad de arcos que **salen** de $v$ (cuántas flechas le arrancan a
ese vértice, no cuántas aristas tiene el grafo en total). "Único" quiere decir:
para cada $n$ hay exactamente un grafo orientado (salvo isomorfismo, o sea
salvo renombrar vértices) con esa propiedad — ni cero, ni dos. Hay que probar
**existencia** (hay al menos uno) y **unicidad** (no hay dos distintos).
→ [Grafo orientado](../../teoria/intro-grafos/resumen.md#1-definiciones-básicas)
→ [Grado de salida en digrafos](../../teoria/intro-grafos/resumen.md#en-digrafos)

**Cómo pensarlo.**

1. **Acotar los valores posibles.** En un grafo orientado de $n$ vértices,
   cada par de vértices tiene **exactamente un** arco entre ellos (nunca los
   dos, y tampoco ninguno — sale de orientar cada arista de un grafo no
   dirigido). Entonces $d_{\text{out}}(v) \in \{0, \dots, n-1\}$: $n$ valores
   posibles para $n$ vértices. Si además son **todos distintos**, no sobra
   ningún valor: $d_{\text{out}}$ es una biyección con $\{0, \dots, n-1\}$.
   Mismo patrón "$n$ valores para $n$ vértices ⇒ biyección" que el
   Ejercicio 6 de esta guía, arriba.
2. **Existencia: construí uno.** Ordená los vértices $v_1, \dots, v_n$ y
   orientá cada par $\{v_i, v_j\}$ con $i<j$ como $v_i \to v_j$. Cada $v_i$
   manda arco a los $n-i$ vértices que están después:
   $d_{\text{out}}(v_i) = n-i$, valores $n-1, n-2, \dots, 0$, todos distintos.
   (Se llama *torneo transitivo*: versión dirigida de un orden total.)
3. **Unicidad: inducción en $n$.** No alcanza con que tu construcción tenga la
   propiedad — hay que ver que **cualquier** grafo orientado con grados de
   salida distintos es forzosamente ese mismo. Sacale el vértice de grado de
   salida máximo ($n-1$) y fijate qué le queda al resto.
   → [Inducción](../../teoria/demostraciones/resumen.md#4-inducción)

**Error clásico a evitar:** confundir "grados de salida distintos" con
"grados de salida $0,1,\dots,n-1$ en algún orden" como si fuera automático por
el enunciado — es una consecuencia que hay que justificar (paso 1), no un dato
extra del problema.

#### Demostración formal

Sea $n \geq 1$ fijo. Hay que probar existencia y unicidad (salvo isomorfismo)
de un grafo orientado $D$ de $n$ vértices con $d_{\text{out}}$ inyectiva.

**Paso 0 — los grados de salida quedan forzados a ser $\{0,\dots,n-1\}$.**
En un grafo orientado, para cada par $u \neq v$ hay **exactamente un** arco
entre ellos. Entonces cada vértice $v$ manda arcos hacia algún subconjunto de
los otros $n-1$ vértices:
$$0 \leq d_{\text{out}}(v) \leq n-1.$$
Si los $n$ grados de salida son distintos, $d_{\text{out}} : V(D) \to
\{0,\dots,n-1\}$ es inyectiva entre conjuntos del mismo cardinal $n$, luego
**biyectiva**. Los grados de salida son, en algún orden, exactamente
$0,1,\dots,n-1$.

**Existencia.** Sea $V=\{v_1,\dots,v_n\}$ y $D$ el digrafo con arco
$v_i \to v_j$ para todo $i<j$ (torneo transitivo). Es grafo orientado: cada
par tiene un único arco, del menor al mayor índice. $v_i$ tiene arco hacia
$v_{i+1},\dots,v_n$, o sea $d_{\text{out}}(v_i) = n-i$. Cuando $i$ recorre
$1,\dots,n$, $n-i$ recorre $n-1,\dots,0$: todos distintos. Existe al menos un
grafo orientado con la propiedad.

**Unicidad, por inducción en $n$.**

*Caso base* $n=1$: un solo vértice, sin arcos posibles, $d_{\text{out}}$
trivialmente inyectiva (dominio de un elemento). Único.

*Paso inductivo.* Vale para $n-1$. Sea $D$ un grafo orientado de $n$ vértices
con $d_{\text{out}}$ inyectiva. Por el Paso 0 hay un vértice $w$ con
$d_{\text{out}}(w) = n-1$: $w$ tiene arco hacia **cada** uno de los otros
$n-1$ vértices. En particular $d_{\text{in}}(w) = 0$: nadie tiene arco hacia
$w$ (si algún $u$ tuviera $u \to w$, como es grafo orientado no puede también
tener $w \to u$ — pero $w \to u$ es justo lo que ya sabemos que vale para
**todo** $u \neq w$; contradicción).

Sea $D' = D - w$ (sacar $w$ y sus arcos). $D'$ es grafo orientado de $n-1$
vértices. Como $d_{\text{in}}(w) = 0$, ningún arco removido era entrante a
otro vértice, así que sacar $w$ **no cambia** el grado de salida de ninguno de
los que quedan: $d_{\text{out}}^{D'}(v) = d_{\text{out}}^{D}(v)$ para todo
$v \neq w$. Esos $n-1$ valores eran distintos en $D$, siguen distintos en
$D'$. Por hipótesis inductiva, $D'$ es el **único** grafo orientado de $n-1$
vértices con grados de salida distintos: el torneo transitivo de $n-1$
vértices.

Entonces $D$ queda totalmente determinado: es $D'$ (único, por HI) más un
vértice $w$ con arco hacia **todos** los de $D'$ — exactamente la construcción
de existencia, con $w$ en el rol de $v_1$. No hay otra forma de armar $D$.
$\blacksquare$

#### Fuentes

- `context/practica/context/practica_2.md` (L134-145) — enunciado del Ejercicio 8 y Figura 2
- `context/teoria/intro-grafos/resumen.md` (L26-33) — definición de digrafo y grafo orientado
- `context/teoria/intro-grafos/resumen.md` (L112-120) — grado de salida y grado de entrada en digrafos
- `context/teoria/intro-grafos/temas/45-grafo-orientado.md` (L1-41) — definición de grafo orientado (fuente original)
- `context/teoria/intro-grafos/temas/38-grado-de-entrada-y-grado-de-salida.md` (L1-54) — definición de $d_{\text{out}}$

---

### Ejercicio 11 ⋆ — Particiones conexas

> Sea $C$ un conjunto. Una familia $\{S_1, \dots, S_k\}$ es una *partición* de
> $C$ si reparte todos los elementos de $C$ en $k$ cajas, sin dejar ninguna
> vacía (no vacías, contenidas en $C$, unión $= C$, disjuntas dos a dos).
>
> a) Mostrar un grafo **conexo** $G$ y una partición de $V(G)$ en dos conjuntos
> $A$ y $B$ tal que **ni $G[A]$ ni $G[B]$** son conexos. ¿Para todo grafo existe
> esta partición?
>
> b) Demostrar que un grafo es conexo **si y sólo si** para toda partición en dos
> conjuntos $A$ y $B$ de $V(G)$ existe una arista en $E(G)$ con un extremo en $A$
> y otro en $B$. Usar la definición de grafo conexo y de camino, **no sólo la
> intuición**.

**Por qué este ejercicio.** El b) es **el teorema que la teórica enuncia y deja
para la práctica**. Es la caracterización de conectividad por cortes, y se usa
en media materia.

**Cómo pensar el a).** Es un $\exists$: construís vos el ejemplo.
Pista de forma: pensá en un camino de 4 vértices $1-2-3-4$ y partilo "salteado"
($A = \{1,3\}$, $B = \{2,4\}$). La segunda pregunta ("¿para todo grafo existe?")
es distinta: pensá en grafos muy chicos o muy densos.
→ [Subgrafo inducido](../../teoria/intro-grafos/resumen.md#5-sacar-cosas-g---v-g---e-subgrafos) —
ojo que $G[A]$ es **inducido**: elegís vértices, las aristas vienen solas.

**Cómo pensar el b).** Es un **si y sólo si**: son dos demostraciones.

1. **($\Rightarrow$) Conexo $\Rightarrow$ toda partición tiene arista cruzada.**
   Tomá $u \in A$ y $v \in B$ (existen porque la partición no deja cajas
   vacías). Por conexidad hay un camino de $u$ a $v$. Ese camino **empieza en
   $A$ y termina en $B$**: en algún momento cruza.
   > Fijate que esto es exactamente el **ejercicio 18 de la guía 1** (cambio de
   > fase) aplicado a la secuencia de vértices del camino. Podés citarlo, o
   > rehacer el argumento del primer vértice que cae en $B$.
   → [Ejercicio 18 de la guía 1](#g1-ej18) y
   [Todo camino contiene un camino simple](../../teoria/intro-grafos/resumen.md#4-caminos-ciclos-y-conectividad)
2. **($\Leftarrow$)** Conviene por **contrarrecíproco**: si $G$ **no** es conexo,
   construí una partición **sin** aristas cruzadas. La construcción sale sola:
   tomá una componente conexa como $A$ y el resto como $B$.
   → [Contrarrecíproco](../../teoria/demostraciones/resumen.md#contrarrecíproco) y
   [Componentes conexas](../../teoria/intro-grafos/resumen.md#5-sacar-cosas-g---v-g---e-subgrafos)

→ Todo el marco: [Particiones y cortes](../../teoria/intro-grafos/resumen.md#6-particiones-y-cortes)

**Error clásico a evitar:** en la ida, decir "es conexo, entonces hay una arista
entre $A$ y $B$" sin exhibir el camino. La consigna avisa: *usar la definición
de camino, no sólo la intuición*.

#### Demostración completa del b)

**($\Rightarrow$) Si $G$ es conexo, toda partición tiene arista cruzada.**

Sea $V(G) = A \,\dot\cup\, B$ una partición cualquiera. Como ninguna caja es
vacía, existen $u \in A$ y $v \in B$.

Por definición de grafo conexo (todo par de vértices tiene un camino que los
une), existe un camino
$$P = v_0, v_1, \dots, v_k$$
con $v_0 = u$, $v_k = v$, y $\{v_i, v_{i+1}\} \in E(G)$ para todo
$i = 0, \dots, k-1$.

Como $v_0 \in A$ y $v_k \in B$, y $A,B$ particionan $V(G)$ (todo vértice está
en $A$ o en $B$, nunca en ambos), el camino tiene que "cambiar de lado" en
algún punto. Formalmente: sea $i$ el menor índice tal que $v_i \in B$ (existe
porque $v_k \in B$). Como $v_0 = u \in A$, es $i \geq 1$, así que $v_{i-1}$
está definido. Por minimalidad de $i$, $v_{i-1} \notin B$, y como $A,B$ es
partición, $v_{i-1} \in A$.

Entonces $\{v_{i-1}, v_i\}$ es una arista de $G$ (el camino la usa) con un
extremo en $A$ y el otro en $B$: es la arista cruzada buscada. $\blacksquare$

**($\Leftarrow$) Si toda partición tiene arista cruzada, $G$ es conexo.**

Por contrarrecíproco: asumimos que $G$ **no** es conexo y construimos una
partición sin ninguna arista cruzada.

Como $G$ no es conexo, existen $u, w \in V(G)$ sin camino entre ellos.
Definimos
$$A = \{\, x \in V(G) : \text{existe un camino de } u \text{ a } x \,\}$$
(los vértices alcanzables desde $u$, incluyendo a $u$ con el camino trivial
de longitud 0) y $B = V(G) \setminus A$.

- $A \neq \emptyset$ porque $u \in A$.
- $B \neq \emptyset$ porque $w \notin A$ (no hay camino $u$-$w$), luego
  $w \in B$.
- $A, B$ es partición de $V(G)$ por construcción ($B$ es el complemento de
  $A$).

Veamos que no hay arista cruzada. Si existiera $\{x,y\} \in E(G)$ con
$x \in A$ e $y \in B$: como $x \in A$ hay un camino
$u = v_0, \dots, v_k = x$; agregándole la arista $\{x,y\}$ se obtiene el
camino $u = v_0, \dots, v_k = x, y$, que llega a $y$. Entonces $y$ es
alcanzable desde $u$, es decir $y \in A$. Pero $y \in B = V(G)\setminus A$:
contradicción.

Por lo tanto $A,B$ es una partición sin arista cruzada, lo que contradice la
hipótesis. Entonces $G$ tiene que ser conexo. $\blacksquare$

##### Fuentes
- `context/teoria/intro-grafos/temas/57-definici-n.md` (L11-15) — definición
  de grafo conexo.
- `context/teoria/intro-grafos/temas/47-caminos.md` (L13-25) — definición de
  camino.
- `context/teoria/intro-grafos/temas/71-conectividad-y-cortes.md` (L3-23) —
  enunciado del teorema en la teórica (sin demostración, remite a la
  práctica).
- `context/practica/context/practica_2.md` (L184-197) — enunciado del
  ejercicio 11.

---

## Guía 3 — Algoritmos en grafos

### Ejercicio 3 ⋆ — Orden topológico

> Dado un grafo dirigido $D$, un orden topológico de $D$ es un orden de los
> vértices tal que si $v \to w \in E(D)$ entonces $v < w$.
>
> a) Demostrar que si un digrafo no tiene ciclos, entonces tiene **por lo menos
> un vértice con grado de entrada 0**.
>
> b) Usando el a), describir un algoritmo para construir un orden topológico en
> un digrafo sin ciclos. Demostrar su correctitud y determinar su complejidad
> temporal y espacial. **No vale usar DFS.**
>
> c) Demostrar que un digrafo admite un orden topológico **si y sólo si** no
> tiene ciclos (es un DAG). Demostrar la ida **por contrarrecíproco**.
>
> d) Mejorar el algoritmo del b) para que corra en $O(|V(D)| + |E(D)|)$.

**Por qué este ejercicio.** Es la unidad entera en un ejercicio: un lema, un
algoritmo, su correctitud, su complejidad, y una optimización.

**Cómo pensar cada ítem.**

- **a)** Es el lema de la teórica. La demostración típica es por **absurdo** o
  por el truco del camino maximal: si todo vértice tuviera grado de entrada
  $\geq 1$, podrías caminar hacia atrás indefinidamente, y con $V$ finito eso
  fuerza un ciclo. → [Los dos resultados que lo hacen funcionar](../../teoria/grafos-algoritmos-03/resumen.md#los-dos-resultados-que-lo-hacen-funcionar)
  y [El truco del "primer elemento"](../../teoria/demostraciones/resumen.md#6-el-truco-del-primer-elemento-que-cumple)
- **b)** El algoritmo recursivo: sacar un vértice de grado de entrada 0,
  ponerlo al final del orden, y recursión sobre $D - u$. La **correctitud sale
  por inducción** en $|V|$ (usando el a) para saber que siempre hay un candidato).
  La complejidad ingenua es $O(n(n+m))$. → [Algoritmo, versión recursiva](../../teoria/grafos-algoritmos-03/resumen.md#algoritmo-versión-recursiva)
- **c)** La ida por contrarrecíproco es corta: si hay un ciclo
  $v_1 \to \dots \to v_k \to v_1$, el orden obligaría a $i_1 < \dots < i_k < i_1$.
  La vuelta la construís con el algoritmo del b). → [Contrarrecíproco](../../teoria/demostraciones/resumen.md#contrarrecíproco)
  y [Teorema: admite orden topológico ⟺ es acíclico](../../teoria/grafos-algoritmos-03/resumen.md#los-dos-resultados-que-lo-hacen-funcionar)
- **d)** La clave es no **rebuscar** el vértice de grado 0 cada vez: mantener un
  arreglo `entrada[v]` y una **cola** con los que ya llegaron a 0. Cada vértice
  se encola una vez, cada arista se procesa una vez.
  → [Algoritmo, versión con cola (lineal)](../../teoria/grafos-algoritmos-03/resumen.md#algoritmo-versión-con-cola-lineal)

**Error clásico a evitar:** en el b), decir "busco el de grado 0" sin decir
**cuánto cuesta buscarlo**. La diferencia entre el b) y el d) es exactamente esa.

---

### Ejercicio 12 ⋆ — Puentes

> Una arista de un grafo $G$ es **puente** si su remoción aumenta la cantidad de
> componentes conexas de $G$. Sea $T$ un árbol DFS de un grafo conexo $G$.
>
> a) Demostrar que $(v,w)$ es puente de $G$ **si y sólo si** $(v,w)$ no pertenece
> a ningún ciclo de $G$.
>
> b) Demostrar que si $(v,w) \in E(G) \setminus E(T)$, entonces $v$ es ancestro
> de $w$ en $T$ o viceversa.
>
> c) Sea $(v,w) \in E(G)$ con nivel de $v$ $\leq$ nivel de $w$ en $T$. Demostrar
> que $(v,w)$ es puente **si y sólo si** $v$ es el padre de $w$ en $T$ y ninguna
> arista de $G \setminus \{(v,w)\}$ une a un descendiente de $w$ (o a $w$) con un
> ancestro de $v$ (o con $v$).
>
> d) Dar un algoritmo lineal basado en DFS para encontrar todas las aristas
> puente de $G$.

**Por qué este ejercicio.** Es el puente (valga) entre las dos unidades de
grafos: el a) es de intro-grafos, el c) y el d) son la teórica de algoritmos.

**Cómo pensar cada ítem.**

- **a)** Es una proposición que ya está en intro-grafos. Las dos direcciones:
  si está en un ciclo, sacarla deja el camino "por el otro lado"; si no está en
  ningún ciclo y sacarla no desconectara, habría dos caminos entre sus extremos
  y eso arma un ciclo. → [Puntos de articulación, aristas de corte](../../teoria/intro-grafos/resumen.md#7-puntos-de-articulación-aristas-de-corte-biconexión)
- **b)** Es **exactamente** el teorema de la teórica: en un grafo no dirigido,
  toda arista de la DFS es de árbol o de retroceso. La demostración es por
  colores: mirá quién se descubre primero.
  → [Clasificación de aristas en DFS](../../teoria/grafos-algoritmos-03/resumen.md#clasificación-de-aristas-en-dfs)
- **c)** Este es el corazón. Traducí la condición del enunciado
  ("ninguna arista une un descendiente de $w$ con un ancestro de $v$") a la
  definición de `low[w]`: es lo mismo que decir $\texttt{low}[w] > d[v]$.
  → [`low[u]`: hasta dónde puede volver el subárbol](../../teoria/grafos-algoritmos-03/resumen.md#lowu-hasta-dónde-puede-volver-el-subárbol-de-u)
  y [El criterio de puente](../../teoria/grafos-algoritmos-03/resumen.md#el-criterio-de-puente)
- **d)** Una DFS que calcula $d$, $\pi$ y `low`, y al retroceder compara.
  Lineal porque es una DFS más trabajo constante por arista.
  → [El algoritmo completo](../../teoria/grafos-algoritmos-03/resumen.md#el-algoritmo-completo)

**Error clásico a evitar:** en el d), olvidarse de excluir **la arista al padre**
al actualizar `low`. Si la contás, `low[w]` nunca supera $d[v]$ y no detectás
ningún puente.

---

## Guía 4 — Divide & Conquer

### Ejercicio 3 ⋆ — Complexity quest

> Calcule la complejidad de un algoritmo que usa $T(n)$ pasos, donde $T$ cumple:
>
> | | | |
> |---|---|---|
> | 1) $T(n) = T(n-2) + 5$ | 5) $T(n) = 2T(n-1)$ | 9) $T(n) = 2T(n-4)$ |
> | 2) $T(n) = T(n-1) + n$ | 6) $T(n) = T(n/2) + n$ | 10) $T(n) = 2T(n/2) + \log n$ |
> | 3) $T(n) = T(n-1) + \sqrt{n}$ | 7) $T(n) = T(n/2) + \sqrt{n}$ | 11) $T(n) = 3T(n/4)$ |
> | 4) $T(n) = T(n-1) + n^2$ | 8) $T(n) = T(n/2) + n^2$ | 12) $T(n) = 3T(n/4) + n$ |
>
> Intentar estimar la complejidad directamente y **luego** calcularla con el
> teorema maestro **de ser posible**.

**Cómo pensarlo.** Lo primero es **clasificar cada ítem**, porque no todos se
resuelven igual:

| Forma | Qué hacer |
|---|---|
| $T(n) = aT(n/b) + f(n)$ — el tamaño se **divide** | **Teorema maestro**: calculá $q = \log_b a$ y compará $f(n)$ con $n^q$ |
| $T(n) = T(n-k) + g(n)$ — el tamaño se **resta**, $a=1$ | **Desenrollar**: $T(n) \approx \sum g(n - ik)$. Suma, no árbol |
| $T(n) = aT(n-k)$ con $a \geq 2$ — se resta y se **multiplica** | Crecimiento **exponencial**: $T(n) = \Theta(a^{n/k})$ |

Los ítems 1-5 y 9 son de las dos últimas filas: **el teorema maestro no aplica**,
y parte de la gracia del ejercicio es que te des cuenta.

→ [El Teorema Maestro: los tres casos y la tabla de ejemplos](../../teoria/divide-and-conquer/resumen.md#los-tres-casos)
→ [La advertencia sobre las recurrencias que restan](../../teoria/divide-and-conquer/resumen.md#cómo-usarlo-en-un-ejercicio)

Para los que sí entran (6, 7, 8, 10, 11, 12):

1. Identificá $a$, $b$, $f(n)$.
2. Calculá $q = \log_b a$.
3. Compará. Ojo con el **10**: $a=2$, $b=2$, $q=1$, y $f(n) = \log n$, que es
   $O(n^{1-\varepsilon})$ → **caso 1**, dominan las hojas. No te confundas con
   el caso 2 sólo porque aparece un $\log$.
4. Ojo con el **7**: $q = \log_2 1 = 0$, y $\sqrt{n} = \Omega(n^{0+\varepsilon})$
   → **caso 3**, domina la raíz. Verificá la condición de regularidad.

→ [El árbol de recursión: de dónde sale todo](../../teoria/divide-and-conquer/resumen.md#el-árbol-de-recursión-de-dónde-sale-todo)
(entender esto es lo que te deja **estimar** antes de aplicar el teorema)

**Si querés demostrarlo en vez de invocar el teorema:**
→ [El método de sustitución](../../teoria/divide-and-conquer/resumen.md#el-método-de-sustitución)
y, del lado de demostraciones, [inducción fuerte](../../teoria/demostraciones/resumen.md#inducción-fuerte-o-global-o-completa)
y [cuántos casos base](../../teoria/demostraciones/resumen.md#cuántos-casos-base)
(el ítem 9, $T(n) = 2T(n-4)$, es **literalmente** el ejemplo que hace la teórica
de demostraciones con rigor: cuatro casos base).

---

### Ejercicio 5 ⋆ — Índice espejo

> Tenemos un arreglo $a = [a_1, \dots, a_n]$ de $n$ enteros **distintos**
> (positivos y negativos) **en orden estrictamente creciente**. Queremos
> determinar si existe una posición $i$ tal que $a_i = i$. Por ejemplo, con
> $a = [-4, -1, 2, 4, 7]$, $i = 4$ es esa posición.
>
> Diseñar un algoritmo de dividir y conquistar **eficiente** (complejidad
> estrictamente menor que lineal) que resuelva el problema. Calcule y justifique
> la complejidad.

**Cómo pensarlo.** "Estrictamente menor que lineal" es una pista enorme: te está
pidiendo $O(\log n)$, o sea **búsqueda binaria**. Pero el arreglo no está
ordenado *por lo que buscás* ($a_i = i$), así que hay que fabricar la
monotonía.

1. **El paso conceptual:** definí $g(i) = a_i - i$. Como los $a_i$ son enteros
   **distintos** y **estrictamente crecientes**, vale $a_{i+1} \geq a_i + 1$, y
   entonces $g$ es **no decreciente**. Buscar $a_i = i$ es buscar $g(i) = 0$ en
   una función monótona.
2. **Aplicá el esquema:** mirás el medio $m$; si $g(m) < 0$ el cero sólo puede
   estar a la derecha, si $g(m) > 0$ sólo a la izquierda, si $g(m)=0$ terminaste.
   → [Más allá de búsqueda binaria: dominio ordenado, predicado, umbral](../../teoria/divide-and-conquer/resumen.md#más-allá-de-un-arreglo-el-esquema-general)
3. **La complejidad:** $T(n) = T(n/2) + \Theta(1)$, que por teorema maestro
   ($a=1$, $b=2$, $q=0$, caso 2 con $r=0$) da $\Theta(\log n)$.
   → [Búsqueda binaria como D&C](../../teoria/divide-and-conquer/resumen.md#la-versión-clásica)
   y [Los tres casos](../../teoria/divide-and-conquer/resumen.md#los-tres-casos)
4. **La correctitud** se demuestra por inducción sobre el tamaño del intervalo:
   la HI es "la llamada recursiva responde bien para el subintervalo".
   → [El patrón D&C, en general](../../teoria/divide-and-conquer/resumen.md#el-patrón-dc-en-general)
   y [Inducción fuerte](../../teoria/demostraciones/resumen.md#inducción-fuerte-o-global-o-completa)

**Error clásico a evitar:** justificar el descarte con "como está ordenado…" sin
explicitar la monotonía de $g$. Sin enteros distintos y crecimiento estricto el
argumento **se cae** — probá con $a = [-10, 1, 1, 1, 8]$ para ver por qué la
hipótesis importa.

**Si te sale, seguí con:** el ejercicio 8 ⋆ (Cazador de falsos) usa la misma
idea de descarte pero en dos dimensiones, y el 6 ⋆ (Potencia logarítmica) es el
mismo esqueleto de "achicar a la mitad" del lado del exponente.

---

## Cómo seguir

Cuando quieras resolver alguno, decime cuál y lo hacemos juntos. La resolución
va a `context/practica/respuestas-practicas/practica_<n>.md`, no acá: este
archivo es el índice de la selección.
