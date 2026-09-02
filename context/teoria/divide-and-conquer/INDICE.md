# Índice — divide-and-conquer

80 archivos · 2371 líneas en total.

> Generado por `tools/indexar.py`. No editar a mano: se regenera.
> Para buscar un término literal es más barato `grep -rl "término" temas/`
> que leer este índice. Este índice sirve para lo que grep no encuentra.

| Archivo | Tema | De qué trata | Conceptos | Líneas |
|---|---|---|---|---|
| `01-divide-and-conquer.md` | Divide and Conquer | TDA - Algo3 | — | 30 |
| `02-plan.md` | Plan | El Teorema Maestro para resolver recurrencias | `Plan` | 42 |
| `03-t-cnicas-algor-tmicas.md` | T cnicas algor tmicas (1/3: Técnicas algorítmicas) | A medida que resolvemos problemas, nos vamos dando cuenta de que hay patrones o enfoques que se repiten una y… | `técnicas algorítmicas`, `patrones`, `enfoques` | 28 |
| `04-t-cnicas-algor-tmicas.md` | T cnicas algor tmicas (2/3: Técnicas algorítmicas) | En general, vemos técnicas porque: | `Técnicas algorítmicas` | 40 |
| `05-t-cnicas-algor-tmicas.md` | T cnicas algor tmicas (3/3: Técnicas algorítmicas) | En general, vemos técnicas porque: | `el mismo tamaño`, `Técnicas algorítmicas` | 46 |
| `06-divide-conquer.md` | Divide conquer | Los algoritmos de D&C suelen tener esta pinta. | `return`, `para`, `Correctitud`, `Complejidad` | 30 |
| `07-ejemplo-de-d-c-merge-sort.md` | Ejemplo de d c merge sort (1/7: Ejemplo de D&C: Merge sort) | Problema: Sorting | `Dividir`, `Conquistar`, `Combinar` | 32 |
| `08-ejemplo-de-d-c-merge-sort.md` | Ejemplo de d c merge sort (2/7: Ejemplo de D&C: Merge sort) | Siendo más precisos, vamos a diseñar un algoritmo MERGESORT( A, l, r ) que recibe un arreglo A y dos índices… | `return` | 36 |
| `09-ejemplo-de-d-c-merge-sort.md` | Ejemplo de d c merge sort (3/7: Ejemplo de D&C: Merge sort) | Se puede implementar en tiempo lineal: copiamos A [ l . . . q ] en L y A [ q + 1 . . . r ] en R . Luego,… | `while`, `else` | 28 |
| `10-ejemplo-de-d-c-merge-sort.md` | Ejemplo de d c merge sort (4/7: Ejemplo de D&C: Merge sort) | <!-- Start of picture text --> | — | 58 |
| `11-ejemplo-de-d-c-merge-sort.md` | Ejemplo de d c merge sort (5/7: Ejemplo de D&C: Merge sort) | — | — | 2 |
| `12-teorema.md` | Teorema | MERGESORT( A, l, r ) termina y deja ordenados exactamente los elementos que estaban en A [ p..r ]. | `Prueba por inducción en`, `Teorema` | 40 |
| `13-ejemplo-de-d-c-merge-sort.md` | Ejemplo de d c merge sort (6/7: Ejemplo de D&C: Merge sort) | Este algoritmo sigue el patrón de D&C. Veamos la cantidad de operaciones que se hace en cada componente del… | `patrón` | 4 |
| `14-dividir.md` | Dividir | Calcular el punto medio cuesta Θ(1). | `Dividir` | 34 |
| `15-ejemplo-de-d-c-merge-sort.md` | Ejemplo de d c merge sort (7/7: Ejemplo de D&C: Merge sort) | Podemos pensar en el árbol de recursión, e intentar llevar la cuenta de cuánto se trabaja en cada llamado. Si… | — | 36 |
| `16-m-todo-de-sustituci-n.md` | M todo de sustituci n | Supongamos que tenemos alguna recurrencia, como por ejemplo | `Método de sustitución` | 8 |
| `17-el-m-todo-de-sustituci-n.md` | El m todo de sustituci n (1/2: El método de sustitución) | Se llama sustitución porque en el paso inductivo vamos a acotar / sustituir T ( n/ 2) por Cf ( n/ 2). | `El método de sustitución` | 28 |
| `18-el-m-todo-de-sustituci-n.md` | El m todo de sustituci n (2/2: El método de sustitución) | Sea d = T (2) la cantidad de operaciones en el caso base de merge sort, y recordemos que existe una c tal que | `El método de sustitución` | 28 |
| `19-algoritmo-de-karatsuba.md` | Algoritmo de karatsuba (1/5: Algoritmo de Karatsuba) | Problema: producto de números | `Algoritmo de Karatsuba` | 28 |
| `20-algoritmo-de-karatsuba.md` | Algoritmo de karatsuba (2/5: Algoritmo de Karatsuba) | Problema: producto de números | `Algoritmo de Karatsuba` | 35 |
| `21-algoritmo-de-karatsuba.md` | Algoritmo de karatsuba (3/5: Algoritmo de Karatsuba) | Luego, usando distributiva tenemos que | `Algoritmo de Karatsuba` | 54 |
| `22-algoritmo-de-karatsuba.md` | Algoritmo de karatsuba (4/5: Algoritmo de Karatsuba) | Alternativa: Calculamos recursivamente sólo | `Algoritmo de Karatsuba` | 38 |
| `23-algoritmo-de-karatsuba.md` | Algoritmo de karatsuba (5/5: Algoritmo de Karatsuba) | La cantidad de operaciones que hace el algoritmo ahora satisface la relación<sup>4</sup> T ( n ) = 3 T ( n/… | `Algoritmo de Karatsuba` | 24 |
| `24-el-teorema-maestro.md` | El teorema maestro (1/4: El Teorema Maestro) | T ( n ) = aT ( n/b ) + f ( n ) , | `Caso`, `El Teorema Maestro`, `Consideremos` | 28 |
| `25-el-teorema-maestro.md` | El teorema maestro (2/4: El Teorema Maestro) | Como vamos a ver más adelante, el caso 1 se corresponde con la situación en la que la mayoría del trabajo se… | `Caso`, `El Teorema Maestro`, `Resultado` | 26 |
| `26-el-teorema-maestro.md` | El teorema maestro (3/4: El Teorema Maestro) | Supongamos que n es potencia de b (y entonces siempre se parte bien<sup>5</sup> ). Tras j niveles, | `El Teorema Maestro`, `Como` | 37 |
| `27-el-teorema-maestro.md` | El teorema maestro (4/4: El Teorema Maestro) | <!-- Start of picture text --> | `El Teorema Maestro` | 29 |
| `28-el-teorema-maestro-caso-1.md` | El teorema maestro caso 1 | Supongamos f ( n ) = O ( n<sup>q−ε</sup> ). Como a = b<sup>q</sup> , el nivel i satisface para alguna… | — | 26 |
| `29-el-teorema-maestro-caso-2.md` | El teorema maestro caso 2 | Supongamos f ( n ) = Θ( n<sup>q</sup> log<sup>r</sup> n ), con r ≥ 0. En el nivel i : a<sup>i</sup> f (… | — | 33 |
| `30-el-teorema-maestro-caso-3.md` | El teorema maestro caso 3 | Supongamos f ( n ) = Ω( n<sup>q+</sup><sup>ε</sup> ) y, para algún 0 < c < 1 y todo n suficientemente grande,… | — | 38 |
| `31-el-algoritmo-de-karatsuba.md` | El algoritmo de karatsuba (1/6: El algoritmo de Karatsuba) | Apliquemos el teorema a la recursión de Karatsuba. La relación era | `El algoritmo de Karatsuba` | 34 |
| `32-mergesort-de-nuevo.md` | Mergesort de nuevo | Para practicar, apliquemos el Teorema Maestro a la recurrencia de Merge Sort T ( n ) = 2 T ( n/ 2) + Θ( n ) | `Mergesort de nuevo` | 28 |
| `33-el-algoritmo-de-karatsuba.md` | El algoritmo de karatsuba (2/6: El algoritmo de Karatsuba) | Unos comentarios interesantes: | `El algoritmo de Karatsuba` | 30 |
| `34-el-algoritmo-de-karatsuba.md` | El algoritmo de karatsuba (3/6: El algoritmo de Karatsuba) | Unos comentarios interesantes: | `Algoritmo de Toom-Cook`, `El algoritmo de Karatsuba` | 32 |
| `35-el-algoritmo-de-karatsuba.md` | El algoritmo de karatsuba (4/6: El algoritmo de Karatsuba) | En Karatsuba mejoramos el algoritmo de producto partiendo los números de n bits en 2 de n/ 2. Mejorará la… | `Algoritmo de Toom-Cook`, `El algoritmo de Karatsuba`, `Unos comentarios interesantes` | 36 |
| `36-el-algoritmo-de-karatsuba.md` | El algoritmo de karatsuba (5/6: El algoritmo de Karatsuba) | Unos comentarios interesantes: | `Algoritmo de Toom-Cook`, `El algoritmo de Karatsuba` | 46 |
| `37-el-algoritmo-de-karatsuba.md` | El algoritmo de karatsuba (6/6: El algoritmo de Karatsuba) | Unos comentarios interesantes: | `Algoritmo de Toom-Cook`, `El algoritmo de Karatsuba` | 108 |
| `38-algoritmo-de-strassen.md` | Algoritmo de strassen (1/3: Algoritmo de Strassen) | Dividimos las matrices en bloques, | `Algoritmo de Strassen` | 26 |
| `39-algoritmo-de-strassen.md` | Algoritmo de strassen (2/3: Algoritmo de Strassen) | Dividimos las matrices en bloques, | `Algoritmo de Strassen` | 36 |
| `40-el-algoritmo-de-strassen.md` | El algoritmo de strassen (1/4: El algoritmo de Strassen) | Con mucha inspiración, es posible darse cuenta, como hizo Strassen, de que con 7 multiplicaciones podemos… | `El algoritmo de Strassen` | 26 |
| `41-algoritmo-de-strassen.md` | Algoritmo de strassen (3/3: Algoritmo de Strassen) | Llamando m = n<sup>2</sup> , | `Algoritmo de Strassen` | 28 |
| `42-el-algoritmo-de-strassen.md` | El algoritmo de strassen (2/4: El algoritmo de Strassen) | Algunos comentarios adicionales: | `El algoritmo de Strassen` | 26 |
| `43-el-algoritmo-de-strassen.md` | El algoritmo de strassen (3/4: El algoritmo de Strassen) | Algunos comentarios adicionales: | `descomposición tensorial`, `El algoritmo de Strassen` | 32 |
| `44-el-algoritmo-de-strassen.md` | El algoritmo de strassen (4/4: El algoritmo de Strassen) | Algunos comentarios adicionales: | `descomposición tensorial`, `Autores Año Complejidad`, `El algoritmo de Strassen` | 38 |
| `45-timba.md` | Timba (1/3: Timba) | — | `Timba` | 2 |
| `46-problema-timbear.md` | Problema timbear (1/2: Problema: Timbear) | Tenemos predicciones para el precio de una acción para distintos días como p 1 . . . pn . Tenemos que elegir… | — | 30 |
| `47-timba.md` | Timba (2/3: Timba) | — | `Timba` | 2 |
| `48-problema-timbear.md` | Problema timbear (2/2: Problema: Timbear) | Tenemos predicciones para el precio de una acción para distintos días como p 1 . . . pn . Tenemos que elegir… | — | 34 |
| `49-timba.md` | Timba (3/3: Timba) | Vamos a usar una estrategia muy útil para resolver problemas: reducirlo a otro (que con un poco de suerte ya… | `Timba` | 28 |
| `50-m-ximo-subarreglo.md` | M ximo subarreglo (1/16: Máximo subarreglo) | Más formalmente, tenemos la siguiente proposición Proposición | `Demostración`, `Máximo subarreglo` | 33 |
| `51-m-ximo-subarreglo.md` | M ximo subarreglo (2/16: Máximo subarreglo) | TDA - Algo3 (DC, FCEyN, UBA) | `Máximo subarreglo` | 20 |
| `52-m-ximo-subarreglo.md` | M ximo subarreglo (3/16: Máximo subarreglo) | Intentemos proponer un enfoque con D&C para resolver el problema. Qué podríamos hacer? Dividir el arreglo a… | `Máximo subarreglo` | 4 |
| `53-izquierda.md` | Izquierda | Está completamente contenido en [ ℓ, m ]. | `Izquierda` | 46 |
| `54-m-ximo-subarreglo.md` | M ximo subarreglo (4/16: Máximo subarreglo) | Para la parte de combinar, alcanza con observar que hay que maximizar para la izquierda y luego para la… | `Máximo subarreglo` | 29 |
| `55-m-ximo-subarreglo.md` | M ximo subarreglo (5/16: Máximo subarreglo) | Para la parte de combinar, alcanza con observar que hay que maximizar para la izquierda y luego para la… | `Máximo subarreglo` | 29 |
| `56-m-ximo-subarreglo.md` | M ximo subarreglo (6/16: Máximo subarreglo) | Hacemos que los llamados recursivos devuelvan el valor máximo y también el intervalo que lo alcanza. | `return`, `Correctitud`, `Máximo subarreglo` | 30 |
| `57-m-ximo-subarreglo.md` | M ximo subarreglo (7/16: Máximo subarreglo) | Podemos usar el Teorema Maestro (aunque esta recursión ya apareció antes) a = 2 , b = 2 , q = 1 , f ( n ) =… | `Complejidad`, `Máximo subarreglo` | 26 |
| `58-m-ximo-subarreglo.md` | M ximo subarreglo (8/16: Máximo subarreglo) | Se puede hacer mejor? Hay alguna parte en donde estemos siendo redundantes? | `Máximo subarreglo` | 20 |
| `59-m-ximo-subarreglo.md` | M ximo subarreglo (9/16: Máximo subarreglo) | Se puede hacer mejor? Hay alguna parte en donde estemos siendo redundantes? En cada llamado recursivo se… | `Máximo subarreglo` | 20 |
| `60-m-ximo-subarreglo.md` | M ximo subarreglo (10/16: Máximo subarreglo) | Se puede hacer mejor? Hay alguna parte en donde estemos siendo redundantes? En cada llamado recursivo se… | `desde cada borde`, `Máximo subarreglo` | 24 |
| `61-m-ximo-subarreglo.md` | M ximo subarreglo (11/16: Máximo subarreglo) | r q tot( X ) = ∑︂ dk, pre( X ) = max ∑︂ dk, ℓ≤q≤r k = ℓ k = ℓ r v suf( X ) = max ∑︂ dk, best( X ) = max ∑︂… | `Máximo subarreglo` | 28 |
| `62-m-ximo-subarreglo.md` | M ximo subarreglo (12/16: Máximo subarreglo) | Sea X = LR , con L y R consecutivos. Entonces | `Máximo subarreglo` | 22 |
| `63-m-ximo-subarreglo.md` | M ximo subarreglo (13/16: Máximo subarreglo) | Sea X = LR , con L y R consecutivos. Entonces | `Máximo subarreglo` | 24 |
| `64-m-ximo-subarreglo.md` | M ximo subarreglo (14/16: Máximo subarreglo) | Sea X = LR , con L y R consecutivos. Entonces | `Máximo subarreglo` | 28 |
| `65-m-ximo-subarreglo.md` | M ximo subarreglo (15/16: Máximo subarreglo) | Sea X = LR , con L y R consecutivos. Entonces | `Máximo subarreglo` | 30 |
| `66-m-ximo-subarreglo.md` | M ximo subarreglo (16/16: Máximo subarreglo) | Con estos valores nos ahorramos gastar Θ( n ) en la parte de combinar, y en cambio sale en O (1). Luego, la… | `Tarea`, `Máximo subarreglo` | 28 |
| `67-b-squeda-binaria.md` | B squeda binaria | La búsqueda binaria es un caso de D&C | `return`, `Precondición`, `Búsqueda binaria` | 36 |
| `68-m-s-all-de-b-squeda-binaria.md` | M s all de b squeda binaria | Pero la idea de búsqueda binaria va más allá de un arreglo. Basta tener: un dominio ordenado de candidatos T… | `Más allá de búsqueda binaria` | 24 |
| `69-encuentro.md` | Encuentro (1/8: Encuentro) | — | `Encuentro` | 2 |
| `70-problema.md` | Problema (1/2: Problema) | Tenemos n amigos distribuidos en distintas posiciones p 1 . . . pn en una recta. Cada amigo tiene una cierta… | `Problema` | 24 |
| `71-encuentro.md` | Encuentro (2/8: Encuentro) | — | `Encuentro` | 2 |
| `72-problema.md` | Problema (2/2: Problema) | Tenemos n amigos distribuidos en distintas posiciones p 1 . . . pn en una recta. Cada amigo tiene una cierta… | `Problema` | 28 |
| `73-encuentro.md` | Encuentro (3/8: Encuentro) | Intentemos repensar lo que nos piden. Que se puedan encontrar en el momento t es equivalente a que exista un… | `Encuentro` | 20 |
| `74-encuentro.md` | Encuentro (4/8: Encuentro) | Intentemos repensar lo que nos piden. Que se puedan encontrar en el momento t es equivalente a que exista un… | `Encuentro` | 26 |
| `75-encuentro.md` | Encuentro (5/8: Encuentro) | Intentemos repensar lo que nos piden. Que se puedan encontrar en el momento t es equivalente a que exista un… | `Encuentro` | 28 |
| `76-encuentro.md` | Encuentro (6/8: Encuentro) | Ahora si podemos proponer un primer algoritmo. | `Complejidad`, `Encuentro` | 26 |
| `77-encuentro.md` | Encuentro (7/8: Encuentro) | Ahora si podemos proponer un primer algoritmo. | `Complejidad`, `Encuentro` | 30 |
| `78-encuentro.md` | Encuentro (8/8: Encuentro) | Notemos que hay un primer punto t a partir del cual los amigos siempre pueden encontrarse. Esto es porque… | `búsqueda binaria`, `Encuentro` | 42 |
| `79-conclusi-n.md` | Conclusi n (1/2: Conclusión) | La técnica de D&C permite resolver algunos problemas. La idea central es subdividir el problema en… | `Conclusión` | 38 |
| `80-conclusi-n.md` | Conclusi n (2/2: Conclusión) | La técnica de D&C permite resolver algunos problemas. La idea central es subdividir el problema en… | `Conclusión` | 36 |

## Mapa de conceptos

Concepto → archivos donde aparece definido o usado.

- **Algoritmo de Karatsuba** → `19-algoritmo-de-karatsuba.md`, `20-algoritmo-de-karatsuba.md`, `21-algoritmo-de-karatsuba.md`, `22-algoritmo-de-karatsuba.md`, `23-algoritmo-de-karatsuba.md`
- **Algoritmo de Strassen** → `38-algoritmo-de-strassen.md`, `39-algoritmo-de-strassen.md`, `41-algoritmo-de-strassen.md`
- **Algoritmo de Toom-Cook** → `34-el-algoritmo-de-karatsuba.md`, `35-el-algoritmo-de-karatsuba.md`, `36-el-algoritmo-de-karatsuba.md`, `37-el-algoritmo-de-karatsuba.md`
- **Autores Año Complejidad** → `44-el-algoritmo-de-strassen.md`
- **Búsqueda binaria** → `67-b-squeda-binaria.md`
- **Caso** → `24-el-teorema-maestro.md`, `25-el-teorema-maestro.md`
- **Combinar** → `07-ejemplo-de-d-c-merge-sort.md`
- **Como** → `26-el-teorema-maestro.md`
- **Complejidad** → `06-divide-conquer.md`, `57-m-ximo-subarreglo.md`, `76-encuentro.md`, `77-encuentro.md`
- **Conclusión** → `79-conclusi-n.md`, `80-conclusi-n.md`
- **Conquistar** → `07-ejemplo-de-d-c-merge-sort.md`
- **Consideremos** → `24-el-teorema-maestro.md`
- **Correctitud** → `06-divide-conquer.md`, `56-m-ximo-subarreglo.md`
- **Demostración** → `50-m-ximo-subarreglo.md`
- **Dividir** → `07-ejemplo-de-d-c-merge-sort.md`, `14-dividir.md`
- **El Teorema Maestro** → `24-el-teorema-maestro.md`, `25-el-teorema-maestro.md`, `26-el-teorema-maestro.md`, `27-el-teorema-maestro.md`
- **El algoritmo de Karatsuba** → `31-el-algoritmo-de-karatsuba.md`, `33-el-algoritmo-de-karatsuba.md`, `34-el-algoritmo-de-karatsuba.md`, `35-el-algoritmo-de-karatsuba.md`, `36-el-algoritmo-de-karatsuba.md`, `37-el-algoritmo-de-karatsuba.md`
- **El algoritmo de Strassen** → `40-el-algoritmo-de-strassen.md`, `42-el-algoritmo-de-strassen.md`, `43-el-algoritmo-de-strassen.md`, `44-el-algoritmo-de-strassen.md`
- **El método de sustitución** → `17-el-m-todo-de-sustituci-n.md`, `18-el-m-todo-de-sustituci-n.md`
- **Encuentro** → `69-encuentro.md`, `71-encuentro.md`, `73-encuentro.md`, `74-encuentro.md`, `75-encuentro.md`, `76-encuentro.md`, `77-encuentro.md`, `78-encuentro.md`
- **Izquierda** → `53-izquierda.md`
- **Mergesort de nuevo** → `32-mergesort-de-nuevo.md`
- **Más allá de búsqueda binaria** → `68-m-s-all-de-b-squeda-binaria.md`
- **Máximo subarreglo** → `50-m-ximo-subarreglo.md`, `51-m-ximo-subarreglo.md`, `52-m-ximo-subarreglo.md`, `54-m-ximo-subarreglo.md`, `55-m-ximo-subarreglo.md`, `56-m-ximo-subarreglo.md`, `57-m-ximo-subarreglo.md`, `58-m-ximo-subarreglo.md`, `59-m-ximo-subarreglo.md`, `60-m-ximo-subarreglo.md`, `61-m-ximo-subarreglo.md`, `62-m-ximo-subarreglo.md`, `63-m-ximo-subarreglo.md`, `64-m-ximo-subarreglo.md`, `65-m-ximo-subarreglo.md`, `66-m-ximo-subarreglo.md`
- **Método de sustitución** → `16-m-todo-de-sustituci-n.md`
- **Plan** → `02-plan.md`
- **Precondición** → `67-b-squeda-binaria.md`
- **Problema** → `70-problema.md`, `72-problema.md`
- **Prueba por inducción en** → `12-teorema.md`
- **Resultado** → `25-el-teorema-maestro.md`
- **Tarea** → `66-m-ximo-subarreglo.md`
- **Teorema** → `12-teorema.md`
- **Timba** → `45-timba.md`, `47-timba.md`, `49-timba.md`
- **Técnicas algorítmicas** → `04-t-cnicas-algor-tmicas.md`, `05-t-cnicas-algor-tmicas.md`
- **Unos comentarios interesantes** → `35-el-algoritmo-de-karatsuba.md`
- **búsqueda binaria** → `78-encuentro.md`
- **descomposición tensorial** → `43-el-algoritmo-de-strassen.md`, `44-el-algoritmo-de-strassen.md`
- **desde cada borde** → `60-m-ximo-subarreglo.md`
- **el mismo tamaño** → `05-t-cnicas-algor-tmicas.md`
- **else** → `09-ejemplo-de-d-c-merge-sort.md`
- **enfoques** → `03-t-cnicas-algor-tmicas.md`
- **para** → `06-divide-conquer.md`
- **patrones** → `03-t-cnicas-algor-tmicas.md`
- **patrón** → `13-ejemplo-de-d-c-merge-sort.md`
- **return** → `06-divide-conquer.md`, `08-ejemplo-de-d-c-merge-sort.md`, `56-m-ximo-subarreglo.md`, `67-b-squeda-binaria.md`
- **técnicas algorítmicas** → `03-t-cnicas-algor-tmicas.md`
- **while** → `09-ejemplo-de-d-c-merge-sort.md`
