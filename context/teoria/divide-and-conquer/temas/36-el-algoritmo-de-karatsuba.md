## El algoritmo de Karatsuba 

Unos comentarios interesantes: 


![](../imagenes/teo04-Divide_and_Conquer.pdf-0037-07.png)



![](../imagenes/teo04-Divide_and_Conquer.pdf-0037-08.png)



![](../imagenes/teo04-Divide_and_Conquer.pdf-0037-09.png)


En Karatsuba mejoramos el algoritmo de producto partiendo los números de _n_ bits en 2 de _n/_ 2. Mejorará la cosa si partimos en 3? Y en 4? 

Se puede! Y mejora. Es más, mientras más partes usamos, mejor. En general, podemos hacer un algoritmo _O_ ( _n_<sup>1+</sup><sup>_ε_</sup> ) para cualquier _ε >_ 0. Este algoritmo (o bien familia de algoritmos) se conoce como **Algoritmo de Toom-Cook** . Pero se puede hacer mejor: podemos elegir la cantidad de particiones de forma dinámica. Haciendo esto, se puede obtener una complejidad _O_ ( _n_ 2 _√_ 2 log _n_ log _n_ ) (este algoritmo es de Knuth). 


![](../imagenes/teo04-Divide_and_Conquer.pdf-0037-12.png)


Y se puede mejorar más: reduciendo el problema a multiplicación de matrices, la complejidad se puede bajar a _O_ ( _n_ log _n_ log log _n_ ) (Strassen). 

> 6Ver _Nature of Computation_ de Moore para más :D 

2do Cuatrimestre de 2026 

TDA - Algo3 (DC, FCEyN, UBA) 

DC - FCEyN - UBA 

31 / 55 

Divide & Conquer 

Algoritmo de Strassen 

Timba y máximo subarreglo 

Búsqueda y extensiones 

Algoritmo de Karatsuba 

