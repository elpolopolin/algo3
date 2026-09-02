## Idea del algoritmo 


![](../imagenes/Graph_Algorithms.pdf-0090-17.png)



![](../imagenes/Graph_Algorithms.pdf-0090-18.png)


> 1 Durante una única DFS, calcular para cada vértice su tiempo de descubrimiento _d_ , su predecesor _π_ y un valor low ( _low_ ). 

> 2 Recorrer las aristas del bosque y decidir cuáles son puentes comparando low[ _v_ ] con _d_ [ _π_ [ _v_ ]]. 


![](../imagenes/Graph_Algorithms.pdf-0090-21.png)


El algoritmo también funciona si _G_ no es conexo: en ese caso, DFS produce un bosque en lugar de un único árbol. 

(DC, FCEyN, UBA) 

DC - FCEyN - UBA 

2<sup>_do_</sup> Cuatrimestre de 2026 47 / 58 

Ordenamiento topológico 

Búsqueda a lo ancho 

Búsqueda en profundidad 

Detección de aristas de corte 

Los grafos como modelos 

