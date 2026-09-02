# De la demostración al código (y a los tests) 

Una fórmula cerrada **demostrada** es un oráculo perfecto para testear la versión recursiva (y viceversa): 

**long long** suma_geom( **int** n) { _// 3^0 + 3^1 + ... + 3^n_ **if** (n == 0) **return** 1; **return** suma_geom(n - 1) + pot3(n); _// pot3(n) = 3^n_ } **void** test() { **for** ( **int** n = 0; n <= 30; ++n) { _// formula cerrada demostrada hoy: (3^(n+1) - 1) / 2_ assert(suma_geom(n) == (pot3(n + 1) - 1) / 2); } } 


![](../imagenes/teo01-demostraciones.pdf-0136-08.png)


El test compara **dos caminos independientes** hacia el mismo valor: si difieren, algo está mal (el código... o la demostración). 

2<sup>_do_</sup> Cuatrimestre de 2026 29 / 36 

(DC, FCEyN, UBA) 

DC - FCEyN - UBA 

Otras herramientas 

Para Cerrar 

Inducción 

Algoritmos recursivos 

¿Qué es una demostración? ¿Cómo demostramos? Complejidad asintótica 

