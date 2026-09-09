# Merge sort (ordenamiento por mezcla)

- Divide el arreglo a la mitad, ordena cada mitad por separado (de forma recursiva) y después **mezcla** ("merge") las dos mitades ya ordenadas en tiempo lineal.
- Es el ejemplo canónico de D&C (**Divide & Conquer**, divide y conquista): dividir, conquistar, combinar.
- Complejidad $\Theta(n \log n)$ siempre (peor, mejor y promedio caso), porque la recurrencia $T(n) = 2T(n/2) + \Theta(n)$ da eso tanto por árbol de recursión como por Teorema Maestro.

## La idea (patrón D&C)

Dado un arreglo $A$ de $n$ enteros, para ordenarlo:

1. **Dividir:** partir $A$ en dos mitades $A_1$ y $A_2$ de tamaño $n/2$.
2. **Conquistar:** ordenar $A_1$ y $A_2$ (llamando recursivamente al mismo algoritmo).
3. **Combinar:** mezclar los dos subarreglos ya ordenados en uno solo ordenado.

El caso base es un subarreglo de longitud 1 (o vacío): ya está ordenado, no hay nada que hacer.

## Pseudocódigo

```
MERGESORT(A, l, r)
    if l = r
        return
    q ← ⌊(l + r) / 2⌋
    MERGESORT(A, l, q)
    MERGESORT(A, q + 1, r)
    MERGE(A, l, q, r)
```

`l` y `r` son los índices que delimitan el subarreglo $A[l:r]$ que se está ordenando en ese llamado. La llamada inicial es `MERGESORT(A, 0, n-1)`.

> Nota: en el material fuente (`08-ejemplo-de-d-c-merge-sort.md`) el segundo llamado recursivo aparece transcripto como `MERGESORT(A, l+1, r)`, que es un error de OCR al extraer el PDF (la fórmula original usa `q+1`, no `l+1`). El pseudocódigo de arriba tiene la versión correcta: la recursión se parte en `[l, q]` y `[q+1, r]`, si no el algoritmo ni siquiera achica el problema.

## MERGE: cómo se combinan dos mitades ordenadas

Dado que $A[l{:}q]$ y $A[q{+}1{:}r]$ ya están ordenados por separado, para mezclarlos:

1. Copiar $A[l..q]$ en un arreglo auxiliar $L$, y $A[q{+}1..r]$ en un arreglo auxiliar $R$.
2. Recorrer $L$ y $R$ a la vez con dos punteros $i, j$, y en cada paso elegir el menor de los dos elementos que están "arriba de la fila" para escribirlo en $A$.
3. Cuando uno de los dos se termina, copiar lo que queda del otro directamente al final.

```
k = l; i = 0; j = 0
while (i < |L| and j < |R|)
    if L[i] <= R[j]
        A[k] = L[i]; i = i + 1
    else
        A[k] = R[j]; j = j + 1
    k = k + 1
// copiar lo que queda de L o de R
```

Este proceso recorre cada elemento una sola vez, así que **MERGE cuesta tiempo lineal**, $\Theta(n)$ para un segmento de tamaño $n$.

![Ejemplo de MERGE](imagenes/teo04-Divide_and_Conquer.pdf-0011-06.png)

![Ejemplo de MERGESORT completo](imagenes/teo04-Divide_and_Conquer.pdf-0012-06.png)

## Por qué es correcto

Se prueba por **inducción en $n = r - l + 1$** (el tamaño del segmento):

- **Caso base** ($n \le 1$): el segmento ya está ordenado (0 o 1 elementos), no hay nada que probar.
- **Caso inductivo** ($n > 1$): ambos llamados recursivos reciben segmentos estrictamente más chicos. Por hipótesis inductiva, cada uno termina, no pierde ni agrega elementos, y deja su mitad ordenada. `MERGE` combina esas dos mitades ya ordenadas preservando el orden, así que el segmento completo queda ordenado.

(La demostración de que `MERGE` en sí hace lo que promete queda como intuición a este nivel de la materia — formalmente se probaría con un invariante de ciclo.)

## Complejidad: por qué es $\Theta(n \log n)$

**Dividir** cuesta $\Theta(1)$ (calcular el punto medio). **Conquistar** son dos llamados recursivos sobre instancias de tamaño $n/2$. **Combinar** (el MERGE) cuesta $\Theta(n)$. Eso da la recurrencia:

