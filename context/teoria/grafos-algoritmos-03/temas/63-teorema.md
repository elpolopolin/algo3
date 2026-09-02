## Teorema 


![](../imagenes/Graph_Algorithms.pdf-0049-07.png)



![](../imagenes/Graph_Algorithms.pdf-0049-08.png)


Para todo _v ∈ V_ ( _G_ ), al terminar BFS, _d_ [ _v_ ] = _δ_ ( _s, v_ ). Además, para todo vértice _v̸_ = _s_ alcanzable desde _s_ , un camino mínimo de _s_ a _v_ se obtiene tomando un camino mínimo de _s_ a _π_ [ _v_ ] y agregando la arista 

( _π_ [ _v_ ] _, v_ ) _._ 


![](../imagenes/Graph_Algorithms.pdf-0049-11.png)


**Idea de la demostración.** Supongamos que la igualdad falla y elijamos un vértice _v_ con _δ_ ( _s, v_ ) mínima entre los que tienen un valor incorrecto. 

2<sup>_do_</sup> Cuatrimestre de 2026 26 / 58 

(DC, FCEyN, UBA) 

DC - FCEyN - UBA 

Ordenamiento topológico 

Búsqueda a lo ancho 

Búsqueda en profundidad 

Detección de aristas de corte 

Los grafos como modelos 

