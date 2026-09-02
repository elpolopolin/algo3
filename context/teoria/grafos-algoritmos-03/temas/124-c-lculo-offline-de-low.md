# Cálculo offline de low 


![](../imagenes/Graph_Algorithms.pdf-0096-06.png)


<!-- Start of picture text -->
a f<br>c d e<br>b g<br>árbol DFS retroceso<br>orden DFS:  a, b, c, d, e, f , g ; postorden:  g, f , e, d, c, b, a<br><!-- End of picture text -->

|_u_|_d_[_u_]|_f_[_u_]|low[_u_]|
|---|---|---|---|
|_a_|1|14|1|
|_b_|2|13|2|
|_c_|3|12|3|
|_d_|4|11|4|
|_e_|5|10|5|
|_f_|6|9|6|
|_g_|7|8|5|



##### **2. Se procesa la arista de retroceso** _ge_ **.** Como _e_ es un ancestro de _g_ , 

low[ _g_ ] _←_ m´ın _{_ 7 _, d_ [ _e_ ] _}_ = 5 _._ 

2<sup>_do_</sup> Cuatrimestre de 2026 52 / 58 

(DC, FCEyN, UBA) 

DC - FCEyN - UBA 

Ordenamiento topológico 

Búsqueda a lo ancho 

Búsqueda en profundidad 

Detección de aristas de corte 

Los grafos como modelos 

