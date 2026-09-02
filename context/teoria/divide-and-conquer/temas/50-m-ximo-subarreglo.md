## Máximo subarreglo 

Más formalmente, tenemos la siguiente proposición Proposición 


![](../imagenes/teo04-Divide_and_Conquer.pdf-0052-07.png)


_r_ max max _dk._ ∑︂ 1 _≤i<j≤n_<sup>(</sup><sup>_pj−pi_) =</sup> 1 _≤ℓ≤r<n k_ = _ℓ_ 

En particular, si ( _i, j_ ) es una solución al problema de la timba, ( _i, j −_ 1) es una solución del problema de máximo subarreglo, y hay una traducción análoga en la otra dirección. **Demostración.** Es inmediata de la igualdad con la suma telescópica que hicimos antes. En base a este resultado, podemos olvidarnos de la timba y quedarnos con el problema del máximo subarreglo. 

TDA - Algo3 (DC, FCEyN, UBA) 

DC - FCEyN - UBA 

2do Cuatrimestre de 2026 40 / 55 

Divide & Conquer 

Algoritmo de Strassen 

Timba y máximo subarreglo 

Búsqueda y extensiones 

Algoritmo de Karatsuba 



<!-- Start of picture text -->
Está completamente Está completamente<br>contenido en [ ℓ, m ]. contenido en [ m  + 1 , r ].<br>Intuitivamente<br>MAXSUB( ℓ, r ) = max { MAXSUB( ℓ, m ) ,  MAXSUB( m  + 1 , r<br><!-- End of picture text -->

