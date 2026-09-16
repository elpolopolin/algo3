# De enunciado a algoritmo

> Guía de modelado para el 1er parcial. Los cuatro temas: teoría de grafos,
> algoritmos sobre grafos, divide & conquer, backtracking.
>
> Esta guía no explica los algoritmos (para eso están los `resumen.md` de cada
> unidad). Explica **cómo darse cuenta de cuál usar** leyendo el enunciado, y
> **cómo escribirlo** para que sume puntos.

---

## 0. Lo primero: qué te están pidiendo

Antes de pensar en algoritmos, clasificá la consigna. En esta materia hay
exactamente cuatro tipos de pedido, y cada uno se responde distinto:

| El enunciado dice | Te piden | Lo que tenés que entregar |
|---|---|---|
| "Demostrar que...", "Probar que..." | una **demostración** | prosa matemática cerrada, con hipótesis, pasos y □ |
| "Decidir si es verdadera o falsa" | **demostración o contraejemplo** | si es falsa, un objeto concreto; si es verdadera, demostración |
| "Diseñar un algoritmo que..." | **modelado + algoritmo + complejidad** | modelo, pseudocódigo, estructuras, complejidad, correctitud |
| "¿Qué complejidad tiene...?" | un **análisis** | la recurrencia, el método, la cuenta, y la cota ajustada |

La mayoría de los puntos perdidos en los parciales corregidos vienen de
entregar una cosa cuando pedían otra: dar un algoritmo cuando pedían la
demostración de que existe, o dar la intuición cuando pedían la cuenta.

---

## 1. La regla que más puntos vale

En el parcial 2C2025 corregido, casi todas las marcas del corrector son de la
misma familia:

> «¿por qué?» · «¿qué complejidad? ¿otras técnicas?» · «no explicás por qué no
> usar Bottom-Up» · «no dice que greedy no siempre es correcto» · «si cubo Rubik
> es n×n, pero de forma general ya no dice nada del enunciado»

Ninguna de esas respuestas estaba equivocada. Estaban **incompletas**. Entonces:

**Toda afirmación que hagas necesita la frase que la sostiene.** No "se ve que
si ya me pasé de peso no puedo volver", sino "como $w_j \geq 0$ para todo $j$,
vale $\text{peso}(a) \geq pa > W$". La teórica de backtracking lo dice con todas
las letras:

> «Es obvio que si ya me pasé de peso, no puedo volver» no es una demostración.

**Si el enunciado enumera ítems, respondé todos los ítems.** Cuando dice
"justifique su elección **y/o la no elección de las otras técnicas**", la
segunda mitad vale puntos propios. Cuando dice "indicando claramente las
estructuras de datos utilizadas y la complejidad temporal y espacial
resultantes", son tres cosas, no una.

**Cuando generalices, generalizá de verdad.** Si el enunciado dice "un cubo de
Rubik" y vos resolvés para $n \times n$, decilo explícitamente y aclarás que el
caso del enunciado es $n = 3$. Si asumís algo que el enunciado no dice, escribí
"asumo que..." — el corrector te lo acepta, pero solo si está escrito.

Y una de estrategia pura: en el formato 1C2025, el multiple choice **resta 2
puntos** por respuesta incorrecta y **0** por no responder. Si dudás entre dos
opciones y no podés descartar ninguna, dejala en blanco. En el parcial de
75/100 que tenés, hay dos preguntas sin responder y fue la decisión correcta.

---

## 2. Teoría de grafos: qué técnica de demostración usar

Acá no hay algoritmo que elegir; hay **técnica de demostración**. La señal está
casi siempre en la forma del enunciado.

| Señal en el enunciado | Técnica | Por qué |
|---|---|---|
| "para todo grafo $G$ vale $\sum \deg(v) = 2m$" | **inducción en $m$** | agregar una arista sube la suma en 2: el paso inductivo es limpio |
| "todo grafo con $n$ vértices y más de $f(n)$ aristas es conexo" | **inducción en $n$**, o **absurdo** | la cota depende de $n$, así que la inducción tiene que ser en $n$ |
| "existen al menos dos vértices con el mismo grado" | **palomar** (o absurdo) | estás contando objetos en cajas |
| "$X$ **si y sólo si** $Y$" | **dos implicaciones** | y casi siempre una de las dos sale por contrarrecíproco |
| "si $G$ admite orden topológico entonces es acíclico" | **contrarrecíproco** | negar "acíclico" te da un objeto concreto (el ciclo) para trabajar |
| "todo par de caminos máximos se cortan" | **contrarrecíproco** | negar la conclusión te da dos caminos disjuntos, que podés pegar |
| "¿cuáles de estos ítems garantizan que $G$ es árbol?" | **contraejemplo** para los que no | y la proposición de los "dos de tres" para los que sí |
| "demostrar en forma constructiva" | **construcción explícita** | te piden el objeto, no su existencia |

