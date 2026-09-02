# Al terminar, las capas coinciden con las distancias 


![](../imagenes/Graph_Algorithms.pdf-0041-06.png)


<!-- Start of picture text -->
d = 1 d = 0 d = 2 d = 3<br>r s t u<br>v w x y<br>d = 2 d = 1 d = 2 d = 3<br><!-- End of picture text -->


![](../imagenes/Graph_Algorithms.pdf-0041-07.png)


<!-- Start of picture text -->
i Li = {v :  d [ v ] =  i} predecesores<br>0 {s} π [ s ] = NIL<br>1 {r , w} π [ r ] =  π [ w ] =  s<br>2 {v , t, x} π [ v ] =  r , π [ t ] =  π [ x ] =  w<br>3 {u, y } π [ u ] =  t, π [ y ] =  x<br><!-- End of picture text -->

El orden de las listas puede cambiar el árbol, pero no las distancias. 

2<sup>_do_</sup> Cuatrimestre de 2026 

(DC, FCEyN, UBA) 

DC - FCEyN - UBA 

23 / 58 

Ordenamiento topológico 

Búsqueda a lo ancho 

Búsqueda en profundidad 

Detección de aristas de corte 

Los grafos como modelos 



