# La matriz reserva una posición para cada par de vértices 


![](../imagenes/Graph_Algorithms.pdf-0009-06.png)



![](../imagenes/Graph_Algorithms.pdf-0009-07.png)



![](../imagenes/Graph_Algorithms.pdf-0009-08.png)



![](../imagenes/Graph_Algorithms.pdf-0009-09.png)


1 _,_ si _vw ∈ E, A_ [ _v , w_ ] = {︄0 _,_ si _vw ∈/ E._ Espacio: Θ( _n_<sup>2</sup> ). Consultar _vw ∈ E_ : _O_ (1). Recorrer _N_ ( _v_ ): _O_ ( _n_ ). Si _G_ es no dirigido, _A_ = _A_<sup>T</sup> . 

0 1 2 3 4 0 0 **1** 0 0 **1** 1 **1** 0 **1 1 1** 2 0 **1** 0 **1** 0 3 0 **1 1** 0 **1** 4 **1 1** 0 **1** 0 

La fila _v_ codifica _N_ ( _v_ ). 

2<sup>_do_</sup> Cuatrimestre de 2026 9 / 58 

(DC, FCEyN, UBA) 

DC - FCEyN - UBA 

Ordenamiento topológico 

Búsqueda a lo ancho 

Búsqueda en profundidad 

Detección de aristas de corte 

Los grafos como modelos 

