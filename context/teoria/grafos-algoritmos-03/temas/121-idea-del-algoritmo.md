## Idea del algoritmo 


![](../imagenes/Graph_Algorithms.pdf-0093-09.png)



![](../imagenes/Graph_Algorithms.pdf-0093-10.png)


- 1 Ejecutar una DFS ordinaria y calcular _T_ , _d_ , _f_ y _π_ . 

- 2 Una vez terminada la DFS, calcular los valores low recorriendo _T_ desde las hojas hacia las raíces. 

- 3 Para cada arista _{π_ [ _v_ ] _, v }_ del bosque, decidir si es puente comparando low[ _v_ ] con _d_ [ _π_ [ _v_ ]]. 


![](../imagenes/Graph_Algorithms.pdf-0093-14.png)


(DC, FCEyN, UBA) 

DC - FCEyN - UBA 

2<sup>_do_</sup> Cuatrimestre de 2026 50 / 58 

Ordenamiento topológico 

Búsqueda a lo ancho 

Búsqueda en profundidad 

Detección de aristas de corte 

Los grafos como modelos 

