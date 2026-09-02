## Lema 

PRINT-PATH( _G, s, v_ ) 


![](../imagenes/Graph_Algorithms.pdf-0051-15.png)



![](../imagenes/Graph_Algorithms.pdf-0051-16.png)



![](../imagenes/Graph_Algorithms.pdf-0051-17.png)



![](../imagenes/Graph_Algorithms.pdf-0051-18.png)


El subgrafo de predecesores _Gπ_ es un árbol BFS con raíz _s_ . Para todo vértice _v_ alcanzable desde _s_ , el único camino simple de _s_ a _v_ en _Gπ_ es un camino mínimo en _G_ , y su longitud es _d_ [ _v_ ] = _δ_ ( _s, v_ ). 

**si** _v_ = _s_ **entonces** IMPRIMIR( _s_ ) **sino, si** _π_ [ _v_ ] = NIL **entonces** IMPRIMIR(︁“no existe camino”)︁ 


![](../imagenes/Graph_Algorithms.pdf-0051-21.png)


**sino** 

PRINT-PATH( _G, s, π_ [ _v_ ]) IMPRIMIR( _v_ ) 


![](../imagenes/Graph_Algorithms.pdf-0051-24.png)


2<sup>_do_</sup> Cuatrimestre de 2026 

(DC, FCEyN, UBA) 

DC - FCEyN - UBA 

27 / 58 

Ordenamiento topológico 

Búsqueda a lo ancho 

Búsqueda en profundidad 

Detección de aristas de corte 

Los grafos como modelos 

