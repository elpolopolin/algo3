# DFS-PUENTES-VISIT calcula low al retroceder 

**Procedimiento** DFS **-** PUENTES **-** VISIT( _G, u_ ) 

_tiempo ← tiempo_ + 1 _d_ [ _u_ ] _← tiempo_ low[ _u_ ] _← d_ [ _u_ ] color[ _u_ ] _←_ gris **para cada** _v ∈_ Adj[ _u_ ] **hacer si** color[ _v_ ] = blanco **entonces** _π_ [ _v_ ] _← u_ DFS-PUENTES-VISIT( _G, v_ ) low[ _u_ ] _←_ m´ın _{_ low[ _u_ ] _,_ low[ _v_ ] _}_ **si no, si** color[ _v_ ] = gris **y** _v̸_ = _π_ [ _u_ ] **entonces** low[ _u_ ] _←_ m´ın _{_ low[ _u_ ] _, d_ [ _v_ ] _}_ 

_tiempo ← tiempo_ + 1 _f_ [ _u_ ] _← tiempo_ color[ _u_ ] _←_ negro 

La condición _v̸_ = _π_ [ _u_ ] evita considerar como arista de retroceso la copia de la arista del árbol que lleva de _u_ a su padre. 

2<sup>_do_</sup> Cuatrimestre de 2026 54 / 58 

(DC, FCEyN, UBA) 

DC - FCEyN - UBA 

Ordenamiento topológico 

Búsqueda a lo ancho 

Búsqueda en profundidad 

Detección de aristas de corte 

Los grafos como modelos 

