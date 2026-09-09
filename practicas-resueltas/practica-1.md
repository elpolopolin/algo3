# Práctica 1 — Demostraciones

Resolución de los 20 ejercicios. La teoría sale de
`../context/teoria/demostraciones/` (unidad **demostraciones**, 187 temas).

**Cómo demostramos** (el molde que se repite en toda la práctica), de
`context/teoria/demostraciones/temas/34-39-c-mo-demostramos.md`:

1. **Formalizar la consigna** — traducir el enunciado a objetos matemáticos.
2. **Comprender qué se pide** — ¿qué asumo? ¿qué tengo que probar?
3. **Considerar ejemplos** — casos chicos, buscar contraejemplos (pero *los
   ejemplos no demuestran*).
4. **Argumento intuitivo** — ¿por qué es cierto?
5. **Elegir estrategia** — inducción, contradicción, contrarrecíproco, partir
   en casos.
6. **Pasar en limpio** — que el lector siga cada paso.

**La conversación Alicia (demuestra) / Beto (escéptico)**, de
`temas/52-57-comprender-qu-se-nos-pide-la-conversaci-.md`:

| Objetivo | Quién juega |
|---|---|
| Probar `∀x. P(x)` | Beto elige el `x`; Alicia responde para *ese* `x` |
| Probar `∃x. P(x)` | Alicia da un `x` concreto y muestra que cumple |
| Probar `P ⇒ Q` | Alicia asume `P` (y lo dice) y deduce `Q` |
| Refutar `∀x. P(x)` | Alicia da **un** `x` que falla (contraejemplo) |

**Los 6 tips** (`temas/177-182-tips-para-escribir-demostraciones.md`), que son
literalmente la grilla de correção de esta práctica:

1. Definí `P(n)` explícitamente, con todos los cuantificadores, antes de empezar.
2. Contá **cuántos casos base** necesita el paso inductivo (¿usa `P(n−1)`?
   ¿`P(n−2)`? ¿`P(n−4)`?).
3. Decí **dónde** usás la hipótesis inductiva (HI) y verificá que el valor cae
   dentro de ℕ y del rango donde vale.
4. Ponele **nombre** a todo, cuantificá todo, **no reuses nombres**.
5. Si decís «sea `x` el mínimo tal que…», probá que el conjunto es **no vacío**.
6. Releé como Beto: ¿en qué oración le mentirías?

---

## Ejercicio 1 — Lógica proposicional

### Qué pide

Dados predicados `A`, `B`, `C`, decidir si cada fórmula es verdadera (tautología,
vale para toda asignación) o falsa, y en ese caso dar un contraejemplo (una
asignación de valores que la rompe).

### Qué teoría aplica

Es el paso previo a todo: *formalizar* y entender qué significa cada conector.
No hay una diapositiva de tablas de verdad en la unidad, así que la mecánica de
tablas es **fuera de fuente** (lógica básica), pero el criterio es el de la
materia: refutar un `∀` (acá: «para toda asignación») es dar **una** asignación
que falla — la jugada de Beto la hace Alicia
(`temas/53-comprender-qu-se-nos-pide-la-conversaci-.md`).

Recordá: `A ⇒ B` es falso **solo** cuando `A` es verdadero y `B` falso.

### Resolución

**a) `A ∧ B ⇒ A`. Verdadera.**
Si `A ∧ B` es verdadero, entonces `A` es verdadero, así que el consecuente vale.
El único modo de que falle sería `A ∧ B` verdadero y `A` falso, imposible.

**b) `A ∨ B ⇒ A`. Falsa.**
Contraejemplo: `A = F`, `B = V`. Antecedente `F ∨ V = V`, consecuente `A = F`.
`V ⇒ F` es falso.

**c) `(A ⇒ B) ⇒ (A ⇒ C)`. Falsa.**
Contraejemplo: `A = V`, `B = V`, `C = F`. Antecedente `A ⇒ B = V`. Consecuente
`A ⇒ C = V ⇒ F = F`. Todo: `V ⇒ F = F`.
(Intuición: que `B` se siga de `A` no dice nada sobre `C`.)

**d) `[(A ⇒ B) ∧ (B ⇒ C)] ⇒ (A ⇒ C)`. Verdadera** (silogismo hipotético /
transitividad de `⇒`).
Supongamos el antecedente: `A ⇒ B` y `B ⇒ C`. Queremos `A ⇒ C`: asumimos `A`.
Por `A ⇒ B`, vale `B`. Por `B ⇒ C`, vale `C`. Luego `A ⇒ C`.
El único caso a revisar es `A ⇒ C` falso, o sea `A = V`, `C = F`: entonces
`A ⇒ B` fuerza `B = V`, y `B ⇒ C` da `V ⇒ F = F`, con lo cual el antecedente es
falso y la implicación global, verdadera.

**e) `(¬A ∧ B) ⇔ ¬(A ∨ ¬B)`. Verdadera.**
Por De Morgan: `¬(A ∨ ¬B) ≡ ¬A ∧ ¬(¬B) ≡ ¬A ∧ B`. Los dos lados del `⇔` son la
misma fórmula, así que la equivalencia vale para toda asignación.

### Fuentes

- `../context/teoria/demostraciones/temas/53-comprender-qu-se-nos-pide-la-conversaci-.md` — refutar un `∀` es dar un caso.
- Mecánica de tablas de verdad: *fuera de fuente* (no está en la unidad).

---

## Ejercicio 2 — Tres intentos de demostrar «n impar ⇒ n² impar»

### Qué pide

Decidir si cada intento es una demostración válida y justificar.

### Qué teoría aplica

- *Los ejemplos no demuestran*: verificar casos «no es una demostración»
  (`temas/58-ejemplo.md`, el caso Goldbach).
- *Rigor*: cada oración se tiene que seguir de la anterior; nada de «porque sí»
  (`temas/15-formalidad-y-rigor.md`).
- *Usar las definiciones formales*: `n` impar `⟺ ∃k. n = 2k+1`.

### Resolución

**a) «Si n = 3, entonces n² = 9, impar. Por lo tanto vale para todo n.»
Incorrecta.**
Un caso —o mil— no prueban un `∀`. Es exactamente el error del apunte con la
conjetura de Goldbach: «verificar que es cierto para todos los casos que se me
ocurren» no es demostración. Beto elige `n`, y `n = 3` es la jugada cómoda que
Alicia **no** puede elegir.

**b) «Sea n impar. Entonces n² es impar porque los impares al cuadrado son
impares.» Incorrecta.**
Es circular: la justificación («los impares al cuadrado son impares») es
*exactamente* lo que hay que probar. No usa la definición de impar ni ninguna
propiedad previa. Falla el rigor: Beto pregunta «¿y esto por qué vale?» y no hay
respuesta.

