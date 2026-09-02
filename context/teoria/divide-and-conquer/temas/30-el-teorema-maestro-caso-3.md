## El Teorema Maestro: Caso 3 

Supongamos _f_ ( _n_ ) = Ω( _n_<sup>_q_+</sup><sup>_ε_</sup> ) y, para algún 0 _< c <_ 1 y todo _n_ suficientemente grande, _af_ ( _n/b_ ) _≤ cf_ ( _n_ ) _._ 

Iterando esta desigualadad, también sabemos que para _n_ suficientemente grande vale que _a_<sup>_i_</sup> _f_ ( _n/b_<sup>_i_</sup> ) _≤ c_<sup>_i_</sup> _f_ ( _n_ ) _._ 

Por lo tanto, aplicando esta desigualdad hasta el último piso donde se pueda (ya que solo vale a partir de un cierto _n_ ), podemos acotar 


![](../imagenes/teo04-Divide_and_Conquer.pdf-0030-09.png)


Los subárboles restantes aportan _O_ ( _n_<sup>_q_</sup> ), que es _O_ ( _f_ ( _n_ )). Concluimos entonces que 


![](../imagenes/teo04-Divide_and_Conquer.pdf-0030-11.png)


TDA - Algo3 (DC, FCEyN, UBA) 

DC - FCEyN - UBA 

2do Cuatrimestre de 2026 27 / 55 

Divide & Conquer Algoritmo de Karatsuba Algoritmo de Strassen Timba y máximo subarreglo Búsqueda y extensiones Los tres casos corresponden a tres formas del árbol Caso 1 Caso 2 Caso 3 El costo aumenta hacia Los niveles son El costo decrece hacia abajo. comparables. abajo. Dominan las hojas Se acumulan niveles Domina la raíz La prueba es simplemente el razonamiento que veníamos haciendo, pero hecho de forma más general. ~~<mark>=</mark>~~ TDA - Algo3 (DC, FCEyN, UBA) DC - FCEyN - UBA 2do Cuatrimestre de 2026 28 / 55 

2do Cuatrimestre de 2026 28 / 55 

Divide & Conquer 

Algoritmo de Strassen 

Timba y máximo subarreglo 

Búsqueda y extensiones 

Algoritmo de Karatsuba 

