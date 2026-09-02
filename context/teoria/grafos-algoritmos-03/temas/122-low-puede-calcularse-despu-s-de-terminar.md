# low puede calcularse después de terminar DFS 

Una vez conocidos el bosque DFS _T_ , los tiempos _d_ y los predecesores _π_ , ejecutamos: **Procedimiento** CALCULAR **-** LOW **-** OFFLINE( _G, T , d, π_ ) 

**para cada** _u ∈ V_ ( _G_ ) **hacer** low[ _u_ ] _← d_ [ _u_ ] **para cada** _{u, v } ∈ E_ ( _G_ ) _\ E_ ( _T_ ), con _v_ ancestro de _u_ , **hacer** low[ _u_ ] _←_ m´ın _{_ low[ _u_ ] _, d_ [ _v_ ] _}_ **para cada** _u ∈ V_ ( _G_ ) **en postorden de** _T_ **hacer si** _π_ [ _u_ ] _̸_ = NIL **entonces** low[ _π_ [ _u_ ]] _←_ m´ın _{_ low[ _π_ [ _u_ ]] _,_ low[ _u_ ] _}_ **retornar** low 

El postorden garantiza que, cuando se procesa _u_ , los valores de todos sus hijos ya fueron calculados. La complejidad es _O_ ( _n_ + _m_ ). 

2<sup>_do_</sup> Cuatrimestre de 2026 51 / 58 

(DC, FCEyN, UBA) 

DC - FCEyN - UBA 

Ordenamiento topológico 

Búsqueda a lo ancho 

Búsqueda en profundidad 

Detección de aristas de corte 

Los grafos como modelos 

