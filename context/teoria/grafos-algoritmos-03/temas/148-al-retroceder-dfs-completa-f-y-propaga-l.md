# Al retroceder, DFS completa _f_ y propaga low 


![](../imagenes/Graph_Algorithms.pdf-0120-06.png)


<!-- Start of picture text -->
a f<br>c d e<br>b g<br>árbol DFS retroceso<br><!-- End of picture text -->

orden: _a, b, c, d, e, f , g_ ; en _c_ se examina _d_ antes que _a_ 

|_u_|_d_[_u_]|_f_[_u_]|low[_u_]|
|---|---|---|---|
|_a_|1|–|1|
|_b_|2|–|2|
|_c_|3|–|1|
|_d_|4|11|4|
|_e_|5|10|5|
|_f_|6|9|5|
|_g_|7|8|5|



##### **13. Ahora** _c_ **examina la arista** _ca_ **.** Como _a_ todavía está abierto, 

##### low[ _c_ ] _←_ m´ın _{_ 3 _, d_ [ _a_ ] _}_ = 1 _._ 

2<sup>_do_</sup> Cuatrimestre de 2026 55 / 58 

(DC, FCEyN, UBA) 

DC - FCEyN - UBA 

Ordenamiento topológico 

Búsqueda a lo ancho 

Búsqueda en profundidad 

Detección de aristas de corte 

Los grafos como modelos 