**c) «Sea n impar. Entonces n = 2k+1 para algún entero k. Luego
n² = (2k+1)² = 4k² + 4k + 1 = 2(2k² + 2k) + 1, impar.» Correcta.**
Formaliza «impar» con la definición (`n = 2k+1`), opera, y exhibe `n²` en la
forma `2·(entero) + 1`, que es la definición de impar. Cada paso es álgebra
verificable. Está bien.

### Fuentes

- `../context/teoria/demostraciones/temas/58-ejemplo.md` — los ejemplos no demuestran (Goldbach).
- `../context/teoria/demostraciones/temas/15-formalidad-y-rigor.md` — rigor: seguir cada paso.
- `../context/teoria/demostraciones/temas/162-contrarrec-proco.md` — la misma cuenta `(2k+1)² = 2(2k²+2k)+1` aparece en la teoría.

---

## Ejercicio 3 — El error del nombre reusado

### Qué pide

En la «demostración» de que par × impar es par, encontrar el error y
reescribirla bien.

### Qué teoría aplica

Tip 4: **no reuses nombres** (`temas/180-tips-para-escribir-demostraciones.md`).
Definiciones formales de par (`m = 2k`) e impar (`n = 2k+1`).

### El error

La demostración escribe:

> Como `m` es par, existe un entero `k` tal que `m = 2k`. Como `n` es impar,
> existe un entero `k` tal que `n = 2k + 1`.

Usa **la misma letra `k`** para dos cosas independientes. Eso obliga a
`m = 2k` y `n = 2k+1` con el *mismo* `k`, es decir `n = m + 1`: solo cubre los
pares en que el impar es el siguiente del par (`m = 4, n = 5`), no el caso
general (`m = 4, n = 7`). El resultado final es cierto, pero la cuenta
`mn = 2k(2k+1)` está probando otra cosa.

### Reescritura correcta

Sean `m`, `n` enteros con `m` par y `n` impar.

- Como `m` es par, existe un entero `k` tal que `m = 2k`.
- Como `n` es impar, existe un entero `j` tal que `n = 2j + 1` (**otro** nombre).

Entonces

    m·n = (2k)(2j + 1) = 2·(k(2j + 1)).

Sea `s = k(2j + 1)`, que es entero. Tenemos `m·n = 2s`, así que `m·n` es par. ∎

(Ni siquiera hace falta desarrollar el cuadrado: factorizar el `2` de `m` alcanza.)

### Fuentes

- `../context/teoria/demostraciones/temas/180-tips-para-escribir-demostraciones.md` — «no reusen nombres».

---

## Ejercicio 4 — Contraejemplo de «∀n∈ℕ, n² ≤ 3n»

### Qué pide

Mostrar que la afirmación es falsa dando un contraejemplo.

### Qué teoría aplica

Refutar un `∀` = exhibir **un** `n` que falla
(`temas/53-comprender-qu-se-nos-pide-la-conversaci-.md`,
`temas/72-y-para-probar-que-no-pertenece.md`: «negar un `∃`/`∀`»).

### Resolución

Tomemos `n = 4`. Entonces `n² = 16` y `3n = 12`, y `16 ≤ 12` es falso.
Luego la afirmación «para todo `n ∈ ℕ`, `n² ≤ 3n`» es falsa. ∎

Para entender por qué (no hace falta para responder): la desigualdad
`n² ≤ 3n` equivale, para `n ≥ 1`, a `n ≤ 3`. Vale para `n ∈ {0,1,2,3}` y falla
para todo `n ≥ 4`. Cualquiera de esos `n` es contraejemplo válido; alcanza con
uno.

### Fuentes

- `../context/teoria/demostraciones/temas/72-y-para-probar-que-no-pertenece.md` — negar un cuantificador con un testigo.

---

## Ejercicio 5 — «∀n impar, ∃ r,s: r+s = n y r−s = 1»

### Qué pide

Demostrar la existencia de `r` y `s`.

### Qué teoría aplica

Probar `∀x. ∃y. P(x, y)`: Beto da el `x` (el `n` impar), Alicia da un `y` (el
par `r,s`) que **puede depender de `x`**
(`temas/54` y `56-comprender-qu-se-nos-pide-la-conversaci-.md`). Demostración
directa: dar el testigo y verificar.

### Resolución

Sea `n ∈ ℕ` impar. Por definición, existe `k ∈ ℕ` con `n = 2k + 1`.

Proponemos `r = k + 1` y `s = k` (dependen de `n` vía `k`). Verificamos:

- `r + s = (k + 1) + k = 2k + 1 = n`. ✓
- `r − s = (k + 1) − k = 1`. ✓

Luego, para todo `n` impar existen `r, s` enteros con `r + s = n` y `r − s = 1`. ∎

(De dónde salen: sumando las dos ecuaciones, `2r = n + 1`, o sea `r = (n+1)/2`,
que es entero justamente porque `n` es impar; y `s = r − 1`.)

### Fuentes

- `../context/teoria/demostraciones/temas/54-comprender-qu-se-nos-pide-la-conversaci-.md` — probar `∃` dando un testigo concreto.

---

## Ejercicio 6 — Elevar al cubo mantiene la paridad

### Qué pide

Demostrar que `n³` tiene la misma paridad que `n`, usando las definiciones
formales.

### Qué teoría aplica

Definiciones: par `⟺ ∃k. n = 2k`, impar `⟺ ∃k. n = 2k+1`. Partir en casos
(`temas/38-c-mo-demostramos.md`). Alternativa: contrarrecíproco
(`temas/162-contrarrec-proco.md`).

### Resolución (directa, por casos)

Sea `n ∈ ℤ`. Todo entero es par o impar.

**Caso `n` par.** Existe `k` con `n = 2k`. Entonces

    n³ = (2k)³ = 8k³ = 2·(4k³),

y `4k³` es entero, así que `n³` es par.

**Caso `n` impar.** Existe `k` con `n = 2k + 1`. Entonces

    n³ = (2k+1)³ = 8k³ + 12k² + 6k + 1 = 2·(4k³ + 6k² + 3k) + 1,

y `4k³ + 6k² + 3k` es entero, así que `n³` es impar.

En ambos casos `n³` tiene la paridad de `n`. ∎

### Fuentes

- `../context/teoria/demostraciones/temas/38-c-mo-demostramos.md` — partir en casos como estrategia.
- `../context/teoria/demostraciones/temas/162-contrarrec-proco.md` — molde `(2k+1)ⁿ = 2(...)+1`.

---

## Ejercicio 7 — 20 pelotas en 3 cajas: alguna caja tiene una cantidad par

### Qué pide

Demostrar **por contradicción** que en toda distribución de 20 pelotas en 3
cajas, alguna caja tiene una cantidad par (el 0 cuenta como par).

