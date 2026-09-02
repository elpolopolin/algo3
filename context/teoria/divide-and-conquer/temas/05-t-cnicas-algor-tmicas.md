## Técnicas algorítmicas 

En general, vemos técnicas porque: 


![](../imagenes/teo04-Divide_and_Conquer.pdf-0005-07.png)


Son patrones de solución que han funcionado en otros problemas, por lo que tiene sentido intentar aplicarlos a nuevos. 


![](../imagenes/teo04-Divide_and_Conquer.pdf-0005-09.png)


En general vienen asociados a conjuntos de herramientas y prácticas para probar correctitud y complejidad. **Ejemplo** : los algoritmos recursivos, cuya correctitud se prueba por inducción y cuya complejidad sale resolviendo alguna relación de recurrencia. 


![](../imagenes/teo04-Divide_and_Conquer.pdf-0005-11.png)


Facilitan la comunicación y la comprensión de los algoritmos. **Ejemplo** : “Hago recursión en _n_ , fijate que _f_ ( _n_ ) depende de _f_ ( _n −_ 4) y de _f_ ( _n −_ 1), así que es inmediato cómo calcularlo”. 

En la clase de hoy vamos a ver Divide&Conquer (D&C): daremos la idea general del patrón, y distintos casos de uso. Aparte, vamos a ver técnicas y teoremas que permiten calcular complejidades de forma sencilla. 

4 / 55 

TDA - Algo3 (DC, FCEyN, UBA) 

DC - FCEyN - UBA 

2do Cuatrimestre de 2026 

Divide & Conquer Algoritmo de Karatsuba Algoritmo de Strassen Timba y máximo subarreglo Búsqueda y extensiones Divide&Conquer Esquemáticamente, un algoritmo de D&C tiene las siguientes partes. 1. Dividir 2. Conquistar 3. Combinar Separar la instancia en Resolverlos recursivamente; Reagrupar las soluciones subproblemas más los casos pequeños se parciales para obtener la pequeños del mismo tipo. resuelven directamente. solución original. En el fondo, es solo recursión, pero vamos a ver que es muy común que los subproblemas tengan todos **el mismo tamaño** , y que la complejidad general suele depender únicamente de (1) la cantidad de subproblemas, (2) su tamaño, y (3) el costo de combinar las soluciones. ~~<mark>—</mark>~~ TDA - Algo3 (DC, FCEyN, UBA) DC - FCEyN - UBA 2do Cuatrimestre de 2026 5 / 55 

2do Cuatrimestre de 2026 5 / 55 

Divide & Conquer 

Algoritmo de Strassen 

Timba y máximo subarreglo 

Búsqueda y extensiones 

Algoritmo de Karatsuba 

