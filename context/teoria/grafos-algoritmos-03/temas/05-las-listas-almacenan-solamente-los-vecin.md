# Las listas almacenan solamente los vecinos existentes 


![](../imagenes/Graph_Algorithms.pdf-0006-06.png)


<!-- Start of picture text -->
0 1 4<br>1 0 2 3 4<br>2 1 3<br>3 1 2 4<br>4 0 1 3<br><!-- End of picture text -->


![](../imagenes/Graph_Algorithms.pdf-0006-07.png)



![](../imagenes/Graph_Algorithms.pdf-0006-08.png)


Adj[ _v_ ] = _N_ ( _v_ ) _._ 

Hay una lista enlazada por vértice. 

En un digrafo se guardan, usualmente, los vecinos de salida: 

_N_<sup>+</sup> ( _v_ ) = _{w_ : _v → w ∈ E}._ 


![](../imagenes/Graph_Algorithms.pdf-0006-13.png)


El orden de los vecinos no está determinado por el grafo. 

2<sup>_do_</sup> Cuatrimestre de 2026 6 / 58 

(DC, FCEyN, UBA) 

DC - FCEyN - UBA 

Ordenamiento topológico 

Búsqueda a lo ancho 

Búsqueda en profundidad 

Detección de aristas de corte 

Los grafos como modelos 

