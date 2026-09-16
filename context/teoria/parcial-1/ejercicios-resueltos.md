# Ejercicios resueltos y explicados

> Ocho ejercicios tipo parcial, uno o dos por tema. Cada uno tiene tres partes:
> **Cómo me di cuenta** (el razonamiento que lleva al enfoque — que es lo que hay
> que entrenar), **La respuesta** (escrita como se entrega) y **Dónde se pierden
> puntos**.
>
> Leé primero solo el enunciado. Pelealo veinte minutos. Recién después abrí la
> solución.

---

# Teoría de grafos

## Ejercicio 1 — Conexo ⟺ toda partición tiene una arista que cruza

*(Práctica 2, ejercicio 11b)*

> Demostrar que un grafo $G$ es conexo **si y sólo si** para toda partición de
> $V(G)$ en dos conjuntos $A$ y $B$ existe una arista de $E(G)$ con un extremo en
> $A$ y otro en $B$. Usar la definición de grafo conexo y de camino, no sólo la
> intuición.

### Cómo me di cuenta

La consigna dice «si y sólo si», así que son **dos demostraciones**, no una. Y
dice explícitamente «no sólo la intuición», que es la forma del enunciado de
avisarte que la respuesta obvia («claro, si no hay arista quedan dos pedazos») no
alcanza.

La pregunta útil es: ¿cuál de las dos direcciones es más fácil **directa** y cuál
por **contrarrecíproco**? Regla práctica: la dirección cuya **negación te da un
objeto concreto** conviene hacerla por contrarrecíproco.

- ($\Rightarrow$) Hipótesis: $G$ conexo. Conclusión: para *toda* partición hay
  arista. Un «para toda» se ataca tomando una partición arbitraria. Y de la
  hipótesis «conexo» sale un camino. **Directa.**
- ($\Leftarrow$) Hipótesis: toda partición tiene arista. Conclusión: $G$ conexo.
  Acá la hipótesis es un «para toda» — incómoda de usar. Pero si niego la
  conclusión, «$G$ no es conexo» me da **dos vértices concretos sin camino entre
  ellos**, y con ellos puedo **construir** la partición que viola la hipótesis.
  **Contrarrecíproco.**

Ese es el reflejo: negar la conclusión para conseguir un objeto con el que
trabajar.

### La respuesta

**($\Rightarrow$)** Supongamos $G$ conexo, y sea $V(G) = A \,\dot\cup\, B$ una
partición cualquiera. Como $A \neq \emptyset$ y $B \neq \emptyset$, existen
$u \in A$ y $v \in B$. Por ser $G$ conexo existe un camino
$P = u = v_0, v_1, \dots, v_k = v$.

Consideremos el conjunto de índices $\{j : v_j \in A\}$. Es no vacío (contiene a
$0$) y no contiene a $k$ (porque $v_k = v \in B$ y la partición es disjunta). Sea
$j^*$ el **mayor** índice tal que $v_{j^*} \in A$. Como $j^* < k$, el vértice
$v_{j^*+1}$ existe, y por maximalidad de $j^*$ no está en $A$; como $A$ y $B$
cubren $V(G)$, está en $B$.

Entonces $\{v_{j^*}, v_{j^*+1}\}$ es una arista de $P$ —y por lo tanto de
$E(G)$— con un extremo en $A$ y el otro en $B$. $\square$

**($\Leftarrow$)** Por contrarrecíproco: supongamos que $G$ **no** es conexo, y
veamos que existe una partición sin aristas que la crucen.

Como $G$ no es conexo, existen $u, v \in V(G)$ tales que no hay ningún camino de
$u$ a $v$. Definimos
$$A := \{w \in V(G) : \text{existe un camino de } u \text{ a } w\}, \qquad B := V(G) \setminus A.$$

$A$ y $B$ forman una partición: $u \in A$ (el camino de longitud 0), así que
$A \neq \emptyset$; $v \in B$ (no hay camino), así que $B \neq \emptyset$; son
disjuntos y cubren $V(G)$ por construcción.

Veamos que ninguna arista cruza. Supongamos que existe $\{a,b\} \in E(G)$ con
$a \in A$ y $b \in B$. Como $a \in A$, hay un camino $u \rightsquigarrow a$;
agregándole la arista $\{a,b\}$ obtenemos un camino $u \rightsquigarrow b$, luego
$b \in A$ — contradicción con $b \in B$.

Por lo tanto existe una partición sin aristas que la crucen, que es la negación
del lado derecho. $\square$

### Dónde se pierden puntos

El «tomar el último vértice del camino que está en $A$» es el paso que la mayoría
saltea escribiendo «en algún momento el camino cruza». Es verdad, pero **el
argumento es el truco del primer (o último) elemento que cumple una propiedad**,
y hay que escribirlo: el conjunto de índices es no vacío y finito, entonces tiene
máximo.

En la vuelta, definir $A$ como «los alcanzables desde $u$» no es una elección
casual: es la única definición que hace que la verificación de «ninguna arista
cruza» salga sola.

---

## Ejercicio 2 — ¿Cuáles garantizan que $G$ es un árbol?

*(Práctica 2, ejercicio 3)*

> Sea $G$ un grafo de $n \geq 2$ nodos **sin nodos de grado 0**. ¿Cuáles de los
> siguientes ítems garantizan que $G$ es un árbol? Para los que no, dar
> contraejemplo.
>
> a) $n-1$ aristas. b) exactamente 2 nodos de grado 1. c) 2 nodos de grado 1 y
> $n-1$ aristas. d) 2 nodos de grado 1 y no tiene ciclos. e) 2 nodos de grado 1 y
> es conexo. f) 2 nodos de grado 1 y todos los demás tienen grado 2.