### Qué teoría aplica

Contradicción: asumir `¬P` y derivar algo falso, **diciéndolo explícitamente**
(`temas/164-contradicci-n-absurdo.md`). La cuenta es la misma idea que la
demostración del palomar (`temas/167-principio-del-palomar-versi-n-simple.md`):
sumar las cantidades y llegar a un absurdo numérico.

### Resolución

Sean `c₁, c₂, c₃` las cantidades de pelotas en cada caja, con
`c₁ + c₂ + c₃ = 20`.

Supongamos por contradicción que **ninguna** caja tiene una cantidad par, es
decir, `c₁, c₂, c₃` son los tres impares.

La suma de tres números impares es impar:
`(2a+1) + (2b+1) + (2c+1) = 2(a + b + c + 1) + 1`.

Entonces `c₁ + c₂ + c₃` es impar. Pero `c₁ + c₂ + c₃ = 20`, que es par. Absurdo.

Luego alguna caja tiene una cantidad par de pelotas. ∎

(El «20» no importa: sirve cualquier total par y cualquier cantidad impar de
cajas.)

### Fuentes

- `../context/teoria/demostraciones/temas/164-contradicci-n-absurdo.md` — decir «asumimos por contradicción» y marcar el absurdo.
- `../context/teoria/demostraciones/temas/167-principio-del-palomar-versi-n-simple.md` — sumar y llegar a la contradicción numérica.

---

## Ejercicio 8 — Completar la inducción de `∑_{i=1}^{n} i = n(n+1)/2`

### Qué pide

Completar el paso inductivo de la demostración por inducción.

### Qué teoría aplica

Cómo se escribe una inducción, los 4 pasos
(`temas/88-91-c-mo-se-escribe-una-demostraci-n-por-ind.md`): definir `P(n)`,
caso base, paso inductivo **marcando dónde se usa la HI**, concluir. Molde de la
suma geométrica: separar el último término
(`temas/100-102-ejemplo-una-suma-geom-trica.md`).

### Resolución

`P(n) : ∑_{i=1}^{n} i = n(n+1)/2`, para `n ≥ 1`. Usa solo `P(n)`, así que un
caso base alcanza.

**Caso base `P(1)`:** `∑_{i=1}^{1} i = 1 = 1·2/2`. ✓ (ya estaba).

**Paso inductivo `∀n ≥ 1: P(n) ⇒ P(n+1)`:** sea `n ≥ 1`. **Asumimos la HI:**
`∑_{i=1}^{n} i = n(n+1)/2`. Queremos `∑_{i=1}^{n+1} i = (n+1)(n+2)/2`.

Separamos el último término:

    ∑_{i=1}^{n+1} i = ( ∑_{i=1}^{n} i ) + (n+1)
                    = n(n+1)/2 + (n+1)          ← acá usamos la HI
                    = (n+1)·( n/2 + 1 )
                    = (n+1)(n+2)/2.

Luego vale `P(n+1)`.

**Conclusión:** por inducción, `∑_{i=1}^{n} i = n(n+1)/2` para todo `n ≥ 1`. ∎

### Fuentes

- `../context/teoria/demostraciones/temas/89-c-mo-se-escribe-una-demostraci-n-por-ind.md` — asumir la HI, decirlo, marcar dónde se usa.
- `../context/teoria/demostraciones/temas/100-proposici-n.md` — «separar el último término: ahí entra la HI».

---

## Ejercicio 9 — Error en «para todo a ≠ 0, aⁿ = 1»

### Qué pide

Encontrar el error de la demostración por inducción.

### Qué teoría aplica

**¡Cuidado con cuántos casos base!**
(`temas/122-127-advertencia.md`): si el paso inductivo usa `P(n−1)` **y**
`P(n−2)`, hacen falta **dos** casos base (`P(0)` y `P(1)`). Si no, la cadena de
dominó no arranca bien.

### El error

El paso inductivo escribe

    aⁿ = (a^{n−1} · a^{n−1}) / a^{n−2} = (1·1)/1 = 1,

usando la HI en `n−1` **y** en `n−2`. Es decir, usa `P(n−1)` y `P(n−2)`, así que
necesita **dos** casos base: `P(0)` y `P(1)`.

Solo se probó `P(0)` (`a⁰ = 1`, cierto). Falta `P(1)`: `a¹ = a`, que **no** es
`1` salvo `a = 1`. Como `P(1)` es falso, el paso inductivo nunca puede
propagarse de `{P(0), P(1)}` a `P(2)`: la ficha `P(1)` no cae, y todo el efecto
dominó se corta ahí.

(Además, para `n = 1` la fórmula usa `a^{n−2} = a^{−1}`, que se sale del dominio
`n ∈ ℕ` — otro sínt del mismo problema: tip 3, «verificá que el valor donde
usás la HI cae dentro de ℕ».)

### Fuentes

- `../context/teoria/demostraciones/temas/122-advertencia.md`, `123-advertencia.md` — «si usa `P(n−1)` y `P(n−2)`: pruebo a mano `P(0)` y `P(1)`».
- `../context/teoria/demostraciones/temas/179-tips-para-escribir-demostraciones.md` — verificar que la HI se usa dentro de ℕ.

---

## Ejercicio 10 — Error en «todos los elementos de un conjunto son iguales»

### Qué pide

Encontrar el error de la demostración (es el clásico «todos los caballos son del
mismo color»).

### Qué teoría aplica

Tip 6 y tip 3: releer el paso inductivo **para todos los `n`**, incluido el
borde, y chequear que el argumento realmente vale ahí
(`temas/182` y `179-tips-para-escribir-demostraciones.md`). El principio de
inducción exige `P(n) ⇒ P(n+1)` para **todo** `n`
(`temas/83-el-principio-de-inducci-n.md`).

### El error

El paso inductivo, de `n−1` a `n`, dice: «`x₁ = … = x_{n−1}` por HI, y aplicando
la HI a un subconjunto de dos elementos, `x_{n−1} = xₙ`, así que todos son
iguales».

Ese argumento necesita que los dos bloques de `n−1` elementos que compara
—`{x₁,…,x_{n−1}}` y `{x₂,…,xₙ}`— **se solapen en al menos un elemento** (el
`x_{n−1}`), para encadenar las igualdades.

Para `n ≥ 3` se solapan. Pero el paso **de `n−1 = 1` a `n = 2`** falla: los
bloques son `{x₁}` y `{x₂}`, que **no comparten ningún elemento**. No hay
puente entre `x₁` y `x₂`. La implicación `P(1) ⇒ P(2)` es falsa, y con eso se
cae todo (de `P(2)` en adelante nunca se prueba nada).

Moraleja: un paso inductivo que «casi siempre» funciona no sirve; tiene que
valer para **todos** los `n`.

### Fuentes

