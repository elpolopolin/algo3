# Exponenciación rápida: el plan 

> 1 **La propiedad habla del exponente:** _P_ ( _n_ ): _para todo a ∈_ N, Exp( _a, n_ ) = _a_<sup>_n_</sup> . El _∀a_ va _adentro_ de _P_ ( _n_ ): la HI sirve para cualquier base. 

> 2 **Caso base** _P_ (0) **:** el primer _if_ . 

> 3 **Paso inductivo** con inducción fuerte: usamos la HI en _⌊_<sup>_<u>n</u>_</sup> 2<sup>_⌋< n_, no en</sup><sup>_n −_1.</sup> 

> 4 **Partir en casos** según la paridad de _n_ , igual que el algoritmo (el segundo _if_ ). 

_−→_ Demostración en el pizarrón. 

Los algoritmos recursivos suelen ser más fáciles de demostrar correctos que los iterativos (que necesitan invariantes): no hay estado que se modifica, sólo llamadas a subproblemas menores. 

2<sup>_do_</sup> Cuatrimestre de 2026 28 / 36 

(DC, FCEyN, UBA) 

DC - FCEyN - UBA 

¿Qué es una demostración? ¿Cómo demostramos? Complejidad asintótica 

Otras herramientas 

Para Cerrar 

Inducción 

Algoritmos recursivos 

