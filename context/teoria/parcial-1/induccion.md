# Inducción, en escalera

> Todos los ejercicios de inducción de las Prácticas 1 y 2, ordenados de menos a
> más difícil. De cada uno te doy **el planteo** —qué es $P(n)$, sobre qué
> inducís, cuántos casos base, qué sacás y dónde usás la HI— y no la cuenta.
> La cuenta es tuya: es lo único que se entrena.
>
> Para los ejercicios de «encontrar el error» sí te doy el diagnóstico, porque ahí
> el diagnóstico **es** la respuesta.

---

## 0. El molde, y la pregunta que va antes

La teórica lo escribe en cuatro pasos:

1. **Definir explícitamente $P(n)$**, con sus cuantificadores.
2. **Probar el caso base** (o los casos base).
3. **Probar el paso inductivo:** asumir la HI, *decir que la asumís*, deducir
   $P(n+1)$, y **marcar dónde** usás la HI.
4. **Concluir:** «por inducción, $P(n)$ vale para todo $n$».

El paso 1 es el que todos saltean y donde nacen casi todos los errores.

Pero antes del paso 1 hay una pregunta que la teórica plantea como advertencia:

> **La inducción es sobre naturales.** No es «sobre conjuntos» ni «sobre
> secuencias» ni «sobre grafos». Si querés inducir sobre otra estructura, $P$
> tiene que hablar de un **tamaño natural** de esa estructura.

Entonces la pregunta cero, siempre, es: **¿sobre qué número induzco?** En los
ejercicios de grafos hay dos candidatos —la cantidad de vértices $n$ y la de
aristas $m$— y elegir mal te deja una demostración que no cierra. La sección 4
trata eso, que es lo que más pesa en el parcial.

### Cómo se ve escrito

Este es el nivel de detalle que se espera. Fijate las cuatro marcas:

> **Proposición.** Para todo $n \geq 1$: $\sum_{i=1}^{n} i = \frac{n(n+1)}{2}$.
>
> *Demostración.* Sea **(1)** $P(n) := \big[\sum_{i=1}^{n} i = n(n+1)/2\big]$.
> Probamos $P(n)$ para todo $n \geq 1$ por inducción en $n$.
>
> **Caso base $P(1)$: (2)** $\sum_{i=1}^{1} i = 1$ y $\frac{1\cdot 2}{2} = 1$.
> Vale.
>
> **Paso inductivo.** Sea $n \geq 1$ y **(3) asumamos $P(n)$**, es decir,
> $\sum_{i=1}^{n} i = n(n+1)/2$. Entonces
> $$\sum_{i=1}^{n+1} i = \Big(\sum_{i=1}^{n} i\Big) + (n+1) \overset{\text{(3) HI}}{=} \frac{n(n+1)}{2} + (n+1) = \frac{n(n+1) + 2(n+1)}{2} = \frac{(n+1)(n+2)}{2},$$
> que es $P(n+1)$.
>
> **(4)** Por inducción, $P(n)$ vale para todo $n \geq 1$. $\square$

Ese es el **Ejercicio 8 de la Práctica 1**, que viene medio completado justamente
para que copies el molde. Hacelo primero, aunque te parezca trivial: es la
plantilla que vas a repetir catorce veces.

---

## Nivel 1 — El molde solo

Tres ejercicios que son el mismo molde con variaciones mínimas. No los saltees:
sirven para que la estructura te salga sin pensar, y así después puedas gastar la
cabeza en la parte difícil.

### P1 · Ejercicio 12 — Suma de impares

> $1 + 3 + 5 + \dots + (2n+1) = (n+1)^2$ para todo $n \geq 0$.

**Planteo.** $P(n) := \big[\sum_{i=0}^{n}(2i+1) = (n+1)^2\big]$. Caso base $n=0$.
Inducción simple en $n$, un solo caso base.

**Dónde está el trabajo.** En nada, y esa es la idea. Lo único a mirar: el índice
arranca en $0$, no en $1$. Si escribís $P(n)$ con el índice mal, el caso base te
da otra cosa y te volvés loco buscando un error que está en el paso 1.

### P1 · Ejercicio 13 — Suma de potencias de 2

> Encontrar una fórmula para $1 + 2 + 2^2 + \dots + 2^n$ y demostrarla por
> inducción.

