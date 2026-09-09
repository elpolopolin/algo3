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