- `../context/teoria/demostraciones/temas/83-el-principio-de-inducci-n.md` — el paso pide `P(n) ⇒ P(n+1)` para todo `n`.
- `../context/teoria/demostraciones/temas/182-tips-para-escribir-demostraciones.md` — releer como Beto: ¿en qué oración le mentirías?

---

## Ejercicio 11 — Error(es) en «conjunto con un positivo ⇒ suma positiva»

### Qué pide

Encontrar el error (¿hay más de uno?) y reescribir bien.

Enunciado: si un conjunto de enteros **no negativos** tiene al menos un
**positivo**, entonces la suma de sus elementos es positiva.

### Qué teoría aplica

- Tip 3: al usar la HI hay que verificar que la entrada más chica **sigue
  cumpliendo las hipótesis** (`temas/179`).
- El truco del «primer elemento» / demostración directa como alternativa limpia
  a una inducción que se complica (`temas/170-176-el-truco-del-primer-elemento-que-cumple.md`).
- La inducción es **sobre un tamaño natural** (`temas/92-advertencia.md`).

### Los errores

Paso inductivo del original: «saco un elemento cualquiera `k`, queda `C` de
`n−1` elementos, por HI la suma de `C` es positiva, y agregar `k ≥ 0` no la hace
no positiva».

1. **La HI no aplica a `C`.** La HI vale para conjuntos de `n−1` elementos *que
   tengan un positivo*. Si saco justo el único positivo, `C` queda con puros
   ceros y `∑C = 0`: no cumple la hipótesis, no puedo invocar la HI.
2. **Caso base insuficiente / inducción mal planteada.** Aun arreglando lo
   anterior (sacando un elemento no positivo), si el conjunto no tiene ningún
   elemento `= 0` no se puede «sacar un no positivo», y el argumento no cubre
   ese caso.
3. Menor: «agregar `k` no negativo no puede hacer la suma no positiva» es un
   `≥`, no da `> 0` por sí solo; depende de que `∑C > 0`, que es justo lo que
   está en duda.

### Reescritura correcta (directa, sin inducción)

Sea `S` un conjunto finito de enteros no negativos con al menos un elemento
positivo. Sea `p ∈ S` un elemento con `p > 0` (existe por hipótesis).

    ∑_{x ∈ S} x  =  p  +  ∑_{x ∈ S, x ≠ p} x.

Cada término de la segunda suma es `≥ 0` (los elementos son no negativos), así
que `∑_{x ≠ p} x ≥ 0`. Luego

    ∑_{x ∈ S} x  ≥  p  +  0  =  p  >  0. ∎

### Fuentes

- `../context/teoria/demostraciones/temas/179-tips-para-escribir-demostraciones.md` — verificar que la entrada chica cumple las hipótesis de la HI.
- `../context/teoria/demostraciones/temas/170-el-truco-del-primer-elemento-que-cumple.md` — a veces una directa reemplaza una inducción engorrosa.

---

## Ejercicio 12 — `1 + 3 + 5 + … + (2n+1) = (n+1)²` por inducción

### Qué pide

Probar por inducción para `n ≥ 0`.

### Qué teoría aplica

Los 4 pasos de una inducción (`temas/88-91`), caso base en `0`
(`temas/82-el-principio-de-inducci-n.md`).

### Resolución

`P(n) : ∑_{i=0}^{n} (2i+1) = (n+1)²`, para `n ≥ 0`. Un caso base.

**Base `P(0)`:** `∑_{i=0}^{0}(2i+1) = 1 = (0+1)²`. ✓

**Paso `∀n ≥ 0: P(n) ⇒ P(n+1)`:** sea `n ≥ 0`. **HI:**
`∑_{i=0}^{n}(2i+1) = (n+1)²`. Queremos `∑_{i=0}^{n+1}(2i+1) = (n+2)²`.

    ∑_{i=0}^{n+1}(2i+1) = ( ∑_{i=0}^{n}(2i+1) ) + (2(n+1)+1)
                        = (n+1)² + (2n+3)              ← HI
                        = n² + 2n + 1 + 2n + 3
                        = n² + 4n + 4
                        = (n+2)².

Luego `P(n+1)`.

**Conclusión:** por inducción, vale para todo `n ≥ 0`. ∎

### Fuentes

- `../context/teoria/demostraciones/temas/90-c-mo-se-escribe-una-demostraci-n-por-ind.md` — estructura completa de la inducción.

---

## Ejercicio 13 — Fórmula para `1 + 2 + 2² + … + 2ⁿ` y demostración

### Qué pide

Encontrar la fórmula cerrada y demostrarla por inducción.

### Qué teoría aplica

Es una suma geométrica; el molde exacto está en la teoría con base `3`
(`temas/100-102-ejemplo-una-suma-geom-trica.md`:
`∑_{i=0}^{n} 3ⁱ = (3^{n+1} − 1)/2`). Acá con base `2`.

### La fórmula

Probando casos: `n=0 → 1`; `n=1 → 3`; `n=2 → 7`; `n=3 → 15`. Son `2^{n+1} − 1`.

**Conjetura:** `∑_{i=0}^{n} 2ⁱ = 2^{n+1} − 1`.

### Demostración

`P(n) : ∑_{i=0}^{n} 2ⁱ = 2^{n+1} − 1`, `n ≥ 0`. Un caso base.

**Base `P(0)`:** `∑_{i=0}^{0} 2ⁱ = 1 = 2¹ − 1`. ✓

**Paso `∀n ≥ 0: P(n) ⇒ P(n+1)`:** sea `n ≥ 0`. **HI:**
`∑_{i=0}^{n} 2ⁱ = 2^{n+1} − 1`.

    ∑_{i=0}^{n+1} 2ⁱ = ( ∑_{i=0}^{n} 2ⁱ ) + 2^{n+1}
                     = (2^{n+1} − 1) + 2^{n+1}       ← HI
                     = 2·2^{n+1} − 1
                     = 2^{n+2} − 1.

Luego `P(n+1)`.

**Conclusión:** por inducción, `∑_{i=0}^{n} 2ⁱ = 2^{n+1} − 1` para todo
`n ≥ 0`. ∎

### Fuentes

- `../context/teoria/demostraciones/temas/101-ejemplo-una-suma-geom-trica.md` — misma suma geométrica con base 3.

---

## Ejercicio 14 — La colonia de hormigas

### Qué pide

Pasar a fórmulas y demostrar por inducción: la población se duplica cada año,
empieza en 10, ¿cuántas hay después de `n` años?

### Qué teoría aplica

**Formalizar la consigna**: un proceso que se repite ⇒ **sucesión definida por
recurrencia** (`temas/40-formalizar-la-consigna.md`,
`temas/42-ejercicio.md`). Es idéntico al ejemplo de la teoría (bacterias que se
triplican, `b₀ = 5`, `b_{n+1} = 3·bₙ`, se prueba `bₙ = 5·3ⁿ`,
`temas/45-versi-n-formalizada.md`).