**Planteo.** Acá hay **dos trabajos distintos** y conviene no mezclarlos:
*descubrir* la fórmula y *demostrarla*. Para descubrirla, calculá los primeros
valores ($1, 3, 7, 15, 31$) y buscá el patrón. Para demostrarla, el molde de
siempre.

**Dónde está el trabajo.** En entender que la inducción **no descubre nada**:
sirve para verificar una fórmula que ya tenés. Si el parcial te pide «encontrar y
demostrar», son dos párrafos separados.

### P1 · Ejercicio 14 — La colonia de hormigas

> La población se duplica todos los años; empieza con 10. ¿Cuántas hormigas hay
> después de $n$ años? Pasar el enunciado a fórmulas y demostrarlo por inducción.

**Planteo.** El ejercicio pide explícitamente **formalizar primero**. La versión
formalizada es: sea $b_0 = 10$ y $b_{n+1} = 2\,b_n$ para todo $n \in \mathbb{N}$;
probar que $b_n = 10 \cdot 2^n$ para todo $n$.

**Dónde está el trabajo.** En la formalización, y es el punto de todo el
ejercicio. La teórica tiene el ejemplo gemelo (la colonia que se triplica) y
marca las cuatro cosas que ganás al formalizar: **nombrar** los objetos,
**explicitar** las relaciones, **cuantificar** las variables y usar **conectores**
lógicos. Fijate que la ambigüedad del castellano —«el doble del doble del
doble... de 10», ¿cuántas veces?— desaparece apenas escribís $b_{n+1} = 2b_n$.

---

## Nivel 2 — El caso base no tiene por qué ser 0

### P1 · Ejercicio 15 — $2^n > n^2$

> Probar por inducción que para $n \geq 5$ vale $2^n > n^2$. **¿Qué pasa para
> $n < 5$?**

**Planteo.** $P(n) := [2^n > n^2]$, caso base $n = 5$ ($32 > 25$), y en el paso
inductivo tomás $n \geq 5$ —no $n \geq 0$— porque la HI sólo la tenés a partir de
ahí.

**Dónde está el trabajo.** En el paso inductivo tenés $2^{n+1} = 2 \cdot 2^n > 2n^2$
por HI, y querés llegar a $(n+1)^2$. Te falta probar que $2n^2 \geq (n+1)^2$, que
equivale a $n^2 - 2n - 1 \geq 0$. **Esa desigualdad auxiliar no vale para todo
$n$** — hay que decir desde qué $n$ vale y verificar que tu caso base está por
encima.

**La segunda pregunta es la importante.** «¿Qué pasa para $n<5$?» no es retórica:
calculalo. Vas a encontrar que la propiedad **vale** para $n=0$ y $n=1$, y
**falla** para $n=2,3,4$. O sea que el caso base corrido no es un capricho de
comodidad: arrancar en 5 es obligatorio, y además el conjunto donde vale la
propiedad no es un intervalo. Ese es exactamente el ejemplo que la teórica usa
con $n! > 2^n$.

---

## Nivel 3 — Diagnosticar inducciones rotas

**Este es el nivel más importante de todos**, y la propia guía lo marca: los tres
ejercicios están con ⋆. La cátedra enseña el esqueleto rompiéndolo, y en el
parcial te van a dar una demostración para que encuentres el error —como pasó con
el ejercicio 2 de la Práctica 2.

Para cada uno, antes de leer el diagnóstico, preguntate las tres cosas del
checklist: *¿está definido $P(n)$? ¿alcanzan los casos base? ¿la HI se aplica a
algo que cumple sus hipótesis?*

### P1 · Ejercicio 9 ⋆ — «$a^n = 1$ para todo $a \neq 0$»

> Caso base $n=0$: $a^0 = 1$. Paso: supongamos $a^{n-1} = 1$. Entonces
> $a^n = \frac{a^{n-1} \cdot a^{n-1}}{a^{n-2}} = \frac{1 \cdot 1}{1} = 1$.

**El error: faltan casos base.** El paso inductivo usa $P(n-1)$ **y** $P(n-2)$
—mirá el denominador—, así que por la regla de la teórica hacen falta **dos**
casos base: $P(0)$ y $P(1)$. Y $P(1)$ dice $a^1 = 1$, que es falso para todo
$a \neq 1$. Ahí se cae todo.

