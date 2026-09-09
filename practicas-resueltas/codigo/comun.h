// Helpers mínimos de test y medición de tiempo, compartidos por los ejercicios.
#pragma once
#include <chrono>
#include <cstdio>
#include <cstdlib>
#include <string>

namespace comun {

inline int fallas = 0;

inline void check(bool ok, const std::string& que, const char* file, int line) {
    if (!ok) {
        std::fprintf(stderr, "FALLA  %s:%d  %s\n", file, line, que.c_str());
        ++fallas;
    }
}

// Termina el programa: 0 si no hubo fallas, 1 si hubo.
inline int resumen() {
    if (fallas == 0) {
        std::puts("OK");
        return 0;
    }
    std::fprintf(stderr, "%d fallas\n", fallas);
    return 1;
}

// Cronómetro de pared, en segundos.
struct Reloj {
    std::chrono::steady_clock::time_point t0 = std::chrono::steady_clock::now();
    double seg() const {
        return std::chrono::duration<double>(
                   std::chrono::steady_clock::now() - t0)
            .count();
    }
};

}  // namespace comun

#define CHECK(cond) ::comun::check((cond), #cond, __FILE__, __LINE__)
#define CHECK_EQ(a, b)                                                    \
    ::comun::check((a) == (b), std::string(#a) + " == " + #b, __FILE__, \
                   __LINE__)
