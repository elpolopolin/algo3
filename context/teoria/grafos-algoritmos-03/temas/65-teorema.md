## Teorema 


![](../imagenes/Graph_Algorithms.pdf-0050-07.png)



![](../imagenes/Graph_Algorithms.pdf-0050-08.png)


Para todo _v ∈ V_ ( _G_ ), al terminar BFS, _d_ [ _v_ ] = _δ_ ( _s, v_ ). Además, para todo vértice _v̸_ = _s_ alcanzable desde _s_ , un camino mínimo de _s_ a _v_ se obtiene tomando un camino mínimo de _s_ a _π_ [ _v_ ] y agregando la arista 

( _π_ [ _v_ ] _, v_ ) _._ 


![](../imagenes/Graph_Algorithms.pdf-0050-11.png)


**Idea de la demostración.** Supongamos que la igualdad falla y elijamos un vértice _v_ con _δ_ ( _s, v_ ) mínima entre los que tienen un valor incorrecto. 

El preprocesamiento toma _O_ ( _n_ ). Con listas de adyacencia, cada vértice se encola a lo sumo una vez y cada lista se examina a lo sumo una vez. Así que la complejidad es _O_ ( _n_ ) + _O_ (<sup>∑︁</sup> _v ∈V_ ( _G_ )<sup>_d_(</sup><sup>_v_)) =</sup><sup>_O_(</sup><sup>_n_+ 2</sup><sup>_m_) =</sup><sup>_O_(</sup><sup>_n_+</sup><sup>_m_).</sup> 

2<sup>_do_</sup> Cuatrimestre de 2026 

(DC, FCEyN, UBA) 

DC - FCEyN - UBA 

26 / 58 

Ordenamiento topológico 

Búsqueda a lo ancho 

Búsqueda en profundidad 

Detección de aristas de corte 

Los grafos como modelos 

