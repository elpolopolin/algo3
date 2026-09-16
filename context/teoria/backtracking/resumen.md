# Resumen — Fuerza bruta y backtracking

> Fuente: `context/teoria/pdfs/fuerza-bruta-y-backtracking.pdf` (55 diapositivas).
> Referencia principal de la cátedra: J. Erickson, *Algorithms*, cap. 2.

Tres cosas para llevarse:

- **Antes de programar nada hay que decidir qué es una solución candidata.** Es
  una decisión de diseño tuya, y cambia la complejidad. Para $n$ reinas los tres
  universos posibles tienen $\binom{n^2}{n}$, $n^n$ y $n!$ elementos, y los tres
  contienen exactamente las mismas soluciones.
- **Una sola recursión responde cinco preguntas distintas** (¿existe?, dame una,
  ¿cuántas?, listalas, la mejor). Por eso se formaliza primero y una sola vez: el
  algoritmo sale casi de arriba.
- **Una poda es una afirmación matemática sobre todas las extensiones.** Si no la
  podés demostrar, no es una poda: es una apuesta.

---

## 0. Vocabulario mínimo

- **Fuerza bruta**: probar todas las posibilidades, una por una, sin ser
  inteligente.
- **Backtracking** (vuelta atrás): fuerza bruta organizada como un recorrido en
  profundidad de un árbol, donde se puede **cortar** ramas enteras que no sirven.
- **Solución candidata**: uno de los objetos del universo que vamos a considerar
  (un vector, un subconjunto, una permutación).
- **Solución válida**: una candidata que además cumple lo que pide el enunciado.
- **Solución parcial**: las primeras decisiones ya tomadas, con el resto sin
  decidir.
- **Poda** (*pruning*): no explorar un subárbol porque demostramos que ahí no hay
  nada que nos sirva.
- **DFS** (*Depth-First Search*, búsqueda en profundidad): el recorrido que hace
  backtracking sobre su árbol — baja hasta el fondo, y cuando no puede más,
  vuelve atrás un nivel y prueba otra rama.
- **Rama y cota** (*branch and bound*): fuerza bruta + cotas + buen orden de
  exploración.

---

## 1. Por qué probar todo

Para muchísimos problemas no se conoce nada sustancialmente mejor que probar
todas las posibilidades: viajante de comercio, coloreo de grafos,
satisfacibilidad, empaquetado.

Y aun cuando hay algo mejor, **el algoritmo mejor casi siempre nace de la fuerza
bruta**: la misma recurrencia con memoria (programación dinámica), o la misma
recurrencia con una decisión que se puede tomar sin mirar el resto (greedy).

Además, la fuerza bruta es el **oráculo** contra el que se testean las versiones
inteligentes. Es el mejor test disponible en toda la materia.

> **Lema de diseño (Erickson).** Probar todas las posibilidades para la próxima
> decisión que sean consistentes con las decisiones anteriores, y dejar que la
> recursión se ocupe del resto. Sin ser inteligentes. Sin saltear opciones
> «obviamente» malas. Probar todo. Después lo hacemos más rápido.

### Combinatoria que hay que saber sin pensar

| Pregunta | Respuesta |
|---|---|
| ¿Cuántas hojas tiene un árbol binario completo de $n$ niveles? | $2^n$ |
| ¿Cuántos subconjuntos tiene un conjunto de $n$ elementos? | $2^n$ (cada elemento está o no está) |
| ¿Cuántas permutaciones tiene un conjunto de $n$ elementos? | $n!$ |
| ¿De cuántas formas reparto $n$ libros en $k$ cajas distintas, **posiblemente vacías**? | $k^n$ (cada libro elige su caja) |
| ¿Cuántos subconjuntos de tamaño $k$ hay en uno de $n$? | $\binom{n}{k}$ |

Para $n = 20$: $n^2 = 400$, $2^n \approx 10^6$, $\binom{n}{n/2} \approx 1{,}8\times10^5$,
$n! \approx 2{,}4 \times 10^{18}$.

> `pdfs/fuerza-bruta-y-backtracking.pdf`, diapositivas 5-7 — ¿por qué probar todo? y quiz combinatorio

---

## 2. Del enunciado a los conjuntos

Antes de escribir un algoritmo, el enunciado se traduce a **tres cosas**:

1. Un conjunto **$\text{Sols}$** de **soluciones candidatas**: el universo de
   objetos que vamos a considerar. Tiene que ser finito y con una descripción
   concreta (vectores, subconjuntos, permutaciones).
2. Un predicado **$\text{válida}(a)$** que dice si la candidata $a$ es realmente
   una solución del problema.
