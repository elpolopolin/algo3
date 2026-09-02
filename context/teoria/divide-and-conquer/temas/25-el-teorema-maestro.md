## El Teorema Maestro 

**Caso** Hipótesis 

### Resultado 

**1** Si _f_ ( _n_ ) = _O_ ( _n_<sup>_q−ε_</sup> ), luego _T_ ( _n_ ) = Θ( _n_<sup>_q_</sup> ) **2** Si _f_ ( _n_ ) = Θ( _n_<sup>_q_</sup> log<sup>_r_</sup> _n_ ) con _r ≥_ 0, _T_ ( _n_ ) = Θ( _n_<sup>_q_</sup> log<sup>_r_+1</sup> _n_ ) **3** _f_ ( _n_ ) = Ω( _n_<sup>_q_+</sup><sup>_ε_</sup> ) y _af_ ( _n/b_ ) _≤ cf_ ( _n_ ) para al- _T_ ( _n_ ) = Θ( _f_ ( _n_ )) gún 0 _< c <_ 1, eventualmente 

Como vamos a ver más adelante, el caso 1 se corresponde con la situación en la que la mayoría del trabajo se hace en las recursiones. El caso 3 se corresponde con la situación en que la mayoría del trabajo se hace en el primer piso. Finalmente, el caso 2 se cumple cuando ambos costos son similares. 

TDA - Algo3 (DC, FCEyN, UBA) 

DC - FCEyN - UBA 

2do Cuatrimestre de 2026 22 / 55 

Divide & Conquer 

Algoritmo de Strassen 

Timba y máximo subarreglo 

Búsqueda y extensiones 

Algoritmo de Karatsuba 

