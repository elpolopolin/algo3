# BFS utiliza una cola para administrar la frontera 

**Función** BFS( _G, s_ ) 

**para cada** _u ∈ V_ ( _G_ ) _\ {s}_ **hacer** color[ _u_ ] _←_ blanco _d_ [ _u_ ] _←∞_ , _π_ [ _u_ ] _←_ NIL color[ _s_ ] _←_ gris _d_ [ _s_ ] _←_ 0, _π_ [ _s_ ] _←_ NIL _Q ←_ cola vacía; ENCOLAR( _Q, s_ ) **mientras** _Q̸_ = ∅ **hacer** _u ←_ DESENCOLAR( _Q_ ) **para cada** _v ∈_ Adj[ _u_ ] **hacer si** color[ _v_ ] = blanco **entonces** color[ _v_ ] _←_ gris _d_ [ _v_ ] _← d_ [ _u_ ] + 1, _π_ [ _v_ ] _← u_ ENCOLAR( _Q, v_ ) color[ _u_ ] _←_ negro 

**devolver** _d, π_ 

(DC, FCEyN, UBA) 

DC - FCEyN - UBA 

2<sup>_do_</sup> Cuatrimestre de 2026 21 / 58 

Ordenamiento topológico 

Búsqueda a lo ancho 

Búsqueda en profundidad 

Detección de aristas de corte 

Los grafos como modelos 

