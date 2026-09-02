## Teorema de los paréntesis 


![](../imagenes/Graph_Algorithms.pdf-0077-07.png)



![](../imagenes/Graph_Algorithms.pdf-0077-08.png)


Para cualesquiera _u, v ∈ V_ , ocurre exactamente una de las siguientes posibilidades: 1 _I_ ( _u_ ) _∩ I_ ( _v_ ) = ∅, y ninguno es descendiente del otro; 2 _I_ ( _u_ ) _⊂ I_ ( _v_ ), y _u_ es descendiente de _v_ ; 3 _I_ ( _v_ ) _⊂ I_ ( _u_ ), y _v_ es descendiente de _u_ . 


![](../imagenes/Graph_Algorithms.pdf-0077-10.png)


#### **Idea de la demostración.** 

Supongamos _d_ [ _u_ ] _< d_ [ _v_ ]. Si _v_ se descubre antes de que termine _u_ , entonces _u_ está gris: la exploración de _v_ se completa antes de regresar a _u_ , y _I_ ( _v_ ) _⊂ I_ ( _u_ ). Si _u_ ya había terminado, entonces _f_ [ _u_ ] _< d_ [ _v_ ], y los intervalos son disjuntos. 

**Dos intervalos nunca se superponen parcialmente.** 

2<sup>_do_</sup> Cuatrimestre de 2026 40 / 58 

(DC, FCEyN, UBA) 

DC - FCEyN - UBA 

Ordenamiento topológico 

Búsqueda a lo ancho 

Búsqueda en profundidad 

Detección de aristas de corte 

Los grafos como modelos 

