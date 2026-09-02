# Al retroceder, DFS completa _f_ y propaga low 


![](../imagenes/Graph_Algorithms.pdf-0108-06.png)


<!-- Start of picture text -->
a f<br>c d e<br>b g<br>árbol DFS retroceso<br>orden:  a, b, c, d, e, f , g ; en  c se examina  d antes que  a<br><!-- End of picture text -->

|_u_|_d_[_u_]|_f_[_u_]|low[_u_]|
|---|---|---|---|
|_a_|1|–|1|
|_b_|–|–|–|
|_c_<br>_d_|–<br>–|–<br>–|–<br>–|
|_e_<br>_f_<br>_g_|–<br>–<br>–|–<br>–<br>–|–<br>–<br>–|



##### **1. Descubre** _a_ **.** 

##### _d_ [ _a_ ] = low[ _a_ ] = 1 _._ 

2<sup>_do_</sup> Cuatrimestre de 2026 

(DC, FCEyN, UBA) 

DC - FCEyN - UBA 

55 / 58 

Ordenamiento topológico 

Búsqueda a lo ancho 

Búsqueda en profundidad 

Detección de aristas de corte 

Los grafos como modelos 

