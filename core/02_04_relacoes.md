# Relações {#sec:relacoes}

Considere as relações a seguir:

* parentesco
* maior ou igual
* igualdade
* lista telefônica, que associa assinante e seu número de telefone
* fronteira (entre países)

Suponha os conjuntos $A$ e $B$. Uma relação $R$ de $A$ em $B$ é um subconjunto de um produto cartesiano $A \times B$, ou seja:

$$
R \subseteq A \times B
$${#eq:definicao-relacao}

ou

$$
R : A \rightarrow B
$${#eq:definicao-relacao-alt}

onde:

* $A$ é o **domínio** (origem ou conjunto de partida de $R$)
* $B$ é o **contradomínio** (destino ou conjunto de chegada de $R$)

Os elementos de $R$ são pares (ou tuplas) dos elementos de $A$ e $B$, ou seja:

$$
(a, b) \in R
$$

ou

$$
a R b
$$

Uma relação pode ser caracterizada por uma propriedade. Neste caso, na notação $R : A \rightarrow B$, $R$ assume uma propriedade. Por exemplo: 

$$
= : A \rightarrow B
$$ 

define a relação de igualdade entre os conjuntos $A$ e $B$ tal que os elementos de $A$ sejam iguais aos elementos de $B$. Em outras palavras, os componentes das tuplas da relação $R$ terão que respeitar a propriedade de igualdade. 

**Exemplo:** Considere os seguintes conjuntos: $A = \{a\}$, $B = \{a, b\}$ e $C = \{0, 1, 2\}$. É válido afirmar que:

* $\{\}$ é uma relação de $A$ em $B$ pois o conjunto vazio é subconjunto de qualquer conjunto
* $A \times B = \{(a, a), (a, b)\}$ é uma relação (qualquer) de $A$ em $B$
* $= : A \rightarrow A = \{(a,a)\}$ (relação de igualdade de $A$ em $A$)
* $= : A \rightarrow B = \{(a,a)\}$ (relação de igualdade de $A$ em $B$)
* $< : C \rightarrow C = \{(0,1), (1,2)\}$ (relação "menor que" de $C$ em $C$)

## Endorrelação

**Endorrelação** é um tipo de relação que considera o mesmo conjunto, ou seja, $R : A \rightarrow A$ (domínio e contradomínio são o mesmo conjunto). Uma endorrelação $R : A \rightarrow A$ pode ser denotada por $(A, R)$, por exemplo:

a) $(N, <=)$
b) $(P(A), \subseteq)$

## Representações gráficas de relações

As relações podem ser representadas graficamente como diagramas de Venn, gráficos em um plano cartesiano ou em grafos. 

### Relações como diagramas de Venn

Diagramas de Venn podem ser utilizados para representar relações visualmente. Na [@fig:relacoes-diagramas-de-venn] o diagrama da esquerda representa a relação $= : A \rightarrow A$ e o da direita a relação $<= : C \rightarrow C$.

