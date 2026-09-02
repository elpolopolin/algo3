## Teorema 


![](../imagenes/teo04-Divide_and_Conquer.pdf-0013-07.png)


MERGESORT( _A, l, r_ ) termina y deja ordenados exactamente los elementos que estaban en _A_ [ _p..r_ ]. 

**Prueba por inducción en** _n_ = _r − l_ + 1 **.** 


![](../imagenes/teo04-Divide_and_Conquer.pdf-0013-10.png)



![](../imagenes/teo04-Divide_and_Conquer.pdf-0013-11.png)



![](../imagenes/teo04-Divide_and_Conquer.pdf-0013-12.png)


Si _n ≤_ 1, el segmento ya está ordenado. Si _n >_ 1, ambas llamadas reciben segmentos de tamaño menor. Por hipótesis inductiva terminan, preservan sus elementos y ordenan cada mitad. Finalmente MERGE los une manteniéndolos ordenados, y eso ordena finalmente el segmento _A_ [ _l_ : _r_ ].<sup>1</sup> 

> 1Para ser correctos, nos faltaría probar que MERGE hace lo que queremos. Eso se podría hacer con un invariante, pero al nivel de la materia vamos a permitirnos decir que “claramente <mark>es</mark> co <mark>rr</mark> ect ~~o”.~~ 

TDA - Algo3 (DC, FCEyN, UBA) 

DC - FCEyN - UBA 2do Cuatrimestre de 2026 12 / 55 

Divide & Conquer 

Algoritmo de Strassen 

Timba y máximo subarreglo 

Búsqueda y extensiones 

Algoritmo de Karatsuba 

