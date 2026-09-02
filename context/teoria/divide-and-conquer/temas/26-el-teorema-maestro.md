## El Teorema Maestro 

Supongamos que _n_ es potencia de _b_ (y entonces siempre se parte bien<sup>5</sup> ). Tras _j_ niveles, 

_j−_ 1 _T_ ( _n_ ) = _a_<sup>_j_</sup> _T_ ( _n/b_<sup>_j_</sup> ) + ∑︂ _a_<sup>_i_</sup> _f_ ( _n/b_<sup>_i_</sup> ) _. i_ =0 

Sea _L_ = log _b n_ . Al llegar a los casos base: 

#### Como 


![](../imagenes/teo04-Divide_and_Conquer.pdf-0026-10.png)


<!-- Start of picture text -->
L− 1<br>T ( n ) =  a ⏞ L ⏟⏟ T (1)⏞ + ∑ i =0 a i f ( n/b i ) .<br>hojas ⏞ ⏟⏟ ⏞<br>niveles internos<br>a L =  a log b n =  n log b a =  n q ,<br><!-- End of picture text -->

<u>las hojas cuestan Θ(</u> _<u>n</u>_<sup>_q_</sup> <u>), y el nivel</u> _<u>i</u>_ <u>cuesta</u> _a_<sup>_i_</sup> _f_ ( _n/b_<sup>_i_</sup> ). 

5El caso más general es similar, y se puede reducir a este ya que las diferencias se las come la complejidad asintótica) 

TDA - Algo3 (DC, FCEyN, UBA) 

DC - FCEyN - UBA 

2do Cuatrimestre de 2026 23 / 55 

Divide & Conquer 

Algoritmo de Strassen 

Timba y máximo subarreglo 

Búsqueda y extensiones 

Algoritmo de Karatsuba 