Hay un segundo síntoma del mismo problema: para $n=1$, el denominador es
$a^{n-2} = a^{-1}$, y nos caímos de $\mathbb{N}$. La teórica lo dice así: «para
$n < k$, $P(n-k)$ no tiene sentido».

**La regla que te tenés que llevar:** contá cuántos valores anteriores usa tu paso
inductivo. Si usa $P(n-1)$ y $P(n-2)$, necesitás dos casos base. Si usa
$P(n-4)$, necesitás cuatro.

### P1 · Ejercicio 10 ⋆ — «Todos los elementos de un conjunto son iguales»

> Caso base $n=1$: el único elemento es igual a sí mismo. Paso: supongamos
> $x_1 = \dots = x_{n-1}$. Como también vale la HI para un conjunto de dos
> elementos, $x_{n-1} = x_n$, y entonces $x_1 = \dots = x_n$.

**El error: la HI se usa para un tamaño del que la HI no habla.** La hipótesis
inductiva es $P(n-1)$ y nada más. La frase «como también vale la HI para un
conjunto de dos elementos» está invocando $P(2)$, que no es lo que asumimos —
salvo en el caso particular $n-1 = 2$.

Y $P(2)$ es justamente lo que habría que demostrar: es el eslabón que falta. El
dominó tiene la primera ficha ($P(1)$) y una regla que tira de la tercera en
adelante, pero **la segunda ficha nunca cae**.

**La regla:** la HI es una afirmación sobre **un** valor (o, en inducción fuerte,
sobre *todos* los menores). Si la aplicás a un valor que no está cubierto, no la
estás usando: la estás asumiendo.

### P1 · Ejercicio 11 ⋆ — «Suma positiva»

> Si un conjunto de enteros no negativos tiene al menos un número positivo,
> la suma de sus elementos es positiva. Inducción en el tamaño $n$.
>
> Caso base $n=1$: si el conjunto tiene un solo número $a$ y es positivo, la suma
> es $a > 0$. Paso: saquemos un elemento cualquiera $k$, quedándonos con un
> subconjunto $C$ de $n-1$ elementos. Por HI la suma de $C$ es positiva, y
> agregarle $k$, que es no negativo, no puede hacerla no positiva.

El enunciado pregunta «¿hay más de uno?». Sí, hay tres, y conviene separarlos.

**Error 1, el grave: la HI se aplica a algo que no cumple sus hipótesis.** $P(n)$
habla de conjuntos que tienen *al menos un elemento positivo*. Si el elemento $k$
que sacás era **el único positivo**, entonces $C$ no tiene ninguno y la HI **no
dice nada sobre $C$**. La frase «por hipótesis inductiva, la suma de los
elementos de $C$ es positiva» es falsa en ese caso.

**Error 2: $P(n)$ nunca se define.** Sin escribirlo, es imposible darse cuenta del
error 1 — de hecho ese es el mecanismo: el error se esconde en la hipótesis que no
escribiste.

**Error 3: «sacar un elemento cualquiera» es una elección, no una deducción.** En
el paso inductivo vos elegís qué sacar. Decir «cualquiera» y después necesitar que
sea uno en particular es hacer trampa.

**Cómo se arregla.** $P(n) := $ «todo conjunto de $n$ enteros no negativos con al
menos un elemento positivo tiene suma positiva». En el paso, tomá un conjunto $X$
arbitrario de $n+1$ elementos con al menos un positivo, **fijá uno positivo $p$**,
y sacá cualquier elemento $k \neq p$ (existe porque $|X| = n+1 \geq 2$). Ahora
$C = X \setminus \{k\}$ tiene $n$ elementos **y sigue conteniendo a $p$**, así que
la HI sí aplica. Y $\text{suma}(X) = \text{suma}(C) + k > 0$ porque $k \geq 0$.

Fijate lo que cambió: **elegir bien qué sacar**. Eso es todo el oficio de la
inducción sobre estructuras, y es lo que vuelve en cada ejercicio de grafos.

---

## Nivel 4 — Inducción sobre grafos

### La decisión que hay que tomar primero: ¿en $n$ o en $m$?