$$T(n) = 2T(n/2) + \Theta(n), \qquad T(1) = \Theta(1)$$

### Intuición: árbol de recursión

Si en un arreglo de $n$ elementos se hacen $cn$ operaciones fuera de la recursión, el árbol de llamados recursivos queda así:

![Árbol de recursión: costo por nivel](imagenes/teo04-Divide_and_Conquer.pdf-0015-07.png)

![Árbol de recursión: cada nivel suma cn](imagenes/teo04-Divide_and_Conquer.pdf-0015-08.png)

En cada "piso" del árbol se hacen en total $cn$ operaciones (el trabajo se reparte entre el doble de nodos, pero cada uno hace la mitad), y hay $\log n$ pisos hasta llegar a los casos base. Sumando: $cn \cdot \log n$, es decir, la complejidad parece ser $O(n \log n)$.

### Prueba formal: método de sustitución

Sea $d = T(2)$ el costo del caso base, y sea $c$ tal que $T(n) \le 2T(n/2) + cn$. Se toma $f(n) = n\log n$ y $C = \max\{c, d\}$, y se prueba por inducción que $T(n) \le Cn\log n$ (lo cual implica $T(n) = O(n\log n)$):

- Caso base $n = 2$: vale por elección de $d$ (y porque $\log 1 = 0$).
- Caso inductivo: usando la hipótesis inductiva sobre $T(n/2)$,
$$T(n) \le 2T(n/2) + cn \le 2 \cdot C\frac{n}{2}\log\frac{n}{2} + cn \le Cn\log n$$

Con esto queda probado que $T(n) = O(n\log n)$ (y junto con la cota inferior análoga, $T(n) = \Theta(n\log n)$).

### Atajo: Teorema Maestro

Para $T(n) = 2T(n/2) + \Theta(n)$: $a = 2$, $b = 2$, $q = \log_2 2 = 1$, $f(n) = \Theta(n)$. Como $f(n) = \Theta(n^q)$, cae en el **caso 2** del Teorema Maestro (con $r = 0$), y da directamente:

$$T(n) = \Theta(n \log n)$$

## Fuentes

- `context/teoria/divide-and-conquer/temas/07-ejemplo-de-d-c-merge-sort.md` (L1-32) — planteo del problema y patrón dividir/conquistar/combinar.
- `context/teoria/divide-and-conquer/temas/08-ejemplo-de-d-c-merge-sort.md` (L1-36) — pseudocódigo de MERGESORT.
- `context/teoria/divide-and-conquer/temas/09-ejemplo-de-d-c-merge-sort.md` (L1-28) — pseudocódigo e idea de MERGE en tiempo lineal.
- `context/teoria/divide-and-conquer/temas/10-ejemplo-de-d-c-merge-sort.md` (L1-58) — figuras de ejemplo de MERGE y MERGESORT.
- `context/teoria/divide-and-conquer/temas/12-teorema.md` (L1-40) — teorema y prueba de correctitud por inducción.
- `context/teoria/divide-and-conquer/temas/14-dividir.md` (L1-34) — costo de cada componente y recurrencia $T(n) = 2T(n/2) + \Theta(n)$.
- `context/teoria/divide-and-conquer/temas/15-ejemplo-de-d-c-merge-sort.md` (L1-36) — análisis por árbol de recursión.
- `context/teoria/divide-and-conquer/temas/18-el-m-todo-de-sustituci-n.md` (L1-28) — prueba formal por sustitución de $T(n) = O(n\log n)$.
- `context/teoria/divide-and-conquer/temas/32-mergesort-de-nuevo.md` (L1-28) — aplicación del Teorema Maestro a la recurrencia de merge sort.

---

# El Teorema Maestro y el método de sustitución

> Ampliación del resumen: cómo resolver recurrencias, no sólo la de merge sort.

## El patrón D&C, en general

Un algoritmo de dividir y conquistar tiene esta pinta:

```
DIVIDIR-Y-CONQUISTAR(X)
  if X es un caso base
      return RESOLVER(X)
  (X_1, ..., X_a) <- DIVIDIR(X)
  para i = 1..a
      Y_i <- DIVIDIR-Y-CONQUISTAR(X_i)
  return COMBINAR(Y_1, ..., Y_a)
```

