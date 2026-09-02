# claude.md — unidad: algoritmos con grafos

Reglas propias de esta unidad. Lo general (economía de contexto, flujo de
respuesta, diagramas, los dos entornos) está en el `claude.md` de la raíz.

## Fuente

- Teoría: `grafos-algoritmos.md`, partido en `temas/` (157 archivos).
  Ruteo por `INDICE.md`. **Nunca responder de memoria**: siempre citar el
  archivo del que sale cada afirmación.
- Demostraciones: unidad aparte, `context/teoria/demos-grafos/`.
- Práctica de esta unidad: `context/practica/pdfs/practica_3.md`.

## Salidas

- `resumen.md` — explicación de cada tema que pregunto. Se **amplía**, no se pisa.
- `respuestas-teoricas/<tema>.md` — cuando el tema es grande y no entra bien en
  el resumen. Dejá el link desde `resumen.md`.
- Ejercicios resueltos: **no van acá**, van a
  `context/practica/respuestas-practicas/`.

Formato de cita, al final de la sección:

```
temas/152-al-retroceder-dfs-completa-f-y-propaga-l.md — Al retroceder, DFS completa f y propaga low
```

## Lenguaje

Esta unidad se explica en el lenguaje **menos técnico posible**:

- Cada palabra técnica o de la materia lleva la explicación entre paréntesis.
- Las siglas en inglés van con nombre completo y traducción la primera vez que
  aparecen en el archivo: *BFS (Breadth-First Search, búsqueda a lo ancho)*,
  *DFS (Depth-First Search, búsqueda en profundidad)*, *MST (Minimum Spanning
  Tree, árbol generador mínimo)*.
- Arrancá cada tema nuevo de `resumen.md` con un "Vocabulario mínimo" si mete
  términos que no salieron antes.

## Imágenes

1. Primero buscá en `imagenes/` (246 figuras ya extraídas de las diapositivas).
2. Si no hay ninguna que sirva, generala y guardala en `imagenes/` **de la raíz
   del repo**, PNG de 600px máximo (ver la escalera del `claude.md` raíz).
3. Rutas relativas desde `resumen.md`: figura de la cátedra
   `imagenes/x.png`; diagrama tuyo `../../../imagenes/x.png`.
4. Para algoritmos, preferí **una imagen por paso** (nodos, cola, vectores)
   antes que una sola con todo.
