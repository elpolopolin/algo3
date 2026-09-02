# Una cola mantiene los vértices disponibles 

##### **ORDEN-TOPOLÓGICO** ( _D_ ) 

##### **Inicialización** 

##### **Construcción del orden** 

- 1 _n ←|V_ ( _D_ ) _| L ←⟨⟩_ 

- 2 **computar** entrada[ _v_ ] = _d_<sup>_−_</sup> ( _v_ ) **para todo** _v ∈ V_ ( _D_ ) 

- 3 _Q ←_ cola vacía 

- 4 **para todo** _v ∈ V_ ( _D_ ) **hacer** 5 **si** entrada[ _v_ ] = 0 **entonces** 6 ENCOLAR( _Q, v_ ) 

- 7 **mientras** _Q̸_ = ∅ **hacer** 

- 8 _u ←_ DESENCOLAR( _Q_ ) 

- 9 agregar _u_ al final de _L_ 

- 10 **para todo** _v ∈ N_<sup>+</sup> ( _u_ ) **hacer** 

- 11 entrada[ _v_ ] _←_ entrada[ _v_ ] _−_ 1 12 **si** entrada[ _v_ ] = 0 **entonces** 13 ENCOLAR( _Q, v_ ) 

- 14 **si** _|L| < n_ **entonces** 15 **devolver** “ _D_ tiene un ciclo” 

- 16 **devolver** _L_ 

Cada vértice se encola una sola vez y cada arista se procesa una sola vez. 

2<sup>_do_</sup> Cuatrimestre de 2026 15 / 58 

(DC, FCEyN, UBA) 

DC - FCEyN - UBA 

Ordenamiento topológico 

Búsqueda a lo ancho 

Búsqueda en profundidad 

Detección de aristas de corte 

Los grafos como modelos 

