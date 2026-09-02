## Ejemplo de D&C: Merge sort 

Se puede implementar en tiempo lineal: copiamos _A_ [ _l . . . q_ ] en _L_ y _A_ [ _q_ + 1 _. . . r_ ] en _R_ . Luego, recorremos _L_ y _R_ a la vez y vamos eligiendo siempre el elemento más chico. MERGE (idea) 


![](../imagenes/teo04-Divide_and_Conquer.pdf-0010-07.png)


_k_ = _l_ ; _i, j_ = 0; **while** ( _i < |L| ∧ j < |R|_ ) **if** _L_ [ _i_ ] _≤ R_ [ _j_ ] _A_ [ _k_ ] _← L_ [ _i_ ]; _i ← i_ + 1 **else** _A_ [ _k_ ] _← R_ [ _j_ ]; _j ← j_ + 1 _k ← k_ + 1 Finalmente, copiar lo que queda al final del subarreglo de _A_ . 

Esto cuesta tiempo lineal. 

2do Cuatrimestre de 2026 9 / 55 

TDA - Algo3 (DC, FCEyN, UBA) 

DC - FCEyN - UBA 

Divide & Conquer 

Algoritmo de Strassen 

Timba y máximo subarreglo 

Búsqueda y extensiones 

Algoritmo de Karatsuba 

