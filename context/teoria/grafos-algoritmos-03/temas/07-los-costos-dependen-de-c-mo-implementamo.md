# Los costos dependen de cómo implementamos cada lista 

Supongamos listas no ordenadas, acceso directo a Adj[ _v_ ] e inserción al frente. **Consultas Actualizaciones** 

recorrer _N_ ( _v_ ) : _O_ ( _d_ ( _v_ )) _,_ decidir si _vw ∈ E_ : _O_ ( _d_ ( _v_ )) _._ 

Para decidir adyacencia debemos buscar _w_ dentro de la lista de _v_ . 

insertar _vw_ : _O_ (1) _,_ remover _vw_ : _O_ ( _d_ ( _v_ ) + _d_ ( _w_ )) _,_ remover _v_ : _O_ ( _n_ + _m_ ) (peor caso). 

2<sup>_do_</sup> Cuatrimestre de 2026 8 / 58 

(DC, FCEyN, UBA) 

DC - FCEyN - UBA 

Ordenamiento topológico 

Búsqueda a lo ancho 

Búsqueda en profundidad 

Detección de aristas de corte 

Los grafos como modelos 

