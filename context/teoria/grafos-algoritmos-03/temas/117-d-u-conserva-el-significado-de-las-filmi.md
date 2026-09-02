# _d_ [ _u_ ] conserva el significado de las filminas de DFS 

Cuando DFS descubre un vértice _u_ , incrementa el contador global _tiempo_ y asigna 

_d_ [ _u_ ] _← tiempo._ 

De este modo, al finalizar, 

_d_ : _V_ ( _G_ ) _−→{_ 1 _, . . . ,_ 2 _|V_ ( _G_ ) _|}_ 

es la función que asigna a cada vértice su tiempo de descubrimiento. Además, si _u_ fue descubierto al examinar la arista _{π_ [ _u_ ] _, u}_ , entonces _π_ [ _u_ ] es su padre en el bosque DFS. 