### El reflejo de los "dos de tres"

Para cualquier ejercicio del tipo "¿esto garantiza que es un árbol?": un grafo
de $n$ vértices es árbol si cumple **dos** de estas tres, y entonces cumple la
tercera automáticamente:

1. es conexo, 2. es acíclico, 3. tiene $n-1$ aristas.

Si el ítem te da dos, listo. Si te da una sola (o dos que en realidad son la
misma disfrazada), buscá contraejemplo. El contraejemplo canónico: **un
triángulo suelto más un camino aparte** tiene $n-1$ aristas y no es árbol.

### Dónde se rompen las inducciones (el ejercicio 2 de la Práctica 2)

Ese ejercicio es una trampa didáctica y vale entenderla porque el error es el
más común de la materia. La demostración de Fede falla porque **construye** el
grafo de $n+1$ en vez de **tomar uno arbitrario**. Al agregar un vértice a un
grafo conexo obtenés un conexo, sí — pero no todos los grafos de $n+1$ vértices
con grados $\geq 1$ se obtienen así. El universo que recorre la inducción es más
chico que el universo del enunciado.

La versión de sacar un vértice tampoco anda: al sacar $v$ de $G$, el grafo
$G - v$ puede tener vértices de grado 0, así que **no se le puede aplicar la
hipótesis inductiva**.

> **Regla:** en inducción sobre grafos, siempre empezá con "sea $G$ un grafo
> arbitrario de $n+1$ vértices que cumple la hipótesis" y sacá algo. Y antes de
> usar la HI, verificá que lo que quedó **cumple las hipótesis** de la HI.

### Caracterizaciones que reemplazan trabajo por trabajo fácil

Casi toda la unidad son equivalencias, y cada una existe para cambiar una
condición cara por una barata. Vale tenerlas en una lista corta:

- $e$ es **puente** $\iff$ $e$ no pertenece a ningún ciclo.
  *(Y con DFS, para una arista del árbol con $\pi[v] = u$:
  $\iff \texttt{low}[v] > d[u]$. La hipótesis de que $u$ es el padre de $v$ es
  parte del teorema: para una arista de retroceso la comparación no significa
  nada.)*
- $G$ es **conexo** $\iff$ toda partición $V = A \,\dot\cup\, B$ tiene una arista
  que cruza.
- $G$ es **bipartito** $\iff$ no tiene ciclos impares.
  *(Y computacionalmente: $\iff$ ninguna arista une dos vértices de la misma
  capa BFS.)*
- $D$ admite **orden topológico** $\iff$ $D$ es acíclico.
- Si $G$ es **conexo**: $G$ admite una **orientación fuertemente conexa**
  $\iff$ $G$ no tiene puentes. *(La hipótesis de conexión es imprescindible: dos
  triángulos disjuntos no tienen puentes y no admiten orientación fuertemente
  conexa. Esto no está en la teórica — sale de la Práctica 3, ejercicio 13b.)*

Cuando un enunciado te pide chequear el lado caro, casi siempre la solución es
chequear el lado barato y citar la caracterización.

---

## 3. Algoritmos sobre grafos: la tabla de señales

### 3.1 Cuando el grafo ya está en el enunciado

| El enunciado pide | Algoritmo | Complejidad |
|---|---|---|
| "mínima cantidad de pasos / movimientos / aristas", **sin pesos** | **BFS** | $O(n+m)$ |
| "distancia", "niveles", "capas" | **BFS** | $O(n+m)$ |
| "¿se puede llegar de $u$ a $v$?", "alcanzable" | BFS o DFS (da igual) | $O(n+m)$ |
| "cantidad / tamaño de componentes conexas" | BFS o DFS con ciclo exterior | $O(n+m)$ |
| "un orden que respete dependencias / precedencias / prerequisitos" | **orden topológico** (cola) | $O(n+m)$ |
| "¿hay ciclos?" en un **digrafo** | orden topológico ($|L| < n$) o DFS (arista de retroceso) | $O(n+m)$ |
| "¿hay ciclos?" en un grafo **no dirigido** | DFS (arista de retroceso al no-padre) | $O(n+m)$ |
| "arista crítica", "cuya remoción desconecta", "sin la cual se corta" | **puentes** con `low` | $O(n+m)$ |
| "vértice crítico", "sin el cual se desconecta" | **puntos de articulación** | $O(n+m)$ |
| "partir en dos grupos sin conflictos internos", "dos colores", "dos equipos" | **bipartito**: BFS por paridad de capas | $O(n+m)$ |
| "orientar las aristas manteniendo que se llegue a todos" ($G$ conexo) | $D(T)$ del árbol DFS; existe $\iff$ no hay puentes | $O(n+m)$ |
| "¿son adyacentes $u$ y $v$?" muchas veces, grafo denso | **matriz** de adyacencia | $\Theta(1)$ por consulta, $\Theta(n^2)$ espacio |
| recorrer vecinos, grafo ralo | **listas** de adyacencia | $\Theta(n+m)$ espacio |

