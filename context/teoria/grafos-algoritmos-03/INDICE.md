# Índice — grafos-algoritmos

157 archivos · 4866 líneas en total.

> Generado por `tools/indexar.py`. No editar a mano: se regenera.
> Para buscar un término literal es más barato `grep -rl "término" temas/`
> que leer este índice. Este índice sirve para lo que grep no encuentra.

| Archivo | Tema | De qué trata | Conceptos | Líneas |
|---|---|---|---|---|
| `01-agenda-de-hoy.md` | Agenda de hoy | Basado en Cormen, Leiserson, Rivest, Stein, Introduction to Algorithms , cap. 20. | — | 28 |
| `02-el-grafo-y-su-representaci-n-son-objetos.md` | El grafo y su representación son objetos diferentes | <!-- Start of picture text --> | `Objeto matemático`, `Estructura de datos` | 51 |
| `03-representamos-el-grafo-mediante-sus-veci.md` | Representamos el grafo mediante sus vecindarios | En la práctica suponemos | `Operaciones que nos interesan` | 38 |
| `04-un-mismo-grafo-admite-distintas-represen.md` | Un mismo grafo admite distintas representaciones | <!-- Start of picture text --> | `Grafo`, `Listas`, `Matriz` | 40 |
| `05-las-listas-almacenan-solamente-los-vecin.md` | Las listas almacenan solamente los vecinos existentes | <!-- Start of picture text --> | — | 47 |
| `06-el-espacio-de-las-listas-es-lineal-en-el.md` | El espacio de las listas es lineal en el tamaño del grafo | ∑︂ \| Adj[ v ] \| = m. v ∈V | `Digrafos`, `Grafos no dirigidos` | 38 |
| `07-los-costos-dependen-de-c-mo-implementamo.md` | Los costos dependen de cómo implementamos cada lista | Supongamos listas no ordenadas, acceso directo a Adj[ v ] e inserción al frente. Consultas Actualizaciones | `Consultas Actualizaciones` | 26 |
| `08-la-matriz-reserva-una-posici-n-para-cada.md` | La matriz reserva una posición para cada par de vértices | 1 , si vw ∈ E, A [ v , w ] = {︄0 , si vw ∈/ E. Espacio: Θ( n<sup>2</sup> ). Consultar vw ∈ E : O (1).… | — | 40 |
| `09-la-operaci-n-dominante-orienta-la-elecci.md` | La operación dominante orienta la elección | Espacio Consultar vw ∈ E Recorrer N ( v ) Recorrer todas las aristas | `Listas`, `Matriz`, `Grafo con pocas aristas`, `Grafo denso` | 32 |
| `10-los-pesos-se-almacenan-junto-con-las-ari.md` | Los pesos se almacenan junto con las aristas | Cada entrada guarda el vecino y el peso: Adj[ v ] ∋ ( w, p ( v , w )) . | `Matriz de adyacencia`, `Listas de adyacencia` | 14 |
| `100-teorema-del-camino-blanco.md` | Teorema del camino blanco (1/2: Teorema del camino blanco) | En el bosque DFS, v es descendiente de u si y solo si, en el instante d [ u ], existe un camino de u a v… | `Teorema del camino blanco` | 34 |
| `101-un-camino-blanco-caracteriza-a-los-desce.md` | Un camino blanco caracteriza a los descendientes (1/2) | — | — | 2 |
| `102-teorema-del-camino-blanco.md` | Teorema del camino blanco (2/2: Teorema del camino blanco) | En el bosque DFS, v es descendiente de u si y solo si, en el instante d [ u ], existe un camino de u a v… | `Idea de la demostración`, `Teorema del camino blanco` | 47 |
| `103-las-aristas-de-un-digrafo-se-dividen-en-.md` | Las aristas de un digrafo se dividen en cuatro tipos | La clasificación se realiza con respecto al bosque DFS obtenido. Árbol. La arista ( u, v ) descubre por… | — | 28 |
| `104-la-corrida-anterior-contiene-los-cuatro-.md` | La corrida anterior contiene los cuatro tipos de arista | <!-- Start of picture text --> | — | 41 |
| `105-el-color-del-destino-clasifica-la-arista.md` | El color del destino clasifica la arista al explorarla (1/2: **Idea clave.**) | Cuando DFS examina una arista ( u, v ), el vértice u está gris. | `Idea clave` | 26 |
| `106-el-color-del-destino-clasifica-la-arista.md` | El color del destino clasifica la arista al explorarla (2/2: **Idea clave.**) | Cuando DFS examina una arista ( u, v ), el vértice u está gris. | `Idea clave` | 30 |
| `107-en-grafos-no-dirigidos-no-hay-aristas-de.md` | En grafos no dirigidos no hay aristas de avance ni de cruce (1/2) | — | — | 2 |
| `108-teorema.md` | Teorema (1/7: Teorema) | En una búsqueda en profundidad de un grafo no dirigido G , toda arista es una arista de árbol o una arista de… | `Teorema` | 32 |
| `109-en-grafos-no-dirigidos-no-hay-aristas-de.md` | En grafos no dirigidos no hay aristas de avance ni de cruce (2/2) | — | — | 2 |
| `11-cuidado.md` | Cuidado | No conviene usar 0 para indicar ausencia si una arista puede tener peso 0. | — | 36 |
| `110-teorema.md` | Teorema (2/7: Teorema) | En una búsqueda en profundidad de un grafo no dirigido G , toda arista es una arista de árbol o una arista de… | `Idea de la demostración`, `Teorema` | 102 |
| `111-para-hallar-los-puentes-alcanza-con-comp.md` | Para hallar los puentes alcanza con completar una única DFS (1/3) | Sea G un grafo no dirigido y sea T el bosque producido por DFS. | — | 16 |
| `112-cantidad-de-puentes.md` | Cantidad de puentes (1/2: Cantidad de puentes) | Como todo puente pertenece al árbol DFS, #puentes ≤ n − 1. | `Cantidad de puentes` | 16 |
| `113-idea-del-algoritmo.md` | Idea del algoritmo (1/3: Idea del algoritmo) | 2<sup>do</sup> Cuatrimestre de 2026 47 / 58 | `Idea del algoritmo` | 34 |
| `114-para-hallar-los-puentes-alcanza-con-comp.md` | Para hallar los puentes alcanza con completar una única DFS (2/3) | Sea G un grafo no dirigido y sea T el bosque producido por DFS. | — | 16 |
| `115-cantidad-de-puentes.md` | Cantidad de puentes (2/2: Cantidad de puentes) | Como todo puente pertenece al árbol DFS, #puentes ≤ n − 1. | `Cantidad de puentes` | 16 |
| `116-idea-del-algoritmo.md` | Idea del algoritmo (2/3: Idea del algoritmo) | El algoritmo también funciona si G no es conexo: en ese caso, DFS produce un bosque en lugar de un único… | `Idea del algoritmo` | 36 |
| `117-d-u-conserva-el-significado-de-las-filmi.md` | _d_ [ _u_ ] conserva el significado de las filminas de DFS | Cuando DFS descubre un vértice u , incrementa el contador global tiempo y asigna | — | 12 |
| `118-propiedad-que-vamos-a-usar.md` | Propiedad que vamos a usar | Si x es un ancestro propio de u en el bosque DFS, entonces d [ x ] < d [ u ]. | `Propiedad que vamos a usar` | 38 |
| `119-low-u-indica-hasta-d-nde-puede-volver-el.md` | low[ _u_ ] indica hasta dónde puede volver el subárbol de _u_ | Definimos low[ u ] como el menor tiempo de descubrimiento de un vértice al que se puede llegar desde u : | — | 28 |
| `12-un-orden-topol-gico-respeta-todas-las-ar.md` | Un orden topológico respeta todas las aristas (1/3: ordenamiento topológico) | Sea D = ( V , E ) un digrafo. Un ordenamiento topológico de D es un orden lineal v 1 , v 2 , . . . , vn de… | `ordenamiento topológico` | 31 |
| `120-para-hallar-los-puentes-alcanza-con-comp.md` | Para hallar los puentes alcanza con completar una única DFS (3/3) | Sea G un grafo no dirigido y sea T el bosque producido por DFS. | — | 6 |
| `121-idea-del-algoritmo.md` | Idea del algoritmo (3/3: Idea del algoritmo) | (DC, FCEyN, UBA) | `Idea del algoritmo` | 36 |
| `122-low-puede-calcularse-despu-s-de-terminar.md` | low puede calcularse después de terminar DFS | Una vez conocidos el bosque DFS T , los tiempos d y los predecesores π , ejecutamos: Procedimiento CALCULAR -… | `para cada`, `Procedimiento`, `en postorden de`, `hacer si`, `entonces`, `retornar` | 24 |
| `123-c-lculo-offline-de-low.md` | Cálculo offline de low (1/11: 1. Inicialización) | <!-- Start of picture text --> | `1. Inicialización` | 43 |
| `124-c-lculo-offline-de-low.md` | Cálculo offline de low (2/11: 2. Se procesa la arista de retroceso) | <!-- Start of picture text --> | `2. Se procesa la arista de retroceso` | 41 |
| `125-c-lculo-offline-de-low.md` | Cálculo offline de low (3/11: 3. Se procesa la arista de retroceso) | <!-- Start of picture text --> | `3. Se procesa la arista de retroceso` | 41 |
| `126-c-lculo-offline-de-low.md` | Cálculo offline de low (4/11) | <!-- Start of picture text --> | — | 39 |
| `127-c-lculo-offline-de-low.md` | Cálculo offline de low (5/11: 5. Se procesa) | <!-- Start of picture text --> | `5. Se procesa` | 43 |
| `128-c-lculo-offline-de-low.md` | Cálculo offline de low (6/11: 6. Se procesa) | <!-- Start of picture text --> | `6. Se procesa` | 43 |
| `129-c-lculo-offline-de-low.md` | Cálculo offline de low (7/11: 7. Se procesa) | <!-- Start of picture text --> | `7. Se procesa` | 43 |
| `13-un-orden-topol-gico-respeta-todas-las-ar.md` | Un orden topológico respeta todas las aristas (2/3: ordenamiento topológico) | Sea D = ( V , E ) un digrafo. Un ordenamiento topológico de D es un orden lineal v 1 , v 2 , . . . , vn de… | `ordenamiento topológico` | 13 |
| `130-c-lculo-offline-de-low.md` | Cálculo offline de low (8/11: 8. Se procesa) | <!-- Start of picture text --> | `8. Se procesa` | 43 |
| `131-c-lculo-offline-de-low.md` | Cálculo offline de low (9/11: 9. Se procesa) | <!-- Start of picture text --> | `9. Se procesa` | 43 |
| `132-c-lculo-offline-de-low.md` | Cálculo offline de low (10/11: 10. Se procesa la raíz) | <!-- Start of picture text --> | `10. Se procesa la raíz` | 41 |
| `133-c-lculo-offline-de-low.md` | Cálculo offline de low (11/11: 11. Se aplica el criterio de puente) | <!-- Start of picture text --> | `11. Se aplica el criterio de puente` | 45 |
| `134-la-primera-fase-extiende-la-inicializaci.md` | La primera fase extiende la inicialización de DFS | Al terminar esta fase, d , low y π están definidos para todos los vértices. La segunda fase solamente… | `para cada`, `Procedimiento`, `hacer si`, `entonces` | 26 |
| `135-dfs-puentes-visit-calcula-low-al-retroce.md` | DFS-PUENTES-VISIT calcula low al retroceder | tiempo ← tiempo + 1 d [ u ] ← tiempo low[ u ] ← d [ u ] color[ u ] ← gris para cada v ∈ Adj[ u ] hacer si… | `entonces`, `Procedimiento`, `para cada`, `hacer si` | 26 |
| `136-al-retroceder-dfs-completa-f-y-propaga-l.md` | Al retroceder, DFS completa _f_ y propaga low (1/17: 1. Descubre) | <!-- Start of picture text --> | `1. Descubre` | 40 |
| `137-al-retroceder-dfs-completa-f-y-propaga-l.md` | Al retroceder, DFS completa _f_ y propaga low (2/17: 2. Avanza por) | <!-- Start of picture text --> | `2. Avanza por`, `y descubre` | 40 |
| `138-al-retroceder-dfs-completa-f-y-propaga-l.md` | Al retroceder, DFS completa _f_ y propaga low (3/17: 3. Avanza por) | <!-- Start of picture text --> | `3. Avanza por`, `y descubre` | 38 |
| `139-al-retroceder-dfs-completa-f-y-propaga-l.md` | Al retroceder, DFS completa _f_ y propaga low (4/17: 4. Desde) | <!-- Start of picture text --> | `4. Desde`, `visita primero a` | 38 |
| `14-lema.md` | Lema (1/6: Lema) | Todo digrafo acíclico (DAG) tiene un vértice v tal que d<sup>(</sup> v ) = 0. | `Lema` | 32 |
| `140-al-retroceder-dfs-completa-f-y-propaga-l.md` | Al retroceder, DFS completa _f_ y propaga low (5/17: 5. Avanza por) | <!-- Start of picture text --> | `5. Avanza por`, `y descubre` | 36 |
| `141-al-retroceder-dfs-completa-f-y-propaga-l.md` | Al retroceder, DFS completa _f_ y propaga low (6/17: 6. Avanza por) | <!-- Start of picture text --> | `6. Avanza por`, `y descubre` | 38 |
| `142-al-retroceder-dfs-completa-f-y-propaga-l.md` | Al retroceder, DFS completa _f_ y propaga low (7/17: 7. Avanza por) | <!-- Start of picture text --> | `7. Avanza por`, `y descubre` | 43 |
| `143-al-retroceder-dfs-completa-f-y-propaga-l.md` | Al retroceder, DFS completa _f_ y propaga low (8/17: encuentra la arista de retroceso) | <!-- Start of picture text --> | `encuentra la arista de retroceso` | 38 |
| `144-al-retroceder-dfs-completa-f-y-propaga-l.md` | Al retroceder, DFS completa _f_ y propaga low (9/17: 9. Finaliza) | <!-- Start of picture text --> | `9. Finaliza`, `y vuelve a` | 41 |
| `145-al-retroceder-dfs-completa-f-y-propaga-l.md` | Al retroceder, DFS completa _f_ y propaga low (10/17: 10. Finaliza) | <!-- Start of picture text --> | `10. Finaliza`, `y vuelve a` | 41 |
| `146-al-retroceder-dfs-completa-f-y-propaga-l.md` | Al retroceder, DFS completa _f_ y propaga low (11/17: 11. Finaliza) | <!-- Start of picture text --> | `11. Finaliza`, `y vuelve a` | 43 |
| `147-al-retroceder-dfs-completa-f-y-propaga-l.md` | Al retroceder, DFS completa _f_ y propaga low (12/17: 12. Finaliza) | <!-- Start of picture text --> | `12. Finaliza`, `y vuelve a` | 43 |
| `148-al-retroceder-dfs-completa-f-y-propaga-l.md` | Al retroceder, DFS completa _f_ y propaga low (13/17: 13. Ahora) | <!-- Start of picture text --> | `13. Ahora`, `examina la arista` | 43 |
| `149-al-retroceder-dfs-completa-f-y-propaga-l.md` | Al retroceder, DFS completa _f_ y propaga low (14/17: 14. Finaliza) | <!-- Start of picture text --> | `14. Finaliza`, `y vuelve a` | 43 |
| `15-un-orden-topol-gico-respeta-todas-las-ar.md` | Un orden topológico respeta todas las aristas (3/3: ordenamiento topológico) | Sea D = ( V , E ) un digrafo. Un ordenamiento topológico de D es un orden lineal v 1 , v 2 , . . . , vn de… | `ordenamiento topológico` | 13 |
| `150-al-retroceder-dfs-completa-f-y-propaga-l.md` | Al retroceder, DFS completa _f_ y propaga low (15/17: 15. Finaliza) | <!-- Start of picture text --> | `15. Finaliza`, `y vuelve a` | 43 |
| `151-al-retroceder-dfs-completa-f-y-propaga-l.md` | Al retroceder, DFS completa _f_ y propaga low (16/17: 16. Finaliza la raíz) | <!-- Start of picture text --> | `16. Finaliza la raíz` | 45 |
| `152-al-retroceder-dfs-completa-f-y-propaga-l.md` | Al retroceder, DFS completa _f_ y propaga low (17/17: 17. Se aplica el criterio de puente) | <!-- Start of picture text --> | `17. Se aplica el criterio de puente` | 45 |
| `153-las-dos-actualizaciones-de-low-re-nen-to.md` | Las dos actualizaciones de low reúnen toda la información | Al descubrir u , inicialmente solamente sabemos que u se alcanza a sí mismo: | — | 6 |
| `154-un-hijo-v-termina-de-procesarse.md` | Un hijo v termina de procesarse | Todo lo que puede alcanzarse desde el subárbol de v también puede alcanzarse desde el subárbol de u . Por eso, | `Un hijo v termina de procesarse` | 58 |
| `155-la-segunda-fase-prueba-una-desigualdad-p.md` | La segunda fase prueba una desigualdad por arista del árbol (1/2: para cada) | Después de completar todas las llamadas a DFS-PUENTES-VISIT, el procedimiento PUENTES( G ) continúa así: | `para cada`, `hacer si`, `entonces`, `retornar` | 24 |
| `156-la-segunda-fase-prueba-una-desigualdad-p.md` | La segunda fase prueba una desigualdad por arista del árbol (2/2: para cada) | Después de completar todas las llamadas a DFS-PUENTES-VISIT, el procedimiento PUENTES( G ) continúa así: | `para cada`, `hacer si`, `entonces`, `retornar` | 8 |
| `157-teorema.md` | Teorema (3/7: Teorema) | Sea G un grafo con uv ∈ E ( G ) y π producido por el algoritmo DFS. Entonces, uv es puente de G , con π [ v ]… | `Teorema` | 76 |
| `16-lema.md` | Lema (2/6: Lema) | Todo digrafo acíclico (DAG) tiene un vértice v tal que d<sup>(</sup> v ) = 0. | `Lema` | 16 |
| `17-teorema.md` | Teorema (4/7: Teorema) | Un digrafo admite un ordenamiento topológico si y solo si es acíclico . | `Teorema` | 32 |
| `18-v-rtices-con-grado-de-entrada-igual-a-ce.md` | Vértices con grado de entrada igual a cero (1/3) | En un DAG siempre existe algún vértice de grado de entrada cero. Cualquiera de ellos puede ocupar la próxima… | — | 22 |
| `19-v-rtices-con-grado-de-entrada-igual-a-ce.md` | Vértices con grado de entrada igual a cero (2/3) | En un DAG siempre existe algún vértice de grado de entrada cero. Cualquiera de ellos puede ocupar la próxima… | — | 4 |
| `20-algoritmo-recursivo.md` | Algoritmo recursivo (1/2: Algoritmo recursivo) | 2<sup>do</sup> Cuatrimestre de 2026 13 / 58 | `Algoritmo recursivo` | 38 |
| `21-v-rtices-con-grado-de-entrada-igual-a-ce.md` | Vértices con grado de entrada igual a cero (3/3) | En un DAG siempre existe algún vértice de grado de entrada cero. Cualquiera de ellos puede ocupar la próxima… | — | 4 |
| `22-algoritmo-recursivo.md` | Algoritmo recursivo (2/2: Algoritmo recursivo) | — | `Algoritmo recursivo` | 22 |
| `23-complejidad.md` | Complejidad | Con listas de adyacencia, buscar y eliminar un vértice cuesta O ( n + m ). Como se realizan hasta n pasos,… | `Complejidad` | 34 |
| `24-el-pr-ximo-v-rtice-debe-tener-grado-de-e.md` | El próximo vértice debe tener grado de entrada cero | En un DAG siempre existe algún vértice de grado de entrada 0. Cualquiera de ellos puede ocupar la próxima… | — | 28 |
| `25-una-cola-mantiene-los-v-rtices-disponibl.md` | Una cola mantiene los vértices disponibles | Cada vértice se encola una sola vez y cada arista se procesa una sola vez. | `para todo`, `hacer`, `entonces`, `devolver`, `Inicialización`, `Construcción del orden` | 48 |
| `26-ejemplo-la-cola-se-actualiza-al-eliminar.md` | Ejemplo: la cola se actualiza al eliminar cada vértice (1/7: Inicialización) | <!-- Start of picture text --> | `Inicialización` | 33 |
| `27-ejemplo-la-cola-se-actualiza-al-eliminar.md` | Ejemplo: la cola se actualiza al eliminar cada vértice (2/7: Procesamos) | <!-- Start of picture text --> | `Procesamos` | 33 |
| `28-ejemplo-la-cola-se-actualiza-al-eliminar.md` | Ejemplo: la cola se actualiza al eliminar cada vértice (3/7: Procesamos) | <!-- Start of picture text --> | `Procesamos` | 33 |
| `29-ejemplo-la-cola-se-actualiza-al-eliminar.md` | Ejemplo: la cola se actualiza al eliminar cada vértice (4/7: **Procesamos** _c_) | <!-- Start of picture text --> | `Procesamos c` | 33 |
| `30-ejemplo-la-cola-se-actualiza-al-eliminar.md` | Ejemplo: la cola se actualiza al eliminar cada vértice (5/7: **Procesamos** _d_) | <!-- Start of picture text --> | `Procesamos d` | 37 |
| `31-ejemplo-la-cola-se-actualiza-al-eliminar.md` | Ejemplo: la cola se actualiza al eliminar cada vértice (6/7: **Procesamos** _e_) | <!-- Start of picture text --> | `Procesamos e` | 31 |
| `32-ejemplo-la-cola-se-actualiza-al-eliminar.md` | Ejemplo: la cola se actualiza al eliminar cada vértice (7/7: **Procesamos** _f_) | <!-- Start of picture text --> | `Procesamos f` | 33 |
| `33-el-resultado-coloca-el-origen-antes-que-.md` | El resultado coloca el origen antes que el destino | <!-- Start of picture text --> | `La ejecución anterior devuelve` | 29 |
| `34-recorrer-un-grafo.md` | Recorrer un grafo | Muchos algoritmos sobre grafos siguen un mismo esquema para recorrer los vértices alcanzables desde un… | `Estructura`, `Orden de procesamiento`, `Recorrido` | 40 |
| `35-bfs-explora-por-distancia-creciente-desd.md` | BFS explora por distancia creciente desde una fuente | Sea G = ( V , E ) un grafo o digrafo sin pesos y sea s ∈ V un vértice fuente. La búsqueda a lo ancho (BFS)… | `sin pesos` | 45 |
| `36-los-colores-describen-el-estado-de-cada-.md` | Los colores describen el estado de cada vértice | Durante la ejecución, cada vértice se encuentra en uno de tres estados. | — | 72 |
| `37-bfs-utiliza-una-cola-para-administrar-la.md` | BFS utiliza una cola para administrar la frontera | (DC, FCEyN, UBA) | `para cada`, `Función`, `mientras`, `hacer si`, `entonces`, `devolver` | 24 |
| `38-ejemplo-la-cola-obliga-a-procesar-el-gra.md` | Ejemplo: la cola obliga a procesar el grafo por capas (1/9: Suponemos que las listas de adyacencia están en orden alfabético.) | <!-- Start of picture text --> | — | 29 |
| `39-ejemplo-la-cola-obliga-a-procesar-el-gra.md` | Ejemplo: la cola obliga a procesar el grafo por capas (2/9: Suponemos que las listas de adyacencia están en orden alfabético.) | <!-- Start of picture text --> | — | 29 |
| `40-ejemplo-la-cola-obliga-a-procesar-el-gra.md` | Ejemplo: la cola obliga a procesar el grafo por capas (3/9: Suponemos que las listas de adyacencia están en orden alfabético.) | <!-- Start of picture text --> | — | 29 |
| `41-ejemplo-la-cola-obliga-a-procesar-el-gra.md` | Ejemplo: la cola obliga a procesar el grafo por capas (4/9: Suponemos que las listas de adyacencia están en orden alfabético.) | <!-- Start of picture text --> | — | 29 |
| `42-ejemplo-la-cola-obliga-a-procesar-el-gra.md` | Ejemplo: la cola obliga a procesar el grafo por capas (5/9: Suponemos que las listas de adyacencia están en orden alfabético.) | <!-- Start of picture text --> | — | 29 |
| `43-ejemplo-la-cola-obliga-a-procesar-el-gra.md` | Ejemplo: la cola obliga a procesar el grafo por capas (6/9: Suponemos que las listas de adyacencia están en orden alfabético.) | <!-- Start of picture text --> | — | 29 |
| `44-ejemplo-la-cola-obliga-a-procesar-el-gra.md` | Ejemplo: la cola obliga a procesar el grafo por capas (7/9: Suponemos que las listas de adyacencia están en orden alfabético.) | <!-- Start of picture text --> | — | 29 |
| `45-ejemplo-la-cola-obliga-a-procesar-el-gra.md` | Ejemplo: la cola obliga a procesar el grafo por capas (8/9: Suponemos que las listas de adyacencia están en orden alfabético.) | <!-- Start of picture text --> | — | 29 |
| `46-ejemplo-la-cola-obliga-a-procesar-el-gra.md` | Ejemplo: la cola obliga a procesar el grafo por capas (9/9: Suponemos que las listas de adyacencia están en orden alfabético.) | <!-- Start of picture text --> | — | 29 |
| `47-al-terminar-las-capas-coinciden-con-las-.md` | Al terminar, las capas coinciden con las distancias | <!-- Start of picture text --> | — | 38 |
| `48-cada-valor-d-v-es-la-longitud-de-un-cami.md` | Cada valor _d_ [ _v_ ] es la longitud de un camino encontrado (1/3) | — | — | 2 |
| `49-lema.md` | Lema (3/6: Lema) | Al terminar BFS, para todo v ∈ V ( G ), | `Lema` | 36 |
| `50-cada-valor-d-v-es-la-longitud-de-un-cami.md` | Cada valor _d_ [ _v_ ] es la longitud de un camino encontrado (2/3) | — | — | 2 |
| `51-lema.md` | Lema (4/6: Lema) | Al terminar BFS, para todo v ∈ V ( G ), | `Demostración`, `Lema` | 42 |
| `52-cada-valor-d-v-es-la-longitud-de-un-cami.md` | Cada valor _d_ [ _v_ ] es la longitud de un camino encontrado (3/3) | — | — | 2 |
| `53-lema.md` | Lema (5/6: Lema) | Al terminar BFS, para todo v ∈ V ( G ), | `Demostración`, `Lema` | 48 |
| `54-la-cola-contiene-v-rtices-de-a-lo-sumo-d.md` | La cola contiene vértices de a lo sumo dos capas (1/3) | — | — | 2 |
| `55-lema-de-la-cola.md` | Lema de la cola (1/3: Lema de la cola) | Si Q = ⟨v 1 , v 2 , . . . , vr ⟩ , entonces d [ v 1] ≤ d [ v 2] ≤· · · ≤ d [ vr ] ≤ d [ v 1] + 1 . | `Lema de la cola` | 34 |
| `56-la-cola-contiene-v-rtices-de-a-lo-sumo-d.md` | La cola contiene vértices de a lo sumo dos capas (2/3) | — | — | 2 |
| `57-lema-de-la-cola.md` | Lema de la cola (2/3: Lema de la cola) | Si Q = ⟨v 1 , v 2 , . . . , vr ⟩ , entonces d [ v 1] ≤ d [ v 2] ≤· · · ≤ d [ vr ] ≤ d [ v 1] + 1 . | `Idea de la demostración`, `Lema de la cola` | 46 |
| `58-la-cola-contiene-v-rtices-de-a-lo-sumo-d.md` | La cola contiene vértices de a lo sumo dos capas (3/3) | — | — | 2 |
| `59-lema-de-la-cola.md` | Lema de la cola (3/3: Lema de la cola) | Si Q = ⟨v 1 , v 2 , . . . , vr ⟩ , entonces d [ v 1] ≤ d [ v 2] ≤· · · ≤ d [ vr ] ≤ d [ v 1] + 1 . | `Idea de la demostración`, `Lema de la cola` | 48 |
| `60-bfs-calcula-las-distancias-m-nimas-desde.md` | BFS calcula las distancias mínimas desde _s_ (1/3) | — | — | 2 |
| `61-teorema.md` | Teorema (5/7: Teorema) | Para todo v ∈ V ( G ), al terminar BFS, d [ v ] = δ ( s, v ). Además, para todo vértice v̸ = s alcanzable… | `Teorema` | 34 |
| `62-bfs-calcula-las-distancias-m-nimas-desde.md` | BFS calcula las distancias mínimas desde _s_ (2/3) | — | — | 2 |
| `63-teorema.md` | Teorema (6/7: Teorema) | Para todo v ∈ V ( G ), al terminar BFS, d [ v ] = δ ( s, v ). Además, para todo vértice v̸ = s alcanzable… | `Idea de la demostración`, `Teorema` | 36 |
| `64-bfs-calcula-las-distancias-m-nimas-desde.md` | BFS calcula las distancias mínimas desde _s_ (3/3) | — | — | 2 |
| `65-teorema.md` | Teorema (7/7: Teorema) | Para todo v ∈ V ( G ), al terminar BFS, d [ v ] = δ ( s, v ). Además, para todo vértice v̸ = s alcanzable… | `Idea de la demostración`, `Teorema` | 40 |
| `66-rbol-bfs-y-reconstrucci-n-de-caminos-m-n.md` | Árbol BFS y reconstrucción de caminos mínimos | — | — | 2 |
| `67-subgrafo-de-predecesores.md` | Subgrafo de predecesores | Después de ejecutar BFS( G, s ), definimos Gπ = ( Vπ, Eπ ), donde | `árbol BFS con raíz`, `Subgrafo de predecesores` | 20 |
| `68-lema.md` | Lema (6/6: Lema) | PRINT-PATH( G, s, v ) | `entonces`, `sino`, `Lema` | 54 |
| `69-descansamos-10-minutos.md` | ¿Descansamos 10 minutos? | 2<sup>do</sup> Cuatrimestre de 2026 28 / 58 | — | 22 |
| `70-dfs-avanza-mientras-encuentra-v-rtices-n.md` | DFS avanza mientras encuentra vértices no descubiertos | La búsqueda en profundidad (DFS) explora las aristas que salen del vértice descubierto más recientemente que… | `descubierto más recientemente`, `bosque` | 29 |
| `71-los-predecesores-forman-un-bosque-dfs.md` | Los predecesores forman un bosque DFS | Cuando DFS descubre a v al examinar una arista ( u, v ), asigna | `subgrafo de predecesores`, `bosque DFS`, `aristas del árbol` | 59 |
| `72-los-colores-indican-el-estado-de-la-llam.md` | Los colores indican el estado de la llamada recursiva | Blanco: todavía no fue descubierto | — | 62 |
| `73-tiempos-de-descubrimiento-y-de-finalizac.md` | Tiempos de descubrimiento y de finalización | <!-- Start of picture text --> | — | 29 |
| `74-dfs-inicia-una-visita-desde-cada-v-rtice.md` | DFS inicia una visita desde cada vértice que sigue blanco | La primera iteración inicializa todos los vértices. La segunda recorre V ( G ): cada llamada realizada allí… | `para cada`, `Procedimiento`, `hacer si`, `entonces` | 26 |
| `75-dfs-visit-profundiza-y-luego-retrocede.md` | DFS-VISIT profundiza y luego retrocede | tiempo ← tiempo + 1 d [ u ] ← tiempo color[ u ] ← gris para cada v ∈ Adj[ u ] hacer si color[ v ] = blanco… | `Procedimiento`, `para cada`, `hacer si`, `entonces` | 24 |
| `76-ejemplo-dirigido-fijamos-el-orden-de-exp.md` | Ejemplo dirigido: fijamos el orden de exploración | El bucle exterior considera u, v , w, x, y , z , en ese orden, y las listas de adyacencia son: | — | 26 |
| `77-corrida-paso-a-paso-dfs-profundiza-antes.md` | Corrida paso a paso: DFS profundiza antes de retroceder (1/12) | <!-- Start of picture text --> | — | 33 |
| `78-corrida-paso-a-paso-dfs-profundiza-antes.md` | Corrida paso a paso: DFS profundiza antes de retroceder (2/12) | <!-- Start of picture text --> | — | 33 |
| `79-corrida-paso-a-paso-dfs-profundiza-antes.md` | Corrida paso a paso: DFS profundiza antes de retroceder (3/12) | <!-- Start of picture text --> | — | 29 |
| `80-corrida-paso-a-paso-dfs-profundiza-antes.md` | Corrida paso a paso: DFS profundiza antes de retroceder (4/12) | <!-- Start of picture text --> | — | 29 |
| `81-corrida-paso-a-paso-dfs-profundiza-antes.md` | Corrida paso a paso: DFS profundiza antes de retroceder (5/12) | <!-- Start of picture text --> | — | 29 |
| `82-corrida-paso-a-paso-dfs-profundiza-antes.md` | Corrida paso a paso: DFS profundiza antes de retroceder (6/12) | <!-- Start of picture text --> | — | 29 |
| `83-corrida-paso-a-paso-dfs-profundiza-antes.md` | Corrida paso a paso: DFS profundiza antes de retroceder (7/12) | <!-- Start of picture text --> | — | 29 |
| `84-corrida-paso-a-paso-dfs-profundiza-antes.md` | Corrida paso a paso: DFS profundiza antes de retroceder (8/12) | <!-- Start of picture text --> | — | 29 |
| `85-corrida-paso-a-paso-dfs-profundiza-antes.md` | Corrida paso a paso: DFS profundiza antes de retroceder (9/12) | <!-- Start of picture text --> | — | 29 |
| `86-corrida-paso-a-paso-dfs-profundiza-antes.md` | Corrida paso a paso: DFS profundiza antes de retroceder (10/12) | <!-- Start of picture text --> | — | 29 |
| `87-corrida-paso-a-paso-dfs-profundiza-antes.md` | Corrida paso a paso: DFS profundiza antes de retroceder (11/12) | <!-- Start of picture text --> | — | 29 |
| `88-corrida-paso-a-paso-dfs-profundiza-antes.md` | Corrida paso a paso: DFS profundiza antes de retroceder (12/12) | <!-- Start of picture text --> | — | 29 |
| `89-la-corrida-produce-dos-rboles-y-doce-mar.md` | La corrida produce dos árboles y doce marcas temporales | <!-- Start of picture text --> | — | 38 |
| `90-el-orden-puede-cambiar-el-bosque.md` | El orden puede cambiar el bosque (1/2) | La salida concreta de DFS puede depender de dos decisiones: el orden en que el bucle exterior considera los… | — | 28 |
| `91-el-orden-puede-cambiar-el-bosque.md` | El orden puede cambiar el bosque (2/2) | La salida concreta de DFS puede depender de dos decisiones: | — | 60 |
| `92-los-tiempos-de-dfs-tienen-una-estructura.md` | Los tiempos de DFS tienen una estructura de paréntesis | El intervalo | — | 35 |
| `93-dos-intervalos-de-dfs-se-anidan-o-son-di.md` | Dos intervalos de DFS se anidan o son disjuntos (1/2) | — | — | 2 |
| `94-teorema-de-los-par-ntesis.md` | Teorema de los par ntesis (1/2: Teorema de los paréntesis) | Para cualesquiera u, v ∈ V , ocurre exactamente una de las siguientes posibilidades: 1 I ( u ) ∩ I ( v ) = ∅,… | `Teorema de los paréntesis` | 32 |
| `95-dos-intervalos-de-dfs-se-anidan-o-son-di.md` | Dos intervalos de DFS se anidan o son disjuntos (2/2) | — | — | 2 |
| `96-teorema-de-los-par-ntesis.md` | Teorema de los par ntesis (2/2: Teorema de los paréntesis) | Para cualesquiera u, v ∈ V , ocurre exactamente una de las siguientes posibilidades: 1 I ( u ) ∩ I ( v ) = ∅,… | `Idea de la demostración`, `Teorema de los paréntesis` | 38 |
| `97-los-tiempos-permiten-reconocer-descendie.md` | Los tiempos permiten reconocer descendientes | — | — | 2 |
| `98-corolario.md` | Corolario | Un vértice v es descendiente propio de u en el bosque DFS si y solo si | `Idea de la demostración`, `Corolario` | 56 |
| `99-un-camino-blanco-caracteriza-a-los-desce.md` | Un camino blanco caracteriza a los descendientes (2/2) | — | — | 2 |

## Mapa de conceptos

Concepto → archivos donde aparece definido o usado.

- **1. Descubre** → `136-al-retroceder-dfs-completa-f-y-propaga-l.md`
- **1. Inicialización** → `123-c-lculo-offline-de-low.md`
- **10. Finaliza** → `145-al-retroceder-dfs-completa-f-y-propaga-l.md`
- **10. Se procesa la raíz** → `132-c-lculo-offline-de-low.md`
- **11. Finaliza** → `146-al-retroceder-dfs-completa-f-y-propaga-l.md`
- **11. Se aplica el criterio de puente** → `133-c-lculo-offline-de-low.md`
- **12. Finaliza** → `147-al-retroceder-dfs-completa-f-y-propaga-l.md`
- **13. Ahora** → `148-al-retroceder-dfs-completa-f-y-propaga-l.md`
- **14. Finaliza** → `149-al-retroceder-dfs-completa-f-y-propaga-l.md`
- **15. Finaliza** → `150-al-retroceder-dfs-completa-f-y-propaga-l.md`
- **16. Finaliza la raíz** → `151-al-retroceder-dfs-completa-f-y-propaga-l.md`
- **17. Se aplica el criterio de puente** → `152-al-retroceder-dfs-completa-f-y-propaga-l.md`
- **2. Avanza por** → `137-al-retroceder-dfs-completa-f-y-propaga-l.md`
- **2. Se procesa la arista de retroceso** → `124-c-lculo-offline-de-low.md`
- **3. Avanza por** → `138-al-retroceder-dfs-completa-f-y-propaga-l.md`
- **3. Se procesa la arista de retroceso** → `125-c-lculo-offline-de-low.md`
- **4. Desde** → `139-al-retroceder-dfs-completa-f-y-propaga-l.md`
- **5. Avanza por** → `140-al-retroceder-dfs-completa-f-y-propaga-l.md`
- **5. Se procesa** → `127-c-lculo-offline-de-low.md`
- **6. Avanza por** → `141-al-retroceder-dfs-completa-f-y-propaga-l.md`
- **6. Se procesa** → `128-c-lculo-offline-de-low.md`
- **7. Avanza por** → `142-al-retroceder-dfs-completa-f-y-propaga-l.md`
- **7. Se procesa** → `129-c-lculo-offline-de-low.md`
- **8. Se procesa** → `130-c-lculo-offline-de-low.md`
- **9. Finaliza** → `144-al-retroceder-dfs-completa-f-y-propaga-l.md`
- **9. Se procesa** → `131-c-lculo-offline-de-low.md`
- **Algoritmo recursivo** → `20-algoritmo-recursivo.md`, `22-algoritmo-recursivo.md`
- **Cantidad de puentes** → `112-cantidad-de-puentes.md`, `115-cantidad-de-puentes.md`
- **Complejidad** → `23-complejidad.md`
- **Construcción del orden** → `25-una-cola-mantiene-los-v-rtices-disponibl.md`
- **Consultas Actualizaciones** → `07-los-costos-dependen-de-c-mo-implementamo.md`
- **Corolario** → `98-corolario.md`
- **Demostración** → `51-lema.md`, `53-lema.md`
- **Digrafos** → `06-el-espacio-de-las-listas-es-lineal-en-el.md`
- **Estructura** → `34-recorrer-un-grafo.md`
- **Estructura de datos** → `02-el-grafo-y-su-representaci-n-son-objetos.md`
- **Función** → `37-bfs-utiliza-una-cola-para-administrar-la.md`
- **Grafo** → `04-un-mismo-grafo-admite-distintas-represen.md`
- **Grafo con pocas aristas** → `09-la-operaci-n-dominante-orienta-la-elecci.md`
- **Grafo denso** → `09-la-operaci-n-dominante-orienta-la-elecci.md`
- **Grafos no dirigidos** → `06-el-espacio-de-las-listas-es-lineal-en-el.md`
- **Idea clave** → `105-el-color-del-destino-clasifica-la-arista.md`, `106-el-color-del-destino-clasifica-la-arista.md`
- **Idea de la demostración** → `102-teorema-del-camino-blanco.md`, `110-teorema.md`, `57-lema-de-la-cola.md`, `59-lema-de-la-cola.md`, `63-teorema.md`, `65-teorema.md`, `96-teorema-de-los-par-ntesis.md`, `98-corolario.md`
- **Idea del algoritmo** → `113-idea-del-algoritmo.md`, `116-idea-del-algoritmo.md`, `121-idea-del-algoritmo.md`
- **Inicialización** → `25-una-cola-mantiene-los-v-rtices-disponibl.md`, `26-ejemplo-la-cola-se-actualiza-al-eliminar.md`
- **La ejecución anterior devuelve** → `33-el-resultado-coloca-el-origen-antes-que-.md`
- **Lema** → `14-lema.md`, `16-lema.md`, `49-lema.md`, `51-lema.md`, `53-lema.md`, `68-lema.md`
- **Lema de la cola** → `55-lema-de-la-cola.md`, `57-lema-de-la-cola.md`, `59-lema-de-la-cola.md`
- **Listas** → `04-un-mismo-grafo-admite-distintas-represen.md`, `09-la-operaci-n-dominante-orienta-la-elecci.md`
- **Listas de adyacencia** → `10-los-pesos-se-almacenan-junto-con-las-ari.md`
- **Matriz** → `04-un-mismo-grafo-admite-distintas-represen.md`, `09-la-operaci-n-dominante-orienta-la-elecci.md`
- **Matriz de adyacencia** → `10-los-pesos-se-almacenan-junto-con-las-ari.md`
- **Objeto matemático** → `02-el-grafo-y-su-representaci-n-son-objetos.md`
- **Operaciones que nos interesan** → `03-representamos-el-grafo-mediante-sus-veci.md`
- **Orden de procesamiento** → `34-recorrer-un-grafo.md`
- **Procedimiento** → `122-low-puede-calcularse-despu-s-de-terminar.md`, `134-la-primera-fase-extiende-la-inicializaci.md`, `135-dfs-puentes-visit-calcula-low-al-retroce.md`, `74-dfs-inicia-una-visita-desde-cada-v-rtice.md`, `75-dfs-visit-profundiza-y-luego-retrocede.md`
- **Procesamos** → `27-ejemplo-la-cola-se-actualiza-al-eliminar.md`, `28-ejemplo-la-cola-se-actualiza-al-eliminar.md`
- **Procesamos c** → `29-ejemplo-la-cola-se-actualiza-al-eliminar.md`
- **Procesamos d** → `30-ejemplo-la-cola-se-actualiza-al-eliminar.md`
- **Procesamos e** → `31-ejemplo-la-cola-se-actualiza-al-eliminar.md`
- **Procesamos f** → `32-ejemplo-la-cola-se-actualiza-al-eliminar.md`
- **Propiedad que vamos a usar** → `118-propiedad-que-vamos-a-usar.md`
- **Recorrido** → `34-recorrer-un-grafo.md`
- **Subgrafo de predecesores** → `67-subgrafo-de-predecesores.md`
- **Teorema** → `108-teorema.md`, `110-teorema.md`, `157-teorema.md`, `17-teorema.md`, `61-teorema.md`, `63-teorema.md`, `65-teorema.md`
- **Teorema de los paréntesis** → `94-teorema-de-los-par-ntesis.md`, `96-teorema-de-los-par-ntesis.md`
- **Teorema del camino blanco** → `100-teorema-del-camino-blanco.md`, `102-teorema-del-camino-blanco.md`
- **Un hijo v termina de procesarse** → `154-un-hijo-v-termina-de-procesarse.md`
- **aristas del árbol** → `71-los-predecesores-forman-un-bosque-dfs.md`
- **bosque** → `70-dfs-avanza-mientras-encuentra-v-rtices-n.md`
- **bosque DFS** → `71-los-predecesores-forman-un-bosque-dfs.md`
- **descubierto más recientemente** → `70-dfs-avanza-mientras-encuentra-v-rtices-n.md`
- **devolver** → `25-una-cola-mantiene-los-v-rtices-disponibl.md`, `37-bfs-utiliza-una-cola-para-administrar-la.md`
- **en postorden de** → `122-low-puede-calcularse-despu-s-de-terminar.md`
- **encuentra la arista de retroceso** → `143-al-retroceder-dfs-completa-f-y-propaga-l.md`
- **entonces** → `122-low-puede-calcularse-despu-s-de-terminar.md`, `134-la-primera-fase-extiende-la-inicializaci.md`, `135-dfs-puentes-visit-calcula-low-al-retroce.md`, `155-la-segunda-fase-prueba-una-desigualdad-p.md`, `156-la-segunda-fase-prueba-una-desigualdad-p.md`, `25-una-cola-mantiene-los-v-rtices-disponibl.md`, `37-bfs-utiliza-una-cola-para-administrar-la.md`, `68-lema.md`, `74-dfs-inicia-una-visita-desde-cada-v-rtice.md`, `75-dfs-visit-profundiza-y-luego-retrocede.md`
- **examina la arista** → `148-al-retroceder-dfs-completa-f-y-propaga-l.md`
- **hacer** → `25-una-cola-mantiene-los-v-rtices-disponibl.md`
- **hacer si** → `122-low-puede-calcularse-despu-s-de-terminar.md`, `134-la-primera-fase-extiende-la-inicializaci.md`, `135-dfs-puentes-visit-calcula-low-al-retroce.md`, `155-la-segunda-fase-prueba-una-desigualdad-p.md`, `156-la-segunda-fase-prueba-una-desigualdad-p.md`, `37-bfs-utiliza-una-cola-para-administrar-la.md`, `74-dfs-inicia-una-visita-desde-cada-v-rtice.md`, `75-dfs-visit-profundiza-y-luego-retrocede.md`
- **mientras** → `37-bfs-utiliza-una-cola-para-administrar-la.md`
- **ordenamiento topológico** → `12-un-orden-topol-gico-respeta-todas-las-ar.md`, `13-un-orden-topol-gico-respeta-todas-las-ar.md`, `15-un-orden-topol-gico-respeta-todas-las-ar.md`
- **para cada** → `122-low-puede-calcularse-despu-s-de-terminar.md`, `134-la-primera-fase-extiende-la-inicializaci.md`, `135-dfs-puentes-visit-calcula-low-al-retroce.md`, `155-la-segunda-fase-prueba-una-desigualdad-p.md`, `156-la-segunda-fase-prueba-una-desigualdad-p.md`, `37-bfs-utiliza-una-cola-para-administrar-la.md`, `74-dfs-inicia-una-visita-desde-cada-v-rtice.md`, `75-dfs-visit-profundiza-y-luego-retrocede.md`
- **para todo** → `25-una-cola-mantiene-los-v-rtices-disponibl.md`
- **retornar** → `122-low-puede-calcularse-despu-s-de-terminar.md`, `155-la-segunda-fase-prueba-una-desigualdad-p.md`, `156-la-segunda-fase-prueba-una-desigualdad-p.md`
- **sin pesos** → `35-bfs-explora-por-distancia-creciente-desd.md`
- **sino** → `68-lema.md`
- **subgrafo de predecesores** → `71-los-predecesores-forman-un-bosque-dfs.md`
- **visita primero a** → `139-al-retroceder-dfs-completa-f-y-propaga-l.md`
- **y descubre** → `137-al-retroceder-dfs-completa-f-y-propaga-l.md`, `138-al-retroceder-dfs-completa-f-y-propaga-l.md`, `140-al-retroceder-dfs-completa-f-y-propaga-l.md`, `141-al-retroceder-dfs-completa-f-y-propaga-l.md`, `142-al-retroceder-dfs-completa-f-y-propaga-l.md`
- **y vuelve a** → `144-al-retroceder-dfs-completa-f-y-propaga-l.md`, `145-al-retroceder-dfs-completa-f-y-propaga-l.md`, `146-al-retroceder-dfs-completa-f-y-propaga-l.md`, `147-al-retroceder-dfs-completa-f-y-propaga-l.md`, `149-al-retroceder-dfs-completa-f-y-propaga-l.md`, `150-al-retroceder-dfs-completa-f-y-propaga-l.md`
- **árbol BFS con raíz** → `67-subgrafo-de-predecesores.md`