### Formalización

Sea `a₀ = 10` y `a_{n+1} = 2·aₙ` para todo `n ∈ ℕ` (`aₙ` = hormigas después de
`n` años, contando `a₀` como la colonia inicial).

**Afirmación:** `∀n ∈ ℕ, aₙ = 10·2ⁿ`.

### Demostración

`P(n) : aₙ = 10·2ⁿ`. Un caso base (la recurrencia usa solo `aₙ`).

**Base `P(0)`:** `a₀ = 10 = 10·2⁰`. ✓

**Paso `∀n ∈ ℕ: P(n) ⇒ P(n+1)`:** sea `n ∈ ℕ`. **HI:** `aₙ = 10·2ⁿ`.

    a_{n+1} = 2·aₙ = 2·(10·2ⁿ) = 10·2^{n+1}.     ← HI en el segundo paso

Luego `P(n+1)`.

**Conclusión:** `aₙ = 10·2ⁿ` para todo `n ∈ ℕ`. Después de `n` años hay
`10·2ⁿ` hormigas. ∎

### Fuentes

- `../context/teoria/demostraciones/temas/40-formalizar-la-consigna.md` — proceso que se repite ⇒ sucesión por recurrencia.
- `../context/teoria/demostraciones/temas/45-versi-n-formalizada.md` — el mismo molde `b_{n+1} = c·bₙ ⇒ bₙ = b₀·cⁿ`.

---

## Ejercicio 15 — `2ⁿ > n²` para `n ≥ 5` (y qué pasa antes)

### Qué pide

Probar `2ⁿ > n²` para `n ≥ 5` por inducción, y analizar `n < 5`.

### Qué teoría aplica

**El caso base no tiene por qué ser 0** (`temas/103-111-el-caso-base-no-tiene-por-qu-ser-0.md`):
la inducción arranca en `n₀ = 5` y en el paso se toma `n ≥ 5`. La teoría hace
exactamente esto con `n! > 2ⁿ` para `n ≥ 4`.

### Análisis de `n < 5`

| n | 2ⁿ | n² | `2ⁿ > n²` |
|---|---|---|---|
| 0 | 1 | 0 | sí |
| 1 | 2 | 1 | sí |
| 2 | 4 | 4 | **no** (igual) |
| 3 | 8 | 9 | **no** |
| 4 | 16 | 16 | **no** (igual) |
| 5 | 32 | 25 | sí |

La propiedad **falla para `n ∈ {2, 3, 4}`**. El caso base corrido a `5` no es un
capricho: antes de `5` la afirmación es directamente falsa.

### Demostración para `n ≥ 5`

`P(n) : 2ⁿ > n²`, `n ≥ 5`.

**Base `P(5)`:** `2⁵ = 32 > 25 = 5²`. ✓

**Paso `∀n ≥ 5: P(n) ⇒ P(n+1)`:** sea `n ≥ 5`. **HI:** `2ⁿ > n²`.

    2^{n+1} = 2·2ⁿ > 2·n²          ← HI

Basta ver que `2n² ≥ (n+1)²` para `n ≥ 5`:

    2n² − (n+1)² = n² − 2n − 1 = (n−1)² − 2 ≥ (5−1)² − 2 = 14 > 0.

Entonces `2n² > (n+1)²`, y encadenando: `2^{n+1} > 2n² > (n+1)²`.

Luego `P(n+1)`.

**Conclusión:** por inducción con caso base en `5`, `2ⁿ > n²` para todo
`n ≥ 5`. ∎

### Fuentes

- `../context/teoria/demostraciones/temas/104-el-caso-base-no-tiene-por-qu-ser-0.md` — mismo esquema con `n! > 2ⁿ`, `n ≥ 4`.
- `../context/teoria/demostraciones/temas/107-proposici-n.md` — «el caso base pasa a ser `P(4)`, y en el paso inductivo tomamos `n ≥ 4`».

---

## Ejercicio 16 — Triángulo de Pascal (inducción en tuplas)

### Qué pide

Pascalito llena una matriz infinita: `1` en la fila 0 y la columna 0; el resto,
suma de arriba + izquierda. Afirma que la celda `(f, c)` termina con

$$\binom{f+c}{f} = \frac{(f+c)!}{f!\;c!}$$

![fórmula de Pascalito](../context/practica/imagenes/practica_1_repaso.pdf-0003-20.png)

Probar por **inducción en la tupla `(f, c)`**, definiendo claramente cuándo un
par es «menor» que otro.

### Qué teoría aplica

**Inducción en tuplas / orden bien fundado**
(`temas/135-142-y-si-mi-objeto-tiene-dos-tama-os-inducci.md`,
`necesitamos-un-orden-bien-fundado.md`): necesito un orden `≺` sobre los pares
**sin cadenas infinitas decrecientes**; entonces puedo asumir `P(f', c')` para
todo `(f', c') ≺ (f, c)` (inducción fuerte). Dos elecciones típicas: **por una
medida** (`(f',c') ≺ (f,c)` si `f'+c' < f+c`) o **lexicográfica**. Lo clave:
**definir el orden explícitamente antes de arrancar**.

### Formalización

Sea `V(f, c)` el número que Pascalito escribe en `(f, c)`, definido por:

- `V(f, c) = 1` si `f = 0` o `c = 0`;
- `V(f, c) = V(f−1, c) + V(f, c−1)` si `f ≥ 1` y `c ≥ 1`.

**Orden.** Para pares `(f, c), (f', c') ∈ ℕ²` definimos

$$(f', c') \prec (f, c) \iff f' + c' < f + c.$$

Es bien fundado porque `f + c ∈ ℕ` y `ℕ` no tiene cadenas infinitas
decrecientes: cualquier `≺`-descenso baja el valor de `f + c`, que no puede
bajar para siempre.

`P(f, c) : V(f, c) = \binom{f+c}{f}`.

### Demostración (inducción fuerte en `≺`)

Sea `(f, c) ∈ ℕ²`. Asumimos como **HI** que `P(f', c')` vale para todo
`(f', c') ≺ (f, c)`.

**Caso borde: `f = 0` o `c = 0`.** Entonces `V(f, c) = 1`. Y
`\binom{f+c}{f}`: si `f = 0`, `\binom{c}{0} = 1`; si `c = 0`, `\binom{f}{f} = 1`.
En ambos, `V(f, c) = 1 = \binom{f+c}{f}`. (No se usa la HI: son los «casos
base», los pares con `f + c` mínimo entre los de su tipo.)

**Caso `f ≥ 1` y `c ≥ 1`.** Por definición,

    V(f, c) = V(f−1, c) + V(f, c−1).

