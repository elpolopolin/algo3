## Máximo subarreglo 

Intentemos proponer un enfoque con D&C para resolver el problema. Qué podríamos hacer? Dividir el arreglo a la mitad, hacer recursión de cada lado, luego al combinar buscar el máximo subarreglo que pasa por el medio. Más formalmente, si buscamos el máximo subarreglo entre dos índices _ℓ_ y _r_ , hay tres opciones, con _m_ = ( _ℓ_ + _r_ ) _/_ 2: 

