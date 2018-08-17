# Álgebra de Conjuntos

Uma **Álgebra** é constituída de operações definidas sobre uma soleção de objetos. Neste contexto, *álgebra de conjuntos* corresponderia às operações definidas sobre todos os conjuntos.

As operações da álgebra de conjuntos podem ser:

- Não reversíveis
    - União
    - Intersecção
    - Diferença
  
- Reversíveis
    - Complemento
    - Conjunto das partes
    - Produto cartesiano
    - União disjunta

## Operações não reversíveis

### União

Sejam $A$ e $B$ dois conjuntos. A união entre eles, $A \cup B$, é definida como:

$$A \cup B = \{x \mid x \in A \lor x \in B\}$$ {#eq:conjuntos-uniao}

Considerando a lógica, o conjunto $A$ pode ser definido como $x \in A$ e o conjunto $B$ pode ser definido como $x \in B$. Ou seja, a propriedade de pertiência é utilizada para indicar uma proposição lógica.

A união corresponde à operação lógica *disjunção* (símbolo $\lor$).

----------------------------------------------------------------------------------
**Exemplo: união entre conjuntos**
----------------------------------------------------------------------------------
Considere os conjuntos:

a) $\mbox{Digitos} = \{0, 1, 2, 3, 4, 5, 6, 7, 8, 9\}$
  
b) $\mbox{Vogais} = \{a, e, i, o, u\}$
  
c) $\mbox{Pares} = \{0, 2, 4, 6, ...\}$

<!-- -->

Então:

a) $\mbox{Digitos} \cup \mbox{Vogais} = \{0, 1, 2, 3, 4, 5, 6, 7, 8, 9, a, e, i, o, u\}$
  
b) $\mbox{Digitos} \cup \mbox{Pares} = \{0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 14, 16, ...\}$

<!-- -->

Suponha os conjuntos:

a) $A = \{x \in N \mid x > 2\}$
  
b) $B = \{x \in N \mid x^2 = x\}$

<!-- -->

Então:

$A \cup B = \{0, 1, 3, 4, 5, 6, ...\}$
----------------------------------------------------------------------------------

**É importante** observar que o resultado da união é um conjunto sem repetições de elementos.

Vejamos as propriedades da união:

- **Elemento neutro**: $A \cup \emptyset = \emptyset \cup A = A$
- **Idempotência**: $A \cup A = A$
- **Comutativa**: $A \cup B = B \cup A$
- **Associativa**: $A \cup (B \cup C) = (A \cup B) \cup C$

### Intersecção

Sejam dois conjuntos $A$ e $B$. A intersercção entre eles, $A \cap B$ é definida como:

$$A \cap B = \{x \mid x \in A \wedge x \in B\}$$ {#eq:interseccao}

A união corresponde à operação lógica *conjunção* (símbolo $\wedge$).

----------------------------------------------------------------------------------
**Exemplo: intersecção**
----------------------------------------------------------------------------------
Considere os conjuntos:

a) $\mbox{Digitos} = \{0, 1, 2, 3, 4, 5, 6, 7, 8, 9\}$

b) $\mbox{Vogais} = \{a, e, i, o, u\}$
  
c) $\mbox{Pares} = \{0, 2, 4, 6, ...\}$

<!-- -->

Então:

a) $\mbox{Digitos} \cap \mbox{Vogais} = \emptyset$

b) $\mbox{Digitos} \cap \mbox{Pares} = \{0, 2, 4, 6, 8\}$
----------------------------------------------------------------------------------

Também podemos utilizar **Diagrama de Venn** para demonstrar a Intersecção, como ilustra a [@fig:interseccao-venn].

