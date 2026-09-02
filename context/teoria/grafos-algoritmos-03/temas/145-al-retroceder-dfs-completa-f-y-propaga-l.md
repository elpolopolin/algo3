# Al retroceder, DFS completa _f_ y propaga low 


![](../imagenes/Graph_Algorithms.pdf-0117-06.png)


<!-- Start of picture text -->
a f<br>c d e<br>b g<br>árbol DFS retroceso<br>orden:  a, b, c, d, e, f , g ; en  c se examina  d antes que  a<br><!-- End of picture text -->

|_u_|_d_[_u_]|_f_[_u_]|low[_u_]|
|---|---|---|---|
|_a_|1|–|1|
|_b_|2|–|2|
|_c_|3|–|3|
|_d_|4|–|4|
|_e_|5|–|5|
|_f_|6|9|5|
|_g_|7|8|5|



**10. Finaliza** _f_ **y vuelve a** _e_ **.** 

_f_ [ _f_ ] = 9 _,_ low[ _e_ ] _←_ m´ın _{_ 5 _,_ low[ _f_ ] _}_ = 5 _._ 

2<sup>_do_</sup> Cuatrimestre de 2026 55 / 58 

(DC, FCEyN, UBA) 

DC - FCEyN - UBA 

Ordenamiento topológico 

Búsqueda a lo ancho 

Búsqueda en profundidad 

Detección de aristas de corte 

Los grafos como modelos 