Los pares `(f−1, c)` y `(f, c−1)` cumplen `(f−1)+c = f+(c−1) = f+c−1 < f+c`, así
que ambos son `≺ (f, c)` y **puedo usar la HI** en los dos:

    V(f−1, c) = \binom{f−1+c}{f−1},      V(f, c−1) = \binom{f+c−1}{f}.

Entonces

    V(f, c) = \binom{f+c−1}{f−1} + \binom{f+c−1}{f}.

Por la **identidad de Pascal** (`\binom{m−1}{k−1} + \binom{m−1}{k} = \binom{m}{k}`,
con `m = f+c`, `k = f`):

    V(f, c) = \binom{f+c}{f}.

Luego `P(f, c)`.

**Conclusión:** por inducción bien fundada sobre `≺`, `V(f, c) = \binom{f+c}{f}`
para todo `(f, c) ∈ ℕ²`. Pascalito no se equivoca. ∎

> Nota: `\binom{f+c}{f} = \binom{f+c}{c}` (elegir `f` de `f+c`, o los `c`
> restantes), así que la fórmula del enunciado y `(f+c)!/(f!c!)` son lo mismo.

### Fuentes

- `../context/teoria/demostraciones/temas/136-y-si-mi-objeto-tiene-dos-tama-os-inducci.md` — inducción en un par `(a, b)`.
- `../context/teoria/demostraciones/temas/138-necesitamos-un-orden-bien-fundado.md` — orden por una medida `a'+b' < a+b`.
- `../context/teoria/demostraciones/temas/142-necesitamos-un-orden-bien-fundado.md` — «definir el orden explícitamente antes de largar la inducción».

---

## Ejercicio 17 — Pascalito recursivo + tests

### Qué pide

Programar recursiva la función que da `V(f, c)`, y escribir tests usando la
**fórmula cerrada** del Ej. 16.

### Qué teoría aplica

**De la demostración al código (y a los tests)**
(`temas/157-159-de-la-demostraci-n-al-c-digo-y-a-los-tes.md`): una fórmula
cerrada demostrada es un **oráculo** para testear la versión recursiva. El test
compara **dos caminos independientes** hacia el mismo valor; si difieren, algo
está mal (el código… o la demostración). Ojo con el tipo de dato (`3³¹` no entra
en `int`).

### Código

[`codigo/p1_pascal.cpp`](codigo/p1_pascal.cpp) — `make p1_pascal`.

```cpp
int64_t pascal_rec(int f, int c) {
    if (f == 0 || c == 0) return 1;
    return pascal_rec(f - 1, c) + pascal_rec(f, c - 1);
}
```

El oráculo calcula `C(f+c, c)` por producto multiplicativo (camino
independiente, sin factoriales que desborden antes de tiempo):

```cpp
int64_t combinatorio(int n, int k) {          // C(n, k)
    if (k > n - k) k = n - k;
    int64_t r = 1;
    for (int i = 1; i <= k; ++i) r = r * (n - k + i) / i;
    return r;
}
```

Tests: casos a mano + `pascal_rec(f, c) == combinatorio(f+c, c)` para toda la
grilla `0..12 × 0..12`, más la identidad de Pascal. Corre y da `OK`.

Cuidado: `pascal_rec` es exponencial (`~C(f+c, f)` llamadas, sin memoización).
Para testear la fórmula alcanza con `f, c` chicos; si se quisiera evaluar celdas
grandes, habría que memoizar o iterar por diagonales.

### Fuentes

- `../context/teoria/demostraciones/temas/157-de-la-demostraci-n-al-c-digo-y-a-los-tes.md` — fórmula cerrada como oráculo de test; dos caminos independientes.
- `../context/teoria/demostraciones/temas/159-de-la-demostraci-n-al-c-digo-y-a-los-tes.md` — cuidado con los límites del tipo de dato.

---

## Ejercicio 18 — Cambio de fase

### Qué pide

`C` conjunto, `A, B ⊆ C` con `A ∪ B = C`. `S = (s₁, …, sₙ)` con `n ≥ 2`,
`s₁ ∈ A`, `sₙ ∈ B`. Probar que existe `i ∈ {1, …, n−1}` con `sᵢ ∈ A` y
`s_{i+1} ∈ B`.

(a) por inducción en `n`; (b) directo, con el «primer elemento de `S` que está
en `B`».

### Qué teoría aplica

- (a) inducción en el tamaño `n` de la secuencia (`temas/92-advertencia.md`: la
  inducción es sobre un tamaño natural).
- (b) el **truco del primer elemento que cumple**
  (`temas/170-176-el-truco-del-primer-elemento-que-cumple.md`): «sea `j` el
  primer índice tal que…», **probando antes que el conjunto es no vacío**.

### (a) Por inducción en `n`

`P(n) : para toda S = (s₁,…,sₙ) con n ≥ 2, s₁ ∈ A, sₙ ∈ B, existe
i ∈ {1,…,n−1} con sᵢ ∈ A y s_{i+1} ∈ B`.

**Base `P(2)`:** `S = (s₁, s₂)` con `s₁ ∈ A`, `s₂ ∈ B`. Tomamos `i = 1`:
`s₁ ∈ A` y `s₂ ∈ B`. ✓

**Paso `∀n ≥ 2: P(n) ⇒ P(n+1)`:** sea `S = (s₁, …, s_{n+1})` con `s₁ ∈ A`,
`s_{n+1} ∈ B`. Miramos `s₂`:

- **Si `s₂ ∈ B`:** tomamos `i = 1` (`s₁ ∈ A`, `s₂ ∈ B`). Listo.
- **Si `s₂ ∉ B`:** como `A ∪ B = C`, entonces `s₂ ∈ A`. Consideramos
  `S' = (s₂, s₃, …, s_{n+1})`, de `n` elementos, con primer elemento
  `s₂ ∈ A` y último `s_{n+1} ∈ B`. Por **HI**, existe `i' ∈ {1, …, n−1}` con
  `s'_{i'} ∈ A` y `s'_{i'+1} ∈ B`. Traduciendo índices (`s'_k = s_{k+1}`), el
  índice `i = i' + 1 ∈ {2, …, n} ⊆ {1, …, n}` cumple `sᵢ ∈ A`, `s_{i+1} ∈ B`.

En ambos casos vale `P(n+1)`.

**Conclusión:** por inducción, `P(n)` para todo `n ≥ 2`. ∎

### (b) Directo, con el primer elemento en `B`

Sea `J = { j ∈ {2, …, n} : sⱼ ∈ B }`.

**`J ≠ ∅`:** `sₙ ∈ B` y `n ≥ 2`, así que `n ∈ J`.