| Inducís en... | Sacás... | ¿Se rompen las hipótesis? |
|---|---|---|
| **$m$ = cantidad de aristas** | una arista | **Casi nunca.** Un grafo menos una arista sigue siendo un grafo. |
| **$n$ = cantidad de vértices** | un vértice | **Casi siempre.** Sacar un vértice cambia grados, puede desconectar, puede dejar vértices aislados. |

De ahí sale toda la dificultad relativa. Los ejercicios que inducen en $m$ salen
en cinco líneas; los que inducen en $n$ son ejercicios de verdad, y el trabajo
entero está en **elegir qué vértice sacar** para que lo que queda cumpla las
hipótesis de la HI.

Regla práctica para elegir sobre qué inducir: mirá **de qué habla la cota del
enunciado**. Si la propiedad involucra una cota que depende de $n$ —como
«más de $(n-1)(n-2)/2$ aristas»— la inducción tiene que ser en $n$, porque si no
la cota no cambia entre un caso y el siguiente.

### P2 · Ejercicio 4 ⋆ — Lema del apretón de manos

> Demostrar por inducción en $|E(G)|$ que $\sum_{v \in V(G)} \deg_G(v) = 2|E(G)|$.

**Planteo.** $P(m) := $ «todo grafo con $m$ aristas cumple
$\sum_v \deg(v) = 2m$». Inducción en $m$. Caso base $m = 0$: todos los grados son
0 y la suma es $0 = 2\cdot 0$.

**Paso.** Sea $G$ un grafo **arbitrario** con $m+1$ aristas. Elegí una arista
$e = \{u,v\}$ y considerá $G - e$, que tiene $m$ aristas. La HI aplica **sin
condiciones**: $G-e$ es un grafo, y eso es todo lo que $P$ pide. Después compará
los grados: $\deg_G(u) = \deg_{G-e}(u) + 1$, lo mismo para $v$, y ningún otro
vértice cambia.

**Por qué es fácil.** Porque $P(m)$ no tiene hipótesis extra: habla de *todo*
grafo con $m$ aristas. Cuando la HI no pide nada, sacar lo que sea funciona.

**Lo único a cuidar:** al sacar la arista, $V(G-e) = V(G)$ — **no se eliminan los
extremos**. Es el error de escritura más común del ejercicio.

### P2 · Ejercicio 5 ⋆ — Equilibrio en digrafos

> Demostrar por inducción en la cantidad de aristas que todo digrafo $D$ cumple
> $\sum_v d^-(v) = \sum_v d^+(v) = |A(D)|$.

**Planteo.** Idéntico al anterior: $P(m)$ sobre todos los digrafos con $m$ arcos,
caso base $m=0$, y en el paso sacás un arco $(u,v)$.

**La única diferencia con el 4:** cada arco aporta **1 a $d^+(u)$ y 1 a $d^-(v)$**,
uno de cada lado, mientras que una arista no dirigida aporta 2 a la misma suma.
Por eso acá da $|A|$ y allá daba $2|E|$. Hacé los dos seguidos y escribí la
diferencia en una línea: es una pregunta natural de multiple choice.

### P2 · Ejercicio 2 — El error de Fede

> Fede dice que todo grafo de $n \geq 2$ vértices con todos los grados $\geq 1$ es
> conexo, y da una demostración por inducción. Dai dice que tiene un
> contraejemplo.
>
> a) Mostrá el contraejemplo. b) ¿Qué error tuvo Fede? c) Una versión más
> rigurosa, ¿arregla el error? d) Fede cambia el paso inductivo para *sacar* un
> vértice en vez de agregar uno. ¿Ahora cuál es el error?

**Este es el ejercicio más importante de la Práctica 2** y no lo parece. Hacelo
entero, los cuatro ítems.

**(a) El contraejemplo.** Buscá el grafo más chico posible con todos los grados
$\geq 1$ que no sea conexo. Pista: dos piezas separadas, cada una con lo mínimo
para que nadie tenga grado 0.

**(b) y (c) El error: construir en vez de tomar arbitrario.** El paso inductivo
dice «agreguemos un vértice $v$ a un grafo $G$ de $n$ vértices». Eso demuestra que
*los grafos que se obtienen agregando un vértice a uno que ya cumple la
hipótesis* son conexos. Pero $P(n+1)$ habla de **todos** los grafos de $n+1$
vértices con grados $\geq 1$, y no todos se obtienen así.