![Diagrama de Venn demonstrando relações entre conjuntos](./graphics/relacao-diagrama-de-venn.png){#fig:relacoes-diagramas-de-venn}

Em Diagramas de Venn o conjunto da esquerda é comumente chamado de *domínio* e o da direita de *imagem*.

### Relações como planos cartesianos

Gráficos em planos cartesianos podem representar relações. Em um plano cartesiano de duas dimensões, os eixos (coordenadas) representam os conjuntos. Por exemplo a relação $R = \{(x, y) \mid y = x^2\}$ pode ser representada pelo gráfico da [@fig:relacao-grafico].

![Gráfico demonstrando relações entre conjuntos](./graphics/relacao-grafico.png){#fig:relacao-grafico width=10cm}

### Relações como grafos

A representaçao de grafos aplica-se apenas a endorrelações. Grafos podem ser representados como matrizes e como diagramas e vértices e arestas.

Considere os conjuntos $A = \{a\}$, $B = \{a, b\}$ e $C = \{0, 1, 2\}$.

A relação $= : B \rightarrow B$, definida por $\{(a,a), (b,b)\}$ seria representada pela matriz e pelo grafo da [@fig:relacao-grafo-1].

![Grafo 1 - demonstrando relações entre conjuntos](./graphics/relacao-grafo-1.png){#fig:relacao-grafo-1 width=10cm}

A relação $<= : C \rightarrow C$ seria representada pela matriz e pelo grafo da [@fig:relacao-grafo-2]:

![Grafo 2 - demonstrando relações entre conjuntos](./graphics/relacao-grafo-2.png){#fig:relacao-grafo-2 width=11cm}

## Exercícios

1. Considere os seguintes conjuntos: $A = \{a\}$, $B = \{a, b\}$ e $C = \{0, 1, 2\}$. Defina as relações a seguir:

a) $\neq : B \rightarrow C$
b) $\neq : A \rightarrow B$

2. Considere o conjunto $A = \{1, 2, 3, 4, 5\}$. Represente as relações a seguir na forma de Diagrama de Venn, Plano cartesiano e Grafo:

a) $= : A \rightarrow A$
b) $(A, =)$
c) $(A, <=)$
d) $(A, >=)$
e) $R = \{(x, y) \mid y = x + y \}$

## Propriedades de endorrelações

### Reflexiva, irreflexiva

Seja $R : A \rightarrow A$, então $R$ é uma:

a) **relação reflexiva**, se $(\forall a \in A)(a \, R \, a)$: para todo elemento $a$ de $A$ existe uma tupla $(a,a)$
b) **relação irreflexiva** (ou **antirreflexiva**), se $(\forall a \in A)(\neg(a \, R \, a))$: para todo elemento $a$ de $A$ não existe uma tupla $(a,a)$.

Uma forma rápida de identificar a relação $R$ no conjunto $A$ como reflexiva ou irreflexiva é realizar os seguintes passos:

1. Definir o produto cartesiano de $A$
2. Definir $C_i \subseteq R$ no qual todas as tuplas tenham componentes iguais (primeiro igual ao segundo)
3. Definir $R \subseteq C_d$ no qual todas as tuplas tenham componentes diferentes (primeiro é diferente do segundo)

Assim, podemos definir que:

* a relação $R$ é reflexiva se $C_i \subseteq R$
* a relação $R$ é irreflexiva se $R \subseteq C_d$

**Exemplo: Seja $A=\{a, b\}$. Conjuntos importantes:**

* $A^2 = \{(a,a),(a,b),(b,a),(b,b)\}$. 
* $C_i = \{(a,a),(b,b)\}$
* $C_d = \{(a,b),(b,a)\}$

As seguintes relações são:

a) Reflexivas:

* $R_1 = \{(a,a),(b,b)\}$
* $R_2 = \{(a,a),(a,b),(b,b)\}$, pois $C_i \subseteq R_2$
* $R_3 = \{(a,a),(b,b),(b,a)\}$, pelo mesmo motivo de $R_2$
* $R_4 = \{(a,a),(a,b),(b,a),(b,b)\}$, idem

b) Irreflexivas:

* $R_5 = \{(a,b),(b,a)\}$
* $R_6 = \{(a,b)\}$, pois $R_6 \subseteq C_d$
* $R_7 = \{(b,a)\}$, pelo mesmo motivo de $R_6$
* $R_8 = \{\}$, idem


**Exemplo: Seja $S = \{0,1,2\}$. Conjuntos importantes:**

* $S^2 = \{(0,0),(0,1),(0,2),(1,0),(1,1),(1,2),(2,0),(2,1),(2,2)\}$
* $C_i = \{(0,0),(1,1),(2,2)\}$
* $C_d = \{(0,1),(0,2),(1,0),(1,2),(2,0),(2,1)\}$

A seguinte relação não é reflexiva e nem irreflexiva:

\begin{align*}
(S,R) = \{(0,2),(2,0),(2,2)\}
\end{align*}

Não é reflexiva porque $C_i \nsubseteq (S,R)$ e não é irreflexiva porque $(S,R) \nsubseteq C_d$.

### Reflexividade de relações em matrizes e grafos

