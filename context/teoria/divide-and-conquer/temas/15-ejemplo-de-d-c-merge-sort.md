## Ejemplo de D&C: Merge sort 

Podemos pensar en el árbol de recursión, e intentar llevar la cuenta de cuánto se trabaja en cada llamado. Si frente a un arreglo de _n_ números se hacen _cn_ operaciones (ignorando la recursión), entonces tenemos los siguientes costos 


![](../imagenes/teo04-Divide_and_Conquer.pdf-0015-07.png)


<!-- Start of picture text -->
cn<br>c ( n/ 2) c ( n/ 2)<br>c ( n/ 4) c ( n/ 4) c ( n/ 4) c ( n/ 4)<br><!-- End of picture text -->


![](../imagenes/teo04-Divide_and_Conquer.pdf-0015-08.png)


<!-- Start of picture text -->
cn<br>2  · c ( n/ 2) =  cn<br>4  · c ( n/ 4) =  cn<br><!-- End of picture text -->

En cada “piso” se hacen _cn_ operaciones, y hay log _n_ pisos. Luego, la complejidad parecería ser _O_ ( _n_ log _n_ ). Vamos a probarlo rigurosamente 

TDA - Algo3 (DC, FCEyN, UBA) 

DC - FCEyN - UBA 

2do Cuatrimestre de 2026 14 / 55 

Divide & Conquer 

Algoritmo de Strassen 

Timba y máximo subarreglo 

Búsqueda y extensiones 

Algoritmo de Karatsuba 

