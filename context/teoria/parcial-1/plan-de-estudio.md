# Plan de estudio — 1er parcial

> Arranca el **martes 15/09**. Asume parcial alrededor del **28/09**.
> Si tu fecha es otra, corré los días: el orden importa más que las fechas.

## La lógica del plan

Los cuatro temas no se estudian en paralelo, se estudian **en cascada**:

**Teoría de grafos** va primero porque es el vocabulario con el que están
escritos los enunciados de la unidad siguiente. Si no tenés fresco qué es un
corte, un subgrafo inducido o un vértice de articulación, los enunciados de
Algoritmos sobre Grafos te van a resultar opacos y vas a perder tiempo
traduciendo en vez de resolviendo.

**Algoritmos sobre grafos** es el tema más largo y el que más superficie tiene:
BFS, DFS, clasificación de aristas, orden topológico, `low` y puentes. Se lleva
cuatro días.

**Divide & Conquer** es más autocontenido y se puede atacar después sin depender
de lo anterior. Dos días.

**Backtracking** va al final porque es el más corto, el más reciente en la
cursada y el que mejor se fija practicando. Un día concentrado alcanza si venís
con la cabeza entrenada de los anteriores.

Los dos últimos días no son de tema nuevo: simulacro y corrección. Eso es
innegociable — es donde vas a descubrir qué creías saber.

---

## Día 1 — martes 15/09 · Grafos: definiciones e invariantes

**Teoría.** `intro-grafos/resumen.md`, secciones 1 a 3. Grafo como par $(V,E)$,
digrafo vs. grafo orientado, isomorfismo, grados, apretón de manos, palomar.

**Práctica 2.** Ejercicios 1 (isomorfismo), 3 (árboles), 4 (suma de grados),
6 (doble grado).

**Foco.** Los invariantes sirven para **descartar** isomorfismo, nunca para
confirmarlo. Y la asimetría del trabajo: para decir que **sí** son isomorfos hay
que exhibir la biyección; para decir que **no**, alcanza con un invariante que
difiera.

**Checkpoint.** ¿Podés escribir de memoria el lema del apretón de manos, sus dos
corolarios, y demostrar que todo grafo con $n \geq 2$ tiene dos vértices del
mismo grado?

---

## Día 2 — miércoles 16/09 · Grafos: conectividad y estructura

**Teoría.** `intro-grafos/resumen.md`, secciones 4 a 10. Caminos y ciclos,
$G-v$ vs. $G-e$, subgrafo inducido, componentes conexas, particiones y cortes,
puntos de articulación, puentes, biconexión, árboles, complemento, bipartitos.

**Práctica 2.** Ejercicios 11 (particiones conexas), 15 (unión vs. junta),
18 (bipartito o ciclo impar).

**Foco.** La lista de caracterizaciones "si y sólo si" de la sección 2 de
`de-enunciado-a-algoritmo.md`. Cada una existe para reemplazar una condición
cara por una barata; son la mitad de los ejercicios de la materia.

**Checkpoint.** ¿Podés enunciar sin mirar las cinco caracterizaciones (puente,
conexo, bipartito, orden topológico, orientación fuerte) y decir para qué sirve
cada una?

---

## Día 3 — jueves 17/09 · Técnicas de demostración sobre grafos

**Teoría.** `demostraciones/resumen.md`. Inducción simple y fuerte, elección del
caso base, contrarrecíproco, absurdo, palomar, el truco del primer elemento.

**Práctica 2.** Ejercicios 2 (el error de Fede — hacelo entero, los cuatro
ítems), 7 (muchas aristas implica conexo), 13, 14 (caminos cruzados).

**Foco.** El ejercicio 2 es el más importante de la guía y no lo parece. El
error de construir el caso $n+1$ en vez de tomar uno arbitrario, y el error de
aplicar la HI a algo que no cumple sus hipótesis, son los dos que más se cobran.

**Checkpoint.** Dado un enunciado del tipo "todo grafo con propiedad $X$ cumple
$Y$", ¿sabés decidir en menos de un minuto si va por inducción en $n$, inducción
en $m$, contrarrecíproco o absurdo?

