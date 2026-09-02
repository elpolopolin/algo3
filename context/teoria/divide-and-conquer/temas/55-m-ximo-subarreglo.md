## Máximo subarreglo 

Para la parte de combinar, alcanza con observar que hay que maximizar para la izquierda y luego para la derecha: 


![](../imagenes/teo04-Divide_and_Conquer.pdf-0056-07.png)


<!-- Start of picture text -->
j<br>CRUZA( ℓ, m, r ) = max ∑︂ dk<br>ℓ≤i≤m<j≤r<br>k = i<br>m j<br>= max dk  + max dk.<br>∑︂ ∑︂<br>ℓ≤i≤m m<j≤r<br>k = i k = m +1<br><!-- End of picture text -->

En qué complejidad podemos calcular esto? En Θ( _r − ℓ_ ), es un recorrido manteniendo el mejor sufijo / prefijo. 

TDA - Algo3 (DC, FCEyN, UBA) 

DC - FCEyN - UBA 

2do Cuatrimestre de 2026 42 / 55 

Divide & Conquer 

Algoritmo de Strassen 

Timba y máximo subarreglo 

Búsqueda y extensiones 

Algoritmo de Karatsuba 

