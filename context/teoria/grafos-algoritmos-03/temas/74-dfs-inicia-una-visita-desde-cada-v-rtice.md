# DFS inicia una visita desde cada vértice que sigue blanco 

**Procedimiento** DFS( _G_ ) 

**para cada** _u ∈ V_ ( _G_ ) **hacer** color[ _u_ ] _←_ blanco _π_ [ _u_ ] _←_ NIL _tiempo ←_ 0 

**para cada** _u ∈ V_ ( _G_ ) **hacer si** color[ _u_ ] = blanco **entonces** DFS-VISIT( _G, u_ ) 

La primera iteración inicializa todos los vértices. La segunda recorre _V_ ( _G_ ): cada llamada realizada allí crea un nuevo árbol del bosque DFS. 

2<sup>_do_</sup> Cuatrimestre de 2026 33 / 58 

(DC, FCEyN, UBA) 

DC - FCEyN - UBA 

Ordenamiento topológico 

Búsqueda a lo ancho 

Búsqueda en profundidad 

Detección de aristas de corte 

Los grafos como modelos 