3. El conjunto de **soluciones válidas**:
   $\text{Sols}_{\text{válidas}} := \{a \in \text{Sols} : \text{válida}(a)\}$.

> **Lo importante.** El enunciado habla de reinas, mochilas o ciudades. Nuestros
> algoritmos van a hablar de **vectores**. Esta traducción es nuestra decisión, y
> hay que escribirla explícitamente.

### El ejemplo que muestra que la elección importa: $n$ reinas

Ubicar $n$ reinas en un tablero $n \times n$ sin que ninguna ataque a otra (ni
misma fila, ni columna, ni diagonal).

| $\text{Sols}$ | $\text{válida}(a)$ | $|\text{Sols}|$ |
|---|---|---|
| subconjuntos de $n$ casillas del tablero | no hay dos en la misma fila, columna ni diagonal | $\binom{n^2}{n}$ |
| vectores $a \in \{1,\dots,n\}^n$: la reina de la fila $i$ está en la columna $a_i$ | $a_i \neq a_j$ y $\|a_i - a_j\| \neq \|i-j\|$ para todo $i<j$ | $n^n$ |
| permutaciones $a$ de $\{1,\dots,n\}$ | $\|a_i - a_j\| \neq \|i-j\|$ para todo $i<j$ | $n!$ |

Los tres $\text{Sols}_{\text{válidas}}$ representan **el mismo conjunto de
tableros**. Para $n = 8$: $4{,}4\times10^9$ contra $1{,}7\times10^7$ contra
$40\,320$.

¿Por qué podemos restringirnos a permutaciones? Porque toda solución válida
tiene exactamente una reina por fila y por columna — **y eso hay que
argumentarlo**, no darlo por obvio.

> **El balance.** Cuanto más «sabemos» de las soluciones válidas, más chico el
> universo... y más complicada la enumeración. En el universo de permutaciones
> hay que recordar qué columnas ya se usaron; en $\{1,\dots,n\}^n$ alcanza con un
> `for` por coordenada.

### Las cinco preguntas

Una vez definido $\text{Sols}_{\text{válidas}}$, casi todo enunciado pregunta una
de estas cinco cosas:

- **Decisión**: ¿existe alguna? — devuelve un booleano.
- **Construcción**: dame una. Algún $a \in \text{Sols}_{\text{válidas}}$, o «no hay».
- **Conteo**: ¿cuántas hay? $|\text{Sols}_{\text{válidas}}|$.
- **Enumeración**: listalas todas.
- **Optimización**: dame la mejor. Hace falta un orden, casi siempre dado por una
  **función de valuación** $\text{valor}: \text{Sols} \to \mathbb{R}$, con
  $a \preceq b \iff \text{valor}(a) \leq \text{valor}(b)$.

> `pdfs/fuerza-bruta-y-backtracking.pdf`, diapositivas 9-12 — del enunciado a los conjuntos, tres traducciones de $n$ reinas, cinco preguntas

---

## 3. El hilo conductor: mochila 0/1

Hay $n$ objetos; el objeto $i$ pesa $w_i \in \mathbb{N}$ y vale $v_i \in \mathbb{N}$.
La mochila soporta peso total $W$. Queremos el subconjunto de valor total máximo
cuyo peso no supere $W$.

- $\text{Sols} := \{0,1\}^n$. El vector $a$ representa el subconjunto
  $\{i : a_i = 1\}$.
- $\text{peso}(a) := \sum_{i=1}^{n} a_i w_i$ y $\text{valor}(a) := \sum_{i=1}^{n} a_i v_i$.
- $\text{válida}(a) := [\text{peso}(a) \leq W]$.
- Piden $\max\{\text{valor}(a) : a \in \text{Sols}_{\text{válidas}}\}$.

Un detalle que conviene mirar siempre en problemas de optimización:
$\text{Sols}_{\text{válidas}} \neq \emptyset$ **siempre**, porque $(0,\dots,0)$ es
válida. Cuando el conjunto sobre el que tomás máximo puede ser vacío, hay que
decidir qué devolver.

**La instancia del apunte**, que vale tener en la cabeza: $n=3$, $w = (2,3,4)$,
$v = (3,4,5)$, $W = 5$. Hay $|\text{Sols}| = 8$ candidatas, $5$ válidas, y el
óptimo es $a^* = (1,1,0)$ con $\text{valor} = 7$.

> `pdfs/fuerza-bruta-y-backtracking.pdf`, diapositivas 13-14 — mochila 0/1 y la instancia del ejemplo

---

## 4. Fuerza bruta y el paso a la recursión

El algoritmo genérico de fuerza bruta para optimización:

