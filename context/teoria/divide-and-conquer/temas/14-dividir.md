## Dividir 


![](../imagenes/teo04-Divide_and_Conquer.pdf-0014-08.png)


Calcular el punto medio cuesta Θ(1). 

Conquistar Combinar Hay dos llamadas sobre MERGE toma Θ( _n_ ). instancias de tamaño _n/_ 2. 

Luego, la complejidad de MERGESORT satisface la siguiente recurrencia<sup>2</sup> 

_T_ ( _n_ ) = 2 _T_ ( _n/_ 2) + Θ( _n_ ) _, T_ (1) = Θ(1) _._ 

Cómo encontramos una cota fina a esta complejidad? 

> 2En realidad deberíamos usar _⌊n/_ 2 _⌋_ y _⌈n/_ 2 _⌉_ , pero en este caso (y en la mayoría de los de la materia) es irrelevante en términos de complejidad de peor caso. 

TDA - Algo3 (DC, FCEyN, UBA) 

DC - FCEyN - UBA 

2do Cuatrimestre de 2026 13 / 55 

Divide & Conquer 

Algoritmo de Strassen 

Timba y máximo subarreglo 

Búsqueda y extensiones 

Algoritmo de Karatsuba 

