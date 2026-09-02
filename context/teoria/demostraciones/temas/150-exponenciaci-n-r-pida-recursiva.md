# Exponenciación rápida, recursiva 

Sean _a ∈_ N y _n ∈_ N. 

**procedure** Exp( _a, n_ ) **if** _n_ = 0 **then return** 1 _b ←_ Exp( _a, ⌊_<sup>_<u>n</u>_</sup> 2<sup>_⌋_) ;</sup> _c ← b_<sup>2</sup> ; **if** _n_ m´od 2 = 1 **then** _c ← c × a_ **return** _c_ 

¿En qué hacemos inducción? La llamada recursiva es con _⌊_<sup>_<u>n</u>_</sup> 2<sup>_⌋< n_(para</sup><sup>_n ≥_1):</sup> inducción fuerte en _n_ , el exponente. 

2<sup>_do_</sup> Cuatrimestre de 2026 27 / 36 

(DC, FCEyN, UBA) 

DC - FCEyN - UBA 

¿Qué es una demostración? 

Complejidad asintótica 

Otras herramientas 

Para Cerrar 

Inducción 

Algoritmos recursivos 

¿Cómo demostramos? 