```
FUERZA-BRUTA()
    mejor ← −∞
    para cada a ∈ Sols:
        si válida(a):
            mejor ← máx(mejor, valor(a))
    devolver mejor
```

Para decisión se devuelve `True` apenas una candidata es válida; para conteo se
suma; para enumeración se imprime.

Costo: $|\text{Sols}| \cdot (\text{costo de válida} + \text{costo de valor})$,
más el costo de **generar** cada elemento. Y ahí está el asunto: ¿cómo se hace
ese `para cada` sobre $\{0,1\}^n$?

### Generar el universo: una decisión por vez

```
GENERAR(i, p)
    // p = (a_1, ..., a_{i−1}) ya decidido
    si i = n+1:  PROCESAR(p);  devolver
    GENERAR(i+1, p ⊕ 0)
    GENERAR(i+1, p ⊕ 1)
```

Se invoca `GENERAR(1, ())`. El símbolo $\oplus$ es concatenar. Cada llamada
decide **una** coordenada; las anteriores ya están fijas en $p$, las siguientes
las decide la recursión. Hay exactamente $2^n$ llamadas con $i = n+1$, una por
vector.

Contar en binario de $0$ a $2^n - 1$ también serviría, pero **solo para vectores
binarios**. La recursión sirve para cualquier universo definido por decisiones.

### Mochila, versión 1: la fuerza bruta recursiva

```
mochila₁(i, p)
    si i = n+1:
        si peso(p) ≤ W:  devolver valor(p)
        si no:           devolver −∞
    devolver máx( mochila₁(i+1, p ⊕ 0), mochila₁(i+1, p ⊕ 1) )
```

El $-\infty$ es el **neutro del máximo**: «esta hoja no aporta». Si todas las
hojas devuelven $-\infty$, no hay solución válida.

Costo: $2^n$ hojas, cada una calcula $\text{peso}(p)$ y $\text{valor}(p)$ en
$O(n)$, más el costo de copiar $p$ en cada nodo. Total $O(n \cdot 2^n)$.

### Mochila, versión 2: el resumen de las decisiones pasadas

En la hoja solo usamos $\text{peso}(p)$ y $\text{valor}(p)$: alcanza con **dos
números acumulados** en lugar del vector entero.

```
mochila₂(i, pa, va)
    si i = n+1:  devolver (pa ≤ W) ? va : −∞
    devolver máx( mochila₂(i+1, pa, va), mochila₂(i+1, pa + w_i, va + v_i) )
```

Se invoca `mochila₂(1, 0, 0)`. Trabajo $O(1)$ por llamada, $2^{n+1}-1$ llamadas:
**$O(2^n)$**.

Notar que para lograr esto **hubo que generalizar el problema**:
$\text{mochila}_2(i, pa, va)$ resuelve «la mejor forma de completar decisiones ya
tomadas», y el problema original es el caso particular $(1,0,0)$.

> **La regla de Erickson.** Cada llamada toma exactamente una decisión,
> consistente con las anteriores. Para eso necesita: (1) la porción de la entrada
> que falta procesar (un índice $i$), y (2) un **resumen de las decisiones ya
> tomadas, lo más chico posible**.
>
> Los parámetros son **lo que la hoja necesita para decidir si es válida y cuánto
> vale, más lo necesario para saber qué decisiones son legales**.

| Problema | Resumen necesario |
|---|---|
| Mochila | $i$, peso acumulado, valor acumulado. *Qué* objetos elegiste es irrelevante. |
| Asignación | $i$ (la próxima persona), el conjunto de tareas ya usadas, el costo acumulado. |
| $n$ reinas | $i$ (la próxima fila) y **todas** las posiciones anteriores. Acá el resumen es la parcial entera. |

> `pdfs/fuerza-bruta-y-backtracking.pdf`, diapositivas 16-20 — fuerza bruta genérica, generar, las dos versiones de mochila, el resumen de decisiones

---

## 5. Soluciones parciales y el árbol de backtracking

**Definición** (para $\text{Sols} = \{0,1\}^n$). Una **solución parcial** es un
vector $p = (a_1,\dots,a_{i-1})$ con $1 \leq i \leq n+1$: las primeras $i-1$
decisiones ya tomadas.

Si $i \leq n$, las **sucesoras** de $p$ son $p \oplus 0$ y $p \oplus 1$.

Las **extensiones** de $p$ son las candidatas que empiezan con $p$:
$$\text{Ext}(p) := \{a \in \text{Sols} : a_j = p_j \text{ para } j < i\}.$$

