## El Teorema Maestro 

### Consideremos 

_T_ ( _n_ ) = _aT_ ( _n/b_ ) + _f_ ( _n_ ) _,_ 

donde _a ≥_ 1, _b >_ 1, _T_ (1) = Θ(1) y _f_ es eventualmente no negativa. Sea _q_ = log _b a_ . El teorema maestro dice que, dado _ε >_ 0, 

**Caso** Hipótesis Resultado **1** Si _f_ ( _n_ ) = _O_ ( _n_<sup>_q−ε_</sup> ) _T_ ( _n_ ) = Θ( _n_<sup>_q_</sup> ) **2** Si _f_ ( _n_ ) = Θ( _n_<sup>_q_</sup> log<sup>_r_</sup> _n_ ) con _r ≥_ 0, _T_ ( _n_ ) = Θ( _n_<sup>_q_</sup> log<sup>_r_+1</sup> _n_ ) **3** Si _f_ ( _n_ ) = Ω( _n_<sup>_q_+</sup><sup>_ε_</sup> ) y _af_ ( _n/b_ ) _≤ cf_ ( _n_ ) para algún _T_ ( _n_ ) = Θ( _f_ ( _n_ )) 0 _< c <_ 1, eventualmente 

TDA - Algo3 (DC, FCEyN, UBA) 

DC - FCEyN - UBA 

2do Cuatrimestre de 2026 

21 / 55 

Divide & Conquer 

Algoritmo de Strassen 

Timba y máximo subarreglo 

Búsqueda y extensiones 

Algoritmo de Karatsuba 