### Cómo me di cuenta

La herramienta es la proposición de los **«dos de tres»**: de las propiedades
*conexo*, *acíclico* y *$n-1$ aristas*, dos cualesquiera implican la tercera. Así
que la pregunta se reduce a: **¿este ítem me da dos de las tres?**

Y para los que no, el contraejemplo casi siempre es el mismo objeto: **una
componente con un ciclo más otra componente aparte**. Ese grafo compensa el ciclo
de más con la desconexión, así que suele acertar la cuenta de aristas y falla en
ser árbol.

### La respuesta

**Resumen: el único que garantiza es el (d).**

Llamemos $G_0$ al grafo de $n=6$ formado por un **triángulo** $\{1,2,3\}$ y un
**camino** $4-5-6$ aparte. Tiene $3+2 = 5 = n-1$ aristas, exactamente dos
vértices de grado 1 (el 4 y el 6), ningún vértice de grado 0, y **no es árbol**
(no es conexo ni acíclico). $G_0$ sirve de contraejemplo para (a), (b) y (c).

**a) No.** $n-1$ aristas es sólo **una** de las tres propiedades. Contraejemplo:
$G_0$.

**b) No.** «Dos vértices de grado 1» no es ninguna de las tres. Contraejemplo:
$G_0$.

**c) No.** Este es el ítem trampa: parece que juntar (a) y (b) da dos
propiedades, pero sólo una de las dos ($n-1$ aristas) pertenece a la proposición.
$G_0$ cumple las dos condiciones a la vez y sigue sin ser árbol.

**d) Sí.** Acíclico es una de las tres; hay que ver que la otra condición fuerza
**conexo**.

Como $G$ es acíclico, es un **bosque**: cada componente conexa es un árbol. Por
hipótesis no hay vértices de grado 0, así que ninguna componente tiene un solo
vértice: toda componente tiene $\geq 2$ vértices. Y por el lema de la teórica
—que aplicado a una componente, que es conexa y acíclica, dice que **todo árbol
con al menos dos vértices tiene al menos dos vértices de grado 1**— cada
componente tiene al menos dos hojas. Nótese que el grado dentro de la componente
es el grado en $G$, porque no hay aristas entre componentes.

*(Ojo con cómo está enunciado ese lema en la teórica: «todo grafo acíclico con al
menos dos vértices tiene al menos dos vértices de grado 1». Suelto es falso — dos
vértices sin ninguna arista son un grafo acíclico con cero vértices de grado 1.
Vale para componentes conexas, o sea para árboles, que es como se usa.)*

Entonces cada componente aporta al menos 2 vértices de grado 1. Si hubiera
$\geq 2$ componentes, $G$ tendría $\geq 4$ vértices de grado 1, contradiciendo
que son exactamente 2. Luego hay **exactamente una componente**: $G$ es conexo.

Conexo y acíclico: $G$ es un árbol. $\square$

**e) No.** Conexo es una de las tres, pero «dos vértices de grado 1» no aporta la
segunda. Contraejemplo con $n=5$: el triángulo $\{1,2,3\}$ más las aristas
$\{1,4\}$ y $\{2,5\}$. Grados: $d(1)=d(2)=3$, $d(3)=2$, $d(4)=d(5)=1$. Es conexo,
no tiene vértices de grado 0, tiene exactamente dos vértices de grado 1 — y tiene
un ciclo, así que **no es árbol**.

**f) No.** Acá sí sale una de las tres, por el lema del apretón de manos:
$$2m = \sum_v \deg(v) = 2\cdot 1 + (n-2)\cdot 2 = 2n-2 \implies m = n-1.$$
Pero eso es todo lo que se obtiene, y con una sola propiedad no alcanza.

Contraejemplo con $n=5$: el triángulo $\{1,2,3\}$ más la arista $\{4,5\}$. Grados:
$2,2,2,1,1$ — exactamente dos de grado 1 y los otros tres de grado 2, como pide el
ítem. Tiene $m = 4 = n-1$ aristas (consistente con la cuenta de arriba) y **no es
árbol**.

### Dónde se pierden puntos

El error de fondo en todo el ejercicio es contar «dos vértices de grado 1» como
si fuera una de las tres propiedades de la proposición. **No lo es**: las tres son
*conexo*, *acíclico* y *$n-1$ aristas*, y nada más. Por eso (c) y (f), que parecen
dar dos cosas, en realidad dan una sola.

En (d), que es el único que sí garantiza, lo que hay que escribir es el puente
entre la hipótesis y «conexo»: el conteo de vértices de grado 1 por componente.
Sin ese paso la respuesta queda afirmada, no demostrada.

Y cuando des un contraejemplo, **verificá todas las hipótesis del enunciado** —
acá, que $n \geq 2$ y que no haya vértices de grado 0. Un contraejemplo que viola
una hipótesis no es un contraejemplo.

---

# Algoritmos sobre grafos

## Ejercicio 3 — Plan de actualización de módulos

*(Parcial 1C2024, problema B — enunciado real)*

> Un sistema consta de módulos interconectados, representados por un digrafo $D$
> donde cada vértice es un módulo y cada arista dirigida indica una dependencia
> directa. Un sistema es **mantenible** si y sólo si no contiene ciclos de
> dependencias.
>
> a) Demostrar que si $D$ no tiene ciclos, entonces es posible establecer una
> secuencia en la que cada módulo se procese sólo después de todos los módulos de
> los que depende.
> b) Describir un algoritmo que verifique si el sistema es mantenible y, en caso
> positivo, determine un orden seguro, en $O(n+m)$.
> c) Dar el pseudocódigo.