- Las parciales de longitud $n$ son las candidatas: $\text{Ext}(a) = \{a\}$.
- La parcial vacía: $\text{Ext}(()) = \text{Sols}$.
- Toda candidata $a$ está en $\text{Ext}(p)$ para **exactamente una** parcial de
  cada longitud: sus prefijos.
- **Cada parcial es un subproblema.**

**Definición.** El **árbol de backtracking** es el árbol con raíz cuyos nodos son
las soluciones parciales, la raíz es $()$, y los hijos de $p$ son sus sucesoras.
Sus hojas son las candidatas.

> **Tres objetos, una sola cosa:**
> conjunto de soluciones parciales $\longleftrightarrow$ árbol de backtracking
> $\longleftrightarrow$ árbol de llamadas recursivas.

Cada nodo del árbol **es** una llamada a $\text{mochila}_2(i, pa, va)$; los
parámetros son el resumen de la parcial, y cada arista es una llamada recursiva.
El algoritmo lo recorre **en profundidad**: baja por $a_1 = 0$ hasta una hoja,
vuelve atrás un nivel (*backtracks*), prueba la otra rama, y así. Cada nodo
devuelve hacia arriba el mejor valor de su subárbol.

Cuando dibujes el árbol de llamadas de una entrada concreta —y eso **cae**—
tenés que poder señalar en cada nodo qué parcial es, y en cada hoja qué candidata
es y si es válida.

### Prefijos o sufijos: da lo mismo, pero elegí uno

La teórica usa **prefijos** $(a_1,\dots,a_{i-1})$ y decide $a_i$: la recursión
avanza con $i+1$ y el caso base es $i = n+1$.

La práctica usa **sufijos** $(a_i,\dots,a_n)$ y decide $a_{i-1}$: la recursión
avanza con $i-1$ y el caso base es $i = 0$. Es el mismo árbol, espejado, y es más
cómodo para hacer inducción en $i$.

> **Lo que sí importa:** escribir explícitamente qué representa la parcial y qué
> representan los parámetros. «$f(i, pa, va)$» no dice nada; «el máximo valor de
> una extensión válida cuando las decisiones $1,\dots,i-1$ acumulan peso $pa$ y
> valor $va$» sí.

> `pdfs/fuerza-bruta-y-backtracking.pdf`, diapositivas 21-25 — parciales, sucesoras, extensiones, árbol de backtracking, prefijos vs. sufijos

---

## 6. Podas por factibilidad

**Definición.** Una **regla de factibilidad** es un predicado $R$ sobre
soluciones parciales tal que, para toda parcial $p$:
$$\neg R(p) \implies \text{Ext}(p) \cap \text{Sols}_{\text{válidas}} = \emptyset.$$

Podar por factibilidad es **no explorar el subárbol de $p$ cuando $\neg R(p)$**.
Dicho al revés: $R(p)$ es una **condición necesaria** para que $p$ tenga alguna
extensión válida.

### Qué hay que demostrar, y qué no

- **Hay que demostrar:** si $p$ no cumple $R$, entonces toda candidata
  $a \in \text{Ext}(p)$ no es válida. Ni más ni menos.
- **No hace falta** que $R(p)$ garantice que *hay* una extensión válida. Una
  regla puede dejar pasar callejones sin salida; lo que no puede es **cerrar un
  pasillo con salida**.
- **Tampoco hace falta** que la poda ayude.

> **Correcta** es una propiedad matemática. **Útil** es una propiedad empírica.

### La poda de mochila

$R(p) := [pa \leq W]$, donde $pa$ es el peso acumulado por las decisiones de $p$.

*Demostración.* Si $pa > W$, sea $a \in \text{Ext}(p)$ cualquiera. Entonces
$\text{peso}(a) = pa + \sum_{j \geq i} a_j w_j \geq pa > W$, porque los $w_j$ son
naturales y los $a_j \in \{0,1\}$. Luego $\neg\text{válida}(a)$. $\square$

Fijate que se usa **una propiedad de la entrada**: los pesos no son negativos.
**Si hubiera pesos negativos, la poda sería incorrecta.**

```
mochila₃(i, pa, va)
    si pa > W:   devolver −∞            // poda por factibilidad
    si i = n+1:  devolver va
    devolver máx( mochila₃(i+1, pa, va), mochila₃(i+1, pa + w_i, va + v_i) )
```

La poda va **antes** del caso base, así también corta hojas; y en la hoja ya no
hace falta chequear $pa \leq W$, porque si llegamos es que la poda no cortó.

### La poda depende de la instancia

Con la instancia $w=(2,3,4)$, $v=(3,4,5)$: si $W = 4$, la poda corta en $(1,1)$ y
ahorra dos nodos. Si $W = 5$, no corta nada por encima de las hojas. Si
$W \geq 9$, no corta nunca.

