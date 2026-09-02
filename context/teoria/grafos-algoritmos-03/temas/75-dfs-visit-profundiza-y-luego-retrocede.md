# DFS-VISIT profundiza y luego retrocede 

**Procedimiento** DFS **-** VISIT( _G, u_ ) 

_tiempo ← tiempo_ + 1 _d_ [ _u_ ] _← tiempo_ color[ _u_ ] _←_ gris **para cada** _v ∈_ Adj[ _u_ ] **hacer si** color[ _v_ ] = blanco **entonces** _π_ [ _v_ ] _← u_ DFS-VISIT( _G, v_ ) _tiempo ← tiempo_ + 1 _f_ [ _u_ ] _← tiempo_ color[ _u_ ] _←_ negro 

La llamada de _u_ queda suspendida mientras se explora recursivamente un vecino blanco. Solo finaliza cuando ya se examinaron todas las aristas que salen de _u_ . 

2<sup>_do_</sup> Cuatrimestre de 2026 34 / 58 

(DC, FCEyN, UBA) 

DC - FCEyN - UBA 

Ordenamiento topológico 

Búsqueda a lo ancho 

Búsqueda en profundidad 

Detección de aristas de corte 

Los grafos como modelos 

