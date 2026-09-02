# Los colores describen el estado de cada vértice 

Durante la ejecución, cada vértice se encuentra en uno de tres estados. 

Blanco: todavía no fue descubierto 


![](../imagenes/Graph_Algorithms.pdf-0030-08.png)



![](../imagenes/Graph_Algorithms.pdf-0030-09.png)


Su distancia es _d_ [ _v_ ] = _∞_ y su predecesor es _π_ [ _v_ ] = NIL. 


![](../imagenes/Graph_Algorithms.pdf-0030-11.png)


Gris: fue descubierto, pero no terminó de procesarse 


![](../imagenes/Graph_Algorithms.pdf-0030-13.png)



![](../imagenes/Graph_Algorithms.pdf-0030-14.png)


El vértice está en la cola. Es parte de la frontera entre los vértices descubiertos y los que todavía no fueron descubiertos. 


![](../imagenes/Graph_Algorithms.pdf-0030-16.png)


Negro: terminó de procesarse 


![](../imagenes/Graph_Algorithms.pdf-0030-18.png)



![](../imagenes/Graph_Algorithms.pdf-0030-19.png)


Toda su lista de adyacencia ya fue examinada. 


![](../imagenes/Graph_Algorithms.pdf-0030-21.png)


Al comienzo de cada iteración, la cola contiene exactamente los vértices grises. 

2<sup>_do_</sup> Cuatrimestre de 2026 

(DC, FCEyN, UBA) 

DC - FCEyN - UBA 

20 / 58 

Ordenamiento topológico 

Búsqueda a lo ancho 

Búsqueda en profundidad 

Detección de aristas de corte 

Los grafos como modelos 