### 3.2 Cuando el grafo NO está en el enunciado (lo más difícil, y lo que más cae)

Este es el ejercicio del **cubo de Rubik**, y es el arquetipo. El enunciado
habla de cubos, fichas, configuraciones, strings, números — y vos tenés que
inventar el grafo. La receta, en este orden, y **escribiendo cada paso**:

**1. ¿Qué es un nodo?** Casi nunca es un objeto del enunciado; casi siempre es
un **estado completo del sistema**. En el cubo, un nodo no es una cara ni una
celda: es *una configuración entera del cubo*. Definí con precisión qué
estructura de datos es un nodo.

**2. ¿Qué es una arista?** Una **transición elemental**, la unidad en la que se
mide lo que te piden. Si te piden "cantidad de jugadas", entonces una arista es
exactamente una jugada. Si una arista fuera dos jugadas, las distancias te darían
mal.

**3. ¿Es dirigido?** Preguntate si toda transición se puede deshacer. En el
cubo sí (rotar 90° horario se deshace con antihorario), entonces el grafo es no
dirigido. En dependencias de módulos, no: es dirigido.

**4. ¿Tiene pesos?** Si todas las transiciones cuestan lo mismo, **no pongas
pesos** — decí explícitamente "todas las aristas tienen peso 1, se puede ver
como un grafo no ponderado". Eso habilita BFS, que es la mitad de la respuesta.

**5. ¿Qué pregunta del grafo es la pregunta del enunciado?** "Mínima cantidad de
jugadas para pasar de $u$ a $v$" $=$ "$\delta(u,v)$ en el grafo" $=$ BFS desde
$u$. Escribí esa traducción como una línea aparte.

**6. ¿De qué tamaño es el grafo?** Este paso es el que casi todos saltean y el
que más puntos vale. La complejidad se pide **en términos de la entrada
original**, no de $n$ y $m$. No alcanza con "BFS cuesta $O(|V|+|E|)$": hay que
decir cuánto valen $|V|$ y $|E|$ para *este* grafo.

**7. ¿Hace falta construir el grafo?** Casi nunca. Un grafo implícito se recorre
generando vecinos **on the fly**: la función `vecinos(u)` aplica las jugadas
válidas y devuelve los estados resultantes. Decilo, y justificá por qué no se
construye con la cuenta del paso 6.

> **Modelo de respuesta (cubo de Rubik, caso $3\times3\times3$ del enunciado):**
> *Un nodo es un estado completo del cubo: un diccionario que a cada
> identificador de cara le asigna una matriz $3 \times 3$ de colores, donde
> `cara[i][j]` es el color de la celda $(i,j)$. Hay una arista $\{u,v\}$ si y
> sólo si existe una jugada válida que transforma $u$ en $v$. El grafo es no
> dirigido porque toda jugada de 90° horario se deshace con la antihoraria
> correspondiente, y todas las aristas tienen peso 1 porque cada una representa
> exactamente una jugada — por eso la distancia en el grafo es, por definición,
> la cantidad mínima de jugadas, que es lo que pide el ítem B. Cada nodo tiene
> grado $6 \times 2 = 12$ (seis caras, dos sentidos de cuarto de vuelta), así que
> $|E| = 12|V|/2 = 6|V|$. El grafo no se construye explícitamente: hay
> $|V| = \frac{8!\cdot 3^7 \cdot 12!\cdot 2^{10}}{2} \approx 4{,}3\times10^{19}$
> estados alcanzables, que no entran en memoria. Se genera con una función
> `vecinos(u)` que aplica las 12 jugadas.*

