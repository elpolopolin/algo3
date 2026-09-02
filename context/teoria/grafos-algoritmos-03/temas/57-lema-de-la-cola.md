## Lema de la cola 


![](../imagenes/Graph_Algorithms.pdf-0046-08.png)



![](../imagenes/Graph_Algorithms.pdf-0046-09.png)


Si _Q_ = _⟨v_ 1 _, v_ 2 _, . . . , vr ⟩_ , entonces _d_ [ _v_ 1] _≤ d_ [ _v_ 2] _≤· · · ≤ d_ [ _vr_ ] _≤ d_ [ _v_ 1] + 1 _._ 


![](../imagenes/Graph_Algorithms.pdf-0046-11.png)


**Idea de la demostración.** Se usa inducción sobre las operaciones realizadas sobre _Q_ . Al comienzo, _Q_ = _⟨s⟩_ , y la propiedad es inmediata. 


![](../imagenes/Graph_Algorithms.pdf-0046-13.png)


Al desencolar _v_ 1, el nuevo primer elemento _v_ 2 satisface _d_ [ _v_ 2] _≥ d_ [ _v_ 1]; las desigualdades se conservan. 


![](../imagenes/Graph_Algorithms.pdf-0046-15.png)


Si _v_ se descubre al procesar _u_ , entonces _d_ [ _v_ ] = _d_ [ _u_ ] + 1. Al agregarlo al final, queda detrás de vértices con distancia _d_ [ _u_ ] o _d_ [ _u_ ] + 1. 

2<sup>_do_</sup> Cuatrimestre de 2026 25 / 58 

(DC, FCEyN, UBA) 

DC - FCEyN - UBA 

Ordenamiento topológico 

Búsqueda a lo ancho 

Búsqueda en profundidad 

Detección de aristas de corte 

Los grafos como modelos 