### Cómo me di cuenta

Tres señales que apuntan al mismo lugar: **digrafo**, **dependencias**, **orden
que las respete**. Eso es literalmente la definición de orden topológico. El
inciso (a) pide el teorema y (b) pide el algoritmo lineal — o sea, la versión con
cola, no la recursiva $O(n(n+m))$.

Cuidado con la orientación de las aristas, que es el error clásico acá. El
enunciado dice sólo «cada arista dirigida indica una dependencia directa», sin
fijar el sentido. **Asumo** que $u \to v$ significa «$u$ necesita que $v$ esté
actualizado», o sea que $v$ va **antes** que $u$. Como el orden topológico
estándar pone el origen antes que el destino, con esa lectura hay que
**invertir**: o das el orden topológico de $D$ y lo leés al revés, o se lo
aplicás a $D$ con las aristas dadas vuelta. Si la convención fuera la opuesta, se
corre el orden topológico directamente sobre $D$.

Escribir ese «asumo que» es parte de la respuesta: el corrector te acepta la
interpretación, pero sólo si está explicitada.

### La respuesta

**a)** Basta probar que todo digrafo acíclico admite un orden topológico. Lo
hacemos por **inducción en $n = |V(D)|$**.

*Lema previo.* Todo digrafo acíclico no vacío tiene un vértice $u$ con
$d^-(u) = 0$. En efecto, tomemos un camino dirigido de longitud máxima
$v_0 \to v_1 \to \dots \to v_k$ (existe porque $D$ es finito y acíclico, así que
los caminos dirigidos no repiten vértices y tienen longitud acotada). Si $v_0$
tuviera un vecino entrante $w$, o bien $w \notin \{v_0,\dots,v_k\}$ y el camino
$w \to v_0 \to \dots \to v_k$ sería más largo (absurdo por maximalidad), o bien
$w = v_j$ para algún $j$, y entonces $v_0 \to \dots \to v_j \to v_0$ sería un
ciclo dirigido (absurdo porque $D$ es acíclico). Luego $d^-(v_0) = 0$. $\square$

*Inducción.* **Caso base $n = 1$:** el único vértice es un orden topológico
válido (no hay aristas que violar).

**Paso inductivo:** sea $D$ acíclico con $n+1$ vértices. Por el lema existe $u$
con $d^-(u) = 0$. El digrafo $D - u$ tiene $n$ vértices y sigue siendo acíclico
(un ciclo de $D-u$ sería un ciclo de $D$), así que por hipótesis inductiva admite
un orden topológico $L'$. Afirmo que $u, L'$ es un orden topológico de $D$: toda
arista de $D$ o bien sale de $u$ —y entonces $u$ está antes que su destino, que
está en $L'$— o bien es una arista de $D-u$, y $L'$ la respeta por HI. No hay
aristas que **entren** a $u$ porque $d^-(u) = 0$, que es exactamente lo que
necesitábamos. $\square$

Traducido al enunciado: si $D$ no tiene ciclos, el orden topológico de $D$
**leído al revés** procesa cada módulo después de todos aquellos de los que
depende.

**b)** Algoritmo: orden topológico por el método de la cola (Kahn).

Mantenemos para cada vértice un contador `entrada[v]` con su grado de entrada, y
una cola con los vértices que ya tienen contador en 0 —es decir, los que están
listos para ser emitidos—. En cada paso sacamos uno de la cola, lo agregamos al
orden, y decrementamos el contador de todos sus vecinos de salida; el que llega a
0 entra a la cola.

Si al terminar el orden tiene menos de $n$ vértices, la cola se vació antes de
tiempo: los vértices que quedaron tienen todos grado de entrada positivo dentro
del subdigrafo restante, y por el lema de (a) eso sólo puede pasar si ese
subdigrafo **tiene un ciclo**. Entonces el sistema no es mantenible. **La
detección de ciclos sale gratis, sin un chequeo aparte.**

*Estructuras:* listas de adyacencia para $D$ (espacio $\Theta(n+m)$), un arreglo
`entrada` de $n$ enteros, una cola, y la lista de salida $L$.

*Complejidad temporal:* calcular todos los `entrada[v]` requiere recorrer todas
las listas una vez, $O(n+m)$. En el ciclo principal, **cada vértice se encola y
se desencola a lo sumo una vez** (entra sólo cuando su contador llega a 0, y el
contador nunca vuelve a subir), y **cada arista se procesa exactamente una vez**
(cuando se decrementa el contador de su destino). Total $O(n+m)$.

*Complejidad espacial:* $O(n+m)$ por las listas, más $O(n)$ por el arreglo, la
cola y $L$. Total $O(n+m)$.

**c)** Pseudocódigo. Uso $D^R$, el digrafo con las aristas invertidas, para que
el orden salga directamente en el sentido de actualización pedido:

```
PLAN-DE-ACTUALIZACIÓN(D)
 1  D^R ← invertir las aristas de D                    // O(n+m)
 2  para todo v ∈ V:  entrada[v] ← 0
 3  para todo (u,v) ∈ E(D^R):  entrada[v] ← entrada[v] + 1
 4  Q ← cola vacía;  L ← ⟨⟩
 5  para todo v ∈ V:
 6      si entrada[v] = 0:  ENCOLAR(Q, v)
 7  mientras Q ≠ ∅:
 8      u ← DESENCOLAR(Q)
 9      agregar u al final de L
10      para todo v ∈ N⁺_{D^R}(u):
11          entrada[v] ← entrada[v] − 1
12          si entrada[v] = 0:  ENCOLAR(Q, v)
13  si |L| < |V|:
14      devolver "el sistema NO es mantenible"       // hay un ciclo
15  devolver L                                        // orden de actualización seguro
```