Si el enunciado pidiera el caso general $n \times n \times n$, el modelo se
mantiene pero **el grado no queda en 12**: hay giros de capas internas, así que el
factor de ramificación pasa a ser $\Theta(n)$ y $|E| = \Theta(n\,|V|)$. Esto es
exactamente lo que el corrector marcó en el parcial de 75/100 («si cubo Rubik es
$n\times n$, pero de forma general ya no dice nada del enunciado»): o resolvés el
caso del enunciado y lo decís, o generalizás **de verdad** y ajustás las cuentas.

Fijate que ahí están los siete pasos, cada uno en una oración, y cada afirmación
con su porqué. Eso es lo que separa un "Bien" de un "Regular".

### 3.3 El truco de duplicar nodos

Cuando el enunciado tiene un **estado extra** además de la posición (paridad,
combustible, "ya usé el pasaje gratis", color del último movimiento), el modelo
no es "grafo + una variable": es un **grafo más grande**. Los nodos pasan a ser
pares $(v, \text{estado})$.

Ejemplo típico: "mínimo de pasos de $s$ a $t$ usando una cantidad par de
aristas". Nodos: $(v, 0)$ y $(v, 1)$ según la paridad de pasos dados. Arista de
$(u, p)$ a $(v, 1-p)$ por cada $uv \in E$. BFS sobre ese grafo, respuesta en
$(t, 0)$. Tamaño: $2n$ nodos y $2m$ aristas, así que sigue siendo $O(n+m)$.

Este patrón resuelve una enorme cantidad de enunciados que parecen necesitar algo
más sofisticado.

### 3.4 Cómo elegir entre BFS y DFS

No es estético, es por lo que garantiza cada uno:

- **BFS** te da **distancias mínimas** (teorema: $d[v] = \delta(s,v)$) y **capas**.
  Si el enunciado tiene la palabra "mínimo" y no hay pesos, es BFS.
- **DFS** te da **estructura de anidamiento**: tiempos $d/f$, teorema de los
  paréntesis, clasificación de aristas, `low`. Si el enunciado habla de ciclos,
  ancestros, puentes, orden topológico o componentes, es DFS.
- Para **alcanzabilidad y componentes conexas** los dos sirven igual y cuestan
  lo mismo. Decí cuál usás y seguí.

Dato para el multiple choice: **el árbol BFS no es único** (depende del orden
de las listas de adyacencia), pero **las distancias sí lo son**. Lo mismo con
DFS: el bosque cambia con el orden, los hechos estructurales no.

---

## 4. Divide & Conquer: las señales y el truco central

### 4.1 Cuándo es D&C

| Señal en el enunciado | Qué hacer |
|---|---|
| "complejidad estrictamente menor que $O(n)$" | **búsqueda binaria**: tiene que haber monotonía escondida |
| "arreglo de tamaño potencia de 2" | partir por la mitad, sin preocuparte por pisos |
| "resolverlo en $O(n \log n)$" | partir a la mitad + combinar en $O(n)$ |
| "menor que $O(n^2)$" sobre una matriz $n \times n$ | partir en cuadrantes; cuidado, el tamaño es $n$, no $n^2$ |
| "mínimo $t$ tal que se cumple $P(t)$", con $P$ monótono | **búsqueda binaria sobre la respuesta** |
| una operación mágica $O(1)$ que resume un bloque | D&C que usa esa operación para descartar bloques |

### 4.2 El truco que resuelve el 80% de los ejercicios de la guía

**La recursión casi nunca puede devolver solamente la respuesta.** Si intentás
resolver el problema devolviendo solo lo que te piden, el `combine` no cierra.
La técnica es **fortalecer el valor de retorno**: devolver una tupla con lo que
te piden *más lo que necesitás de cada mitad para poder combinar*.

Es literalmente lo que hace `es_derecha_dominante` del parcial 2C2025:
`return es_dominante, suma_total` — devuelve el booleano que te piden **y** la
suma, porque sin la suma no podés comparar las mitades.

La lista de la Práctica 4 vista con ese lente:

| Ejercicio | Lo que te piden | Lo que hay que devolver además | Recurrencia |
|---|---|---|---|
| 4 (Izquierda dominante) | un booleano | la **suma** del segmento | $T(n) = 2T(n/2) + O(1)$, $\Theta(n)$ |
| 7 (Distancia máxima en árbol) | el camino más largo | la **altura** del subárbol | un recorrido, $\Theta(n)$ |
| 9 (Máxima subsecuencia), sin fortalecer | la suma máxima contigua | nada: la mejor suma que cruza el medio se barre en $O(n)$ | $T(n)=2T(n/2)+O(n)$, $\Theta(n\log n)$ |
| 9, fortalecido | ídem | máximo prefijo, máximo sufijo y **suma total** | $T(n)=2T(n/2)+O(1)$, $\Theta(n)$ |
| 11 (Contar inversiones) | la cantidad | el segmento **ordenado** | $T(n)=2T(n/2)+O(n)$, $\Theta(n \log n)$ |

