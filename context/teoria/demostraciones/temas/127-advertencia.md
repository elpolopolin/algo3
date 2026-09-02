## Advertencia 


![](../imagenes/teo01-demostraciones.pdf-0106-09.png)



![](../imagenes/teo01-demostraciones.pdf-0106-10.png)


Si nuestra demostración de _P_ ( _n_ ) usa _P_ ( _n −_ 1) _, P_ ( _n −_ 2) _, . . . , P_ ( _n − k_ ) para un _k ≥_ 1 fijo, entonces necesitamos _k_ **casos base** . Para _n < k_ , « _P_ ( _n − k_ )» no tiene sentido: nos caemos de N. 


![](../imagenes/teo01-demostraciones.pdf-0106-12.png)



![](../imagenes/teo01-demostraciones.pdf-0106-13.png)



![](../imagenes/teo01-demostraciones.pdf-0106-14.png)



![](../imagenes/teo01-demostraciones.pdf-0106-15.png)


Si uso _P_ ( _n −_ 1) y _P_ ( _n −_ 2): pruebo a mano _P_ (0) y _P_ (1). Si uso _P_ ( _n −_ 4): pruebo a mano _P_ (0) _, P_ (1) _, P_ (2) _, P_ (3). Si uso _P_ ( _⌊n/_ 2 _⌋_ ) con inducción fuerte: alcanza un solo caso base, _P_ (0), porque _⌊n/_ 2 _⌋ < n_ para todo _n ≥_ 1 y nunca nos caemos de N. 

Veamos el ejemplo del principio: la recurrencia _T_ ( _n_ ) = 2 _T_ ( _n −_ 4), ahora con rigor. 

(DC, FCEyN, UBA) 

2<sup>_do_</sup> Cuatrimestre de 2026 

23 / 36 

DC - FCEyN - UBA 

¿Qué es una demostración? 

¿Cómo demostramos? 

Complejidad asintótica 

Otras herramientas 

Para Cerrar 

Inducción 

Algoritmos recursivos 