> **Moraleja.** La poda **no cambia el peor caso**. Hay instancias (por ejemplo,
> $W \geq \sum w_j$) en que el árbol podado es el árbol entero.

### Restringir el universo y podar son la misma idea

Con $\text{Sols} = \{1,\dots,n\}^n$ para $n$ reinas:
- $R_1(p) :=$ las reinas de $p$ están en columnas distintas.
- $R_2(p) :=$ ninguna pareja de reinas de $p$ se ataca (columnas **y** diagonales).

*Demostración de $R_2$.* Sea $p = (a_1,\dots,a_{i-1})$ con $\neg R_2(p)$: existen
$j < k < i$ con $a_j = a_k$ o $|a_j - a_k| = |j-k|$. Sea $a \in \text{Ext}(p)$
cualquiera. Como $a$ extiende a $p$, los valores $a_j$ y $a_k$ son los mismos,
luego ese par se ataca en $a$, luego $\neg\text{válida}(a)$. $\square$

Y acá está la observación importante: **elegir $\text{Sols} = $ permutaciones es
lo mismo que tomar $\text{Sols} = \{1,\dots,n\}^n$ y podar con $R_1$.** En un caso
la restricción va en la definición de las sucesoras, en el otro en un `if`.

En 4 reinas, con la poda se visitan **33 nodos** (16 de ellos rojos) contra los
**341** del árbol completo de $\{1,\dots,4\}^4$.

### El molde de la demostración

Casi todas las podas por factibilidad se demuestran igual:

1. «Sea $p$ una solución parcial tal que $\neg R(p)$.» Escribir qué significa
   concretamente: una suma que se pasó, un par que se ataca, un color repetido.
2. «Sea $a \in \text{Ext}(p)$ cualquiera.» Escribir qué sabemos de $a$: coincide
   con $p$ en las primeras $i-1$ coordenadas.
3. Mostrar que **la violación se hereda**: lo que estaba mal en $p$ sigue mal en
   $a$, porque $a$ contiene a $p$ y lo que agrega no lo arregla. Acá va la
   propiedad de monotonía (pesos $\geq 0$, la arista que ya estaba, etc.).
4. Concluir $\neg\text{válida}(a)$. Como $a$ era cualquiera,
   $\text{Ext}(p) \cap \text{Sols}_{\text{válidas}} = \emptyset$. $\square$

> **Cuidado.** «Es obvio que si ya me pasé de peso, no puedo volver» **no es una
> demostración**. La frase que la reemplaza es: «como $w_j \geq 0$ para todo $j$,
> $\text{peso}(a) \geq pa > W$».

### Lo que NO es una poda

- «Si el objeto $i$ pesa más que el promedio, no lo pongo.» → puede perder el
  óptimo. Es una **heurística**, no una poda.
- «En $n$ reinas, la primera reina nunca va en la columna 1.» → falso: para
  $n=5$, $(1,3,5,2,4)$ es solución.
- «Si ya encontré una solución válida, corto.» → correcto para **decisión** (y
  para **construcción**, donde alcanza con una); **incorrecto** para
  optimización, conteo y enumeración.

> `pdfs/fuerza-bruta-y-backtracking.pdf`, diapositivas 28-35 — definición de regla de factibilidad, qué demostrar, mochila, dependencia de la instancia, $n$ reinas, el molde, lo que no es poda

---

## 7. Podas por optimalidad

En optimización hay una **segunda** razón para no bajar por un subárbol: aunque
tenga extensiones válidas, ninguna es mejor que la mejor que ya encontramos.

**Ingredientes:**
- Una variable $\text{mejor}$ con el valor de la mejor solución válida encontrada
  hasta el momento ($-\infty$ al principio).
- Una **cota superior** $U(p)$ tal que, para toda extensión **válida** $a$ de $p$:
  $\text{valor}(a) \leq U(p)$.

**Regla:** si $U(p) \leq \text{mejor}$, no explorar el subárbol de $p$.

*Por qué es correcto:* toda extensión válida de $p$ vale a lo sumo
$U(p) \leq \text{mejor}$, y $\text{mejor}$ es el valor de una solución válida ya
encontrada. Cortar no cambia el máximo.

Para minimizar es simétrico: una **cota inferior** $L(p)$, y se corta si
$L(p) \geq \text{mejor}$.

### La cota de mochila

$$U(p) := va + \sum_{j \geq i} v_j$$

el valor acumulado más el de **todos** los objetos que faltan decidir.