Y siempre se demuestran las mismas dos cosas, de la misma manera:

- **Correctitud:** por **inducción** (fuerte, casi siempre), usando la recursión.
  La HI es "las llamadas recursivas devuelven lo correcto para instancias más
  chicas".
- **Complejidad:** calculando el tamaño de cada $X_i$ y el costo de `COMBINAR`,
  y resolviendo la recurrencia que sale.

De ahí la forma canónica
$$T(n) = a\,T(n/b) + f(n),$$
con $a$ = cuántos subproblemas, $n/b$ = de qué tamaño, $f(n)$ = lo que cuesta
dividir + combinar.

## El árbol de recursión: de dónde sale todo

Suponiendo $n$ potencia de $b$, tras $j$ niveles:
$$T(n) = a^j\,T(n/b^j) + \sum_{i=0}^{j-1} a^i f(n/b^i).$$

Sea $L = \log_b n$ (la altura). Al llegar a los casos base:
$$T(n) = \underbrace{a^L\,T(1)}_{\text{hojas}} + \underbrace{\sum_{i=0}^{L-1} a^i f(n/b^i)}_{\text{niveles internos}}.$$

Y como
$$a^L = a^{\log_b n} = n^{\log_b a} = n^q, \qquad \text{con } q := \log_b a,$$
**las hojas cuestan $\Theta(n^q)$** y el nivel $i$ cuesta $a^i f(n/b^i)$.

El teorema maestro es simplemente *quién gana*: las hojas, los niveles
intermedios, o la raíz.

## Los tres casos

Comparamos siempre $f(n)$ contra $n^q$ con $q = \log_b a$.

| Caso | Condición sobre $f$ | Forma del árbol | Resultado |
|---|---|---|---|
| **1** | $f(n) = O(n^{q-\varepsilon})$ para algún $\varepsilon > 0$ | el costo **aumenta** hacia abajo | $T(n) = \Theta(n^q)$ — **dominan las hojas** |
| **2** | $f(n) = \Theta(n^q \log^r n)$, con $r \geq 0$ | los niveles son **comparables** | $T(n) = \Theta(n^q \log^{r+1} n)$ — **se acumulan los niveles** |
| **3** | $f(n) = \Omega(n^{q+\varepsilon})$ **y** $a f(n/b) \leq c f(n)$ para algún $0 < c < 1$ | el costo **decrece** hacia abajo | $T(n) = \Theta(f(n))$ — **domina la raíz** |

La condición extra del caso 3 ($a f(n/b) \le c f(n)$, llamada *de regularidad*)
es la que hace que la suma de los niveles sea una geométrica decreciente:
iterándola sale $a^i f(n/b^i) \leq c^i f(n)$, y la serie converge.

### Cómo usarlo en un ejercicio

1. Identificar $a$, $b$ y $f(n)$.
2. Calcular $q = \log_b a$.
3. Comparar $f(n)$ con $n^q$ y ver en cuál de los tres casos cae.
4. Si **no cae en ninguno**, el teorema maestro no aplica y hay que ir por árbol
   de recursión o sustitución.

Ejemplos rápidos:

| Recurrencia | $a$, $b$, $f$ | $q = \log_b a$ | Caso | $T(n)$ |
|---|---|---|---|---|
| $T(n) = 2T(n/2) + n$ (merge sort) | $2, 2, n$ | $1$ | 2 ($r=0$) | $\Theta(n \log n)$ |
| $T(n) = T(n/2) + \Theta(1)$ (búsqueda binaria) | $1, 2, 1$ | $0$ | 2 ($r=0$) | $\Theta(\log n)$ |
| $T(n) = 3T(n/2) + n^2$ (Strassen ingenuo) | $3, 2, n^2$ | $\log_2 3 \approx 1.58$ | 3 | $\Theta(n^2)$ |
| $T(n) = 3T(n/4)$ | $3, 4, 0$ | $\log_4 3$ | 1 | $\Theta(n^{\log_4 3})$ |

