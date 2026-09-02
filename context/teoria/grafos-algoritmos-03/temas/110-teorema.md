## Teorema 


![](../imagenes/Graph_Algorithms.pdf-0086-07.png)



![](../imagenes/Graph_Algorithms.pdf-0086-08.png)


En una búsqueda en profundidad de un grafo no dirigido _G_ , toda arista es una arista de árbol o una arista de retroceso. 


![](../imagenes/Graph_Algorithms.pdf-0086-10.png)


**Idea de la demostración.** 

Sea _{u, v } ∈ E_ y supongamos _d_ [ _u_ ] _< d_ [ _v_ ]. 


![](../imagenes/Graph_Algorithms.pdf-0086-13.png)


Si la arista se examina primero desde _u_ , entonces _v_ todavía está blanco y la arista se incorpora al árbol. 


![](../imagenes/Graph_Algorithms.pdf-0086-15.png)


Si se examina primero desde _v_ , entonces _u_ todavía está gris y es un ancestro de _v_ ; la arista es de retroceso. 

Estas dos posibilidades agotan los casos. 

2<sup>_do_</sup> Cuatrimestre de 2026 46 / 58 

(DC, FCEyN, UBA) 

DC - FCEyN - UBA 

Ordenamiento topológico 

Búsqueda a lo ancho 

Búsqueda en profundidad 

Detección de aristas de corte 

Los grafos como modelos 



Para hallar los puentes alcanza con completar una única DFS 

Sea _G_ un grafo no dirigido y sea _T_ el bosque producido por DFS. toda arista que no pertenece a _T_ está contenida en un ciclo; por lo tanto, solamente las aristas de _T_ pueden ser puentes. 

2<sup>_do_</sup> Cuatrimestre de 2026 47 / 58 

(DC, FCEyN, UBA) 

DC - FCEyN - UBA 

Ordenamiento topológico 

Búsqueda a lo ancho 

Búsqueda en profundidad 

Detección de aristas de corte 

Los grafos como modelos 



Para hallar los puentes alcanza con completar una única DFS 

Sea _G_ un grafo no dirigido y sea _T_ el bosque producido por DFS. toda arista que no pertenece a _T_ está contenida en un ciclo; por lo tanto, solamente las aristas de _T_ pueden ser puentes. Cantidad de puentes Como todo puente pertenece al árbol DFS, #puentes _≤ n −_ 1. 


![](../imagenes/Graph_Algorithms.pdf-0088-08.png)



![](../imagenes/Graph_Algorithms.pdf-0088-09.png)


2<sup>_do_</sup> Cuatrimestre de 2026 47 / 58 

(DC, FCEyN, UBA) 

DC - FCEyN - UBA 

Ordenamiento topológico 

Búsqueda a lo ancho 

Búsqueda en profundidad 

Detección de aristas de corte 

Los grafos como modelos 

