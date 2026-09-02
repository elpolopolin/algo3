## El algoritmo de Strassen 

Algunos comentarios adicionales: 


![](../imagenes/teo04-Divide_and_Conquer.pdf-0048-07.png)


Se podrá hacer mejor? Onda, partir en más subbloques y encontrar (mágicamente) nuevas reescrituras? 


![](../imagenes/teo04-Divide_and_Conquer.pdf-0048-09.png)



![](../imagenes/teo04-Divide_and_Conquer.pdf-0048-10.png)


Si y no. Ahora no es tan sencillo “descubrir” los subbloques, ni aprender como pegarlos. Strassen (con herramientas de Schönhage) demostró que, en el fondo, su algoritmo se corresponde con encontrar una **descomposición tensorial** del producto. El juego entonces es encontrar mejores descomposiciones tensoriales. 

**Autores Año Complejidad** Strassen 1969 _O_ <u>(</u> _n_<sup>2</sup><sup>_._8074)</sup> Coppersmith–Winograd 1990 _O_ (︁ _n_<sup>2</sup><sup>_._375477+</sup><sup>_ε_)︁</sup> Vassilevska Williams 2012 _O_ (︁ _n_<sup>2</sup><sup>_._3729+</sup><sup>_ε_)︁</sup> Le Gall 2014 _O_ (︁ _n_<sup>2</sup><sup>_._372864+</sup><sup>_ε_)︁</sup> Duan–Wu–Zhou 2023 _O_ (︁ _n_<sup>2</sup><sup>_._371866+</sup><sup>_ε_)︁</sup> Vassilevska Williams–Xu–Xu–Zhou 2024 _O_ (︁ _n_<sup>2</sup><sup>_._371552+</sup><sup>_ε_)︁</sup> Dupont et al. ( _preprint_ ) 2026 _O_ <u><mark>(</mark></u> _n_<sup>2</sup><sup>_._37117</sup><sup><mark>7+</mark></sup><sup>_ε_</sup><sup><u><mark>)</mark></u></sup> 

TDA - Algo3 (DC, FCEyN, UBA) 

<u>DC - FCEyN - UBA</u> 

<u>2do Cuatrimestre de 2026</u> 37 / 55 

Divide & Conquer 

Algoritmo de Strassen 

Timba y máximo subarreglo 

Búsqueda y extensiones 

Algoritmo de Karatsuba 

