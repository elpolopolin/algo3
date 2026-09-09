//ej2.cpp


/* cola "q" vacia. g grafo no firigido con nodos del [1 a n]
se agrega a q el vertice 1 y se marca como visitado
se desencola el siguiente vertice v de la cola q

*/

//input 1<=n<=2 . 10(ala5) cantidad de nodos en el arbol
// luego todas las demas lineas describen los ejes del arbol
// ejes "x" e "y" (1 <= x,y <= n) se garantiza q el grafo ing es un arbol
// ultima linea contiene n naturales distintos a1,a2,a3... (1<=a<=n)

//output imprime "yes" si la secuencia representa un recorrido BFS valido en
// el arbol o "no" en caso contrario

// algoritmoi de busqueda en anchura bfs

#include <iostream>
#include <vector>
#include <queue>

int main(){
    int n;
    std::cin >> n;
    std::vector<std::vector<int>> arbol(n+1);
    std::vector<std::vector<int>> ady(n+1);    // acá van los ejes crudos
    std::vector<bool> visitados(n+1);
    int x;
    int y;

    for (int i = 1; i <= n-1; i++){
        std::cin >> x >> y; //vecinos
        ady[x].push_back(y);   
        ady[y].push_back(x); //push_back metodo de vector
    }

   std::vector<int> secuenciaAverificar(n);
    for (int i = 0; i < n; i++) {
        std::cin >> secuenciaAverificar[i];
    }

    for (int i = 0; i < n; i++) //reordenamiento de los adyacentes antes de hacer el bfs
        for (int u : ady[secuenciaAverificar[i]])
            arbol[u].push_back(secuenciaAverificar[i]);
    
    //bfs
    std::queue<int> cola;
    int indice;
    cola.push(1); //se empieza por el primer grafo
    visitados[1] = true;
    bool fin = false;
    int posicion = 0;

    while (cola.empty() == false && fin == false) {
        indice = cola.front();
        cola.pop();

        // comparo contra la secuencia dada
        if (indice != secuenciaAverificar[posicion]) {
            fin = true;
        } else {
            posicion++;
            for (int nodo : arbol[indice]) {
                if (!visitados[nodo]) {
                    visitados[nodo] = true;   // marco al encolar
                    cola.push(nodo);
                }
            }
        }
        
    }
    
    if(fin == true){
        std::cout<<"No";
    }else {
        std::cout <<"Yes";
    }

    return 0;





}