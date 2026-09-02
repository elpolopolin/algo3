# El próximo vértice debe tener grado de entrada cero 

En un DAG siempre existe algún vértice de grado de entrada 0. Cualquiera de ellos puede ocupar la próxima posición del orden. 

- _v_ entrada[ _v_ ] _←_ entrada[ _v_ ] _−_ 1 1 Agregar _u_ al final del orden. 2 Eliminar conceptualmente a _u_ . 

- _u_ 3 Disminuir el grado de entrada de cada vecino saliente. 

- entrada[ _u_ ] = 0 _w_ entrada[ _w_ ] _←_ entrada[ _w_ ] _−_ 1 4 Encolar los vecinos cuyo grado pasa a ser 0. 

   - Solo se modifican los grados de entrada de los vértices _v ∈ N_<sup>+</sup> ( _u_ ). 

2<sup>_do_</sup> Cuatrimestre de 2026 14 / 58 

(DC, FCEyN, UBA) 

DC - FCEyN - UBA 

Ordenamiento topológico 

Búsqueda a lo ancho 

Búsqueda en profundidad 

Detección de aristas de corte 

Los grafos como modelos 

