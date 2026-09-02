# low[ _u_ ] indica hasta dónde puede volver el subárbol de _u_ 

Definimos low[ _u_ ] como el menor tiempo de descubrimiento de un vértice al que se puede llegar desde _u_ : 

bajando cero o más aristas del árbol DFS; y luego usando, a lo sumo, una arista que no pertenece al árbol. Más precisamente, 

⎧ _d_ [ _u_ ] _,_ low[ _u_ ] = m´ın _d_ [ _v_ ] : _{u, v }_ es una arista de retroceso y _v_ es ancestro de _u,_ ⎨ ⎩ low[ _w_ ] : _π_ [ _w_ ] = _u_ 

⎫ ⎬ ⎭<sup>_._</sup> 

2<sup>_do_</sup> Cuatrimestre de 2026 

49 / 58 

(DC, FCEyN, UBA) 

DC - FCEyN - UBA 

Ordenamiento topológico 

Búsqueda a lo ancho 

Búsqueda en profundidad 

Detección de aristas de corte 

Los grafos como modelos 