![Diagrama de Venn demonstrando a intersecção entre conjuntos A e B](./graphics/algebra-de-conjuntos_6_0.png){#fig:interseccao-venn width=6cm}

A [@fig:interseccao-venn] considera os conjuntos $A = \{1,2,3\}$ e $B = \{3,4,5\}$ e mostra o resultado de $A \cap B$. A área mais ao centro, colorida como uma mistura das cores dos conjuntos, corresponde à intersecção (não é necesssário utilizar cores, entretanto).

Sejam $A$ e $B$ dois conjuntos não vazios. Se $A \cap B = \emptyset$, então $A$ e $B$ são chamados *conjuntos disjuntos*, *conjuntos independentes*, ou *conjuntos mutuamente exclusivos*.

Propriedades da intersecção:

- **Elemento neutro**: $A \cap U = U \cap A = A$
- **Idempotência**: $A \cap A = A$
- **Comutativa**: $A \cap B = B \cap A$
- **Associativa**: $A \cap (B \cap C) = (A \cap B) \cap C$

## Propriedades envolvendo união e intersecção

As propriedades a seguir envolvem as operações de união e intersecção:

- **Distributividade da intersecção sobre a união**: $A \cap (B \cup C) = (A \cap B) \cup (A \cap C)$
- **Distributividade da união sobre a intersecção**: $A \cup (B \cap C) = (A \cup B) \cap (A \cup C)$
- **Absorção**: $A \cap (A \cup B) = A$ e $A \cup (A \cap B) = A$.


## Operações reversíveis

Entende-se por **operação reversível** uma operação a partir de cujo resultado pode-se recuperar os operandos originais.

### Complemento

Considere o conjunto universo $U$. O complemento de um conjunto $A \subseteq U$, denotado por $\sim{A}$ é definido como:

$$\sim{A} = \{x \in U \mid x \notin A \}$$ {#eq:complemento}

----------------------------------------------------------------------------------
**Exemplos: complemento**
----------------------------------------------------------------------------------
1. Considere o conjunto universo definido por $\mbox{Digitos} = \{0, 1, 2, ..., 9\}$. Seja $A = \{0, 1, 2\}$. Então, $\sim{A} = \{3, 4, 5, 6, 7, 8, 9\}$.

<!-- -->

2. Suponha conjunto universo $\mathbb{N}$. Seja $A = \{0, 1, 2\}$. Então $\sim{A} = \{ x \in \mathbb{N} \mid x > 2 \}$.

<!-- -->

3. Para qualquer conjunto universo $U$, valem:
   
a) $\sim{\emptyset} = U$

b) $\sim{U} = \emptyset$

<!-- -->

4. Suponha que $U$ é o conjunto universo. Então, para qualquer conjunto $A \subseteq U$, valem:
   
a) $A \cup \sim{A} = U$
   
b) $A \cap \sim{A} = \emptyset$
----------------------------------------------------------------------------------

No último exemplo, observe que:

- a união de um conjunto com seu complemento sempre resulta no conjunto universo ($p \lor \sim{p} = \mbox{Verdadeiro}$); e
- a intersecção de um conjunto com seu complemento sempre resulta no conjunto vazio ($p \wedge \sim{p} = \mbox{Falso}$).

Também vale a noção de *duplo complemento* (ou *dupla negação*):

$$\sim\sim{A} = A$$ {#eq:duplo-complemento}

A propriedade denominada **DeMorgan** vale-se do complemento, envolvendo as operações de unição e interseção ([@tbl:demorgan-conjuntos-logica]).

| DeMorgan na Álgebra de conjuntos        | Propriedade DeMorgan na Lógica                             |
|-----------------------------------------|------------------------------------------------------------|
| $\sim(A \cup B) = \sim{A} \cap \sim{B}$ | $\lnot(p \lor q) \Leftrightarrow \lnot{p} \wedge \lnot{q}$ |
| $\sim(A \cap B) = \sim{A} \cup \sim{B}$ | $\lnot(p \wedge q) \Leftrightarrow \lnot{p} \lor \lnot{q}$ |

: DeMorgan na álgebra de conjuntos e na Lógica {#tbl:demorgan-conjuntos-logica}

### Diferença

Sejam os conjuntos $A$ e $B$. A diferença dos conjuntos $A$ e $B$, denotada por $A - B$ é definida como:

$$A - B = A \cap \sim{B}$$ {#eq:diferenca}

ou

$$A - B = \{x \mid x \in A \wedge x \notin B \}$$ {#eq:diferenca-notacao-2}

----------------------------------------------------------------------------------
**Exemplos: diferença**
----------------------------------------------------------------------------------
1. Suponha os conjuntos: $\mbox{Digitos} = \{0, 1, 2, ..., 9\}$, $\mbox{Vogais} = \{a, e, i, o, u\}$ e $\mbox{Pares} = \{0, 2, 4, 6, ...\}$. Utilizando a diferença, temos:

a) $\mbox{Digitos} - \mbox{Vogais} = \mbox{Digitos}$

b) $\mbox{Digitos} - \mbox{Pares} = \{1, 3, 5, 7, 9\}$

<!-- -->

2. Para qualquer conjunto universo $U$ e qualquer $A \subseteq U$, valem:
   
a) $\emptyset - \emptyset = \emptyset$

b) $U - \emptyset = U$