### Dónde se pierden puntos

Tres cosas, y las tres se olvidan seguido:

**El sentido de las aristas.** Si no aclarás la inversión, el orden que entregás
es exactamente el inverso del pedido. Una línea alcanza, pero tiene que estar.

**La justificación del $O(n+m)$.** No alcanza con escribir la cota: hay que decir
*por qué*. «Cada vértice se encola una vez y cada arista se procesa una vez» es
la frase.

**La complejidad espacial.** El enunciado no la pidió explícitamente acá, pero en
el formato 1C2025 sí la piden y se olvida sistemáticamente.

---

## Ejercicio 4 — Determinar si un grafo es bipartito, en tiempo lineal

*(Práctica 3, ejercicio 10c y 10d)*

> Diseñar un algoritmo lineal para determinar si un grafo conexo $G$ es
> bipartito. Si lo es, devolver una bipartición; si no, devolver un ciclo impar.
> Después generalizarlo a grafos no conexos.

### Cómo me di cuenta

«Bipartito» tiene dos caracterizaciones: *existe una partición sin aristas
internas* y *no hay ciclos impares*. La primera es la definición y no sugiere
algoritmo; la segunda tampoco, porque enumerar ciclos es carísimo.

La que sirve es la **tercera**, la computacional, y sale de la demostración del
teorema: si agrupás los vértices por la **paridad de su distancia a una raíz**,
esa es la única bipartición candidata. Y como necesito distancias sin pesos,
**BFS**.

El enunciado además pide **devolver el ciclo impar** cuando falla, y ahí está la
gracia: el ítem (a) del ejercicio dice que si una arista no-árbol une dos
vértices de la misma paridad, el único ciclo que cierra tiene longitud impar. O
sea, el certificado ya está ahí — hay que saber leerlo.

### La respuesta

Corremos $\text{BFS}(G, r)$ desde un vértice cualquiera $r$, que nos da $d[v]$ y
$\pi[v]$ para todo $v$. Definimos
$$V := \{v : d[v] \text{ es par}\}, \qquad W := \{v : d[v] \text{ es impar}\}.$$

Después recorremos todas las aristas. Si **alguna** arista $\{u,v\}$ cumple
$d[u] \equiv d[v] \pmod 2$, el grafo no es bipartito y esa arista es el
certificado. Si **ninguna** la cumple, $(V,W)$ es una bipartición.

*Correctitud, ida.* Si ninguna arista une vértices de la misma paridad, entonces
por definición toda arista tiene un extremo en $V$ y otro en $W$: $(V,W)$ es una
bipartición y $G$ es bipartito.

*Correctitud, vuelta.* Supongamos que existe $\{u,v\} \in E(G)$ con $d[u]$ y
$d[v]$ de la misma paridad. Sean $P_u$ y $P_v$ los caminos del árbol BFS de $r$ a
$u$ y de $r$ a $v$, de longitudes $d[u]$ y $d[v]$. Sea $x$ el **ancestro común más
profundo** de $u$ y $v$ en el árbol. El camino de $x$ a $u$ tiene longitud
$d[u]-d[x]$, el de $x$ a $v$ tiene $d[v]-d[x]$, y son disjuntos salvo en $x$.
Cerrando con la arista $\{u,v\}$ obtenemos un ciclo de longitud
$$(d[u]-d[x]) + (d[v]-d[x]) + 1 = d[u]+d[v]-2d[x]+1,$$
que es **impar** porque $d[u]+d[v]$ es par (misma paridad) y $2d[x]$ también. Por
la caracterización, un grafo con un ciclo impar no es bipartito. $\square$

*Reconstrucción del ciclo:* subir simultáneamente desde $u$ y desde $v$ por los
punteros $\pi$ hasta encontrar el ancestro común, guardando los vértices
recorridos. Cuesta $O(n)$.

*Complejidad:* BFS es $O(n+m)$; el recorrido de aristas es $O(m)$; la
reconstrucción del ciclo, si hace falta, $O(n)$. Total **$O(n+m)$** temporal, y
$O(n+m)$ espacial (listas de adyacencia, más los arreglos $d$ y $\pi$ de tamaño
$n$).

**Generalización a grafos no conexos.** $G$ es bipartito **si y sólo si** todas
sus componentes conexas lo son: la ida es inmediata (una bipartición de $G$
restringida a una componente es una bipartición de ella), y la vuelta también
(la unión de biparticiones de componentes disjuntas es una bipartición de $G$,
porque no hay aristas entre componentes).

Entonces envolvemos lo anterior en un ciclo exterior que arranca un BFS desde
cada vértice todavía blanco, acumulando los $V_i$ y $W_i$ de cada componente. El
costo sigue siendo $O(n+m)$: el ciclo exterior mira cada vértice una vez, y la
suma de los BFS recorre cada lista de adyacencia una sola vez en total.

### Dónde se pierden puntos

La vuelta de la correctitud es la parte que se saltea. Decir «si hay una arista
dentro de una capa, no es bipartito» es afirmar la conclusión, no demostrarla:
hay que **exhibir el ciclo impar** y contar su longitud.

