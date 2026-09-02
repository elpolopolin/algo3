## Divide&Conquer 

Los algoritmos de D&C suelen tener esta pinta. 

DIVIDIR-Y-CONQUISTAR( _X_ ) 


![](../imagenes/teo04-Divide_and_Conquer.pdf-0007-08.png)


**if** _X_ es un caso base **return** RESOLVER( _X_ ) ( _X_ 1 _, . . . , Xa_ ) _←_ DIVIDIR( _X_ ) **para** _i_ = 1 _, . . . , a Yi ←_ DIVIDIR-Y-CONQUISTAR( _Xi_ ) **return** COMBINAR( _Y_ 1 _, . . . , Ya_ ) 

Típicamente, se demuestra **Correctitud** , por inducción, usando la recursión. **Complejidad** : calculando el tamaño de cada _X_ 1 _. . . Xa_ , y el costo de COMBINAR (en general, el caso base suele ser _O_ (1), aunque podría no serlo). 

TDA - Algo3 (DC, FCEyN, UBA) 

DC - FCEyN - UBA 

2do Cuatrimestre de 2026 6 / 55 

Divide & Conquer 

Algoritmo de Strassen 

Timba y máximo subarreglo 

Búsqueda y extensiones 

Algoritmo de Karatsuba 