La máxima subsecuencia va con las dos filas porque muestra el efecto en estado
puro: el enunciado **pide** $\Theta(n\log n)$, que es lo que sale sin fortalecer;
pero si la recursión devuelve máximo prefijo, máximo sufijo y suma total, el
`combine` pasa a ser $O(1)$
—`mejor = máx(mejorIzq, mejorDer, sufIzq + prefDer)`— y el algoritmo baja a
$\Theta(n)$. Por eso la guía aclara que «el algoritmo más rápido que conocemos
tiene complejidad $O(n)$».

Cuando te trabes en un D&C, la pregunta a hacerse no es "¿cómo divido?" sino:
**¿qué información necesitaría de cada mitad para responder en $O(1)$ o $O(n)$?**
Eso es el valor de retorno.

Y un detalle de redacción: al fortalecer el retorno cambiás el problema. Decilo.
"Generalizo el problema: la función devuelve el par (es dominante, suma), y el
problema original es la primera componente del llamado sobre el arreglo entero."

### 4.3 Búsqueda binaria donde no hay arreglo ordenado

La búsqueda binaria no necesita un arreglo. Necesita tres cosas:

1. un **dominio ordenado** de candidatos,
2. un **predicado** $P(t)$ que sepas evaluar,
3. un **único umbral** donde $P$ cambia de falso a verdadero.

Entonces encontrás el umbral en $O(\log |T|)$ veces el costo de evaluar $P$.

- **Índice espejo** (ej. 5): el arreglo es estrictamente creciente de enteros
  distintos, entonces $g(i) = a_i - i$ es **no decreciente**. "$a_i - i \geq 0$"
  es un predicado monótono. Buscás binariamente el cambio de signo: $O(\log n)$.
  *La monotonía hay que demostrarla, no afirmarla: si $a_{i+1} > a_i$ y son
  enteros, entonces $a_{i+1} \geq a_i + 1$, luego $g(i+1) \geq g(i)$.*
- **Encuentro mínimo** (ej. 15): acá se busca **sobre la respuesta**. El
  predicado es $P(t) := $ "todos los amigos pueden llegar a un punto común en
  tiempo $t$", que se evalúa en $O(n)$ intersectando los intervalos
  $[x_i - v_i t,\; x_i + v_i t]$. $P$ es monótono porque si alcanza $t$,
  alcanza cualquier $t' > t$ (los intervalos solo crecen). Costo:
  $O(n \log(\text{rango}))$.
- **Diferencia mínima** (ej. 13): $A$ crece y $B$ decrece, entonces
  $A[i] - B[i]$ es **estrictamente creciente**. El mínimo de $|A[i]-B[i]|$ está
  junto al cambio de signo. $O(\log n)$.

La pregunta que destraba estos ejercicios: *¿hay alguna función de la posición
que sea monótona aunque el enunciado no lo diga?*

### 4.4 Teorema Maestro: el checklist

Forma: $T(n) = a\,T(n/b) + f(n)$, con $q = \log_b a$.

| Caso | Condición | Resultado |
|---|---|---|
| 1 | $f(n) = O(n^{q-\varepsilon})$, algún $\varepsilon > 0$ | $\Theta(n^q)$ — mandan las hojas |
| 2 | $f(n) = \Theta(n^q \log^r n)$, $r \geq 0$ | $\Theta(n^q \log^{r+1} n)$ — se acumulan los niveles |
| 3 | $f(n) = \Omega(n^{q+\varepsilon})$ **y** $a f(n/b) \leq c f(n)$, $0<c<1$ | $\Theta(f(n))$ — manda la raíz |

Los cuatro errores que cuestan puntos, en orden de frecuencia:

1. **Usarlo cuando el tamaño se resta.** $T(n) = T(n-1) + n$ o
   $T(n) = 2T(n-1)$ **no** son de la forma del teorema. Esas se desenrollan:
   $T(n)=T(n-1)+n$ da $\Theta(n^2)$ (Gauss), $T(n)=2T(n-1)$ da $\Theta(2^n)$.
   La Práctica 4 ejercicio 3 mezcla las dos familias justamente para que te des
   cuenta: los ítems 1 a 5 y 9 se restan, los demás se dividen.
2. **Usar $\varepsilon$ negativo.** El caso 1 pide $\varepsilon > 0$. Esto es
   exactamente la pregunta 4 del parcial 1C2024: la "demostración" usa
   $\varepsilon = -6$, y por eso es incorrecta aunque el resultado pareciera
   salir.
