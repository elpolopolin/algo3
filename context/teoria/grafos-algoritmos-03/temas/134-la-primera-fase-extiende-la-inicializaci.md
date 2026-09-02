# La primera fase extiende la inicialización de DFS 

**Procedimiento** PUENTES( _G_ ) 

**para cada** _u ∈ V_ ( _G_ ) **hacer** color[ _u_ ] _←_ blanco _π_ [ _u_ ] _←_ NIL _d_ [ _u_ ] _←∞_ low[ _u_ ] _←∞ tiempo ←_ 0 

**para cada** _u ∈ V_ ( _G_ ) **hacer si** color[ _u_ ] = blanco **entonces** DFS-PUENTES-VISIT( _G, u_ ) 

Al terminar esta fase, _d_ , low y _π_ están definidos para todos los vértices. La segunda fase solamente inspeccionará las aristas _{π_ [ _v_ ] _, v }_ del bosque DFS. 

2<sup>_do_</sup> Cuatrimestre de 2026 53 / 58 

(DC, FCEyN, UBA) 

DC - FCEyN - UBA 

Ordenamiento topológico 

Búsqueda a lo ancho 

Búsqueda en profundidad 

Detección de aristas de corte 

Los grafos como modelos 