Como `J ⊆ ℕ` es no vacío, tiene mínimo. Sea `j = mín J`. Notar `j ≥ 2`, así que
`j − 1 ≥ 1`, y `i := j − 1 ∈ {1, …, n−1}`.

- **`s_{i+1} = sⱼ ∈ B`** por definición de `J`.
- **`sᵢ = s_{j−1} ∈ A`:**
  - Si `j − 1 = 1`: `s_{j−1} = s₁ ∈ A` por hipótesis.
  - Si `j − 1 ≥ 2`: como `j` es el **mínimo** de `J` y `j − 1 < j` con
    `j − 1 ∈ {2, …, n}`, resulta `j − 1 ∉ J`, es decir `s_{j−1} ∉ B`. Y como
    `A ∪ B = C`, entonces `s_{j−1} ∈ A`.

Luego `i = j − 1` cumple `sᵢ ∈ A` y `s_{i+1} ∈ B`. ∎

### Fuentes

- `../context/teoria/demostraciones/temas/170-el-truco-del-primer-elemento-que-cumple.md` — «sea `i` el primer índice tal que…».
- `../context/teoria/demostraciones/temas/174-ejemplo.md` — «hay que justificar que el conjunto es no vacío».

---

## Ejercicio 19 — Principio del palomar (versión con piso)

### Qué pide

Probar: si tengo `n > 0` cajas y `m` objetos repartidos, entonces existe una
caja con al menos `⌊(m−1)/n⌋ + 1` objetos.

### Qué teoría aplica

**El principio del palomar** (`temas/165-169-el-principio-del-palomar.md`): la
versión simple (`m > n ⇒ alguna caja con ≥ 2`) se prueba **por contradicción**
sumando las cantidades. La versión con promedios: «alguna caja tiene al menos
`⌈m/n⌉` — no pueden estar todas por debajo del promedio».
Notá que `⌊(m−1)/n⌋ + 1 = ⌈m/n⌉` para `m ≥ 1`.

### Resolución (por contradicción)

Sean `c₁, …, cₙ` las cantidades de objetos en cada caja, con
`∑_{i=1}^{n} cᵢ = m`.

Supongamos por contradicción que **ninguna** caja tiene `⌊(m−1)/n⌋ + 1` objetos
o más, es decir, `cᵢ ≤ ⌊(m−1)/n⌋` para todo `i`.

Entonces

    m = ∑_{i=1}^{n} cᵢ  ≤  ∑_{i=1}^{n} ⌊(m−1)/n⌋  =  n · ⌊(m−1)/n⌋.

Como `⌊(m−1)/n⌋ ≤ (m−1)/n`, tenemos

    m  ≤  n · (m−1)/n  =  m − 1,

es decir `m ≤ m − 1`. Absurdo.

Luego existe una caja con al menos `⌊(m−1)/n⌋ + 1` objetos. ∎

(Si `m = 0`: `⌊−1/n⌋ + 1 = −1 + 1 = 0`, y toda caja tiene `≥ 0` — el enunciado
vale trivialmente. El argumento de arriba es para `m ≥ 1`.)

### Fuentes

- `../context/teoria/demostraciones/temas/167-principio-del-palomar-versi-n-simple.md` — la prueba por contradicción sumando `∑ cᵢ`.
- `../context/teoria/demostraciones/temas/169-principio-del-palomar-versi-n-simple.md` — la versión con promedios y techo `⌈m/n⌉`.

---

## Ejercicio 20 — Complejidad asintótica

### Qué pide

Con `f`, `g` dados en 4 incisos, decidir para cada uno:
- (a) `g ∈ O(f)`? `f ∈ O(g)`? dando constantes `c, n₀`.
- (b) `g ∈ Ω(f)`? `f ∈ Ω(g)`?
- (c) `g ∈ Θ(f)`? `f ∈ Θ(g)`?

### Qué teoría aplica

Definiciones (`temas/62-64`):

- `g ∈ O(f)` si `∃ c > 0, n₀ ≥ 0` tal que `∀n ≥ n₀: g(n) ≤ c·f(n)`.
- `g ∈ Ω(f)` si `∃ c > 0, n₀ ≥ 0` tal que `∀n ≥ n₀: g(n) ≥ c·f(n)`.
- `g ∈ Θ(f)` si `g ∈ O(f)` **y** `g ∈ Ω(f)`.

Cómo se prueba una pertenencia a `O`: **exhibir** `c` y `n₀` y probar la
desigualdad (`temas/66-c-mo-se-demuestra-una-pertenencia-a-o.md`). Cómo se
prueba que **no** pertenece: para toda `c, n₀`, dar un `n ≥ n₀` que la rompe —
Beto da `c, n₀`, nosotros respondemos con `n` dependiente de ellas
(`temas/72-76-y-para-probar-que-no-pertenece.md`, ejemplo `n² ∉ O(n)`).

Propiedades útiles (`temas/78-80`):

- **Simetría:** `g ∈ O(f) ⟺ f ∈ Ω(g)`. (Sale directo de las definiciones.)
- Polinomios: dominados por su término de mayor grado.
- `2ⁿ` crece más que cualquier polinomio; `n!` crece más que `2ⁿ`.

La simetría ahorra la mitad del trabajo: **el inciso (b) se deduce del (a)**.
`g ∈ Ω(f) ⟺ f ∈ O(g)`, y `f ∈ Ω(g) ⟺ g ∈ O(f)`.

Las constantes **no tienen que ser ajustadas** (`temas/68-ejemplo.md`).

---

### i) `g(n) = f(n) = n`

**O:** `g ∈ O(f)` con `c = 1, n₀ = 0` (`n ≤ 1·n`). `f ∈ O(g)` igual, `c = 1`.
**Ω:** por simetría, `g ∈ Ω(f)` (⟸ `f ∈ O(g)`) y `f ∈ Ω(g)`.
**Θ:** `g ∈ Θ(f)` y `f ∈ Θ(g)`. Son la misma función.

---

### ii) `g(n) = 5n + 2`,  `f(n) = ½n − 20`

Las dos son lineales, así que se espera `Θ` en ambos sentidos. Cuidado: `f` es
negativa para `n < 40`, así que las constantes van a necesitar `n₀ ≥ 40`.

**`g ∈ O(f)`:** buscamos `c` con `5n + 2 ≤ c(½n − 20)` para `n` grande.
Tomamos `c = 11`:

    11(½n − 20) = 5.5n − 220.
    5n + 2 ≤ 5.5n − 220  ⟺  222 ≤ 0.5n  ⟺  n ≥ 444.

Con `c = 11, n₀ = 444`: para todo `n ≥ 444`, `5n + 2 ≤ 11·f(n)`. ✓

**`f ∈ O(g)`:** para `n ≥ 0`,

    f(n) = ½n − 20 ≤ ½n ≤ 5n ≤ 5n + 2 = g(n).

