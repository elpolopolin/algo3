# DFS avanza mientras encuentra vértices no descubiertos 

La búsqueda en profundidad (DFS) explora las aristas que salen del vértice **descubierto más recientemente** que todavía tiene aristas sin examinar. 


![](../imagenes/Graph_Algorithms.pdf-0053-07.png)


<!-- Start of picture text -->
Si puede avanzar: visita<br>v w recursivamente un vecino<br>blanco.<br>u x<br>Si no puede avanzar:<br>retrocede al vértice des-<br>z y<br>de el cual llegó.<br><!-- End of picture text -->

Cuando termina de explorar lo alcanzable desde una fuente, el algoritmo elige otro vértice no descubierto. Por eso, en general, produce un **bosque** y no un único árbol. 

2<sup>_do_</sup> Cuatrimestre de 2026 29 / 58 

(DC, FCEyN, UBA) 

DC - FCEyN - UBA 

Ordenamiento topológico 

Búsqueda a lo ancho 

Búsqueda en profundidad 

Detección de aristas de corte 

Los grafos como modelos 