Volvé a la tabla de Alicia y Beto de la teórica: en un $\forall$, **el $x$ lo
elige Beto**. Fede eligió el suyo. Por eso la versión «más rigurosa» del ítem (c)
**no arregla nada**: está mejor escrita, con $P(n)$ explícito y los
cuantificadores en su lugar, pero sigue construyendo el grafo de $n+1$ en vez de
tomar uno cualquiera. El error no era de prolijidad.

Para verlo concreto: tomá tu contraejemplo de (a) y preguntate si se obtiene
agregándole un vértice a un grafo de $n$ vértices con todos los grados $\geq 1$.
No se obtiene — y ahí está el agujero, señalado con el dedo.

**(d) El otro error: la HI aplicada a algo que no cumple sus hipótesis.** Ahora sí
toma un $G$ arbitrario de $n+1$ vértices y le saca un vértice $v$. Bien. Pero
$G - v$ **puede tener vértices de grado 0** —todos los que eran vecinos sólo de
$v$—, y entonces no cumple la hipótesis de $P(n)$. La frase exacta donde miente
es «El grafo $G - v$ tiene $n$ vértices y los grados de todos sus vértices son al
menos 1»: eso no se sigue de nada.

Y notá que es **el mismo error del Ejercicio 11 de la Práctica 1**. Si los hacés
seguidos, el patrón se te queda.

### P2 · Ejercicio 7 ⋆ — Muchas aristas implica conexo

> Demostrar por inducción en la cantidad de vértices que todo grafo de $n$
> vértices con más de $\frac{(n-1)(n-2)}{2}$ aristas es conexo.

**Planteo.** $P(n) := $ «todo grafo de $n$ vértices con más de $(n-1)(n-2)/2$
aristas es conexo». Inducción en $n$. Caso base $n=2$: la cota es 0, así que hay
al menos una arista, y un grafo de dos vértices con una arista es conexo.

**El paso, que es donde está todo el ejercicio.** Tomás $G$ arbitrario con $n+1$
vértices y $m > n(n-1)/2$ aristas, y querés sacar un vértice $v$ tal que $G-v$
siga cumpliendo la hipótesis de la HI, o sea $m - \deg(v) > (n-1)(n-2)/2$.

Hacé la cuenta de cuánto podés permitirte que valga $\deg(v)$:
$$\frac{n(n-1)}{2} - \frac{(n-1)(n-2)}{2} = \frac{(n-1)\big[n - (n-2)\big]}{2} = n-1.$$

O sea: **te alcanza con encontrar un vértice de grado $\leq n-1$**. Ahora te
quedan dos cosas por resolver, y las dos son cortas:

1. ¿Siempre existe uno? Si **todos** los vértices tuvieran grado $\geq n$, como el
   grafo tiene $n+1$ vértices el grado máximo posible es $n$, así que todos
   tendrían grado exactamente $n$ y $G$ sería el completo $K_{n+1}$ — que es
   conexo, y ese caso lo cerrás aparte.
2. Una vez que $G-v$ es conexo por HI, ¿cómo pegás $v$? Necesitás $\deg(v) \geq 1$.
   Probalo por absurdo: si $\deg(v) = 0$, las $m$ aristas viven entre los otros
   $n$ vértices, y ahí no entran más de $n(n-1)/2$.

**Lo que hay que llevarse:** la elección del vértice no fue estética. Salió de
**hacer la cuenta primero** —cuánto puedo permitirme que valga $\deg(v)$— y
después buscar un vértice que la cumpla. Ese es el método.

**El subítem que se olvida.** El Ejercicio 12b pregunta si se puede dar una cota
mejor a partir de algún $n_0$. La respuesta es **no, la cota es ajustada**, y se
responde exhibiendo el **grafo extremal**: un $K_{n-1}$ más un vértice aislado
tiene exactamente $(n-1)(n-2)/2$ aristas y es disconexo. O sea que bajar la cota
aunque sea en uno rompe el enunciado, para todo $n \geq 2$. Un contraejemplo
explícito es toda la respuesta.

