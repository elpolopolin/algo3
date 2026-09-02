## Algoritmo de Strassen 

Dividimos las matrices en bloques, 


![](../imagenes/teo04-Divide_and_Conquer.pdf-0043-07.png)



![](../imagenes/teo04-Divide_and_Conquer.pdf-0043-08.png)


y análogamente para _C_ 21 y _C_ 22. 

En este algoritmo, qué complejidad tiene combinar? _O_ ( _n_<sup>2</sup> ), o sea, lineal con respecto a la entrada. 

La recurrencia de la cantidad de operaciones es 

_T_ ( _m_ ) = 8 _T_ ( _m/_ 4) + Θ( _m_ ) 

con _m_ = _n_<sup>2</sup> . Usando Maestro, sale que la complejidad es Θ( _m_<sup>3</sup><sup>_/_2</sup> ) = Θ(( _n_<sup>2</sup> )<sup>3</sup><sup>_/_2</sup> ) = Θ( _n_<sup>3</sup> ). O sea, no mejoramos nada. 

DC - FCEyN - UBA 2do Cuatrimestre de 2026 34 / 55 

TDA - Algo3 (DC, FCEyN, UBA) 

Divide & Conquer 

Algoritmo de Strassen 

Timba y máximo subarreglo 

Búsqueda y extensiones 

Algoritmo de Karatsuba 