---

## Día 4 — viernes 18/09 · Representación y BFS

**Teoría.** `grafos-algoritmos-03/resumen.md`, secciones 0 a 9. Listas vs.
matriz, los tres colores, el algoritmo línea por línea, el lema de la cola, el
teorema $d[v] = \delta(s,v)$, el árbol BFS.

**Práctica 3.** Ejercicios 1 (representación — hacé la tabla completa de las 8
operaciones × 4 estructuras), 15 (componentes conexas), 16 (árboles geodésicos).

**Foco.** El ejercicio 1 parece de trámite y es el que más multiple choice
alimenta. Y que **las distancias son únicas pero el árbol BFS no**: depende del
orden de las listas de adyacencia.

**Checkpoint.** ¿Podés escribir el pseudocódigo de BFS de memoria y explicar en
una frase por qué cuesta $O(n+m)$?

---

## Día 5 — sábado 19/09 · DFS y orden topológico

**Teoría.** `grafos-algoritmos-03/resumen.md`, la sección de orden topológico y
la de clasificación de aristas. Tiempos $d/f$, teorema de los paréntesis, teorema
del camino blanco, los cuatro tipos de arista y por qué en no dirigidos solo hay
dos.

**Práctica 3.** Ejercicios 3 (orden topológico, los cuatro ítems), 10 (grafos
bipartitos), 12b (toda arista no-árbol une ancestro con descendiente).

**Foco.** El ejercicio 3b pide el algoritmo **sin usar DFS** y el 3d pide
mejorarlo a lineal — esa es exactamente la diferencia entre la versión ingenua
$O(n(n+m))$ y la versión con cola. Tené las dos.

**Checkpoint.** Dado un DAG dibujado, ¿podés dar un orden topológico válido y
justificarlo en una línea? (Cae literal: pregunta 12 del parcial 1C2025.)

---

## Día 6 — domingo 20/09 · Descanso

Repaso liviano de las plantillas de pseudocódigo, nada más. Escribilas a mano
una vez: BFS, DFS con `low`, orden topológico. Quince minutos.

---

## Día 7 — lunes 21/09 · Puentes, `low` y modelado de grafos implícitos

**Teoría.** `grafos-algoritmos-03/resumen.md`, la sección de puentes. La
definición de `low`, las dos actualizaciones (y por qué son distintas), el
criterio $\texttt{low}[v] > d[u]$.

**Práctica 3.** Ejercicios 11 (puentes vs. puntos de corte — los cuatro ítems
V/F), 12 (puentes, completo), 13 (orientaciones fuertes), 14 (orientación de
calles).

**Y además:** la sección 3.2 de `de-enunciado-a-algoritmo.md`, los siete pasos
del modelado. Rehacé el ejercicio del cubo de Rubik (pregunta 14 del 1C2025)
escribiendo los siete pasos, y compará con el modelo de respuesta.

**Foco.** Ese ejercicio del cubo es el arquetipo de "modelar el problema", que
es tu punto flojo. El error del corregido fue no aclarar la generalización a
$n \times n$.

**Checkpoint.** ¿Podés modelar desde cero un problema de estados y transiciones
—fichas, configuraciones, strings— nombrando nodo, arista, dirigido/no, peso,
pregunta traducida, tamaño del grafo y si se construye o no?

---

## Día 8 — martes 22/09 · D&C: recurrencias y Teorema Maestro

**Teoría.** `divide-and-conquer/resumen.md`, todo. Merge sort, árbol de
recursión, los tres casos, método de sustitución, búsqueda binaria.

**Práctica 4.** Ejercicios 1, 2 (identificar divide/conquer/combine en código
dado) y **3 completo, los doce ítems**.

**Foco.** El ejercicio 3 mezcla a propósito recurrencias que se **dividen** (sí
aplica el teorema) con las que se **restan** (no aplica). Clasificá los doce
antes de resolver ninguno.

**Checkpoint.** ¿Sabés decir por qué $T(n) = 2T(n/2) + \log n$ da $\Theta(n)$ y
no $\Theta(n \log n)$?

---

## Día 9 — miércoles 23/09 · D&C: diseño

