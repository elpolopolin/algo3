# Al retroceder, DFS completa _f_ y propaga low 


![](../imagenes/Graph_Algorithms.pdf-0110-06.png)


<!-- Start of picture text -->
a f<br>c d e<br>b g<br>árbol DFS retroceso<br>orden:  a, b, c, d, e, f , g ; en  c se examina  d antes que  a<br><!-- End of picture text -->


![](../imagenes/Graph_Algorithms.pdf-0110-07.png)


<!-- Start of picture text -->
u d [ u ] f [ u ] low[ u ]<br>a 1 – 1<br>b 2 – 2<br>c 3 – 3<br>d – – –<br>e – – –<br>f – – –<br>g – – –<br><!-- End of picture text -->

##### **3. Avanza por** _bc_ **y descubre** _c_ **.** 

##### _d_ [ _c_ ] = low[ _c_ ] = 3 _._ 

2<sup>_do_</sup> Cuatrimestre de 2026 

(DC, FCEyN, UBA) 

DC - FCEyN - UBA 

55 / 58 

Ordenamiento topológico 

Búsqueda a lo ancho 

Búsqueda en profundidad 

Detección de aristas de corte 

Los grafos como modelos 