> **Ojo:** el teorema maestro sólo sirve para recurrencias de la forma
> $T(n) = aT(n/b) + f(n)$, es decir, cuando el tamaño se **divide**. Las del tipo
> $T(n) = T(n-1) + g(n)$ o $T(n) = 2T(n-1)$, donde el tamaño se **resta**, no
> entran: esas se resuelven desenrollando la recursión (telescoping) o con
> inducción. Por ejemplo $T(n) = T(n-1) + n$ da $\Theta(n^2)$ (suma de Gauss) y
> $T(n) = 2T(n-1)$ da $\Theta(2^n)$.

## El método de sustitución

Cuando el teorema maestro no aplica, o cuando el ejercicio pide "demostrar", se
**adivina la forma de la respuesta y se prueba por inducción**.

Ejemplo con merge sort. Sea $d = T(2)$ el costo del caso base, y sabemos que
existe $c$ tal que
$$T(n) \leq 2T(n/2) + cn.$$
Tomamos $f(n) = n \log n$ y $C = \max\{c, d\}$, y probamos que
$T(n) \leq C n \log n$, lo cual implica $T(n) = O(n \log n)$.

Se hace por inducción con **caso base $n = 2$** (no $n=1$, porque $\log 1 = 0$ y
la cota se caería). El caso base vale por la elección de $d$; el paso inductivo
usa la HI sobre $n/2$.

Dos detalles que son exactamente los de la unidad de demostraciones: hay que
**elegir bien el caso base** y **exhibir las constantes** al final.

---

# Búsqueda binaria y sus extensiones

## La versión clásica

```
BINARY-SEARCH(A, x, l, r)
  Precondición: A[l:r] está ordenado
  if l > r: return NO-ESTÁ
  m <- ⌊(l + r) / 2⌋
  if A[m] = x:   return m
  if x < A[m]:   return BINARY-SEARCH(A, x, l, m-1)
  si no:         return BINARY-SEARCH(A, x, m+1, r)
```

Es D&C con $a = 1$ (una sola rama sobrevive), $b = 2$, $f(n) = \Theta(1)$:
$$T(n) \leq T(n/2) + \Theta(1) \quad\Longrightarrow\quad T(n) = O(\log n).$$

## Más allá de un arreglo: el esquema general

La idea de búsqueda binaria **no necesita un arreglo**. Alcanza con tener:

1. un **dominio ordenado** de candidatos $T$;
2. un **predicado** $P(t)$ que sabemos evaluar;
3. un **único umbral** $t^\star$ donde el predicado cambia:
$$P(t) = \begin{cases} \text{falso} & t < t^\star \\ \text{verdadero} & t \geq t^\star \end{cases}$$

Con eso podemos encontrar el menor $t$ que cumple la propiedad en
$O(\log |T|)$, asumiendo que evaluar $P$ cuesta $O(1)$.

**Esto es lo que hay que buscar en los ejercicios.** La pregunta no es "¿está
ordenado el arreglo?" sino: *¿puedo definir un predicado monótono sobre las
posiciones, de modo que mirar el punto medio me deje descartar la mitad?* Si la
respuesta es sí, hay un algoritmo $O(\log n)$.

Ejemplo del patrón: si $a$ está **estrictamente creciente** con enteros
distintos, la función $g(i) = a_i - i$ es **no decreciente**, así que
"$a_i - i \geq 0$" es un predicado monótono: se puede buscar binariamente el
punto donde cambia de signo.

## Fuentes

- `temas/05-t-cnicas-algor-tmicas.md` (L1-46) — por qué estudiamos técnicas
- `temas/06-divide-conquer.md` (L1-30) — el esqueleto de D&C, correctitud por inducción
- `temas/18-el-m-todo-de-sustituci-n.md` (L1-28) — método de sustitución en merge sort
- `temas/26-el-teorema-maestro.md` (L1-37), `temas/27-el-teorema-maestro.md` (L1-29) — árbol de recursión, hojas vs. niveles internos
- `temas/28-el-teorema-maestro-caso-1.md` (L1-26) — caso 1, dominan las hojas
- `temas/29-el-teorema-maestro-caso-2.md` (L1-33) — caso 2, se acumulan los niveles
- `temas/30-el-teorema-maestro-caso-3.md` (L1-38) — caso 3, domina la raíz, y la tabla de las tres formas del árbol
- `temas/67-b-squeda-binaria.md` (L1-36) — búsqueda binaria como D&C
- `temas/68-m-s-all-de-b-squeda-binaria.md` (L1-24) — dominio ordenado, predicado, umbral