**Práctica 4.** Ejercicios 4 (izquierda dominante), 5 (índice espejo),
7 (distancia máxima en árbol), 11 (contar inversiones), 13 (diferencia mínima),
15 (encuentro mínimo).

**Foco.** La sección 4.2 de `de-enunciado-a-algoritmo.md`: **fortalecer el valor
de retorno**. Antes de escribir cada uno, contestá por escrito "¿qué necesito de
cada mitad para poder combinar?". Ese es el ejercicio real.

Y el 15 es el otro patrón: búsqueda binaria **sobre la respuesta**, no sobre el
arreglo.

**Checkpoint.** ¿Podés resolver el `es_derecha_dominante` del parcial 2C2025
(ejercicio 5) identificando $a$, $b$, $f(n)$, el caso del teorema y la
complejidad final?

---

## Día 10 — jueves 24/09 · Backtracking

**Teoría.** `backtracking/resumen.md` completo. Los tres conjuntos, el árbol de
backtracking, las cinco preguntas, las dos familias de podas, complejidad.

**Práctica.** No hay guía publicada todavía. Usá:
- Los ejercicios del archivo `ejercicios-resueltos.md`.
- Pregunta 15 del parcial 1C2025 (las dos demostraciones de Sudoku).
- Ejercicio 6 del parcial 2C2025 (partición de hojas entre dos ayudantes + árbol
  de recursión).
- Y rehacé mochila con las dos podas, escribiendo las dos demostraciones.

**Foco.** El molde de cuatro pasos para demostrar una poda. Escribilo tres veces
sobre tres podas distintas hasta que salga solo.

**Checkpoint.** ¿Podés hacer la tabla de las cinco preguntas de memoria, y
explicar por qué el corte temprano solo vale para decisión?

---

## Día 11 — viernes 25/09 · Simulacro

Cuatro horas cronometradas, libro cerrado, sin interrupciones. Formato mixto:
multiple choice con puntaje negativo, respuestas cortas todo-o-nada, y ejercicios
a desarrollar.

Lo importante no es la nota: es medir **cuánto tardás en cada tipo de ejercicio**.
Los parciales son de 4 a 5 horas y el tiempo alcanza holgado *si* no te quedás
trabado. Anotá dónde te trabaste.

---

## Día 12 — sábado 26/09 · Corrección y cierre

Corregí el simulacro con el mismo criterio del corrector: no "¿está bien la
idea?" sino "¿escribí la justificación?". Usá el checklist de seis puntos de
`de-enunciado-a-algoritmo.md`, sección 7.

Después, cerrá solo los huecos que aparecieron. No repases lo que ya sabés.

**Domingo 27:** descanso. En serio.

---

## Cómo estudiar cada día

Tres bloques de 50 minutos con 10 de pausa alcanzan. La distribución que rinde:

**Bloque 1 — teoría activa.** Leer el resumen **con un papel al lado**,
reescribiendo las definiciones y los enunciados de teoremas con tus palabras. Si
no podés reescribir un teorema sin mirar, todavía no lo leíste.

**Bloque 2 — práctica.** Los ejercicios del día. Regla dura: **no mirar la
solución antes de veinte minutos de pelearla**. El momento incómodo en que no
sabés cómo empezar es exactamente el que estás entrenando, y es el que vas a
tener en el parcial.

**Bloque 3 — escritura.** Tomá **uno** de los ejercicios que resolviste y
escribilo completo, como si lo entregaras: modelo, algoritmo, estructuras,
correctitud, complejidad temporal y espacial. Uno por día, prolijo. Esto es lo
que directamente te da los puntos que el corregido de 75/100 perdió.

Y una advertencia sobre tus dos puntos flojos declarados. **Modelar** y
**escribir el algoritmo** no se arreglan leyendo más teoría: se arreglan haciendo
el paso 1 por escrito antes de pensar en código. Cada vez que agarres un
enunciado de diseño, lo primero que escribís en la hoja es qué es un nodo (o qué
es una candidata, o cómo parto el arreglo). Si esa línea no sale, no sigas al
pseudocódigo — el problema está ahí.
