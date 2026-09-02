## Ejemplo de D&C: Merge sort 

Siendo más precisos, vamos a diseñar un algoritmo MERGESORT( _A, l, r_ ) que recibe un arreglo _A_ y dos índices _l, r_ con _l ≤ r_ que ordena el subarreglo _A_ [ _l_ : _r_ ]. Con esta notación, siguiendo la idea de la slide anterior el algoritmo es 

MERGESORT( _A, l, r_ ) 


![](../imagenes/teo04-Divide_and_Conquer.pdf-0009-08.png)


**if** _l_ = _r_ 

**return** 

_q ←⌊_ ( _p_ + _r_ ) _/_ 2 _⌋_ MERGESORT( _A, l, q_ ) MERGESORT( _A, l_ + 1 _, r_ ) MERGE( _A, l, q, r_ ) 

**return** 

Cómo se hace el MERGE al en la última línea? 

2do Cuatrimestre de 2026 8 / 55 

TDA - Algo3 (DC, FCEyN, UBA) 

DC - FCEyN - UBA 

Divide & Conquer 

Algoritmo de Strassen 

Timba y máximo subarreglo 

Búsqueda y extensiones 

Algoritmo de Karatsuba 

