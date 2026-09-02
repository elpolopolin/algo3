# La segunda fase prueba una desigualdad por arista del árbol 

Después de completar todas las llamadas a DFS-PUENTES-VISIT, el procedimiento PUENTES( _G_ ) continúa así: 

_B ←_ ∅ **para cada** _v ∈ V_ ( _G_ ) **hacer si** _π_ [ _v_ ] _̸_ = NIL **y** low[ _v_ ] _> d_ [ _π_ [ _v_ ]] **entonces** _B ← B ∪_ {︁ _{π_ [ _v_ ] _, v }_ }︁ **retornar** _B_ 

No es necesario recorrer todo _E_ ( _G_ ) en esta fase: alcanza con recorrer los vértices no raíz, uno por cada arista del bosque DFS. 

