# El color del destino clasifica la arista al explorarla 

Cuando DFS examina una arista ( _u, v_ ), el vértice _u_ está gris. 

color[ _v_ <u>]</u> tipo de <u>(</u> _u, v_ <u>)</u> razón blanco árbol _v_ se descubre mediante ( _u, v_ ) gris retroceso _v_ es un ancestro activo de _u_ negro avance o cruce _v_ ya terminó de procesarse 

#### **Idea clave.** 

Los vértices grises forman una cadena de ancestros: son exactamente las llamadas activas de la pila. Por eso, una arista hacia un vértice gris necesariamente vuelve hacia un ancestro. 

2<sup>_do_</sup> Cuatrimestre de 2026 45 / 58 

(DC, FCEyN, UBA) 

DC - FCEyN - UBA 

Ordenamiento topológico 

Búsqueda a lo ancho 

Búsqueda en profundidad 

Detección de aristas de corte 

Los grafos como modelos 

