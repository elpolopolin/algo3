## Subgrafo de predecesores 


![](../imagenes/Graph_Algorithms.pdf-0051-07.png)



![](../imagenes/Graph_Algorithms.pdf-0051-08.png)


Después de ejecutar BFS( _G, s_ ), definimos _Gπ_ = ( _Vπ, Eπ_ ), donde 

_Vπ_ = _{s} ∪{v ∈ V_ : _π_ [ _v_ ] _̸_ = NIL _}, Eπ_ = _{_ ( _π_ [ _v_ ] _, v_ ) : _v ∈ Vπ \ {s}}._ 

Un **árbol BFS con raíz** _s_ contiene exactamente los vértices alcanzables desde _s_ , y el camino del árbol de _s_ a cada uno de ellos es un camino mínimo en _G_ . 


![](../imagenes/Graph_Algorithms.pdf-0051-12.png)