*Es cota superior:* si $a \in \text{Ext}(p)$, entonces
$\text{valor}(a) = va + \sum_{j\geq i} a_j v_j \leq va + \sum_{j \geq i} v_j$
porque $a_j \leq 1$ y $v_j \geq 0$. (Ni siquiera usamos que $a$ es válida.)

Es una cota **floja**: ignora la capacidad. Una mejor es $va$ más el óptimo de la
mochila **fraccionaria** con lo que queda. Cota más ajustada = más poda, pero más
cuesta cada nodo. Otra vez, un balance.

*Truco de implementación:* precalcular $S_i := \sum_{j \geq i} v_j$ para todo $i$
en $O(n)$; entonces $U(p) = va + S_i$ cuesta $O(1)$.

### Relajar para acotar

Toda **relajación** da una cota. La cota fraccionaria de mochila es una
relajación (permitimos $a_j \in [0,1]$). En asignación, la cota
$L_2(p) := ca + \sum_{k \geq i} \min_j c_{kj}$ relaja el hecho de que las tareas
no se pueden repetir: resuelve un problema más fácil cuyo óptimo es
$\leq$ el del original.

*Demostración de $L_2$:* sea $\pi \in \text{Ext}(p)$. Entonces
$\text{costo}(\pi) = ca + \sum_{k\geq i} c_{k\pi(k)}$, y para cada $k \geq i$ vale
$c_{k\pi(k)} \geq \min_j c_{kj}$ por definición de mínimo. Sumando,
$\text{costo}(\pi) \geq L_2(p)$. $\square$

### El algoritmo con las dos podas

```
Globales: mejor ← −∞,  S_i = Σ_{j≥i} v_j  precalculado

mochila₄(i, pa, va)
    si pa > W:             devolver        // factibilidad
    si va + S_i ≤ mejor:   devolver        // optimalidad
    si i = n+1:  mejor ← va;  devolver     // hoja: acá va > mejor
    mochila₄(i+1, pa + w_i, va + v_i)      // primero «lo pongo»
    mochila₄(i+1, pa, va)
```

Ya **no devuelve un valor**: actualiza $\text{mejor}$. Es lo natural cuando la
poda depende de una variable global que cambia. Al terminar
`mochila₄(1,0,0)`, $\text{mejor}$ es el óptimo.

### El orden de exploración importa

Una poda por optimalidad compara contra $\text{mejor}$. Si $\text{mejor} = -\infty$,
**no corta nada**. Encontrar rápido una buena solución hace que las podas actúen
antes. Por eso:

- explorar primero $a_i = 1$;
- ordenar los objetos por $v_j / w_j$ decreciente, para que las primeras hojas
  visitadas sean «casi greedy»;
- o inicializar $\text{mejor}$ con el valor de cualquier solución válida (por
  ejemplo, la que da un greedy) — es correcto siempre que sea el valor de una
  solución válida **real**.

Nada de esto cambia el peor caso; cambia (mucho) el caso típico. Fuerza bruta +
cotas + buen orden se llama **branch and bound** (rama y cota).

> `pdfs/fuerza-bruta-y-backtracking.pdf`, diapositivas 36-42 — cota superior, mochila, relajaciones, asignación, orden de exploración

---

## 8. Las cinco variantes: la misma recursión

| Pregunta | Hoja válida / no válida | Combinar hijos | Corte temprano | Podas |
|---|---|---|---|---|
| **Decisión** | `True` / `False` | $\vee$ | **sí**, al primer `True` | factibilidad |
| **Construcción** | guardar $p$ / nada | $\vee$ | **sí** | factibilidad |
| **Conteo** | $1$ / $0$ | $+$ | no | factibilidad |
| **Enumeración** | imprimir $p$ / nada | — | no | factibilidad |
| **Optimización** | $\text{valor}(p)$ / $-\infty$ | $\max$ | no | factibilidad **y** optimalidad |

La formalización ($\text{Sols}$, válida, parciales, sucesoras) es **la misma en
las cinco filas**. Por eso se escribe primero y una sola vez.

### Decisión

```
reinas(i, p)
    si ¬R₂(p):   devolver False        // la reina i−1 ataca a otra
    si i = n+1:  devolver True
    para j ← 1 hasta n:
        si reinas(i+1, p ⊕ j):  devolver True
    devolver False
```

El `devolver True` temprano dentro del `for` es una **poda gratis**: si una rama
da `True`, las otras no cambian el resultado. **Solo vale para decisión.**

### Conteo

```
contarReinas(i, p)
    si ¬R₂(p):   devolver 0
    si i = n+1:  devolver 1
    c ← 0
    para j ← 1 hasta n:  c ← c + contarReinas(i+1, p ⊕ j)
    devolver c
```

