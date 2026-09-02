# Al retroceder, DFS completa _f_ y propaga low 


![](../imagenes/Graph_Algorithms.pdf-0112-06.png)


<!-- Start of picture text -->
a f<br>c d e<br>b g<br>árbol DFS retroceso<br>orden:  a, b, c, d, e, f , g ; en  c se examina  d antes que  a<br><!-- End of picture text -->


![](../imagenes/Graph_Algorithms.pdf-0112-07.png)


<!-- Start of picture text -->
u d [ u ] f [ u ] low[ u ]<br>a 1 – 1<br>b 2 – 2<br>c 3 – 3<br>d 4 – 4<br>e 5 – 5<br>f – – –<br>g – – –<br><!-- End of picture text -->

##### **5. Avanza por** _de_ **y descubre** _e_ **.** 

_d_ [ _e_ ] = low[ _e_ ] = 5 _._ 

2<sup>_do_</sup> Cuatrimestre de 2026 55 / 58 

(DC, FCEyN, UBA) 

DC - FCEyN - UBA 

Ordenamiento topológico 

Búsqueda a lo ancho 

Búsqueda en profundidad 

Detección de aristas de corte 

Los grafos como modelos 