Y en la generalización, el «si y sólo si» sobre componentes también hay que
enunciarlo, aunque sea en una línea. Es lo que el enunciado llama «observando
que».

---

# Divide & Conquer

## Ejercicio 5 — Izquierda dominante

*(Práctica 4, ejercicio 4)*

> Un arreglo de tamaño potencia de 2 es **«más a la izquierda»** si la suma de su
> mitad izquierda supera a la de la derecha, **y** cada una de las mitades es a su
> vez «más a la izquierda». Escribir un algoritmo D&C que lo determine, con
> complejidad estrictamente menor que $O(n^2)$.

### Cómo me di cuenta

La definición **ya es recursiva** y ya te dice cómo partir. El problema no es
«cómo divido» sino otra cosa, y conviene detectarlo intentando escribir el
algoritmo ingenuo:

```
dominante(A, l, r):
    ... = dominante(mitad izquierda)
    ... = dominante(mitad derecha)
    return izq and der and (suma(izq) > suma(der))     ← acá
```

Ese `suma(izq)` cuesta $O(n)$ si lo calculás en cada nivel, y te da
$T(n) = 2T(n/2) + O(n) = \Theta(n\log n)$. Anda, pero se puede mejor — y sobre
todo, muestra el síntoma: **la recursión devuelve menos de lo que el `combine`
necesita**.

La técnica es **fortalecer el valor de retorno**: que cada llamada devuelva el
booleano **y la suma** del segmento. La suma sale gratis de las dos mitades, así
que el `combine` pasa a costar $O(1)$.

### La respuesta

Generalizamos el problema. La función devuelve un **par**:
$$f(l, r) = (\text{¿es } A[l..r] \text{ más a la izquierda?},\; \textstyle\sum_{k=l}^{r} A[k]).$$
El problema original es la primera componente de $f(0, n-1)$.

```
IZQUIERDA-DOMINANTE(A, l, r)
    si l = r:                                  // segmento de un elemento
        devolver (true, A[l])                  // no tiene mitades: vale vacuamente
    q ← ⌊(l+r)/2⌋
    (domIzq, sumIzq) ← IZQUIERDA-DOMINANTE(A, l, q)
    (domDer, sumDer) ← IZQUIERDA-DOMINANTE(A, q+1, r)
    dom ← domIzq ∧ domDer ∧ (sumIzq > sumDer)
    devolver (dom, sumIzq + sumDer)
```

Llamada inicial: `IZQUIERDA-DOMINANTE(A, 0, n−1)`, y la respuesta es la primera
componente.

*Correctitud, por inducción fuerte en el tamaño $t = r-l+1$ del segmento.*

**Caso base $t=1$:** un segmento de un elemento no tiene mitades, así que cumple
la definición vacuamente y su suma es $A[l]$. ✔

**Paso inductivo $t>1$:** como $n$ es potencia de 2, ambas mitades tienen tamaño
$t/2 < t$, así que por hipótesis inductiva cada llamada devuelve correctamente
el booleano y la suma de su mitad. La definición dice que el segmento es «más a
la izquierda» si y sólo si se cumplen las tres cosas: la mitad izquierda lo es,
la derecha lo es, y $\text{suma(izq)} > \text{suma(der)}$ — que es exactamente la
conjunción que calcula la línea `dom`. Y la suma del segmento es la suma de las
dos mitades. ✔ $\square$

*Complejidad.* Dividir cuesta $O(1)$ (calcular $q$), hay 2 subproblemas de tamaño
$n/2$, y combinar cuesta $O(1)$ (dos comparaciones, un `and`, una suma):
$$T(n) = 2\,T(n/2) + \Theta(1).$$

Por Teorema Maestro: $a = 2$, $b = 2$, $q = \log_2 2 = 1$, $f(n) = \Theta(1)$.
Como $f(n) = O(n^{1-\varepsilon})$ tomando $\varepsilon = 1$ (que es $> 0$),
estamos en el **caso 1**:
$$T(n) = \Theta(n^{q}) = \Theta(n).$$

Es estrictamente menor que $O(n^2)$, como pedía el enunciado. Espacial: $O(\log n)$
por la pila de recursión, y $O(1)$ adicional por llamada.

*Verificación con el ejemplo:* $A = [8,6,7,4,5,1,3,2]$ da sumas $25$ y $11$ con
$25 > 11$, y recursivamente $14>11$, $8>6$, $7>4$, $6>5$, $5>1$, $3>2$: **true**.
$A = [8,4,7,6,5,1,3,2]$ falla en $[8,4]$ vs. $[7,6]$, porque $12 \not> 13$:
**false**. ✔

### Dónde se pierden puntos

El caso base. «Un elemento es más a la izquierda» necesita la justificación de
que la condición se cumple vacuamente (no hay mitades que comparar). Si no lo
decís, queda como una decisión arbitraria.

Y al aplicar el Teorema Maestro, **nombrar el $\varepsilon$**. En el parcial
1C2024 hay una pregunta entera dedicada a una demostración que usa
$\varepsilon = -6$ y es incorrecta justamente por eso.

---

## Ejercicio 6 — Índice espejo

*(Práctica 4, ejercicio 5)*

> Dado $a = [a_1,\dots,a_n]$ de enteros **distintos** (positivos y negativos) en
> orden **estrictamente creciente**, determinar si existe $i$ con $a_i = i$.
> Ejemplo: $a = [-4,-1,2,4,7]$, con $i = 4$. La complejidad debe ser
> estrictamente menor que lineal.

### Cómo me di cuenta

