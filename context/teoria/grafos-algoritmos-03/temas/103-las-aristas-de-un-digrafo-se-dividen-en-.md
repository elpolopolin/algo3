# Las aristas de un digrafo se dividen en cuatro tipos 

La clasificación se realiza con respecto al bosque DFS obtenido. Árbol. La arista ( _u, v_ ) descubre por primera vez a _v_ , por lo que 

_π_ [ _v_ ] = _u._ 

Retroceso. La arista ( _u, v_ ) va desde _u_ hacia uno de sus ancestros _v_ . Los bucles se consideran aristas de retroceso. 

Avance. La arista ( _u, v_ ) no pertenece al bosque y va hacia un descendiente propio de _u_ . Cruce. Es cualquier otra arista: sus extremos son incomparables en el árbol DFS o pertenecen a árboles distintos. 

La clasificación depende del bosque DFS y, por lo tanto, puede cambiar cuando cambia el orden de exploración. 

DC - FCEyN - UBA 

2<sup>_do_</sup> Cuatrimestre de 2026 43 / 58 

(DC, FCEyN, UBA) 

Ordenamiento topológico 

Búsqueda a lo ancho 

Búsqueda en profundidad 

Detección de aristas de corte 

Los grafos como modelos 

