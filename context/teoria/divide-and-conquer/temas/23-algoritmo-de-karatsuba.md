## Algoritmo de Karatsuba 

La cantidad de operaciones que hace el algoritmo ahora satisface la relación<sup>4</sup> _T_ ( _n_ ) = 3 _T_ ( _n/_ 2) + Θ( _n_ ) _._ 

Si analizamos el árbol de recursión podemos encontrar un nuevo candidato para la recursión (en este caso, es Θ( _n_<sup>log2 3</sup> )). En vez de hacer eso, vamos a ver una herramienta que automatiza el razonamiento que estábamos haciendo. 

- 4Alguien podría criticar que falta un +1 en la recursión porque los números son un poco más grandes que 

- _n/_ 2, pero podemos absorberlo en el Θ( _n_ ) del final argumentando un poco. 

DC - FCEyN - UBA 2do Cuatrimestre de 2026 20 / 55 

TDA - Algo3 (DC, FCEyN, UBA) 

Divide & Conquer 

Algoritmo de Strassen 

Timba y máximo subarreglo 

Búsqueda y extensiones 

Algoritmo de Karatsuba 

