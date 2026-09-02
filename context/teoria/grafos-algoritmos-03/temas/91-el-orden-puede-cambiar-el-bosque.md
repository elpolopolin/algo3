# El orden puede cambiar el bosque 

La salida concreta de DFS puede depender de dos decisiones: 


![](../imagenes/Graph_Algorithms.pdf-0074-07.png)


el orden en que el bucle exterior considera los vértices; 


![](../imagenes/Graph_Algorithms.pdf-0074-09.png)


el orden de los vértices en cada lista de adyacencia. 

Esos órdenes pueden modificar las raíces, las aristas del bosque y los tiempos _d_ y _f_ . 

Tiempo de ejecución con listas de adyacencia 


![](../imagenes/Graph_Algorithms.pdf-0074-13.png)



![](../imagenes/Graph_Algorithms.pdf-0074-14.png)


La inicialización y el bucle exterior cuestan Θ( _|V |_ ). 

DFS-VISIT se llama exactamente una vez por vértice y, en total, el bucle recorre todas las aristas una vez 

∑︂ _|_ Adj[ _u_ ] _|_ = Θ( _|E|_ ) _. u∈V_ 

Por lo tanto, el tiempo total es 

Θ( _|V |_ + _|E|_ ) _._ 


![](../imagenes/Graph_Algorithms.pdf-0074-20.png)


2<sup>_do_</sup> Cuatrimestre de 2026 

(DC, FCEyN, UBA) 

DC - FCEyN - UBA 

38 / 58 

Ordenamiento topológico 

Búsqueda a lo ancho 

Búsqueda en profundidad 

Detección de aristas de corte 

Los grafos como modelos 