«Estrictamente menor que lineal» sobre un arreglo ordenado es la firma de
**búsqueda binaria**. Pero el arreglo está ordenado por $a_i$, no por $a_i - i$,
y lo que buscamos es dónde $a_i - i$ vale cero. Así que la pregunta real es:

> ¿hay alguna función de la posición que sea **monótona**, aunque el enunciado no
> lo diga?

Y sí: $g(i) := a_i - i$. La intuición es que $a$ crece **al menos** de a uno por
paso (son enteros distintos y crecientes) mientras que $i$ crece exactamente de a
uno, así que $g$ nunca baja. Esa intuición hay que convertirla en una línea de
demostración.

### La respuesta

Definimos $g(i) := a_i - i$ para $1 \leq i \leq n$.

*Lema: $g$ es no decreciente.* Sea $1 \leq i < n$. Como $a$ es estrictamente
creciente y sus elementos son **enteros**, vale $a_{i+1} \geq a_i + 1$. Entonces
$$g(i+1) = a_{i+1} - (i+1) \geq (a_i + 1) - i - 1 = a_i - i = g(i). \qquad \square$$

Buscar $i$ con $a_i = i$ es buscar $i$ con $g(i) = 0$. Como $g$ es no
decreciente, el predicado $P(i) := [g(i) \geq 0]$ es **monótono**: falso para los
índices chicos, verdadero a partir de cierto umbral $i^*$. Entonces:

1. Buscamos binariamente el **menor** $i^*$ con $g(i^*) \geq 0$.
2. Si no existe (todos los $g(i) < 0$), no hay solución.
3. Si existe, chequeamos $g(i^*) = 0$: si vale, $i^*$ es la respuesta; si
   $g(i^*) > 0$, entonces por monotonía $g(i) > 0$ para todo $i \geq i^*$ y
   $g(i) < 0$ para todo $i < i^*$, así que **no hay solución**.

```
ÍNDICE-ESPEJO(a, n)
    lo ← 1;  hi ← n;  res ← NIL
    mientras lo ≤ hi:
        m ← ⌊(lo+hi)/2⌋
        si a[m] − m ≥ 0:  res ← m;  hi ← m − 1     // sigo buscando a la izquierda
        si no:            lo ← m + 1
    si res = NIL:          devolver "no existe"
    si a[res] − res = 0:   devolver res
    si no:                 devolver "no existe"
```

*Complejidad.* $T(n) = T(n/2) + \Theta(1)$. Teorema Maestro con $a=1$, $b=2$,
$q = \log_2 1 = 0$, $f(n) = \Theta(1) = \Theta(n^0 \log^0 n)$: **caso 2** con
$r = 0$, así que $T(n) = \Theta(n^0 \log n) = \Theta(\log n)$. Espacial $O(1)$ si
se escribe iterativo, $O(\log n)$ si es recursivo.

*Verificación:* $a = [-4,-1,2,4,7]$ da $g = [-5,-3,-1,0,2]$. El menor $i$ con
$g(i) \geq 0$ es $i=4$, y $g(4) = 0$: devuelve 4. ✔

### Dónde se pierden puntos

**La monotonía hay que demostrarla.** «Como el arreglo está ordenado, $a_i - i$
es creciente» es falso en general (si los elementos fueran reales, o si se
repitieran) — se apoya en que son **enteros distintos**, y esa hipótesis hay que
usarla explícitamente.

Y el paso 3: no alcanza con encontrar el umbral, hay que chequear que ahí el
valor sea exactamente 0 y **argumentar por qué si no lo es, no hay solución en
ningún otro lado**.

---

# Backtracking

## Ejercicio 7 — Las dos cotas del Sudoku

*(Parcial 1C2025, pregunta 15 — enunciado real)*

> Sudoku $N$: rellenar una matriz $N\times N$ con números de 1 a $N$ sin repetir
> en la misma fila ni en la misma columna. Dadas estas dos soluciones:
>
> ```python
> def Sudoku(estado, celda):              def Sudoku_poda(estado, celda):
>     if celda == N*N:                        if celda == N*N:
>         return int(es_valido(estado))           return 1
>     fil, col = celda // N, celda % N        fil, col = celda // N, celda % N
>     retorno = 0                             retorno = 0
>     for num in range(1, N+1):               for num in range(1, N+1):
>         estado[fil][col] = num                  estado[fil][col] = num
>         retorno += Sudoku(estado, celda+1)      if es_valido(estado):
>         estado[fil][col] = 0                        retorno += Sudoku_poda(estado, celda+1)
>     return retorno                              estado[fil][col] = 0
>                                             return retorno
> ```
>
> Demostrar que: **A)** los estados visitados por `Sudoku` son $\Theta(N^{(N^2)})$;
> **B)** los de `Sudoku_poda` son $O((N!)^N \cdot N^2)$.
> Se puede usar sin demostrar que $\sum_{i=1}^{n} p^i \in \Theta(p^n)$.

### Cómo me di cuenta

«Estados visitados» = **nodos del árbol de backtracking** = llamadas recursivas.
No es la complejidad temporal (eso sería nodos × trabajo por nodo). Leer bien qué
se cuenta es la mitad del ejercicio.

Para **(A)**, sin poda: el árbol es completo. Hay $N^2$ celdas y cada una abre
$N$ ramas, así que es un árbol $N$-ario de altura $N^2$. La cuenta sale de la
suma geométrica que el enunciado regala.

Para **(B)**, con poda: el árbol visitado es un subárbol, y sus nodos son
**exactamente los estados parciales válidos**. Entonces hay que **contar estados
válidos**, no nodos del árbol completo. Y para contarlos conviene **relajar**:
contar usando sólo la restricción de filas e ignorando la de columnas da una cota
superior, porque todo estado válido cumple ambas.

