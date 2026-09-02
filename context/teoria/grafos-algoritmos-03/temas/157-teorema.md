## Teorema 


![](../imagenes/Graph_Algorithms.pdf-0127-10.png)



![](../imagenes/Graph_Algorithms.pdf-0127-11.png)


Sea _G_ un grafo con _uv ∈ E_ ( _G_ ) y _π_ producido por el algoritmo DFS. Entonces, _uv_ es puente de _G_ , con _π_ [ _v_ ] = _u_ si y solo si low[ _v_ ] _> d_ [ _u_ ] 


![](../imagenes/Graph_Algorithms.pdf-0127-13.png)


DC - FCEyN - UBA 

2<sup>_do_</sup> Cuatrimestre de 2026 57 / 58 

(DC, FCEyN, UBA) 

Ordenamiento topológico 

Búsqueda a lo ancho 

Búsqueda en profundidad 

Detección de aristas de corte 

Los grafos como modelos 

El algoritmo encuentra todos los puentes en tiempo lineal 


![](../imagenes/Graph_Algorithms.pdf-0128-06.png)


La inicialización cuesta Θ( _|V |_ ). 


![](../imagenes/Graph_Algorithms.pdf-0128-08.png)


Cada vértice es descubierto una sola vez. 


![](../imagenes/Graph_Algorithms.pdf-0128-10.png)


Cada arista aparece dos veces en las listas de adyacencia y provoca solamente una cantidad constante de operaciones. 


![](../imagenes/Graph_Algorithms.pdf-0128-12.png)


La segunda fase recorre _V_ ( _G_ ) una vez. 

Por lo tanto, con listas de adyacencia, 

Θ( _|V |_ + _|E|_ ) _._ 

Se almacenan los arreglos color, _π_ , _d_ , _f_ y low, además de la pila de recursión y la salida. El espacio adicional es 

_O_ ( _|V |_ ) 

sin contar la representación del grafo ni la lista de puentes devuelta. 

2<sup>_do_</sup> Cuatrimestre de 2026 

(DC, FCEyN, UBA) 

DC - FCEyN - UBA 

58 / 58 

