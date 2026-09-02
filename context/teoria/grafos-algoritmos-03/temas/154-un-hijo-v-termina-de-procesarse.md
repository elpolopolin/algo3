## Un hijo _v_ termina de procesarse 


![](../imagenes/Graph_Algorithms.pdf-0125-09.png)



![](../imagenes/Graph_Algorithms.pdf-0125-10.png)


Todo lo que puede alcanzarse desde el subárbol de _v_ también puede alcanzarse desde el subárbol de _u_ . Por eso, 

low[ _u_ ] _←_ m´ın _{_ low[ _u_ ] _,_ low[ _v_ ] _}._ 


![](../imagenes/Graph_Algorithms.pdf-0125-13.png)


Se examina una arista que no es la arista al padre 


![](../imagenes/Graph_Algorithms.pdf-0125-15.png)



![](../imagenes/Graph_Algorithms.pdf-0125-16.png)


La arista _uv_ permite alcanzar directamente un vértice ya descubierto. Por eso, 

low[ _u_ ] _←_ m´ın _{_ low[ _u_ ] _, d_ [ _v_ ] _}._ 


![](../imagenes/Graph_Algorithms.pdf-0125-19.png)


Como la actualización con low[ _v_ ] se realiza después de la llamada recursiva, los valores se propagan de las hojas hacia la raíz. 

(DC, FCEyN, UBA) 

DC - FCEyN - UBA 

2<sup>_do_</sup> Cuatrimestre de 2026 

56 / 58 

Ordenamiento topológico 

Búsqueda a lo ancho 

Búsqueda en profundidad 

Detección de aristas de corte 

Los grafos como modelos 