3. **Caer en el hueco entre casos.** Si $f$ está entre $n^q$ y $n^{q+\varepsilon}$
   sin ser $\Theta(n^q \log^r n)$, el teorema no aplica. Hay que decir "no
   aplica" e ir por árbol de recursión o sustitución.
4. **Olvidar la condición de regularidad del caso 3.** No alcanza con que $f$
   crezca más rápido.

Un caso que confunde y conviene tener resuelto: $T(n) = 2T(n/2) + \log n$
(Práctica 4, ítem 10). Acá $q = 1$ y $f(n) = \log n = O(n^{1-\varepsilon})$ con,
por ejemplo, $\varepsilon = 1/2$. Es **caso 1**: $T(n) = \Theta(n)$. La
intuición: hay $n$ hojas y cada una cuesta $\Theta(1)$; el trabajo de combinar
es despreciable.

---

## 5. Backtracking: la receta de siete pasos

La teórica es explícita sobre qué te van a pedir, y en qué orden. Seguilo como
checklist — cada paso es un ítem que suma.

**1. Candidatas.** Elegir $\text{Sols}$ y escribir qué representa cada vector.
Esta es una **decisión de diseño tuya** y cambia la complejidad. Para $n$ reinas
hay tres universos posibles ($\binom{n^2}{n}$, $n^n$, $n!$) y los tres contienen
las mismas soluciones válidas.

**2. Válidas.** Escribir $\text{válida}(a)$ **como fórmula**. Si es
optimización, también $\text{valor}(a)$ y el orden.

**3. Parciales y sucesoras.** Qué es una decisión, cuáles son legales, y —lo
importante— cuál es el **resumen mínimo de las decisiones pasadas** que necesita
la recursión. Regla de Erickson: los parámetros son *lo que la hoja necesita
para decidir si es válida y cuánto vale, más lo necesario para saber qué
decisiones son legales*. En mochila alcanza con $(i, pa, va)$: **qué** objetos
elegiste es irrelevante.

**4. Función recursiva.** Caso base (la hoja) y caso recursivo. Y **escribí su
semántica en castellano**: no "$f(i, pa, va)$", sino "el máximo valor de una
extensión válida cuando las decisiones $1,\dots,i-1$ acumulan peso $pa$ y valor
$va$". Sin esa frase no se puede demostrar nada.

**5. Podas.** Factibilidad y optimalidad, **con demostración**.

**6. Complejidad.** Nodos del árbol $\times$ trabajo por nodo. Espacio:
profundidad $\times$ estado.

**7. Implementar** y testear contra la versión sin podas.

### 5.1 Las cinco preguntas, un solo algoritmo

Casi todo enunciado pregunta una de cinco cosas, y se responden con la misma
recursión cambiando tres casillas:

| Pregunta | Hoja válida / no válida | Combinar | Corte temprano | Podas |
|---|---|---|---|---|
| Decisión (¿existe?) | `True` / `False` | $\vee$ | sí, al primer `True` | factibilidad |
| Construcción (dame una) | guardar $p$ / nada | $\vee$ | sí | factibilidad |
| Conteo (¿cuántas?) | $1$ / $0$ | $+$ | **no** | factibilidad |
| Enumeración (listalas) | imprimir / nada | — | **no** | factibilidad |
| Optimización (la mejor) | $\text{valor}(p)$ / $-\infty$ | $\max$ | **no** | factibilidad **y** optimalidad |

Dos cosas de esta tabla caen seguro: que el **corte temprano al encontrar una
solución vale para decisión y construcción**, pero es **incorrecto para conteo,
enumeración y optimización** (cortar te haría perder soluciones que hay que
contar, listar o comparar); y que las **podas por optimalidad no aplican a conteo
ni enumeración**, porque no hay un "mejor" contra qué comparar.

### 5.2 El molde de la demostración de una poda

Toda poda por factibilidad se demuestra igual. Memorizá los cuatro pasos:

1. "Sea $p$ una solución parcial tal que $\neg R(p)$." — y escribí qué significa
   concretamente: una suma que se pasó, un par que se ataca, un color repetido.
2. "Sea $a \in \text{Ext}(p)$ cualquiera." — $a$ coincide con $p$ en las primeras
   $i-1$ coordenadas.
3. Mostrar que **la violación se hereda**: lo que estaba mal en $p$ sigue mal en
   $a$, y acá va la **propiedad de la entrada** que lo garantiza (los pesos son
   no negativos, la arista ya estaba, etc.).