c) $U - A = \sim{A}$

d) $U - U = \emptyset$
----------------------------------------------------------------------------------

### Conjunto das partes

Para qualquer conjunto $A$ sabe-se que:

- $A \subseteq A$
- $\emptyset \subseteq A$
- Para qualquer elemento $a \in A$, é visível que $\{a\} \subseteq A$

A operação unária chamada *conjunto das partes*, ao ser aplicada ao conjunto $A$, resulta no conjunto de todos os subconjuntos de $A$. Suponha um conjunto $A$. O conjunto das partes de $A$ (ou conjunto potência), denotado por $\mbox{P}(A)$ ou $2^A$, é definido por:

$$\mbox{P}(A) = \{X \mid X \subseteq A \}$$ {#eq:conjunto-das-partes}

----------------------------------------------------------------------------------
**Exemplos: conjunto das partes**
----------------------------------------------------------------------------------
Sejam os conjuntos $A = \{a\}$, $B = \{a, b\}$, $C = \{a, b, c\}$ e $D = \{a, \emptyset, \{a, b\}\}$, então:

1. $\mbox{P}(\emptyset) = \{\emptyset\}$

2. $\mbox{P}(A) = \{\emptyset, \{a\}\}$

3. $\mbox{P}(B) = \{\emptyset, \{a\}, \{b\}, \{a, b\}\}$

4. $\mbox{P}(C) = \{\emptyset, \{a\}, \{b\}, \{c\}, \{a, b\}, \{a, c\}, \{b, c\}, \{a, b, c\}\}$

5. $\mbox{P}(D) = \{\emptyset, \{a\}, \{\emptyset\}, \{\{a, b\}\}, \{a, \emptyset\}, \{a, \{a, b\}\}, \{\emptyset, \{a,b\}\}, \{a, \emptyset, \{a, b\}\} \}$
----------------------------------------------------------------------------------


### Produto Cartesiano

A operação **produto cartesiano **é uma operação binária que, quando aplicada a dois conjuntos $A$ e $B$, resulta em um conjunto constituído de sequências de duas componentes (tuplas), sendo que a primeira componente de cada sequência é um elemento de $A$, e a segunda componente, um elemento de $B$.

Uma sequência de $n$ componentes, denominada *$n$-upla ordenada* (lê-se: ênupla ordenada), consiste de $n$ objetos (não necessariamente distintos) em uma ordem fixa. Por exemplo, uma 2-upla (tupla) ordenada é denominada *par ordenado*. Um par ordenado no qual a primeira componente é $x$ e a segunda é $y$ é definido como $\langle x, y \rangle$ ou $(x, y)$.

Uma $n$-upla ordenada é definida como:

$$\langle x_1, x_2, x_3, ..., x_n \rangle$$ {#eq:enupla}

Uma $n$-upla ordenada não deve ser confundida com um conjunto, pois a ordem das componentes é importante. Assim:

$$\langle x, y \rangle \neq \langle y, x \rangle$$ {#eq:enupla-ordem}

O **produto cartesiano** dos conjuntos $A$ e $B$, denotado por $A \times B$ é definido por:

$$A \times B = \{ \langle a, b \rangle \mid a \in A \wedge b \in B \}$$ {#eq:produto-cartesiano}

O produto cartesiano de um conjunto com ele mesmo é definido por $A \times A = A^2$

----------------------------------------------------------------------------------
**Exemplos: produto cartesiano**
----------------------------------------------------------------------------------
Sejam os conjuntos $A = \{a\}$, $B = \{a, b\}$ e $C = \{0, 1, 2\}$. Então:

1. $A \times B = \{ \langle a, a \rangle, \langle a, b \rangle \}$

2. $B \times C = \{ \langle a, 0 \rangle, \langle a, 1 \rangle, \langle a, 2 \rangle, \langle b, 0 \rangle, \langle b, 1 \rangle, \langle b, 2\rangle \}$

3. $A^2 = \{ \langle a, a \rangle \}$
----------------------------------------------------------------------------------

### União disjunta

Diferentemente da *união*, que desconsidera repetições de elementos no conjunto resultante, a *união disjunta* permite que os elementos do conjunto resultante sejam duplicados, uma vez que seja identificada a sua fonte. A *união disjunta* dos conjuntos $A$ e $B$, denotada por $A + B$ ou $A \dot\cup\ B$ é definida como:

$$A + B = \{ \langle a, A \rangle \mid a \in A\} \cup \{ \langle b, B \rangle \mid b \in B\}$$ {#eq:uniao-disjunta}

ou

$$A + B = \{ a_A \mid a \in A\} \cup \{ b_B \mid b \in B\}$$ {#eq:uniao-disjunta-notacao-2}

----------------------------------------------------------------------------------
**Exemplo: união disjunta**
----------------------------------------------------------------------------------
Suponha os conjuntos $\mbox{Silva} = \{\mbox{João}, \mbox{Maria}, \mbox{José}\}$ e $\mbox{Souza} = \{\mbox{Pedro}, \mbox{Ana}, \mbox{José}\}$. Então:

1. $\mbox{Silva} + \mbox{Souza} = \{ \langle \mbox{João}, \mbox{Silva} \rangle, \langle \mbox{Maria}, \mbox{Silva} \rangle, \langle \mbox{José}, \mbox{Silva} \rangle, \langle \mbox{Pedro}, \mbox{Souza} \rangle, \langle \mbox{Ana}, \mbox{Souza} \rangle, \langle \mbox{José}, \mbox{Souza} \rangle \}$ 

<!-- -->

ou 
   
<!-- -->

2. $\mbox{Silva} + \mbox{Souza} = \{ \mbox{João}_{\mbox{Silva}}, \mbox{Maria}_{\mbox{Silva}}, \mbox{José}_{\mbox{Silva}}, \mbox{Pedro}_{\mbox{Souza}}, \mbox{Ana}_{\mbox{Souza}}, \mbox{José}_{\mbox{Souza}} \}$
----------------------------------------------------------------------------------


## Relações entre a Lógica e as operações sobre conjuntos

É possível estabelecer uma relação entre a lógica e as operações da álgebra de conjuntos, como mostra a [@tbl:conectivos-logicos-operacoes-sobre-conjuntos].

---------------------------------------------------------------------------------------------------------------------------------------------------
Propriedade                 Lógica                                                              Teoria dos conjuntos 
--------------------------- ------------------------------------------------------------------- ---------------------------------------------------
**idempotência**            $p \land p \Leftrightarrow p$ \                                     $A \cap A = A$ \
                            $p \lor p \Leftrightarrow p$                                        $A \cup A = A$ \

**comutativa**              $p \land q \Leftrightarrow q \land p$ \                             $A \cap B = B \cap A$ \ 
                            $p \lor q \Leftrightarrow q \lor p$                                 $A \cup B = B \cup A$ \

**associativa**             $p \land (q \land r) \Leftrightarrow (p \land q) \land r$ \         $A \cap (B \cap C) = (A \cap B) \cap C$ \
                            $p \lor (q \lor r) \Leftrightarrow (p \lor q) \lor r$               $A \cup (B \cup C) = (A \cup B) \cup C$ \

**distributiva**            $p \land (q \lor r) \Leftrightarrow (p \land q) \lor (p \land r)$ \ $A \cap (B \cup C) = (A \cap B) \cup (A \cap C)$ \
                            $p \lor (q \land r) \Leftrightarrow (p \lor q) \land (p \lor r)$    $A \cup (B \cap C) = (A \cup B) \cap (A \cup C)$ \

**negação** ou \            $\neg \neg p \Leftrightarrow p$ \                                   $\sim{\sim{A}} = A$ \
**complemento**             $p \land \neg p \Leftrightarrow F$ \                                $A \cap \sim{A} = \emptyset$ \
                            $p \lor \neg p \Leftrightarrow V$                                   $A \cup \sim{A} = U$ \

**DeMorgan**                $\neg(p \lor q) \Leftrightarrow \neg p \land \neg q$ \              $\sim{(A \cup B)} = \sim{A} \cap \sim{B}$ \
                            $\neg(p \land q) \Leftrightarrow \neg p \lor \neg q$                $\sim{(A \cap B)} = \sim{A} \cup \sim{B}$ \

**elemento neutro**         $p \land V \Leftrightarrow p$ \                                     $A \cap U = A$ \
                            $p \lor F \Leftrightarrow p$                                        $A \cup \emptyset = A$ \

**elemento absorvente**     $p \land F \Leftrightarrow F$ \                                     $A \cap \emptyset = \emptyset$ \
                            $p \lor V \Leftrightarrow V$                                        $A \cup U = U$ \

**absorção**                $p \land (p \lor q) \Leftrightarrow p$ \                            $A \cap (A \cup B) = A$ \
                            $p \lor (p \land q) \Leftrightarrow p$                              $A \cup (A \cap B) = A$
---------------------------------------------------------------------------------------------------------------------------------------------------

: Conectivos lógicos x operações sobre conjuntos {#tbl:conectivos-logicos-operacoes-sobre-conjuntos}

Ainda, as relações lógicas e as relações sobre conjuntos são análogas:

* **implicação/contigência**: na lógica: $p \Rightarrow q$, na teoria dos conjuntos: $A \subseteq B$
* **equivalência/igualdade**: na lógica: $p \Leftrightarrow q$, na teoria dos conjuntos: $A = B$

Como já visto, $p(x)$ é uma proposição que descreve uma propriedade de um elemento $x \in A$. Assim, 
a continência e a igualdade de dois conjuntos $A = \{ x \mid p(x) \}$ e $B = \{ x \mid q(x) \}$
pode ser vista assim:

* **contingência**: $A \subseteq B$ se e somente se $(\forall x \in U)(p(x) \Rightarrow q(x))$
* **igualdade**: $A = B$ se e somente se $(\forall x \in U)(p(x) \Leftrightarrow q(x))$

Exemplos:

* $A = U$ se e somente se $(\forall x \in U)(p(x) \Leftrightarrow V)$
* $A = \emptyset$ se e somente se $(\forall x \in U)(p(x) \Leftarrow F)$


## Provando propriedades

### Prova da propriedade *elemento neutro da união*

Elemento neutro é definido como: 

$$A \cup \emptyset = \emptyset \cup A = A$$ {#eq:elemento-neutro}

Assim, há duas igualdades, que podem ser analisadas considerando a validade da transitividade [da igualdade]. Assim, temos que observar alguns casos: 

**(A) Para provar $A \cup \emptyset = \emptyset \cup A$**:

*O primeiro caso (1)*: Seja $x \in A \cup \emptyset$. Então devemos provar que $A \cup \emptyset \subseteq \emptyset \cup A$:

- $x \in A \cup \emptyset \Rightarrow$ (definição de união)
- $x \in A \lor x \in \emptyset \Rightarrow$ (comutatividade da disjunção)
- $x \in \emptyset \lor x \in A \Rightarrow$ (definição de união)
- $x \in \emptyset \cup A$

Portanto, $A \cup \emptyset \subseteq \emptyset \cup A$.

*O segundo caso (2)*: Seja $x \in \emptyset \cup A$. Então devemos provar que $\emptyset \cup A \subseteq A \cup \emptyset$:

- $x \in \emptyset \cup A \Rightarrow$ (definição de união)
- $x \in \emptyset \lor x \in A \Rightarrow$ (comutatividade da disjunção)
- $x \in A \lor x \in \emptyset \Rightarrow$ (definição de união)
- $x \in A \cup \emptyset$

Portanto, $\emptyset \cup A = A \cup \emptyset$.

*Terceiro caso (3)*: De (1) e (2) concluímos que $A \cup \emptyset = \emptyset \cup A$.

**(B) Para provar $A \cup \emptyset = A$**:

*Quarto caso (4)*: Seja $x \in A \cup \emptyset$. Então devemos provar que $A \cup \emptyset \subseteq A$:

- $x \in A \cup \emptyset \Rightarrow$ (definição de união)
- $x \in A \lor x \in \emptyset \Rightarrow$ ($x \in \emptyset$ é sempre *false*)
- $x \in A$

Portanto, $A \cup \emptyset \subseteq A$.

*Quinto caso (5)*: Seja $x \in A$. Então devemos provar que $A \subseteq A \cup \emptyset$:

- $x \in A \Rightarrow$ ($x \in A$ é sempre *true*, portanto podemos considerar $p \Rightarrow p \lor q)$
- $x \in A \lor x \in \emptyset$ (definição de união)
- $x \in A \cup \emptyset$

Portanto, $A \subseteq A \cup \emptyset$.

*Sexto caso (6)*: De (4) e (5) concluímos que $A \cup \emptyset = A$.

*Sétimo caso (7)*: Por fim, de (3) e (6) e pela transitividade da igualdade, concluímos que $A \cup \emptyset = \emptyset \cup A = A$ e provamos a propriedade do *elemento neutro* da união.


## Exercícios

**Exercício 1**: Suponha o conjunto universo $S = \{p, q, r, s, t, u, v, w\}$ bem como os seguintes conjuntos: 

- $A = \{p, q, r, s\}$
- $B = \{r, t, v\}$
- $C = \{p, s, t, u\}$

Determine:

a) $B \cap C$

b) $A \cup C$

c) $\sim{C}$

d) $A \cap B \cap C$

e) $\sim(A \cup B)$

f) $(A \cup B) \cap \sim{C}$

**Exercício 2**: Considere os conjuntos $A = \{a\}$, $B = \{a, b\}$ e $C = \{0, 1, 2\}$. Calcule os seguintes produtos cartesianos:

1. $(A \times B) \times C$
2. $A \times (B \times C)$
3. $B^2$
4. $C^2$

**Exercício 3**: Considere os conjuntos $D = \{0, 1, 2, ..., 9\}$, $V = \{a, e, i, o, u\}$, e $P = \{0, 2, 4, 6, ...\}$. Então, encontre:

1. $D + V$
2. $D + P$
3. $V + V$
4. $V + \emptyset$

**Exercício 4**: Utilizando um banco de dados relacional, crie duas tabelas: *Palavras1* e *Palavras2*, respectivamente. Utilizando linguagem SQL, crie e apresente o resultado de uma consulta que realiza o produto cartesiano entre as duas tabelas.

**Exercício 5**: Crie um programa que lê $n$ arquivos de entrada. Cada arquivo contém uma palavra em cada linha. O programa deve ler os  arquivos e gerar um arquivo de saída chamado *pc.txt* contendo o produto cartesiano entre as palavras dos arquivos de entrada. Cada linha do arquivo de saída deve representar um elemento do produto cartesiano (uma $n$-upla) cujos componentes devem estar separados por um espaço [em branco].
**Exemplo**: Para os arquivos de entrada:

|palavras1.txt|
|-------------|
|jose|
|maria|

|palavras2.txt|
|-------------|
|silva|
|santos|

|palavras3.txt|
|-------------|
|moreira|
|aires|

o arquivo resultante seria:

|pc.txt|
|---------------|
|jose silva moreira|
|jose silva aires|
|jose santos moreira|
|jose santos aires|
|maria silva moreira|
|maria silva aires|
|maria santos moreira|
|maria santos aires|

**Exercício 6**: Faça uma pesquisa sobre as provas das propriedades das operações da álgebra de conjuntos e, em formato técnico-científico, apresente cada uma. 
Não se esqueça de apresentar as referências.

## Projeto do capítulo

Este capítulo deu continuidade à [@sec:teoria-dos-conjuntos] e apresentou operações e propriedades sobre conjuntos que constituem a **Álgebra de conjuntos**.

Como forma de fundamentar os conceitos apresentados este capítulo traz o **projeto do capítulo**, uma atividade prática que envolve computação e escrita de textos.

O projeto deste capítulo deve alcançar os objetivos:

1. utilizar uma linguagem de programação para criar uma estrutura de dados **Conjunto**, com as funcionalidades:
    * adicionar elemento
    * remover elemento
    * verificar pertinência
    * verificar continência
    * realizar união (com outro conjunto)
    * realizar intersecção (com outro conjunto)
    * realizar diferença (com outro conjunto)
    * realizar complemento (em relação a outro conjunto)
    * gerar o conjunto das partes
    * realizar o produto cartesiano (com outro conjunto)
    * realizar a união disjunta (com outro conjunto)
2. escrever um texto didático explicando e demonstrando a implementação e os cocneitos utilizados. Para cada funcionalidade, apresentar: o conceito (definição), a operação (como funciona), a demonstração (com exemplos). Esse texto deve usar notação matemática (o resultado é um arquivo **PDF**).

**Importante:** No *Objetivo 1* não pode ser utilizado recurso da linguagem que já implemente recursos de conjuntos e opreações sobre conjuntos. Utilize lista, vetor ou outra estrutura de dados semelhante.

Por fim, o conteúdo deve ser disponibilizado em um repositório do Github. Deve haver um arquivo `README.md` identificando e apresentando o trabalho, bem como descrevendo os procedimentos adotados.

