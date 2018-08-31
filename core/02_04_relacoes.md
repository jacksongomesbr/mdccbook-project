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