Con `c = 1, n₀ = 0`. ✓

**(b) Ω:** por simetría, `g ∈ Ω(f)` (⟸ `f ∈ O(g)`), `f ∈ Ω(g)` (⟸ `g ∈ O(f)`).
**(c) Θ:** `g ∈ Θ(f)` y `f ∈ Θ(g)`.

---

### iii) `g(n) = 2n² − 50n − 4`,  `f(n) = n`

`g` es cuadrática, `f` lineal.

**`g ∈ O(f)`? NO.** Mismo argumento que `n² ∉ O(n)` de la teoría. Sean `c, n₀`
positivas cualesquiera. Para `n` grande, `g(n) = 2n² − 50n − 4 ≥ n²` (vale para
`n ≥ 51`, porque `n² − 50n − 4 ≥ 0` ahí). Tomamos `n = máx(n₀, 51, ⌈c⌉ + 1)`.
Entonces `n ≥ n₀` y `g(n) ≥ n² > c·n = c·f(n)` (porque `n > c`). Ninguna
elección de `c, n₀` sirve. `g ∉ O(f)`.

**`f ∈ O(g)`? SÍ.** Para `n ≥ 51`: `f(n) = n ≤ n² ≤ 2n² − 50n − 4 = g(n)`. Con
`c = 1, n₀ = 51`. ✓

**(b) Ω:**
- `g ∈ Ω(f)`? ⟺ `f ∈ O(g)` → **SÍ**.
- `f ∈ Ω(g)`? ⟺ `g ∈ O(f)` → **NO**.

**(c) Θ:**
- `g ∈ Θ(f)`? necesita `g ∈ O(f)` → **NO**.
- `f ∈ Θ(g)`? necesita `f ∈ Ω(g)` → **NO**.

Resumen: `g` domina estrictamente a `f` (`g ∈ Ω(f) \ O(f)`).

---

### iv) `g(n) = 2ⁿ`,  `f(n) = n!`

**`g ∈ O(f)`? SÍ.** Para `n ≥ 4`, `n! > 2ⁿ` (es la propiedad
`temas/104-el-caso-base-no-tiene-por-qu-ser-0.md`; para `n ≥ 1`, incluso
`2ⁿ ≤ n!` desde `n = 4`: `2⁴ = 16 ≤ 24 = 4!`, y el cociente `n!/2ⁿ` crece porque
cada factor nuevo `(n+1)/2 > 1`). Con `c = 1, n₀ = 4`: `2ⁿ ≤ 1·n!`. ✓

**`f ∈ O(g)`? NO.** `n! ∉ O(2ⁿ)`: `n!` crece más que `2ⁿ` (`temas/80`). Sean
`c, n₀` cualesquiera. Para `n ≥ 4`, `n!/2ⁿ = (4!/2⁴)·∏_{k=5}^{n}(k/2)`, y cada
`k/2 ≥ 2.5`, así que `n!/2ⁿ → ∞`. Tomamos `n` grande con
`n!/2ⁿ > c` (existe porque el cociente diverge) y `n ≥ n₀`: entonces
`n! > c·2ⁿ`. Ninguna `c, n₀` sirve. `f ∉ O(g)`.

**(b) Ω:**
- `g ∈ Ω(f)`? ⟺ `f ∈ O(g)` → **NO**.
- `f ∈ Ω(g)`? ⟺ `g ∈ O(f)` → **SÍ**.

**(c) Θ:** ninguno (`g ∉ Ω(f)`, `f ∉ O(g)`).

Resumen: `n!` domina estrictamente a `2ⁿ`.

---

### Tabla final

| Caso | `g∈O(f)` | `f∈O(g)` | `g∈Ω(f)` | `f∈Ω(g)` | `g∈Θ(f)` | `f∈Θ(g)` |
|---|---|---|---|---|---|---|
| i) `n` / `n` | sí (c=1) | sí (c=1) | sí | sí | sí | sí |
| ii) `5n+2` / `½n−20` | sí (c=11, n₀=444) | sí (c=1) | sí | sí | sí | sí |
| iii) `2n²−50n−4` / `n` | **no** | sí (c=1, n₀=51) | sí | **no** | **no** | **no** |
| iv) `2ⁿ` / `n!` | sí (c=1, n₀=4) | **no** | **no** | sí | **no** | **no** |

### Fuentes

- `../context/teoria/demostraciones/temas/62-cota-superior.md`, `63-cota-inferior.md`, `64-orden-exacto.md` — definiciones de `O`, `Ω`, `Θ`.
- `../context/teoria/demostraciones/temas/66-c-mo-se-demuestra-una-pertenencia-a-o.md` — exhibir `c` y `n₀`.
- `../context/teoria/demostraciones/temas/74-ejemplo.md`, `76-ejemplo.md` — `n² ∉ O(n)`: Beto da `c, n₀`, respondemos con `n`.
- `../context/teoria/demostraciones/temas/79-propiedades-tiles-para-no-sufrir.md` — simetría `g ∈ O(f) ⟺ f ∈ Ω(g)`.
- `../context/teoria/demostraciones/temas/80-propiedades-tiles-para-no-sufrir.md` — polinomios y jerarquía `polinomio ≪ 2ⁿ ≪ n!`.
- `../context/teoria/demostraciones/temas/104-el-caso-base-no-tiene-por-qu-ser-0.md` — `n! > 2ⁿ` para `n ≥ 4`.

---

## Resumen de técnicas por ejercicio

| Ej. | Técnica |
|---|---|
| 1 | Tablas de verdad / contraejemplo para refutar `∀` |
| 2 | Reconocer qué es (y qué no es) una demostración |
| 3 | Error de nombre reusado; factorizar con la definición |
| 4 | Contraejemplo |
| 5 | Directa, `∃` con testigo dependiente |
| 6 | Directa por casos (par / impar) |
| 7 | Contradicción + paridad de una suma |
| 8 | Inducción simple (completar el paso) |
| 9 | Contar casos base (usa `P(n−1)` y `P(n−2)` ⇒ 2 bases) |
| 10 | El paso inductivo tiene que valer para **todo** `n` (falla `1→2`) |
| 11 | La HI necesita que la entrada chica cumpla las hipótesis; directa limpia |
| 12 | Inducción simple |
| 13 | Suma geométrica + inducción |
| 14 | Formalizar recurrencia + inducción |
| 15 | Caso base corrido (`n₀ = 5`) |
| 16 | Inducción en tuplas con orden bien fundado + identidad de Pascal |
| 17 | Fórmula cerrada como oráculo de test |
| 18 | (a) inducción en `n`; (b) truco del primer elemento (probar no vacío) |
| 19 | Palomar por contradicción |
| 20 | Definiciones de `O/Ω/Θ`, exhibir constantes, simetría, jerarquía de órdenes |
