# Al retroceder, DFS completa _f_ y propaga low 


![](../imagenes/Graph_Algorithms.pdf-0109-06.png)


<!-- Start of picture text -->
a f<br>c d e<br>b g<br>árbol DFS retroceso<br><!-- End of picture text -->

orden: _a, b, c, d, e, f , g_ ; en _c_ se examina _d_ antes que _a_ 


![](../imagenes/Graph_Algorithms.pdf-0109-08.png)


<!-- Start of picture text -->
u d [ u ] f [ u ] low[ u ]<br>a 1 – 1<br>b 2 – 2<br>c – – –<br>d – – –<br>e – – –<br>f – – –<br>g – – –<br><!-- End of picture text -->

##### **2. Avanza por** _ab_ **y descubre** _b_ **.** 

##### _d_ [ _b_ ] = low[ _b_ ] = 2 _._ 

2<sup>_do_</sup> Cuatrimestre de 2026 

(DC, FCEyN, UBA) 

DC - FCEyN - UBA 

55 / 58 

Ordenamiento topológico 

Búsqueda a lo ancho 

Búsqueda en profundidad 

Detección de aristas de corte 

Los grafos como modelos 

