#include <iostream>
#include <vector>
#include <string>
using namespace std;

int main(){
    int n;                                  // cantidad de apellidos
    cin >> n;                               // leo n de la primera linea

    vector<string> apellidos(n);            // reservo n casilleros para los strings

    for(int i = 0; i < n; i++){             // recorro de 0 a n-1
        cin >> apellidos[i];                // leo el apellido i y lo guardo en la posicion i
    }

    // ---------- estructuras del grafo ----------
    // El nodo NO es un objeto: es un numero de 0 a 25. 'a'=0, 'b'=1, ..., 'z'=25.

    bool adj[26][26] = {};                  // adj[u][v] = true significa "u tiene que ir antes que v"
                                            // el = {} deja las 676 celdas en false

    int indeg[26] = {};                     // indeg[v] = cuantas flechas ENTRAN a la letra v
                                            // o sea: cuantas letras tienen que salir antes que v
                                            // el = {} deja los 26 contadores en 0

    // ---------- PARTE 1: leer los pares y armar las flechas ----------

    for(int i = 0; i < n - 1; i++){         // ojo el n-1: comparo el par (i, i+1),
                                            // asi que el ultimo i valido es n-2

        string s = apellidos[i];            // el apellido que va PRIMERO en la lista
        string t = apellidos[i+1];          // el que va JUSTO DESPUES
                                            // quiero que se cumpla s <= t con el alfabeto nuevo

        int minLargo = s.size();            // arranco suponiendo que s es el mas corto
        if(t.size() < s.size())             // si en realidad t es mas corto...
            minLargo = t.size();            // ...me quedo con el largo de t
                                            // minLargo = hasta donde puedo comparar sin salirme de ningun string

        int j = 0;                          // posicion donde estoy comparando
        while(j < minLargo && s[j] == t[j]){ // mientras no me pase del final Y las letras sean iguales...
            j++;                            // ...avanzo a la siguiente posicion
        }
        // al salir del while pasa UNA de dos cosas:
        //   (A) j == minLargo  -> nunca encontre una diferencia (uno es prefijo del otro)
        //   (B) j <  minLargo  -> en la posicion j las letras difieren

        if(j == minLargo){                  // ---- CASO (A): uno es prefijo del otro ----
                                            // ej: s="hola", t="holamundo"
                                            // aca la comparacion la decide el LARGO, no las letras.
                                            // el alfabeto no influye en nada.

            if(s.size() > t.size()){        // si el primero es el mas LARGO (ej: "holamundo" antes de "hola")
                cout << "Impossible" << endl; // esta mal ordenado y ningun alfabeto lo puede arreglar
                return 0;                   // corto el programa, no tiene sentido seguir
            }
                                            // si s es el mas corto: esta bien ordenado.
                                            // NO agrego ninguna flecha porque este par
                                            // no me dice nada sobre el alfabeto.

        } else {                            // ---- CASO (B): difieren en la posicion j ----
                                            // ej: s="sarmiento", t="mitre", j=0 -> 's' vs 'm'
                                            // la comparacion se decide ACA y lo que viene despues no importa

            int u = s[j] - 'a';             // convierto la letra a numero: 's'-'a' = 18
            int v = t[j] - 'a';             // 'm'-'a' = 12

            if(!adj[u][v]){                 // solo si esta flecha NO estaba ya puesta
                                            // (si la cuento dos veces, indeg[v] nunca llega a 0
                                            //  y me da un "Impossible" falso)
                adj[u][v] = true;           // marco la flecha u -> v
                indeg[v]++;                 // v ahora tiene una restriccion mas encima
            }
        }
    }
    // al terminar este for tengo TODAS las restricciones cargadas en adj e indeg

    // ---------- PARTE 2: armar el alfabeto (orden topologico) ----------
    // idea: 26 veces, agarro una letra que no tenga restricciones pendientes,
    // la pongo en el resultado, y "libero" a las letras que dependian de ella.

    bool usada[26] = {};                    // usada[u] = true si u ya esta en el resultado
                                            // hace falta porque cuando saco una letra su indeg
                                            // queda en 0 y la volveria a elegir para siempre

    string res = "";                        // aca voy construyendo el alfabeto, letra por letra

    for(int paso = 0; paso < 26; paso++){   // necesito colocar exactamente 26 letras

        int elegida = -1;                   // -1 = todavia no encontre candidata

        for(int u = 0; u < 26; u++){        // escaneo las 26 letras desde la 'a'
            if(!usada[u] && indeg[u] == 0){ // busco una que NO haya usado y que NO tenga
                                            // ninguna letra pendiente de salir antes que ella
                elegida = u;
                break;                      // me quedo con la primera que encuentro y corto
            }
        }

        if(elegida == -1){                  // no encontre ninguna libre, pero todavia faltan letras
                                            // => las que quedan se apuntan entre si formando un CICLO
                                            // ej: c->g, g->p, p->c  ("c tiene que ir antes que c")
            cout << "Impossible" << endl;
            return 0;
        }

        usada[elegida] = true;              // la marco para no volver a elegirla
        res += (char)('a' + elegida);       // la paso de numero a letra y la pego al resultado
                                            // ej: 12 + 'a' = 'm'

        for(int v = 0; v < 26; v++){        // ahora que "elegida" ya salio...
            if(adj[elegida][v]){            // ...para cada letra v que dependia de ella
                indeg[v]--;                 // le saco esa restriccion de encima
                                            // si v llega a 0, queda libre para elegirse mas adelante
            }
        }
    }

    cout << res << endl;                    // si llegue aca, coloque las 26 letras: alfabeto valido
    return 0;
}