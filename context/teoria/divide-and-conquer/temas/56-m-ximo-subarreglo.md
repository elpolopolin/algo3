## Máximo subarreglo 

Hacemos que los llamados recursivos devuelvan el valor máximo y también el intervalo que lo alcanza. 

MAX-SUBARRAY( _d, ℓ, r_ ) 


![](../imagenes/teo04-Divide_and_Conquer.pdf-0057-08.png)


**if** _ℓ_ = _r_ : **return** ([ _ℓ, ℓ_ ] _, dℓ_ ) _m ←⌊_ ( _ℓ_ + _r_ ) _/_ 2 _⌋ L ←_ MAX-SUBARRAY( _d, ℓ, m_ ) _R ←_ MAX-SUBARRAY( _d, m_ + 1 _, r_ ) _C ←_ MAX-CROSSING( _d, ℓ, m, r_ ) **return** el candidato de mayor suma entre _L, R, C_ 

**Correctitud** : por inducción, dado que solo hay 3 casos posibles (y tomamos el máximo entre los 3). 

TDA - Algo3 (DC, FCEyN, UBA) 

DC - FCEyN - UBA 

2do Cuatrimestre de 2026 43 / 55 

Divide & Conquer 

Algoritmo de Strassen 

Timba y máximo subarreglo 

Búsqueda y extensiones 

Algoritmo de Karatsuba 