### P2 · Ejercicio 17 — Triángulo inductivo

> Demostrar por inducción que todo grafo de $2n$ vértices con más de $n^2$ aristas
> tiene un triángulo.

**Planteo.** $P(n) := $ «todo grafo de $2n$ vértices con más de $n^2$ aristas
tiene un triángulo». Inducción en $n$. Caso base $n=1$: dos vértices y más de una
arista es imposible en un grafo simple, así que $P(1)$ vale **por vacuidad** —
decilo, es una respuesta legítima y elegante.

**El paso.** Acá no sacás un vértice sino **dos**: los extremos de una arista. Sea
$G$ con $2n+2$ vértices y más de $(n+1)^2$ aristas, y supongamos por absurdo que
no tiene triángulos. Tomá cualquier arista $\{u,v\}$.

La clave: **si no hay triángulos, $u$ y $v$ no tienen ningún vecino en común**.
De ahí sacás una cota para $\deg(u) + \deg(v)$ en términos de $2n+2$. Después
contá cuántas aristas desaparecen al borrar $u$ y $v$ —ojo, la arista $\{u,v\}$ se
cuenta una sola vez— y verificá que lo que queda es un grafo de $2n$ vértices con
más de $n^2$ aristas. La HI te da un triángulo, que contradice el supuesto.

**Por qué este es más lindo que el 7:** la elección de qué sacar viene de la
**propiedad que querés negar** (no hay triángulos ⟹ no hay vecinos comunes), no de
una cuenta de grados. Son los dos estilos.

**La segunda pregunta del enunciado** («¿se puede dar una cota mejor que $n^2$ a
partir de algún $n_0$?») se responde igual que en el 7: **no**, y el testigo es el
**bipartito completo balanceado $K_{n,n}$**, que tiene exactamente $n^2$ aristas y
ningún triángulo — porque es bipartito, y un triángulo es un ciclo impar.
Cualquier cota menor que $n^2$ lo tendría como contraejemplo.

### P2 · Ejercicio 13 — Dos vértices que no son de articulación

> Demostrar por inducción que todo $G$ conexo con $|V| \geq 2$ tiene al menos dos
> vértices distintos $v_1, v_2$ tales que $G - v_1$ y $G - v_2$ son conexos.

**El más difícil de la guía.** Dejalo para el final.

**Planteo.** $P(n) := $ «todo grafo conexo de $n \geq 2$ vértices tiene al menos
dos vértices que no son de articulación». Inducción (fuerte, conviene) en $n$.
Caso base $n=2$: el único grafo conexo de dos vértices es $K_2$, y sacar
cualquiera de los dos deja un solo vértice, que es conexo.

**El paso, por casos.** Tomá $G$ conexo con $n+1$ vértices.

- Si $G$ **no tiene** ningún punto de articulación, listo: cualquier par de
  vértices sirve, y hay al menos dos.
- Si $G$ **tiene** un punto de articulación $v$, entonces $G-v$ tiene $k \geq 2$
  componentes conexas $C_1, \dots, C_k$. Para cada $i$, el subgrafo inducido por
  $V(C_i) \cup \{v\}$ es **conexo** y tiene al menos 2 vértices, así que por HI
  tiene dos vértices que no son de articulación **en él**; al menos uno de los dos
  es distinto de $v$.

Te quedan dos cosas por cerrar, y son el ejercicio: (i) por qué
$V(C_i) \cup \{v\}$ es conexo y por qué tiene menos de $n+1$ vértices —que es lo
que habilita la HI—, y (ii) por qué un vértice que no es de articulación **dentro
de $C_i \cup \{v\}$** tampoco lo es en $G$ entero. Para (ii), pensá qué pasa con
los caminos que salen de $C_i$: todos pasan por $v$.

Como tomás dos componentes distintas, te salen dos vértices distintos.

---

## Nivel 5 — Cuando el objeto no tiene un solo tamaño

### P1 · Ejercicio 16 ⋆ — El triángulo de Pascal

> Pascalito llena una matriz infinita: 1 en toda la fila 0 y toda la columna 0, y
> en el resto la suma del de arriba más el de la izquierda. Demostrar **por
> inducción en la tupla $(f,c)$** que la celda $(f,c)$ contiene $\binom{f+c}{c}$.
> **Definir claramente cuándo un par $(f,c)$ es menor que otro.**

