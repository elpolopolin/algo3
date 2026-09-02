## Timba 

Vamos a usar una estrategia muy útil para resolver problemas: reducirlo a otro (que con un poco de suerte ya resolvió otra persona, o bien es más fácil). Definamos 

_dk_ = _pk_ +1 _− pk,_ 1 _≤ k < n._ 

_dk_ indica la ganancia que obtenemos si compramos al día _k_ y vendemos al _k_ + 1. Si compramos el día _i_ y vendemos el día _j_ , vale que 

_pj − pi_ = ( _pi_ +1 _− pi_ ) + ( _pi_ +2 _− pi_ +1) + _· · ·_ + ( _pj − pj−_ 1) _j−_ 1 = _dk._ ∑︂ _k_ = _i_ 

O sea, los índices que maximizan _pj − pi_ son exactamente los que maximizan<sup>∑︁</sup><sup>_j_</sup> _k_<sup>_−_</sup> =<sup>1</sup> _i_<sup>_dk_.</sup> 

2do Cuatrimestre de 2026 39 / 55 

TDA - Algo3 (DC, FCEyN, UBA) 

DC - FCEyN - UBA 

Divide & Conquer 

Algoritmo de Strassen 

Timba y máximo subarreglo 

Búsqueda y extensiones 

Algoritmo de Karatsuba 