Esa idea —contar una supercota olvidando parte de las restricciones— es la misma
que la de las cotas para podar por optimalidad.

### La respuesta

**A)** Sin poda, `Sudoku` llama recursivamente para **todos** los $N$ valores en
cada celda, sin condición. El árbol de llamadas es entonces el árbol $N$-ario
completo de altura $N^2$: la raíz es la llamada con `celda = 0`, y cada nodo con
`celda = k < N²` tiene exactamente $N$ hijos con `celda = k+1`.

La cantidad de nodos en el nivel $k$ es $N^k$, para $0 \leq k \leq N^2$. El total:
$$\#\text{estados} = \sum_{k=0}^{N^2} N^k.$$

Por la propiedad dada, con $p = N$ y $n = N^2$, esa suma está en
$\Theta(N^{N^2})$. (El término $k=0$ agrega 1, que no cambia el orden.)

Luego la cantidad de estados visitados por `Sudoku` es $\Theta(N^{(N^2)})$. $\square$

**B)** Con poda, se hace la llamada recursiva **sólo si** `es_valido(estado)`. Por
lo tanto los nodos visitados a profundidad $k \geq 1$ son exactamente los estados
con las primeras $k$ celdas (en orden por filas) completadas de manera **válida**:
sin repetidos en ninguna fila ni en ninguna columna.

Acotemos cuántos hay a profundidad $k$. Escribamos $k = rN + c$ con
$0 \leq c < N$: el estado tiene $r$ filas **completas** y $c$ celdas en la fila
$r$.

Usamos sólo la restricción de **filas** (ignorar la de columnas sólo puede
aumentar la cuenta, así que sigue siendo cota superior):

- Cada fila completa es una secuencia de $N$ valores **distintos** de
  $\{1,\dots,N\}$, es decir una permutación: a lo sumo $N!$ posibilidades por
  fila, y $r$ filas independientes dan a lo sumo $(N!)^r$.
- La fila parcial tiene $c$ valores distintos elegidos y ordenados entre $N$:
  a lo sumo $\frac{N!}{(N-c)!} \leq N!$ posibilidades.

Entonces, llamando $E_k$ a la cantidad de estados válidos a profundidad $k$:
$$E_k \;\leq\; (N!)^r \cdot \frac{N!}{(N-c)!} \;\leq\; (N!)^r \cdot N!.$$

Si $c > 0$ entonces $r \leq N-1$, y la cota queda $(N!)^{N-1}\cdot N! = (N!)^N$.
Si $c = 0$ entonces la fila parcial está vacía (factor 1) y $r \leq N$, con lo que
la cota es $(N!)^N$. **En todos los casos $E_k \leq (N!)^N$.**

Como hay $N^2 + 1$ profundidades posibles ($k = 0, 1, \dots, N^2$):
$$\#\text{estados} = \sum_{k=0}^{N^2} E_k \;\leq\; (N^2+1)\cdot (N!)^N \;=\; O\big((N!)^N \cdot N^2\big). \qquad \square$$

### Dónde se pierden puntos

En (A), confundir «estados visitados» con «complejidad temporal». La complejidad
temporal sería $\Theta(N^{N^2})$ nodos $\times$ el costo de `es_valido` en las
hojas — otra cuenta.

En (B), el paso que se saltea es **por qué alcanza con contar usando sólo la
restricción de filas**. La frase es: «todo estado válido cumple ambas
restricciones, así que la cantidad de estados que cumplen sólo la de filas es una
cota superior».

Y una observación sobre el esquema de corrección de este ejercicio en particular:
el enunciado aclara que para tener el ejercicio **Bien** las **dos**
demostraciones tienen que estar Bien. Con una sola bien hecha se obtiene Regular.
Conviene repartir el tiempo, no volcarlo todo en (A).

---

## Ejercicio 8 — Repartir las entregas entre dos ayudantes

*(Parcial 2C2025, ejercicio 6 — enunciado real)*

> Hay que repartir $n$ entregas entre dos ayudantes (Alicia y Carlos). Cada
> entrega $j$ tiene $h_j$ hojas. El objetivo es minimizar la diferencia entre la
> cantidad de hojas que corrige cada uno. El algoritmo dado es:
>
> ```python
> def particion(h, solucion):                  def diferencia(h, solucion):
>     if len(solucion) == len(h):                  sum_a = 0; sum_c = 0
>         return diferencia(h, solucion)           for i in range(len(h)):
>     part_a = solucion + ['A']                        if solucion[i] == 'A': sum_a += h[i]
>     part_c = solucion + ['C']                        if solucion[i] == 'C': sum_c += h[i]
>     return min(particion(h, part_a),             return abs(sum_a − sum_c)
>                particion(h, part_c))
> ```
>
> Asumiendo que las líneas `part_a` y `part_c` son $O(1)$, reportar la
> complejidad. Y dibujar el árbol de recursión con $h = [1,5,3]$, escribiendo el
> valor de los nodos de soluciones válidas.

### Cómo me di cuenta

Es backtracking de **optimización** sin podas, sobre el universo
$\text{Sols} = \{A, C\}^n$ — un vector binario disfrazado de letras. Las dos
cuentas de siempre: **cuántos nodos** y **cuánto cuesta cada uno**.

Lo que hace este ejercicio distinto de mochila es que el trabajo **no** es $O(1)$
por nodo: `diferencia` recorre las $n$ entregas cada vez que se llega a una hoja.
Es exactamente la situación de `mochila₁` versus `mochila₂` de la teórica: la
función no lleva un resumen acumulado, así que recalcula todo en la hoja.

