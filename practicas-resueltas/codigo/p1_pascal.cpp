// Práctica 1 — Ejercicio 17 (Triángulo de Pascal)
//
// Reproduce el proceso de "Pascalito": celda (f,c) = 1 si f==0 o c==0,
// y suma de la de arriba (f-1,c) y la de la izquierda (f,c-1) en otro caso.
//
// El test usa como oráculo la fórmula cerrada demostrada en el Ej. 16:
//     valor(f, c) = C(f+c, c) = (f+c)! / (f! c!)
// calculada por un camino independiente (producto multiplicativo).
//
// (idea de "dos caminos independientes hacia el mismo valor":
//  context/teoria/demostraciones/temas/157-de-la-demostraci-n-al-c-digo-y-a-los-tes.md)

#include <cstdint>
#include "comun.h"

// Proceso de Pascalito, recursivo tal cual la definición.
int64_t pascal_rec(int f, int c) {
    if (f == 0 || c == 0) return 1;
    return pascal_rec(f - 1, c) + pascal_rec(f, c - 1);
}

// Oráculo: C(f+c, c) por producto, sin factoriales intermedios (evita overflow
// antes de tiempo). C(n,k) = prod_{i=1..k} (n-k+i)/i.
int64_t combinatorio(int n, int k) {
    if (k > n - k) k = n - k;  // C(n,k) = C(n,n-k)
    int64_t r = 1;
    for (int i = 1; i <= k; ++i) {
        r = r * (n - k + i) / i;  // el cociente parcial siempre es entero
    }
    return r;
}

int main() {
    // Casos a mano.
    CHECK_EQ(pascal_rec(0, 0), 1);
    CHECK_EQ(pascal_rec(0, 5), 1);
    CHECK_EQ(pascal_rec(3, 0), 1);
    CHECK_EQ(pascal_rec(1, 1), 2);
    CHECK_EQ(pascal_rec(2, 2), 6);
    CHECK_EQ(pascal_rec(4, 2), 15);

    // Contra la fórmula cerrada, para toda la región donde no hay overflow
    // de int64 (f+c <= 62 es de sobra seguro para C(f+c, .) con f,c chicos).
    for (int f = 0; f <= 12; ++f) {
        for (int c = 0; c <= 12; ++c) {
            CHECK_EQ(pascal_rec(f, c), combinatorio(f + c, c));
        }
    }

    // Identidad de Pascal, que es el corazón del paso inductivo del Ej. 16.
    for (int f = 1; f <= 10; ++f) {
        for (int c = 1; c <= 10; ++c) {
            CHECK_EQ(pascal_rec(f, c),
                     pascal_rec(f - 1, c) + pascal_rec(f, c - 1));
        }
    }

    return comun::resumen();
}