4. Concluir $\neg\text{válida}(a)$. Como $a$ era cualquiera,
   $\text{Ext}(p) \cap \text{Sols}_{\text{válidas}} = \emptyset$. $\square$

Para optimalidad el molde es el mismo pero con una **cota**: demostrar que
$\text{valor}(a) \leq U(p)$ para toda extensión válida $a$. La forma más fácil
de conseguir una cota es **relajar**: resolver un problema más fácil cuyo óptimo
sea $\geq$ el del original (permitir fracciones en mochila, ignorar que las
tareas no se repiten en asignación).

Y la distinción que cae en multiple choice:

> **Correcta** es una propiedad matemática. **Útil** es una propiedad empírica.

Una poda que nunca corta es inútil pero no incorrecta. Una regla que "casi
siempre anda" no es una poda, es una apuesta.

Y las podas **no cambian el peor caso**. Para mochila con las dos podas, la
familia de instancias donde el árbol podado es el árbol entero necesita las dos
condiciones a la vez: $W \geq \sum w_j$, que anula la poda por factibilidad, **y**
un orden de exploración que haga subir `mejor` de a poco —por ejemplo
$v = (1,1,\dots,1)$ explorando primero $a_i = 0$—, que anula la de optimalidad.
Solo con $W \geq \sum w_j$ no alcanza: la poda por optimalidad puede seguir
cortando muchísimo.

### 5.3 Complejidad de backtracking

$$T = \sum_{\text{nodos visitados } p} (\text{trabajo en } p)$$

Cota cómoda: (nodos del árbol completo) $\times$ (máximo trabajo por nodo). Un
árbol de altura $n$ con $\leq k$ hijos por nodo tiene $O(k^n)$ nodos.

Las cuentas que hay que tener a mano:

| Universo | Nodos | Ejemplo |
|---|---|---|
| vectores binarios | $2^{n+1}-1 = O(2^n)$ | subconjuntos, mochila |
| vectores en $\{1..k\}^n$ | $O(k^n)$ | repartir $n$ objetos en $k$ cajas |
| permutaciones | $\sum_{i=0}^{n} \frac{n!}{(n-i)!} \leq e \cdot n! = O(n!)$ | asignación, $n$ reinas |

Y la aclaración que el corrector busca: **decir cuánto cuesta cada nodo y de qué
depende**. "Árbol binario de altura $n$, $O(2^n)$ nodos, $O(1)$ por nodo,
entonces $O(2^n)$" es suficiente. "Es exponencial" no lo es.

Ojo con el costo de copiar la parcial: si pasás $p$ por copia, cada nodo cuesta
$O(n)$ y el total se multiplica. Si la compartís y deshacés al volver (que *es*
el backtrack), es $O(1)$. **Hay que decidirlo y decirlo.**

---

## 6. Plantillas de pseudocódigo

Estas cinco resuelven casi todo. Vale escribirlas de memoria una vez por día
hasta que salgan solas.

### BFS — distancias mínimas sin pesos

```
BFS(G, s)
    para cada u ∈ V(G) \ {s}:
        color[u] ← blanco;  d[u] ← ∞;  π[u] ← NIL
    color[s] ← gris;  d[s] ← 0;  π[s] ← NIL
    Q ← cola vacía;  ENCOLAR(Q, s)
    mientras Q ≠ ∅:
        u ← DESENCOLAR(Q)
        para cada v ∈ Adj[u]:
            si color[v] = blanco:
                color[v] ← gris
                d[v] ← d[u] + 1;  π[v] ← u
                ENCOLAR(Q, v)
        color[u] ← negro
    devolver d, π
```
$O(n+m)$ con listas. Cada vértice se encola **una sola vez** — de ahí sale la
complejidad, y es la frase que hay que escribir.

### DFS con tiempos y `low` — puentes

```
DFS-VISIT(G, u)
    color[u] ← gris;  tiempo ← tiempo + 1;  d[u] ← tiempo
    low[u] ← d[u]
    para cada v ∈ Adj[u]:
        si color[v] = blanco:
            π[v] ← u
            DFS-VISIT(G, v)
            low[u] ← mín(low[u], low[v])
            si low[v] > d[u]:  marcar (u,v) como PUENTE
        sino si v ≠ π[u]:
            low[u] ← mín(low[u], d[v])
    color[u] ← negro;  tiempo ← tiempo + 1;  f[u] ← tiempo
```
Las dos actualizaciones de `low` son distintas: con el **hijo** se propaga
`low[v]` (después de la recursión), con la **arista de retroceso** se usa `d[v]`
(nunca `low[v]`).

