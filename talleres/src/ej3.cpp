#include <iostream>
#include <vector>
#include <string>
using namespace std;

int main(){
    int n;
    cin >> n;
    vector<string> apellidos(n);
    for(int i = 0; i < n; i++){
        cin >> apellidos[i];
    }

    bool adj[26][26] = {}; //comienzan en false {}. true significa q en adj[u][v] u tiene q ir antes q v
    int indeg[26] = {}; //cuantas letras tienen q salir antes q 'v'

    // Parte 1: armar las restricciones
    for(int i = 0; i < n - 1; i++){
        string s = apellidos[i];
        string t = apellidos[i+1];

        int minLargo = s.size();
        if(t.size() < s.size()) minLargo = t.size();
        int j = 0;
        while(j < minLargo && s[j] == t[j]){ //agarro pos de primer letra distinta
            j++;
        }

        if(j == minLargo){ //no encontro ninguna letra distinta, una es prefijo de otra
            if(s.size() > t.size()){
                cout << "Impossible" << endl;
                return 0;
            }
        } else {
            int u = s[j] - 'a'; //convertir la letra a numero
            int v = t[j] - 'a';
            if(!adj[u][v]){ //si la flecha no estaba puesta entre los nodos la ponemos
                adj[u][v] = true; //marco la flecha u -> v
                indeg[v]++; // v ahora tiene una restriccion mas encima
            }
        }
    }

    //construir el alfabeto
    bool usada[26] = {};
    string res = "";

    for(int paso = 0; paso < 26; paso++){
        int elegida = -1;
        for(int u = 0; u < 26; u++){
            if(!usada[u] && indeg[u] == 0){
                elegida = u;
                break;
            }
        }

        if(elegida == -1){
            cout << "Impossible" << endl;
            return 0;
        }

        usada[elegida] = true;
        res += (char)('a' + elegida);

        for(int v = 0; v < 26; v++){
            if(adj[elegida][v]){
                indeg[v]--;
            }
        }
    }

    cout << res << endl;
    return 0;
}