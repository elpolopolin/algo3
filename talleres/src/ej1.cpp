#include <iostream>
#include <vector>
using namespace std;

int main() { 
    int n;
    std::cin >> n;
    std::vector<int> padre(n+1); //n+1 posiciones arrancan en 0 padre[0] queda sin usar
    //vector es arrray de c normal int a[100]; 
    //tiene un tamano fijo escrito en el codigo, vector no; le decis el tamano
    // a partir de n

    // todos los socios son padres porq siempre va de arriba hacia abajo
    // nunca es un ciclo. (logica de estafa piramidal padreeee)

    //std::cout <<"ingresa la cantidad de socios-vendedores [1 al 2000]"


    /*while (n>2000 or n<1){ //prevenir errores, por ahi es al pedo
        std::cout <<"ingresa la cantidad de socios-vendedores [1 al 2000]"
        std::cin >> n;
    }*/

    for (int i = 1; i <= n; ++i) { //complejidad O(n)
        //ingresar los padres de cada hijo
        //2std::cout <<"padre de" << i;
        std::cin >> padre[i]; //cin = objeto de la bib estandar de c++ q maneja la entrada de datos(keyboard input)
    /* if (padre[i] == i) {
            std::cout <<"no se puede revender a si mismo";
            std::cin >> padre[i];
        }
            */ //esto estaba garantizado
        //ahora hay que verificar que no existan ciclos de reventa
    }

    //devolver cantidad de mesas minima, es la rama mas larga, la hoja con mas padres
    int mesas;
    int mesasRecorrida;
    mesas = 0;
    for (int h =1; h <= n; h++) { //O(n)
        mesasRecorrida = 1;
        int actual = h; //socio-vendedor actual
        while(padre[actual] != -1){
            actual = padre[actual];
            mesasRecorrida = mesasRecorrida + 1;
        }
        if (mesasRecorrida > mesas){
            mesas = mesasRecorrida;
        }   
    }   
    std::cout << mesas;
    return 0;
    /* COMPLEJIDAD
    - n ≤ 2000
    - 3 segundos de tiempo
    - 256 MB de memoria

    Regla de dedo: una CPU hace ~10⁸–10⁹ operaciones simples por segundo.

    Con n = 2000:
    - O(n²) = 4.000.000 operaciones → entra sobradísimo (ni 3s ni 0.01s, nada).
    - O(n) = 2000 → obvio.

    */

    // para el output se garantiza que ningun socio-vendedor se siente 
    // con su padre


    // cin saltea espacios y saltos de linea solo.

}