### Orden topológico — versión lineal

```
ORDEN-TOPOLÓGICO(D)
    computar entrada[v] = d⁻(v) para todo v
    Q ← cola con todos los v tales que entrada[v] = 0
    L ← ⟨⟩
    mientras Q ≠ ∅:
        u ← DESENCOLAR(Q);  agregar u al final de L
        para todo v ∈ N⁺(u):
            entrada[v] ← entrada[v] − 1
            si entrada[v] = 0:  ENCOLAR(Q, v)
    si |L| < n:  devolver "D tiene un ciclo"
    devolver L
```
$O(n+m)$: cada vértice se encola una vez, cada arista se procesa una vez.
Detección de ciclos **gratis**.

### D&C con retorno fortalecido

```
RESOLVER(A, l, r)
    si r − l + 1 ≤ 1:
        devolver (respuesta_base, info_base)
    q ← ⌊(l+r)/2⌋
    (resp_izq, info_izq) ← RESOLVER(A, l, q)
    (resp_der, info_der) ← RESOLVER(A, q+1, r)
    resp ← COMBINAR(resp_izq, resp_der, info_izq, info_der)
    info ← ACTUALIZAR(info_izq, info_der)
    devolver (resp, info)
```
El costo de `COMBINAR` es el $f(n)$ del teorema maestro. Si es $O(1)$ te da
$\Theta(n)$; si es $O(n)$ te da $\Theta(n\log n)$.

### Backtracking con las dos podas

```
Globales: mejor ← −∞,  sol[1..n],  mejorSol,  S[i] = Σ_{j≥i} v_j  (precalculado en O(n))

BT(i, pa, va)
    si pa > W:            devolver          // poda por factibilidad
    si va + S[i] ≤ mejor: devolver          // poda por optimalidad
    si i = n+1:                             // hoja: acá va > mejor
        mejor ← va;  mejorSol ← copia de sol;  devolver
    sol[i] ← 1;  BT(i+1, pa + w_i, va + v_i)
    sol[i] ← 0;  BT(i+1, pa, va)
```
La poda va **antes** del caso base (así también corta hojas). Explorar primero
"lo pongo" hace que `mejor` suba rápido y la poda por optimalidad actúe antes.

`sol[1..i-1]` **es** la parcial $p$: se comparte y se deshace al volver, que es
literalmente el backtrack. Copiar `mejorSol` cuesta $O(n)$ pero sólo pasa cuando
mejora. Si sólo te piden el **valor** óptimo y no la solución, sacá `sol` y
`mejorSol`: la hoja queda en `mejor ← va`.

---

## 7. Checklist de entrega

Antes de dar por cerrado un ejercicio de diseño de algoritmos, verificá que
escribiste **las seis cosas**:

- [ ] **El modelo.** Qué es un nodo / qué es una candidata / cómo parto. Con la
      traducción explícita del enunciado.
- [ ] **El algoritmo.** Pseudocódigo o descripción precisa. Si usás uno conocido
      modificado, alcanza con detallar *las modificaciones* — pero detallalas.
- [ ] **Las estructuras de datos.** Listas o matriz de adyacencia, cola, arreglo
      de memoización, y **por qué** esa y no otra.
- [ ] **La correctitud.** Por qué el algoritmo responde lo que se pregunta. Si
      hay podas o cortes, la demostración de que no pierden soluciones.
- [ ] **La complejidad temporal**, con la cuenta: la recurrencia y su método, o
      "nodos × trabajo por nodo", o "cada arista se procesa una vez".
- [ ] **La complejidad espacial.** Se olvida siempre y se pide casi siempre.

Y si el enunciado pedía comparar con otras técnicas, o justificar por qué **no**
usaste alguna: eso es un séptimo ítem y vale puntos propios.

---

## Fuentes

- `context/teoria/intro-grafos/resumen.md` — caracterizaciones, invariantes, "dos de tres"
- `context/teoria/grafos-algoritmos-03/resumen.md` — BFS, DFS, orden topológico, `low`, puentes
- `context/teoria/divide-and-conquer/resumen.md` — teorema maestro, sustitución, búsqueda binaria generalizada
- `context/teoria/pdfs/fuerza-bruta-y-backtracking.pdf` — las cinco preguntas, el molde de las podas, la receta de siete pasos
- `context/practica/context/practica_2.md`, `practica_3.md`, `practica_4.md` — ejercicios citados
- Parciales 1C2024, 1C2025 (enunciado y corregido 75/100) y 2C2025 corregido — formato, puntajes y marcas del corrector
