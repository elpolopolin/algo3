# Prácticas resueltas — Algoritmos y Estructuras de Datos III

Resolución completa de las prácticas 1, 2 y 3, apoyada en el material de
`../context/teoria/`. Un `.md` por práctica:

| Archivo | Contenido | Teoría que usa |
|---|---|---|
| [`practica-1.md`](practica-1.md) | Demostraciones y complejidad asintótica (20 ej.) | `context/teoria/demostraciones` |
| [`practica-2.md`](practica-2.md) | Introducción a grafos (18 ej.) | `context/teoria/intro-grafos` |
| [`practica-3.md`](practica-3.md) | Algoritmos sobre grafos: BFS, DFS (18 ej.) | `context/teoria/grafos-algoritmos-03` |

Cada ejercicio tiene: **qué pide**, **qué teoría aplica** (citada al pie),
**resolución** (demostración formal / pseudocódigo + complejidad /
contraejemplo) y, cuando hay que implementar, un link al código en `codigo/`.

## Entorno de código (C++)

Los ejercicios que piden implementar algo viven en `codigo/`. Es la lengua
franca de la cátedra Algo3.

```
codigo/
  Makefile          make <target> compila y corre; make test corre todo
  comun.h           helpers de test (CHECK, CHECK_EQ) y cronómetro
  grafo.h grafo.cpp  grafo con lista de adyacencias (se usa desde la práctica 3)
  p1_pascal.cpp     Práctica 1 – Ej. 17 (triángulo de Pascal recursivo + tests)
  p3_triangulos.cpp Práctica 3 – Ej. 2 (algoritmo cúbico y cuadrático)
  ...
  tests/            casos de test por ejercicio
```

### Compilar y correr

Requiere `g++`/`clang++` con C++17 y `make`.

```sh
cd codigo
make p1_pascal      # compila y corre un ejercicio puntual
make test           # compila y corre todos los ejecutables de test
make clean
```

Cada `.cpp` con `main()` corre sus propios `assert`/`CHECK` y termina con
`OK` si todo pasó.
