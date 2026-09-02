# Ahora sí: _T_ ( _n_ ) = 2 _T_ ( _n −_ 4), con rigor 

El plan para hacerla bien: 

> 1 **Definir** _T_ **con su dominio:** sea _T_ : N _→_ N tal que _T_ ( _n_ ) = 2 _T_ ( _n −_ 4) para todo _n ≥_ 4. De _T_ (0) _, . . . , T_ (3) no sabemos nada: sea _a_ = m´ax( _T_ (0) _, T_ (1) _, T_ (2) _, T_ (3)). _<u>n</u>_ 

> 2 **Definir la propiedad:** _P_ ( _n_ ) : _T_ ( _n_ ) _≤ a ·_ 2 4 . 

> 3 **Cuatro casos base** (0 _≤ n ≤_ 3): la recursión resta 4. 

> 4 **Paso inductivo** (inducción fuerte): para _n ≥_ 4, 0 _≤ n −_ 4 _< n_ legitima usar _P_ ( _n −_ 4). 

> 5 **Concluir con la definición de** _O_ **:** exhibir constantes concretas _c_ y _n_ 0. 

_−→_ Demostración completa en el pizarrón. 

Mismo resultado que el alumno del principio, pero ahora **sin baches** : dominio claro, cuatro casos base, HI explícita, y la definición de _O_ aplicada con constantes concretas. 

2<sup>_do_</sup> Cuatrimestre de 2026 24 / 36 

(DC, FCEyN, UBA) 

DC - FCEyN - UBA 

¿Qué es una demostración? 

¿Cómo demostramos? 

Complejidad asintótica 

Otras herramientas 

Para Cerrar 

Inducción 

Algoritmos recursivos 



¿Y si mi objeto tiene dos «tamaños»? Inducción en tuplas 

A veces el estado natural del problema es un **par** ( _a, b_ ): una celda de una matriz, dos índices de una recursión, . . . ¿En qué hacemos inducción? 

2<sup>_do_</sup> Cuatrimestre de 2026 25 / 36 

(DC, FCEyN, UBA) 

DC - FCEyN - UBA 

Complejidad asintótica 

Otras herramientas 

Para Cerrar 

Inducción 

Algoritmos recursivos 

¿Qué es una demostración? 

¿Cómo demostramos? 

