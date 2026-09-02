## El algoritmo de Karatsuba 

Unos comentarios interesantes: 


![](../imagenes/teo04-Divide_and_Conquer.pdf-0038-07.png)



![](../imagenes/teo04-Divide_and_Conquer.pdf-0038-08.png)



![](../imagenes/teo04-Divide_and_Conquer.pdf-0038-09.png)


En Karatsuba mejoramos el algoritmo de producto partiendo los números de _n_ bits en 2 de _n/_ 2. Mejorará la cosa si partimos en 3? Y en 4? 

Se puede! Y mejora. Es más, mientras más partes usamos, mejor. En general, podemos hacer un algoritmo _O_ ( _n_<sup>1+</sup><sup>_ε_</sup> ) para cualquier _ε >_ 0. Este algoritmo (o bien familia de algoritmos) se conoce como **Algoritmo de Toom-Cook** . Pero se puede hacer mejor: podemos elegir la cantidad de particiones de forma dinámica. Haciendo esto, se puede obtener una complejidad _O_ ( _n_ 2 _√_ 2 log _n_ log _n_ ) (este algoritmo es de Knuth). 


![](../imagenes/teo04-Divide_and_Conquer.pdf-0038-12.png)



![](../imagenes/teo04-Divide_and_Conquer.pdf-0038-13.png)


Y se puede mejorar más: reduciendo el problema a multiplicación de matrices, la complejidad se puede bajar a _O_ ( _n_ log _n_ log log _n_ ) (Strassen). Lo óptimo se cree que es _O_ ( _n_ log _n_ ) (conjetura de Kolmogorov, entre otros), y fue alcanzado en 2019. La constante escondida es tan grande que para que el algoritmo <u>sea práctico la entrada tiene que tener tamaño por lo menos 2</u><sup>1038</sup> .<sup>6</sup> 

- 6Ver _Nature of Computation_ de Moore para más :D 

2do Cuatrimestre de 2026 31 / 55 

TDA - Algo3 (DC, FCEyN, UBA) 

DC - FCEyN - UBA 

Divide & Conquer 

Algoritmo de Strassen 

Timba y máximo subarreglo 

Búsqueda y extensiones 

Algoritmo de Karatsuba 

Pausa 

Pausa 

TDA - Algo3 (DC, FCEyN, UBA) 

DC - FCEyN - UBA 

2do Cuatrimestre de 2026 32 / 55 

Divide & Conquer 

Algoritmo de Strassen 

Timba y máximo subarreglo 

Búsqueda y extensiones 

Algoritmo de Karatsuba 

El algoritmo de Strassen 

Problema: multiplicar matrices Dadas dos matrices _A_ y _B_ , queremos calcular _C_ = _AB_ . Usando el algoritmo del CBC... Qué complejidad alcanzamos? 

TDA - Algo3 (DC, FCEyN, UBA) 

DC - FCEyN - UBA 

2do Cuatrimestre de 2026 33 / 55 

Divide & Conquer 

Algoritmo de Strassen 

Timba y máximo subarreglo 

Búsqueda y extensiones 

Algoritmo de Karatsuba 

El algoritmo de Strassen 

Problema: multiplicar matrices Dadas dos matrices _A_ y _B_ , queremos calcular _C_ = _AB_ . Usando el algoritmo del CBC... Qué complejidad alcanzamos? Es _O_ ( _n_<sup>3</sup> ). Para mejorarlo, vamos a usar de vuelta D&C. 

TDA - Algo3 (DC, FCEyN, UBA) 

DC - FCEyN - UBA 

2do Cuatrimestre de 2026 33 / 55 

Divide & Conquer 

Algoritmo de Strassen 

Timba y máximo subarreglo 

Búsqueda y extensiones 

Algoritmo de Karatsuba 