**Planteo.** El enunciado te dice qué es lo difícil: la matriz no se indexa por un
natural sino por un **par**, y la inducción es sobre naturales. La teórica lo
resuelve con un **orden bien fundado** —un orden sin cadenas infinitas
decrecientes— y da dos opciones:

- **Por una medida:** $(f',c') \prec (f,c)$ si $f' + c' < f + c$. Reduce todo a
  inducción (fuerte) en el natural $f+c$.
- **Lexicográfico:** $(f',c') \prec (f,c)$ si $f' < f$, o si $f' = f$ y $c' < c$.

Para este ejercicio **la medida $f+c$ es la natural**, porque la recurrencia usa
$(f-1,c)$ y $(f,c-1)$, y los dos tienen suma exactamente uno menos.

**Estructura.** $P(f,c) := [M[f][c] = \binom{f+c}{c}]$. Casos base: $f=0$ (toda la
fila) y $c=0$ (toda la columna) — son **dos familias** de casos base, no dos
casos. Paso: para $f,c \geq 1$, asumís $P$ para todo par $\prec (f,c)$, en
particular para $(f-1,c)$ y $(f,c-1)$, y usás la identidad de Pascal
$\binom{a-1}{b-1} + \binom{a-1}{b} = \binom{a}{b}$.

**Lo que se corrige:** que **definas el orden explícitamente antes de largar la
inducción**. El enunciado lo pide con todas las letras y vale puntos por sí solo.

**El Ejercicio 17** es la continuación: programar la función recursiva y testearla
contra la fórmula cerrada. Vale hacerlo — es el mismo bucle
«fórmula ↔ implementación ↔ test» que después usás para verificar backtracking
contra fuerza bruta.

### P1 · Ejercicio 18 ⋆ — Cambio de fase, dos veces

> $A \cup B = C$, y $S = (s_1,\dots,s_n)$ con $n \geq 2$, $s_1 \in A$,
> $s_n \in B$. Probar que existe $i$ con $s_i \in A$ y $s_{i+1} \in B$.
> **(a)** por inducción en $n$; **(b)** en forma directa, tomando el primer
> elemento $s_j \in B$ con $j > 1$.

**Este ejercicio es el más útil de toda la guía**, porque te hace demostrar lo
mismo de dos maneras y comparar.

**(a) El planteo inductivo.** $P(n) := $ «para toda secuencia de $n \geq 2$
elementos de $C$ con $s_1 \in A$ y $s_n \in B$, existe $i \leq n-1$ con
$s_i \in A$ y $s_{i+1} \in B$». Caso base $n=2$: inmediato con $i=1$.

En el paso, mirá $s_2$ y **partí en dos casos**: si $s_2 \in B$, terminaste con
$i=1$; si no, como $A \cup B = C$ forzosamente $s_2 \in A$, y entonces la
subsecuencia $(s_2, \dots, s_{n+1})$ tiene longitud $n$, empieza en $A$ y termina
en $B$ — la HI aplica.

Fijate que otra vez lo que hace andar la inducción es **verificar que lo que queda
cumple las hipótesis de la HI**, y que para eso hubo que abrir en casos.

**(b) El planteo directo.** Sea $j := \min\{\,j > 1 : s_j \in B\,\}$. **Justificá
que el conjunto es no vacío** —el enunciado te lo pide explícitamente, y es porque
$s_n \in B$ con $n > 1$—. Después tomá $i = j-1$ y mostrá que $s_{j-1} \in A$,
abriendo en si $j-1 = 1$ o $j - 1 > 1$.

**La moraleja.** La versión (b) entra en cinco renglones y la (a) en quince. Es el
**truco del primer elemento que cumple**, que la teórica presenta justamente como
lo que «muchas veces reemplaza una inducción engorrosa». Cuando en el parcial te
pidan probar que *existe* una posición donde algo cambia, probá primero con el
mínimo: casi siempre sale más corto.

---

## Cuándo NO es inducción

Tres ejercicios de las guías que parecen de inducción y no lo son. Vale hacerlos
para calibrar el reflejo.