Para um conjunto $A$ é possível verificar se uma endorrelação $R : A \to A$ é reflexiva ou irreflexiva analisando a sua representação como matriz ou grafo:

a) **Matriz**

* **Reflexiva**: a diagonal da matriz contém somente o valor verdadeiro
* **Irreflexiva**: a diagonal da matriz contém somente o valor falso

b) **Grafo**

* **Reflexiva**: qualquer nó tem um arco com origem e destino nele mesmo
* **Irreflexiva**: qualquer nó não tem um arco com origem e destino nele mesmo

### Simétrica, antissimétrica

Seja $R : A \to A$ uma endorrelação em $A$, então $R$ é uma:

a) **relação simétrica**, se $(\forall a,b \in A)(a \, R \, b \to b \, R \, a)$: para todo par de elementos $a$ e $b$ de $A$, sendo $a = b$ ou não, se há uma tupla $(a,b)$ então há uma tupla $(b,a)$
b) **relação antissimétrica**, $(\forall a, b \in A), (a \, R \, b \land a \neq b) \implies (\neg b \, R \, a)$: para todo par de elementos $a$ e $b$ de $A$, se há uma tupla $(a,b)$ e $a \neq b$, então não há a tupla $(b,a)$.

**Exemplos: Seja $A=\{a, b\}$. Conjuntos importantes:** 

* $A^2 = \{(a,a),(a,b),(b,a),(b,b)\}$
* $C_s = A^2$
* $C_a = \{(a,a),(b,b)\}$

As seguintes relações são:

a) Simétricas:

* $R_1 = \{(a,a),(b,b)\}$
* $R_4 = \{(a,a),(a,b),(b,a),(b,b)\}$
* $R_5 = \{(a,b),(b,a)\}$
* $R_8 = \{\}$
* $R_9 = \{(a,a)\}$
* $R_{10} = \{(b,b)\}$
* $R_{11} = \{(a,a),(a,b),(b,a)\}$
* $R_{12} = \{(a,b),(b,a),(b,b)\}$

b) Antissimétricas:

* $R_1 = \{(a,a),(b,b)\}$
* $R_2 = \{(a,a),(a,b),(b,b)\}$
* $R_3 = \{(a,a),(b,b),(b,a)\}$
* $R_6 = \{(a,b)\}$
* $R_8 = \{\}$

### Simétrica e antissimétrica em matrizes e grafos

Para um conjunto $A$ uma forma de entender e verificar se uma endorrelação $R : A \to A$ é simétrica ou antissimétrica é analisar a sua representação como matriz ou grafo:

a) **Matriz**

* Simétrica: a metade acima ou abaixo da diagonal é espelhada na outra
* Antissimétrica: se uma célula em uma metade da diagonal for verdadeira, a correspondente na outra metade é falsa

b) **Grafo**

* Simétrica: entre dois nós: a) não existe seta; ou b) existem duas setas, uma em cada sentido
* Antissimétrica: há no máximo uma seta entre dois nós quaisquer

### Transitiva, não transitiva

Seja $A$ um conjunto e $R$ uma endorrelação em $A$, então $R$ é uma:

a) **transitiva** se $(\forall a, b, c \in A), (a \, R \, b \land b \, R \, c \to a \, R \, c)$; e
b) **não-transitiva** é o contrário da relação transitiva

## Atividade de pesquisa

1. Uma relação pode ser classificada nos seguintes tipos (que não são mutuamente exclusivos):

a) funcional
b) injetora
c) total
d) sobrejetora
e) monomorfismo
f) epimorfismo
g) isomorfismo

Escolha três dos tipos e, para cada um, apresente:

a) definição (incluindo representação formal)
b) dois exemplos

2. As *Redes de Petri* são o modelo computacional do tipo concorrente mais utilizado em computação, informática e engenharia. Faça uma pesquisa sobre Redes de Petri e apresente:

a) definição (conceito)
b) significado dos símbolos da representação gráfica da rede
c) dois exemplos
d) como definir uma Rede de Petri utilizando Relação (utilizando exemplos)
