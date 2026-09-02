## El algoritmo de Strassen 

Con mucha inspiración, es posible darse cuenta, como hizo Strassen, de que con 7 multiplicaciones podemos recuperar todos los bloques de _C_ . Estos son los elegidos: 

_M_ 1 = ( _A_ 11 + _A_ 22)( _B_ 11 + _B_ 22) _, M_ 2 = ( _A_ 21 + _A_ 22) _B_ 11 _, M_ 3 = _A_ 11( _B_ 12 _− B_ 22) _, M_ 4 = _A_ 22( _B_ 21 _− B_ 11) _, M_ 5 = ( _A_ 11 + _A_ 12) _B_ 22 _, M_ 6 = ( _A_ 21 _− A_ 11)( _B_ 11 + _B_ 12) _, M_ 7 = ( _A_ 12 _− A_ 22)( _B_ 21 + _B_ 22) _._ 

Por ejemplo, _C_ 11 = _M_ 1 + _M_ 7 + _M_ 4 _− M_ 5 (cuidado, lo revisé a mano). Esto reduce el problema de multiplicar dos matrices de _n × n_ a multiplicar 7 de _∼ n/_ 2 _× n/_ 2 y hacer _O_ (1) sumas que se pueden hacer en _O_ ( _n_<sup>2</sup> ). Luego, la recurrencia queda como: 

_T_ ( _n_<sup>2</sup> ) = 7 _T_ ( _n_<sup>2</sup> _/_ 4) + Θ( _n_<sup>2</sup> ) 

TDA - Algo3 (DC, FCEyN, UBA) 

DC - FCEyN - UBA 

2do Cuatrimestre de 2026 35 / 55 

Divide & Conquer 

Algoritmo de Strassen 

Timba y máximo subarreglo 

Búsqueda y extensiones 

Algoritmo de Karatsuba 

