## Lema 


![](../imagenes/Graph_Algorithms.pdf-0044-07.png)



![](../imagenes/Graph_Algorithms.pdf-0044-08.png)


Al terminar BFS, para todo _v ∈ V_ ( _G_ ), 

_d_ [ _v_ ] _≥ δ_ ( _s, v_ ) _._ 


![](../imagenes/Graph_Algorithms.pdf-0044-11.png)


**Demostración.** El único valor finito inicial es _d_ [ _s_ ] = 0. Cuando _v_ es descubierto desde _u_ , el algoritmo asigna 

_π_ [ _v_ ] = _u, d_ [ _v_ ] = _d_ [ _u_ ] + 1 _._ 

Sale por inducción sobre el número de descubrimientos (número de llamadas a ENCOLAR), los predecesores determinan un camino de _s_ a _v_ de longitud _d_ [ _v_ ]. Como _δ_ ( _s, v_ ) es la longitud mínima de un camino de _s_ a _v_ , 

_δ_ ( _s, v_ ) _≤ d_ [ _v_ ] _._ 

Falta probar que BFS no encuentra un camino más largo que el mínimo. 

2<sup>_do_</sup> Cuatrimestre de 2026 

(DC, FCEyN, UBA) 

DC - FCEyN - UBA 

24 / 58 

Ordenamiento topológico 

Búsqueda a lo ancho 

Búsqueda en profundidad 

Detección de aristas de corte 

Los grafos como modelos 



