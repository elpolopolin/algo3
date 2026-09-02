## Búsqueda binaria 

La búsqueda binaria es un caso de D&C 

BINARY-SEARCH( _A, x, ℓ, r_ ) 


![](../imagenes/teo04-Divide_and_Conquer.pdf-0068-08.png)


**Precondición** : _A_ [ _ℓ_ : _r_ ] está ordenado **if** _ℓ> r_ : **return** NO-ESTÁ _m ←⌊_ ( _ℓ_ + _r_ ) _/_ 2 _⌋_ **if** _A_ [ _m_ ] = _x_ : **return** _m_ **if** _x < A_ [ _m_ ]: **return** BINARY-SEARCH( _A, x, ℓ, m −_ 1) **si no** : 

**return** BINARY-SEARCH( _A, x, m_ + 1 _, r_ ) 

La complejidad respeta una recursión de la forma 

_T_ ( _n_ ) _≤ T_ ( _n/_ 2) + Θ(1) 

y usando el Teorema Maestro se puede ver que esto es _O_ (log _n_ ). 

TDA - Algo3 (DC, FCEyN, UBA) 

2do Cuatrimestre de 2026 49 / 55 

DC - FCEyN - UBA 

Divide & Conquer 

Algoritmo de Strassen 

Timba y máximo subarreglo 

Búsqueda y extensiones 

Algoritmo de Karatsuba 