Semántica: $\text{contarReinas}(i,p) = |\text{Ext}(p) \cap \text{Sols}_{\text{válidas}}|$,
la cantidad de extensiones válidas de $p$. Con eso, la corrección de la poda dice
exactamente que si $\neg R_2(p)$ ese conjunto es vacío y $0$ es la respuesta
correcta. Para $n=8$ devuelve **92**.

### Construcción

Para devolver una solución hay que **tener** la parcial. Se usa un arreglo global
`sol[1..n]` que se comparte y **se deshace al volver** — eso es literalmente el
backtrack — y se copia a `mejorSol` solo al mejorar, en $O(n)$.

Si en cambio pasás $p \oplus 0$ **por copia**, cada nodo cuesta $O(n)$. Hay que
decidirlo y decirlo.

### Enumeración

Mismo recorrido; en cada hoja válida, imprimir y seguir. Nada de corte temprano.

- Las podas por **factibilidad** siguen valiendo tal cual.
- Las podas por **optimalidad no aplican** (no hay «mejor»). Salvo que pidan
  *todas* las óptimas: ahí sí, pero cortando con $U(p) < \text{mejor}$ **estricto**,
  y vaciando la lista cada vez que $\text{mejor}$ mejora.
- Cota inferior de complejidad: hay que **escribir** cada solución, así que
  $\Omega(n \cdot |\text{Sols}_{\text{válidas}}|)$.

> `pdfs/fuerza-bruta-y-backtracking.pdf`, diapositivas 44-48 — decisión, construcción, enumeración, conteo, tabla resumen

---

## 9. Complejidad

Un algoritmo de backtracking recorre un árbol. Su tiempo es
$$T = \sum_{\text{nodos visitados } p} (\text{trabajo en } p),$$
sin contar las llamadas recursivas.