**P1 · Ejercicio 19 ⋆ (Palomar general).** «Con $n > 0$ cajas y $m$ objetos, hay
una caja con al menos $\lfloor \frac{m-1}{n} \rfloor + 1$ objetos.» Es **por
absurdo**: suponé que todas tienen a lo sumo $\lfloor (m-1)/n \rfloor$, sumá, y
llegá a $m \leq m-1$. Tres líneas.

**P2 · Ejercicio 6 ⋆ (Doble grado).** «Todo grafo no trivial tiene dos vértices
del mismo grado.» El enunciado pide **reducción al absurdo**, no inducción. La
idea: los grados van de $0$ a $n-1$, pero $0$ y $n-1$ no pueden convivir, así que
quedan $n-1$ valores posibles para $n$ vértices.

**P1 · Ejercicio 18b**, ya visto.

**El reflejo a entrenar:** la inducción sirve cuando la estructura de tamaño $n+1$
**se construye a partir de** una de tamaño $n$ y la propiedad se hereda. Si lo que
hay es un conteo, o un «existe el primero que...», o una cota que sale de sumar,
probablemente haya un camino más corto.

---

## Checklist antes de entregar

Directo de la teórica, con lo que agrega esta guía:

1. **¿Definiste $P(n)$ explícitamente**, con todos sus cuantificadores, antes de
   empezar? (Sin esto no podés detectar el error del Ejercicio 11.)
2. **¿Sobre qué número inducís?** Si es un grafo: ¿$n$ o $m$? ¿Por qué?
3. **¿Cuántos casos base necesitás?** Contá qué valores anteriores usa tu paso.
   Si usa $P(n-1)$ y $P(n-2)$, son dos.
4. **En el paso inductivo, ¿tomaste un objeto arbitrario de tamaño $n+1$ y
   sacaste algo**, o lo construiste a partir de uno de tamaño $n$? Lo segundo está
   mal (error de Fede).
5. **¿Verificaste que lo que quedó cumple las hipótesis de la HI?** Esta es la que
   más se cobra.
6. **¿Marcaste dónde usás la HI?**
7. Si escribiste «sea $x$ el mínimo tal que...»: **¿probaste que el conjunto es no
   vacío?**
8. Releela como Beto, el escéptico: **¿en qué oración le mentirías?**

---

## Orden sugerido

Si tenés una tarde: **P1 8 → 12 → 15 → 9 → 10 → 11 → P2 4 → P2 2 → P2 7**.

Los tres del medio (9, 10, 11) son el corazón: son los que te dan el ojo para
detectar el error, que es lo que después te van a pedir. Y P2 2 es el mismo error
que P1 11, pero disfrazado de grafos — hacelos con poca distancia entre uno y
otro.

Si te sobra tiempo: **P1 18 (los dos incisos) → P1 16 → P2 17 → P2 13**.

---

## Nota sobre el Ejercicio 16 de la Práctica 2

> «Sean $G_2 = K_2$ y $G_{n+1} = G_n \cup K_1$ para todo $n \geq 2$. Demostrar por
> inducción que $G_n$ tiene un único par de vértices de igual grado.»

**Chequeá este enunciado contra el PDF original antes de pelearlo**, porque tal
como está transcripto en `practica_2.md` la afirmación es falsa. Con $\cup$ = unión
disjunta (que es como la define el Ejercicio 15 de esa misma guía), $G_n$ es una
arista más $n-2$ vértices aislados, con grados $1,1,0,0,\dots,0$. Para $n = 4$ los
grados son $1,1,0,0$: hay **dos** pares de vértices de igual grado, no uno.

Probablemente la operación del enunciado original sea otra (la junta, o el
complemento) — la construcción clásica para «todos los grados distintos salvo un
par» alterna complemento y agregado de un vértice. Si el PDF dice lo mismo que la
transcripción, es una errata de la guía y vale preguntarlo en clase.

---

## Fuentes

- `context/teoria/demostraciones/resumen.md` — el principio, los 4 pasos, casos
  base corridos, inducción fuerte, cuántos casos base, orden bien fundado, el
  truco del primer elemento, el checklist
- `context/practica/context/practica_1.md` — ejercicios 8 a 19
- `context/practica/context/practica_2.md` — ejercicios 2, 4, 5, 6, 7, 13, 16, 17
