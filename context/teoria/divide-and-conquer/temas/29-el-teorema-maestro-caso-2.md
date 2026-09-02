## El Teorema Maestro: Caso 2 

Supongamos _f_ ( _n_ ) = Θ( _n_<sup>_q_</sup> log<sup>_r_</sup> _n_ ), con _r ≥_ 0. En el nivel _i_ : _a_<sup>_i_</sup> _f_ ( _n/b_<sup>_i_</sup> ) = Θ(︁ _a_<sup>_i_</sup> ( _n/b_<sup>_i_</sup> )<sup>_q_</sup> log<sup>_r_</sup> ( _n/b_<sup>_i_</sup> ))︁ = Θ( _n_<sup>_q_</sup> ( _L − i_ )<sup>_r_</sup> ) _,_ 

pues _a_ = _b_<sup>_q_</sup> y log( _n/b_<sup>_i_</sup> ) = Θ( _L − i_ ). Entonces 

Como _L_ = Θ(log _n_ ), 


![](../imagenes/teo04-Divide_and_Conquer.pdf-0029-09.png)


<!-- Start of picture text -->
L− 1 L<br>∑︂ a i f ( n/b i ) = Θ n q ∑︂ s r<br>i =0 (︄ s =1 )︄<br>= Θ( n q L r +1 ) .<br>T ( n ) = Θ( n q log r +1 n ) .<br><!-- End of picture text -->

TDA - Algo3 (DC, FCEyN, UBA) 

DC - FCEyN - UBA 

2do Cuatrimestre de 2026 

26 / 55 

Divide & Conquer 

Algoritmo de Strassen 

Timba y máximo subarreglo 

Búsqueda y extensiones 

Algoritmo de Karatsuba 