**Cota superior cómoda:**
$$T \leq (\#\text{nodos del árbol completo}) \times (\text{máximo trabajo por nodo}).$$

Un árbol donde cada nodo tiene a lo sumo $k$ hijos y de altura $n$ tiene **a lo
sumo**
$$1 + k + k^2 + \dots + k^n = \frac{k^{n+1}-1}{k-1} = O(k^n) \text{ nodos}$$
($2^{n+1}-1$ si $k=2$). Con podas, el árbol visitado es un **subárbol** del
completo, así que la misma cota sigue valiendo — y en el peor caso, en general,
se alcanza.

> **Nivel de rigor esperado:** alcanza con «árbol binario de altura $n$, $O(2^n)$
> nodos, $O(1)$ por nodo». Pero **sí hay que decir cuánto cuesta cada nodo y de
> qué depende**.

### Mochila: las cuatro versiones

| Versión | Nodos | Trabajo por nodo | Tiempo |
|---|---|---|---|
| $\text{mochila}_1(i,p)$, copia $p$ | $2^{n+1}-1$ | $O(n)$ | $O(n\cdot 2^n)$ |
| $\text{mochila}_2(i,pa,va)$ | $2^{n+1}-1$ | $O(1)$ | $O(2^n)$ |
| $\text{mochila}_3$ (factibilidad) | $\leq 2^{n+1}-1$ | $O(1)$ | $O(2^n)$ |
| $\text{mochila}_4$ (ambas podas) | $\leq 2^{n+1}-1$ | $O(1)$ | $O(2^n)$ |

Otra forma de verlo: $T(m) = 2T(m-1) + O(1)$ con $m = n-i+1$ objetos por decidir,
que da $T(m) = O(2^m)$.

**Espacio:** profundidad de recursión $n$, cada llamada $O(1)$ $\Rightarrow$
$O(n)$. Si guardamos `sol` y `mejorSol`, $O(n)$ más. Si copiamos $p$ en cada
llamada, hasta $n$ copias vivas de longitud $\leq n$: $O(n^2)$.

### $n$ reinas: el universo importa (otra vez)

Con $\text{Sols} = \{1,\dots,n\}^n$: cada nodo tiene $n$ hijos, altura $n$, así que
$\frac{n^{n+1}-1}{n-1} = O(n^n)$ nodos. Chequear la reina nueva contra las
anteriores cuesta $O(n)$. Total: $O(n^{n+1})$.

Con $\text{Sols} = $ permutaciones: en el nivel $i$ hay $\frac{n!}{(n-i)!}$ nodos, y
$$\sum_{i=0}^{n} \frac{n!}{(n-i)!} = n!\sum_{k=0}^{n}\frac{1}{k!} \leq e\cdot n!,$$
o sea $O(n!)$ nodos y $O(n \cdot n!)$ de tiempo.

$n^n$ contra $n!$: por Stirling, $n! \approx (n/e)^n$, una ganancia de $e^n$.
Para $n=12$: $8{,}9\times10^{12}$ contra $4{,}8\times10^{8}$.

### Hasta dónde llega la fuerza bruta

Suponiendo $10^8$ operaciones por segundo:

| Nodos | $n=10$ | $n=20$ | $n=30$ |
|---|---|---|---|
| $2^n$ | $10^{-5}$ s | $0{,}01$ s | $11$ s |
| $n^2 \cdot 2^n$ | $10^{-3}$ s | $4$ s | $2{,}7$ hs |
| $n!$ | $0{,}04$ s | 770 años | $8\times10^{16}$ años |
| $n^n$ | 100 s | $3\times10^{10}$ años | — |

$2^n$ es razonable hasta $n \approx 30$; $n!$ hasta $n \approx 12$; $n^n$ hasta
$n \approx 9$. Las podas mueven estos límites en la práctica, a veces muchísimo,
**pero no cambian las columnas**.

> `pdfs/fuerza-bruta-y-backtracking.pdf`, diapositivas 49-52 — la cuenta básica, las cuatro versiones de mochila, $n$ reinas, tabla de tiempos

---

## 10. La receta, y los tips

Frente a un enunciado nuevo, **en este orden**:

1. **Candidatas:** elegir $\text{Sols}$ y escribir la semántica — qué objeto del
   enunciado representa cada vector.
2. **Válidas:** escribir $\text{válida}(a)$ como fórmula. Si es optimización,
   $\text{valor}(a)$ y el orden.
3. **Parciales y sucesoras:** qué es una decisión, qué decisiones son legales, qué
   resumen de las decisiones pasadas necesita la recursión.
4. **Función recursiva:** caso base (la hoja: ¿válida?, ¿cuánto vale?) y caso
   recursivo (combinar sucesoras con $\vee$, $+$, $\max$). **Escribir su
   semántica.**
5. **Podas:** factibilidad y optimalidad, con demostración.
6. **Complejidad:** nodos $\times$ trabajo por nodo; espacio: profundidad $\times$
   estado.
7. **Implementar**, y testear contra la versión sin podas.

**Tips de la cátedra:**

1. Antes de programar, escribí $\text{Sols}$ y $\text{válida}$ en un papel. Si no
   podés, no entendés el problema todavía.
2. Diseñá la versión más simple (decisión, o el valor óptimo). Construir, contar
   y enumerar son modificaciones de cinco líneas.
3. Los parámetros son el resumen de las decisiones pasadas. Si necesitás la
   parcial entera, compartila y deshacé al volver.
4. Toda poda viene con una demostración de una línea que empieza «sea $a$ una
   extensión cualquiera de $p$» y termina «luego $a$ no es válida» (o «luego
   $\text{valor}(a) \leq U(p)$»).
5. El peor caso con podas es, en general, el mismo que sin podas. **No prometas
   más de lo que podés demostrar.**
6. Testeá contra la fuerza bruta pura. Es el mejor test que vas a tener en toda
   la materia.

### Qué hay que saber hacer al terminar la práctica

Según la propia teórica, los seis objetivos son:

1. Convertir un enunciado en lenguaje natural en una descripción de conjuntos de
   soluciones: candidatas, válidas, parciales; y para optimización, una función
   de valuación.
2. Dar una función recursiva que resuelva el problema, y **demostrar que es
   correcta** respecto de esa descripción.
3. Implementarla con backtracking (el pasaje de la fórmula al código no se
   demuestra: se asume directo).
4. Modificarla para que construya la solución, o las enumere, o las cuente.
5. Proponer podas por factibilidad y por optimalidad, y **demostrar que no
   pierden soluciones**.
6. Calcular la complejidad temporal y espacial.

> `pdfs/fuerza-bruta-y-backtracking.pdf`, diapositivas 8, 53-54 — objetivos de la práctica, la receta, tips

---

## Bibliografía de la cátedra

- J. Erickson, *Algorithms*, cap. 2 (Backtracking). Libre en
  `jeffe.cs.illinois.edu/teaching/algorithms`. **Referencia principal de esta
  clase.**
- G. Brassard, P. Bratley, *Fundamentals of Algorithmics*, cap. 9.
- S. Skiena, *The Algorithm Design Manual*, cap. 9 (Combinatorial search).
- T. Cormen et al., *Introduction to Algorithms*, cap. 4 y apéndice C.
- J. Kleinberg, É. Tardos, *Algorithm Design*, cap. 2 y cap. 10.
