# Resumen — Demostraciones

Tres cosas para llevarse de esta unidad:

- Una demostración es una **conversación con un escéptico**. Todo lo que no le
  digas explícitamente, no cuenta.
- **Formalizar la consigna** (nombrar, cuantificar, escribir las relaciones) es
  la mitad del trabajo. Si formalizás mal, lo que sigue no importa.
- La inducción no es una receta: es un esqueleto (`P(n)`, casos base, HI, paso).
  Casi todos los errores son de esqueleto, no de cuentas.

---

## 1. ¿Para quién escribimos?

No existe "la" demostración correcta en abstracto: depende del **contexto**, de
qué le podemos asumir al lector.

- Una demostración **heurística** ("$n! + 1$ no es divisible por nada menor que
  $n$, entonces es primo") convence a un apurado y puede ser **falsa**:
  $4! + 1 = 25 = 5^2$.
- Una demostración **totalmente formal** (escrita en Lean 4, por ejemplo)
  convence a una computadora pero es ilegible para un humano.

En esta materia apuntamos al punto intermedio: *razonablemente formal*, escrita
para un par humano escéptico.

### La conversación Alicia / Beto

Herramienta mental que se usa todo el tiempo. **Alicia** demuestra, **Beto** es
el escéptico que busca el agujero. Según la forma de lo que hay que probar, le
toca elegir a uno o al otro:

| Hay que probar | Quién elige | Qué tenés que hacer |
|---|---|---|
| $\forall x.\, P(x)$ | **Beto** elige el $x$ | responder para *ese* $x$, no para el cómodo |
| $\exists x.\, P(x)$ | **Alicia** elige el $x$ | dar un $x$ concreto y verificar $P(x)$ |
| $P \Rightarrow Q$ | — | asumir $P$ (**y decirlo**) y deducir $Q$ |
| $\forall x.\exists y.\, P(x,y)$ | Beto el $x$, Alicia el $y$ | el $y$ **puede depender** del $x$ |
| $\exists y.\forall x.\, P(x,y)$ | Alicia el $y$, Beto el $x$ | el $y$ **no puede** depender del $x$ |

Las dos últimas filas son proposiciones **completamente distintas**. Confundirlas
es un error clásico de parcial.

## 2. Formalizar la consigna

Rara vez nos dan el problema ya formalizado. **Si formalizamos mal, todo lo que
hagamos después es irrelevante.**

Ejemplo. Consigna en criollo: *"una colonia empieza con 5 y se triplica por
hora; después de un rato hay el triple del triple del triple... de 5"*.
¿Cuántas veces "el triple"? ¿$n$ o $n+1$? Cada persona lo lee distinto.

Versión formalizada:

> Sea $b_0 = 5$ y $b_{n+1} = 3 \cdot b_n$ para todo $n \in \mathbb{N}$.
> Probar que $\forall n \in \mathbb{N},\ b_n = 5 \cdot 3^n$.

Lo que ganamos al formalizar:

1. **Nombra** los objetos (la sucesión $b$, la cantidad $b_n$, la hora $n$).
2. **Explicita las relaciones** ($b_0 = 5$, $b_{n+1} = 3 b_n$).
3. **Cuantifica** las variables ("sea", "para todo", "existe").
4. Usa **conectores lógicos** ("si", "entonces", "luego", "porque").

Cuando un ejercicio dice "definir claramente…" o "pasar el enunciado a fórmulas",
está pidiendo exactamente estos cuatro puntos.

## 3. Complejidad asintótica

Comparamos funciones $f, g : \mathbb{N} \to \mathbb{R}_{\geq 0}$ "para $n$
grande, salvo constantes".

| Conjunto | Definición | En criollo |
|---|---|---|
| $g \in O(f)$ | $\exists c > 0, n_0 \geq 0$ tales que $g(n) \leq c \cdot f(n)$ para todo $n \geq n_0$ | cota **superior**: $g$ no crece más rápido que $f$ |
| $g \in \Omega(f)$ | $\exists c > 0, n_0 \geq 0$ tales que $g(n) \geq c \cdot f(n)$ para todo $n \geq n_0$ | cota **inferior** |
| $g \in \Theta(f)$ | $g \in O(f)$ **y** $g \in \Omega(f)$ | orden **exacto** |

### Cómo se prueba una pertenencia a $O$

Es un $\exists$: **elegimos nosotros** las constantes. Hay que **exhibirlas** y
probar la desigualdad para todo $n \geq n_0$.

> **Probar que $3n^2 + 10n \in O(n^2)$.**
>
> Elegimos $c = 13$ y $n_0 = 1$. Sea $n \geq 1$. Como $n \geq 1$, vale
> $n \leq n^2$, entonces
> $$3n^2 + 10n \leq 3n^2 + 10n^2 = 13n^2 = c \cdot n^2.$$
> Luego para todo $n \geq n_0$ vale $3n^2 + 10n \leq c \cdot n^2$. $\square$

Dos detalles que sí se corrigen: las constantes **no tienen que ser ajustadas**
($c = 1000$, $n_0 = 40$ también sirven), y hay que **decir dónde** se usa
$n \geq 1$.

### Cómo se prueba una **no** pertenencia

Hay que **negar** un $\exists$: para *toda* elección de $c$ y $n_0$, exhibir un
$n \geq n_0$ que rompe la desigualdad. Volvemos a la conversación: Beto nos da
$c$ y $n_0$, y nosotros respondemos con un $n$ **que depende de ellos**.

> **Probar que $n^2 \notin O(n)$.**
>
> Sean $c$ y $n_0$ constantes positivas cualesquiera. Tomemos
> $n = \max(n_0, \lceil c \rceil + 1)$. Entonces $n \geq n_0$, y como $n > c$,
> multiplicando por $n > 0$ obtenemos $n^2 > c \cdot n$. Luego no vale
> $n^2 \leq c \cdot n$ para todo $n \geq n_0$. Como $c$ y $n_0$ eran arbitrarias,
> ninguna elección sirve. $\square$

### Propiedades para no sufrir

- **Transitividad:** $f \in O(g)$ y $g \in O(h)$ $\Rightarrow$ $f \in O(h)$.
- **Suma:** $f_1 \in O(g)$ y $f_2 \in O(g)$ $\Rightarrow$ $f_1 + f_2 \in O(g)$.
- **Simetría:** $g \in O(f) \iff f \in \Omega(g)$.
- Los polinomios están dominados por su término de mayor grado; $2^n$ crece más
  que cualquier polinomio; $n!$ crece más que $2^n$.

## 4. Inducción

### El principio

Sea $P(n)$ una proposición sobre los naturales. Si probamos:

1. **Caso base:** $P(0)$ es cierta (podría ser otro punto de arranque).
2. **Paso inductivo:** para todo $n \in \mathbb{N}$, $P(n) \Rightarrow P(n+1)$.

entonces $P(n)$ es cierta **para todo** $n \in \mathbb{N}$.

Como el dominó: si cae la primera ficha, y cada ficha tira la siguiente, caen
todas.

![El principio de inducción](imagenes/teo01-demostraciones.pdf-0083-10.png)

### Cómo se escribe (los 4 pasos)

1. **Definir explícitamente $P(n)$**, con sus cuantificadores. *Este es el paso
   que más se saltea, y donde nacen casi todos los errores.*
2. **Probar el caso base** (o **los** casos base — ver más abajo).
3. **Probar el paso inductivo:** asumir la hipótesis inductiva (HI), **decir que
   la asumimos**, y deducir $P(n+1)$ marcando **dónde** se usa la HI.
4. **Concluir:** «por inducción, $P(n)$ vale para todo $n \in \mathbb{N}$».

> **Advertencia.** La inducción es **sobre naturales**. No es "sobre conjuntos"
> ni "sobre secuencias". Si querés hacer inducción sobre otra estructura, $P$
> tiene que hablar de un **tamaño natural** de esa estructura.

Esa advertencia es la que rompe la mayoría de las demostraciones falsas de la
guía: se hace "inducción sobre el conjunto" sacando un elemento cualquiera, sin
que $P$ hable del tamaño.

### El caso base no tiene por qué ser 0

> **Para todo $n \geq 4$, $n! > 2^n$.**

¿Y para $n < 4$? $0! = 1 = 2^0$, $1! = 1 < 2$, $2! = 2 < 4$, $3! = 6 < 8$: la
propiedad es **falsa**. El caso base corrido **no es un capricho**. El caso base
pasa a ser $P(4)$, y en el paso inductivo tomamos $n \geq 4$, porque la HI la
tenemos sólo a partir de ahí.

### Inducción fuerte (o global, o completa)

Si para todo $n \in \mathbb{N}$ vale
$$\big(\forall k \in \mathbb{N}.\ k < n \Rightarrow P(k)\big) \Rightarrow P(n),$$
entonces $P(n)$ es cierta para todo $n$.

La HI ahora es: «$P$ vale para **todos** los $k < n$». Es la herramienta natural
cuando la recursión **salta**: $T(n)$ definido con $T(n-4)$, $a_n$ definido con
$a_{n-1}$ y $a_{n-2}$, `Exp(a,n)` que llama a `Exp(a, ⌊n/2⌋)`. Es equivalente a
la inducción común, pero mucho más cómoda para recursiones.

### ¿Cuántos casos base?

> Si la demostración de $P(n)$ usa $P(n-1), P(n-2), \dots, P(n-k)$ para un
> $k \geq 1$ fijo, hacen falta **$k$ casos base**. Para $n < k$, "$P(n-k)$" no
> tiene sentido: nos caemos de $\mathbb{N}$.

| La recursión usa | Casos base a mano |
|---|---|
| $P(n-1)$ | $P(0)$ |
| $P(n-1)$ y $P(n-2)$ | $P(0)$, $P(1)$ |
| $P(n-4)$ | $P(0)$, $P(1)$, $P(2)$, $P(3)$ |
| $P(\lfloor n/2 \rfloor)$ (inducción fuerte) | sólo $P(0)$ — porque $\lfloor n/2 \rfloor < n$ para todo $n \geq 1$ y nunca nos caemos de $\mathbb{N}$ |

### El plan completo, con una recurrencia

Para $T(n) = 2T(n-4)$, hecho **con rigor**:

1. **Definir $T$ con su dominio:** sea $T : \mathbb{N} \to \mathbb{N}$ con
   $T(n) = 2T(n-4)$ para todo $n \geq 4$. De $T(0), \dots, T(3)$ no sabemos nada:
   sea $a = \max(T(0), T(1), T(2), T(3))$.
2. **Definir la propiedad:** $P(n) : T(n) \leq a \cdot 2^{n/4}$.
3. **Cuatro casos base** ($0 \leq n \leq 3$), porque la recursión resta 4.
4. **Paso inductivo** (inducción fuerte): para $n \geq 4$, vale
   $0 \leq n-4 < n$, lo que legitima usar $P(n-4)$.
5. **Concluir con la definición de $O$:** exhibir constantes concretas $c$ y $n_0$.

Sin baches: dominio claro, cuatro casos base, HI explícita, y la definición de
$O$ aplicada con constantes concretas.

### Inducción cuando el objeto tiene dos tamaños

Si el objeto se indexa por un par $(a,b)$ (una celda $(f,c)$ de una matriz, por
ejemplo), no hay un "natural" obvio para inducir. Hace falta un **orden bien
fundado** $\prec$ sobre los pares: un orden **sin cadenas infinitas
decrecientes**. Con eso se puede usar inducción fuerte: para probar $P(a,b)$
podemos asumir $P(a', b')$ para todo $(a',b') \prec (a,b)$.

Dos elecciones habituales:

- **Por una medida:** $(a',b') \prec (a,b)$ si $a' + b' < a + b$ (o si $b' < b$,
  cuando la recursión sólo achica la segunda componente). Reduce todo a inducción
  en un natural.
- **Lexicográfico:** $(a',b') \prec (a,b)$ si $a' < a$, o si $a' = a$ y $b' < b$.

Lo importante: **definir el orden explícitamente antes de largar la inducción**.

## 5. Contrarrecíproco y absurdo

### Contrarrecíproco

Probar $P \Rightarrow Q$ es equivalente a probar $\lnot Q \Rightarrow \lnot P$.

> **Si $n^2$ es par, entonces $n$ es par.**
>
> Por contrarrecíproco: si $n$ es impar, $n = 2k+1$ para algún $k \in \mathbb{N}$,
> entonces $n^2 = 4k^2 + 4k + 1 = 2(2k^2+2k)+1$ es impar. $\square$

Sirve cuando la negación de la conclusión es *más manejable* que la hipótesis
original. Un enunciado del tipo "si no tiene ciclos entonces…" casi siempre se
ataca por contrarrecíproco.

### Contradicción (absurdo)

Para probar $P$: asumimos $\lnot P$ y derivamos algo falso. Hay que **decir
explícitamente** «asumimos por contradicción que…», y **marcar dónde aparece el
absurdo**.

### Principio del palomar

> Si repartimos $m$ objetos en $n$ cajas y $m > n$, entonces alguna caja tiene al
> menos 2 objetos.

**Demostración.** Por contradicción: supongamos que toda caja tiene a lo sumo 1
objeto. Sea $c_i$ la cantidad de objetos de la caja $i$. Entonces
$$m = \sum_{i=1}^{n} c_i \leq \sum_{i=1}^{n} 1 = n,$$
contradiciendo $m > n$. $\square$

La misma idea con **promedios**: alguna caja tiene al menos
$\lceil m/n \rceil$ objetos — *"no pueden estar todas por debajo del promedio"*.
Esa es la versión que se generaliza a las cotas del tipo
$\lfloor (m-1)/n \rfloor + 1$.

## 6. El truco del "primer elemento que cumple"

$\mathbb{N}$ está **bien ordenado**: todo subconjunto no vacío de $\mathbb{N}$
tiene mínimo. Eso habilita un truco que muchas veces **reemplaza una inducción
engorrosa**:

> *"sea $i$ el primer índice tal que…"*, *"sea $x$ el mínimo elemento que…"*

> **Todo natural $n \geq 2$ tiene un divisor primo.**
>
> Sea $D = \{d \in \mathbb{N} \mid d \geq 2,\ d \mid n\}$. $D \neq \emptyset$
> porque $n \in D$. Sea $p = \min D$. Si $p$ no fuera primo, tendría un divisor
> $d$ con $2 \leq d < p$; pero $d \mid p$ y $p \mid n$ implican $d \mid n$,
> entonces $d \in D$ y $d < p$, contradiciendo la minimalidad de $p$. Luego $p$
> es primo. $\square$

**Hay que justificar que el conjunto es no vacío.** Si no, el mínimo no existe.
Este truco vuelve todo el tiempo en el resto de la materia: *"la primera
iteración en la que…"*, *"el primer momento en que…"*.

## 7. Checklist antes de entregar

1. **Definí $P(n)$ explícitamente**, con todos sus cuantificadores, antes de empezar.
2. Contá **cuántos casos base** necesita tu paso inductivo (¿usa $P(n-1)$? ¿$P(n-2)$? ¿$P(n-4)$?).
3. **Decí dónde usás la HI**, y verificá que el valor donde la usás cae dentro de
   $\mathbb{N}$ (y del rango donde vale).
4. Ponele **nombre** a todo, **cuantificá** todo, y no reúses nombres.
5. Si escribiste "sea $x$ el mínimo tal que…": probá que el conjunto es **no vacío**.
6. Releé tu demostración **como Beto, el escéptico**: ¿en qué oración le mentirías?

## Fuentes

- `temas/08-a-qui-n-queremos-convencer.md` (L1-18) — heurístico vs. formal, el contexto
- `temas/40-formalizar-la-consigna.md` (L1-38) — formalizar mal invalida todo
- `temas/45-versi-n-formalizada.md` (L1-38) — ejemplo de la colonia formalizado
- `temas/51-qu-ganamos-al-formalizar.md` (L1-48) — nombrar, explicitar, cuantificar, conectar
- `temas/57-comprender-qu-se-nos-pide-la-conversaci-.md` (L1-24) — Alicia/Beto y los cuantificadores
- `temas/60-repaso-complejidad-asint-tica.md` (L1-42), `temas/62-cota-superior.md` (L1-16), `temas/63-cota-inferior.md` (L1-16), `temas/64-orden-exacto.md` (L1-38) — definiciones de $O$, $\Omega$, $\Theta$
- `temas/66-c-mo-se-demuestra-una-pertenencia-a-o.md` (L1-70), `temas/70-ejemplo.md` (L1-45) — exhibir $c$ y $n_0$
- `temas/72-y-para-probar-que-no-pertenece.md` (L1-38), `temas/76-ejemplo.md` (L1-42) — negar el $\exists$
- `temas/80-propiedades-tiles-para-no-sufrir.md` (L1-45) — transitividad, suma, simetría
- `temas/86-el-principio-de-inducci-n.md` (L1-32) — el dominó
- `temas/91-c-mo-se-escribe-una-demostraci-n-por-ind.md` (L1-10) — los 4 pasos
- `temas/92-advertencia.md` (L1-36) — la inducción es sobre naturales
- `temas/111-proposici-n.md` (L1-56) — $n! > 2^n$ y el caso base corrido
- `temas/120-principio-de-inducci-n-fuerte.md` (L1-52) — inducción fuerte
- `temas/127-advertencia.md` (L1-54) — cuántos casos base
- `temas/134-ahora-s-t-n-2-t-n-4-con-rigor.md` (L1-64) — el plan de 5 pasos con una recurrencia
- `temas/142-necesitamos-un-orden-bien-fundado.md` (L1-52) — orden bien fundado, medida y lexicográfico
- `temas/162-contrarrec-proco.md` (L1-52) — contrarrecíproco
- `temas/164-contradicci-n-absurdo.md` (L1-42) — absurdo
- `temas/169-principio-del-palomar-versi-n-simple.md` (L1-44) — palomar y la versión con promedios
- `temas/170-el-truco-del-primer-elemento-que-cumple.md` (L1-24), `temas/176-ejemplo.md` (L1-48) — buen orden y el mínimo
- `temas/182-tips-para-escribir-demostraciones.md` (L1-34) — checklist