### La respuesta

**Complejidad.** El árbol de llamadas es binario (dos hijos por nodo: `'A'` y
`'C'`) y de altura $n$, porque el caso base es `len(solucion) == len(h)` $= n$.
Tiene entonces $2^{n+1}-1 = O(2^n)$ nodos, de los cuales $2^n$ son hojas.

- En los nodos **internos** el trabajo es $O(1)$: dos concatenaciones (dadas como
  $O(1)$ por el enunciado) y un `min`.
- En las **hojas** se llama a `diferencia`, que recorre las $n$ entregas:
  $\Theta(n)$ por hoja.

Total:
$$T(n) = \underbrace{O(2^n)\cdot O(1)}_{\text{internos}} + \underbrace{2^n \cdot \Theta(n)}_{\text{hojas}} = \Theta(n \cdot 2^n).$$

**Complejidad espacial:** la profundidad de la recursión es $n$ y cada llamada
mantiene una `solucion` de longitud $\leq n$; si las listas se copian, hay hasta
$n$ copias vivas de longitud $\leq n$, o sea $O(n^2)$. Si se compartiera el
arreglo deshaciendo al volver, sería $O(n)$.

**Cómo se mejoraría** (no lo pide, pero es la observación que vale): pasando dos
acumuladores `sum_a` y `sum_c` como parámetros, cada hoja responde en $O(1)$ y el
algoritmo baja a $\Theta(2^n)$. Es exactamente el paso de `mochila₁` a
`mochila₂`.

**El árbol para $h = [1,5,3]$.** Cada nodo es una solución parcial; las hojas son
los $2^3 = 8$ vectores completos, y su valor es $|{\text{suma}_A} - \text{suma}_C|$:

```
                              []
                   ┌───────────┴───────────┐
                 [A]                       [C]
             ┌────┴────┐               ┌────┴────┐
          [A,A]     [A,C]           [C,A]     [C,C]
          ┌─┴─┐     ┌─┴─┐           ┌─┴─┐     ┌─┴─┐
        AAA AAC   ACA ACC         CAA CAC   CCA CCC
         9   3     1   7           7   1     3   9
```

La cuenta de cada hoja, con $h = [1,5,3]$:

| hoja | suma A | suma C | valor |
|---|---|---|---|
| AAA | $1+5+3=9$ | $0$ | $9$ |
| AAC | $1+5=6$ | $3$ | $3$ |
| ACA | $1+3=4$ | $5$ | $1$ |
| ACC | $1$ | $5+3=8$ | $7$ |
| CAA | $5+3=8$ | $1$ | $7$ |
| CAC | $5$ | $1+3=4$ | $1$ |
| CCA | $3$ | $1+5=6$ | $3$ |
| CCC | $0$ | $9$ | $9$ |

El mínimo es **1**, alcanzado por ACA y CAC (Alicia corrige $\{1,3\}$ = 4 hojas y
Carlos la de 5, o al revés). El árbol es simétrico: cambiar todas las A por C da
el mismo valor, porque la diferencia está en valor absoluto.

### Dónde se pierden puntos

En el parcial corregido, la respuesta a la complejidad fue $O(2^n \cdot |h|)$ —
que es correcta— pero el corrector marcó el árbol con **«no son estos los
valores»**. Vale la pena hacer la tabla de las ocho hojas a mano en vez de
completarlas de memoria: es un minuto y evita perder el ítem entero.

Y sobre el árbol: el enunciado pide «para los nodos de soluciones válidas,
escriba su valor». Acá **todas** las hojas son válidas (cualquier reparto es un
reparto legal), así que hay que escribir los ocho valores. Si el enunciado
tuviera restricciones, habría hojas sin valor.

---

# Para hacer vos

Cuatro más, sin solución, del mismo estilo y dificultad. Resolvelos escribiendo
los seis ítems del checklist.

1. **(Grafos)** Demostrar que si $G$ es conexo y tiene exactamente un ciclo,
   entonces $G$ no tiene puentes... o dar un contraejemplo. *(Práctica 3,
   ejercicio 11b. Pensá primero qué pasa con las aristas que no están en el
   ciclo.)*

2. **(Algoritmos sobre grafos)** Un tablero de $n \times n$ tiene algunas casillas
   bloqueadas. Un caballo de ajedrez está en $(r_0,c_0)$ y quiere llegar a
   $(r_1,c_1)$ con la mínima cantidad de saltos. Modelá el problema y dá un
   algoritmo, con su complejidad **en términos de $n$**. *(Aplicá los siete pasos
   de la sección 3.2 de la guía de modelado.)*

3. **(D&C)** Práctica 4, ejercicio 7: dado un árbol binario cualquiera, devolver
   el tamaño del camino más largo, sin hacer recorridos innecesarios. *(La ayuda
   de la guía dice: «posiblemente necesite conocer más que sólo los caminos más
   largos de sus subárboles». Eso es fortalecer el retorno.)*

4. **(Backtracking)** Dado un grafo $G$ y un entero $k$, contar de cuántas formas
   se pueden colorear los vértices con $k$ colores de modo que ningún par de
   vértices adyacentes comparta color. Dá $\text{Sols}$, $\text{válida}$, la
   función recursiva con su semántica, una poda por factibilidad **con
   demostración**, y la complejidad. *(Ojo: es conteo, no optimización — mirá qué
   fila de la tabla de las cinco preguntas te toca.)*
