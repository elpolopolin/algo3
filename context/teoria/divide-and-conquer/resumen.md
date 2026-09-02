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
