# Noções de lógica e técnicas de demonstração

Depois de ver sobre teoria dos conjuntos fica mais evidente a necessidade de estabelecer uma linguagem lógico-matemática para demonstrações e provas. Este capítulo apresenta uma revisão dos conceitos de lógica e traz técnicas de demonstração úteis nos capítulos seguintes sobre provas.

## Tautologia e contradição

Seja $w$ uma fórmula. Então:

a) $w$ é chamada de **tautologia** se $w$ for **verdadeira** (considerando todas as combinações possíveis de valores de sentenças variáveis -- entradas). Por exemplo: a fórmula $p \lor \neg p$ é uma tautologia; 
b) $w$ é chamada **contradição** se $w$ for **falsa**. Por exemplo: a fórmula $p \wedge \neg p$ é uma contradição. 

A tabela-verdade da [@tbl:tv-tautologia-contradicao] resume os valores de entrada possíveis para $p$ e $\neg p$ demonstrando tautologia e contradição das fórmulas de exemplo.

| $p$ | $\neg p$ | $p \lor \neg p$ | $p \wedge \neg p$ |
|:---:|:--------:|:---------------:|:-----------------:|
|  V  |     F    |        V        |        F          |
|  F  |     V    |        V        |        F          |

: Tabela-verdade demonstrando tautologia e contradição {#tbl:tv-tautologia-contradicao}

## Implicação e equivalência

A **relação de implicação** é definida como: sejam $p$ e $q$ duas fórmulas. Então $p$ *implica* $q$ se e somente se $p \to q$ é uma tautologia. Isso é denotado por:

$$p \Rightarrow q$$ {#eq:relacao-implicacao} 

Para exemplificar, considere a tabela-verdade a seguir.

|$p$|$q$|$p \lor q$|$p \to (p \lor q)$|$p \land q$|$(p \land q) \to p$|
|:-:|:-:|:--------:|:----------------:|:---------:|:-:
| V | V |     V    |V                 |V          |V|
| V | F |     V    |V                 |F          |V|
| F | V |V         |V                 |F          |V|
| F | F |F         |V                 |F          |V|

Vale a implicação chamada **adição**, definida por $p \Rightarrow p \lor q$. Para validar essa afirmação, verificamos que $p \to (p \lor q)$ é uma tautologia aplicando o condicional (quarta coluna da tabela-verdade).

Vale a implicação chamada **simplificação**, definida por $p \land q \Rightarrow q$. Para validar essa afirmação, verificamos que $(p \land q) \to p$ é uma tautologia (sexta coluna da tabela-verdade).

A **relação de equivalência** é definida como: sejam $p$ e $q$ duas fórmulas. Então $p$ *é equivalente a* $q$ se e somente se $p \leftrightarrow q$ é uma tautologia. Isso é denotado por:

$$p \Leftrightarrow q$$ {#eq:relacao-equivalencia}

Considere a relação de equivalência da fórmula: 

$$p \lor (q \land r) \Leftrightarrow (p \lor q) \land (p \lor r)$$

Para verificar a validade da equivalência, basta construir a tabela-verdade para demonstrar que $p \lor (q \land r) \leftrightarrow (p \lor q) \land (p \lor q)$ (chamada de $S$) é uma tautologia, ou seja:

|$p$|$q$|$r$|$q \land r$|$p \lor (q \land r)$|$p \lor q$|$p \lor r$|$(p \lor q) \land (p \lor r)$|$S$|
|:-:|:-:|:-:|:---------:|:------------------:|:--------:|:--------:|:---------------------------:|:---------:|
|V  |V  |V  |V          |V                   |V         |V         |V                            |V          |
|V  |V  |F  |F          |V                   |V         |V         |V                            |V          |
|V  |F  |V  |F          |V                   |V         |V         |V                            |V          |
|V  |F  |F  |F          |V                   |V         |V         |V                            |V          |
|F  |V  |V  |V          |V                   |V         |V         |V                            |V          |
|F  |V  |F  |F          |F                   |V         |F         |F                            |V          |
|F  |F  |V  |F          |F                   |F         |V         |F                            |V          |
|F  |F  |F  |F          |F                   |F         |F         |F                            |V          |

Também é interessante observar que a fórmula ilustra que a *distributividade* do conectivo **ou** sobre o conectivo **e** é verdadeira sempre, ou seja, é uma tautologia. O mesmo valeria para a distributividade do conectivo **e** sobre o conectivo **ou**? Verifique.

Para verificar a equivalência da fórmula:

$$(p \leftrightarrow q) \Leftrightarrow (p \rightarrow q) \land (q \rightarrow p)$$

basta demonstrar que $(p \leftrightarrow q) \leftrightarrow (p \rightarrow q) \land (q \rightarrow p)$ (chamada de $S$) é uma tautologia. Isso é conseguido utilizando a tabela-verdade:

|$p$|$q$|$p \leftrightarrow q$|$p \rightarrow q$|$q \rightarrow p$|$(p \rightarrow q) \land (q \rightarrow p)$|$S$   |
|:-:|:-:|:-------------------:|:---------------:|:---------------:|:-----------------------------------------:|:----:|
|V  |V  |V                    |V                |V                |V                                          |V     |
|V  |F  |F                    |F                |V                |F                                          |V     |
|F  |V  |F                    |V                |F                |F                                          |V     |
|F  |F  |V                    |V                |V                |V                                          |V     |

: Tabela-verdade: bicondição x condição {#tbl:tv-bicondicao-condicao}

Essa forma em particular demonstra formalmente por que a bicondição pode ser expressa por duas condições: "ida" e "volta".

Para verificar a equivalência da fórmula:

$$p \rightarrow q \Leftrightarrow \neg q \rightarrow \neg p$$

basta demonstrar que $p \rightarrow q \leftrightarrow \neg q \rightarrow \neg p$ (chamada de $S$) é uma tautologia. Isso é conseguido utilizando a tabela-verdade:

|$p$|$q$|$\neg p$|$\neg q$|$p \rightarrow q$|$\neg q \rightarrow \neg p$|  $S$   |
|:-:|:-:|:------:|:------:|:---------------:|:-------------------------:|:------:|
|V  |V  |F       |F       |V                |V                          |V       |
|V  |F  |F       |V       |F                |F                          |V       |
|F  |V  |V       |F       |V                |V                          |V       |
|F  |F  |V       |V       |V                |V                          |V       |

: Tabela-verdade: contraposição {#tbl:tv-contraposicao}

Essa relação de equivalência é conhecida como **contraposição**.

Para verificar a equivalência da fórmula:

$$p \rightarrow q \Leftrightarrow p \land \neg q \rightarrow F$$

basta demonstrar que $p \rightarrow q \leftrightarrow p \land \neg q \rightarrow F$ (chamada de $S$) é uma tautologia. Isso é conseguido utilizando a tabela-verdade:

|$p$|$q$|$\neg q$|$p \rightarrow q$|$p \land \neg q$|$p \land \neg q \rightarrow F$|   $S$   |
|:-:|:-:|:------:|:---------------:|:--------------:|:----------------------------:|:-------:|
|V  |V  |F       |V                |F               |V                             |V        |
|V  |F  |V       |F                |V               |F                             |V        |
|F  |V  |F       |V                |F               |V                             |V        |
|F  |F  |V       |V                |F               |V                             |V        |

: Tabela-verdade: redução ao absurdo {#tbl:tv-reducao-ao-absurdo}

Essa relação de equivalência é conhecida como **redução ao absurdo**.

## Quantificadores

Seja $A$ um conjunto. Uma proposição $p(x)$ sobre $A$:

a) descreve alguma propriedade de um elemento $x \in A$; e
b) tem valor lógico dependendo do elemento $x \in A$.

Então:

a) o **conjunto verdade** $p(x) = \{x \in A \mid p(x) \mbox{é verdadeira}\}$
b) o **conjunto falsidade** $p(x) = \{x \in A \mid p(x) \mbox{é falsa}\}$

Ainda:

a) se $p(x)$ é verdadeira para qualquer $x \in A$ então é uma tautologia, ou seja, o conjunto verdade é $A$;
b) se $p(x)$ é falsa para qualquer $x \in A$ então é uma contradição, ou seja, o conjunto falsidade é $A$.

----------------------------------------------------------------------------------
**Exemplos: conjuntos verdade e falsidade, tautologia e contradição**
----------------------------------------------------------------------------------
Suponha o conjunto universo $N$, então:

a) para $p(n) = n > 1$:

- conjunto verdade: $\{2, 3, 4, ... \}$
  
- conjunto falsidade: $\{0, 1\}$

- náo é tautologia e nem contradição. Por exemplo, é verdadeira para $n = 2$, mas falsa para $n = 0$

<!-- -->

b) para $p(n) = n! < 10$:

- conjunto verdade: $\{0,1,2,3\}$
  
- conjunto falsidade: $\{n \in N \mid n > 3\}$

- não é tautologia e nem contradição. Por exemplo, é verdadeira para $n = 0$, mas falsa para $n = 4$

<!-- -->

c) para $p(n) = n + 1 > n$:

- conjunto verdade: $N$

- conjunto falsidade: $\emptyset$

- é uma tautologia

<!-- -->

d) para $p(n) = 2n \mbox{ é ímpar}$

- conjunto verdade: $\emptyset$

- conjunto falsidade: $N$

- é uma contradição

----------------------------------------------------------------------------------

Os **quantificadores** são utilizados na lógica para, com relação a uma determinada proposição $p(x)$, quantificar os valores de $x$ que devem ser considerados.

O **quantificador universal**, simbolizado por $\forall$, quando associado a uma proposição $p(x)$, é denotado como qualquer uma das três opções a seguir:

$$
(\forall x \in A)(p(x)) \qquad   (\forall x \in A)p(x)   \qquad   \forall x \in A, p(x)
$${#eq:quantificador-universal}

ou, quando é claro sobre qual conjunto de valores a proposição está definida, pode-se usar:

$$
(\forall x)(p(x)) \qquad   (\forall x)p(x)   \qquad   \forall x, p(x)
$${#eq:quantificador-universal-claro}

A leitura da fórmula $(\forall x \in A) p(x)$ é: "qualquer $x$, $p(x)$" ou "para todo $x$, $p(x)$"

O **quantificador existencial**, simbolizado por $\exists$, quando associado a uma proposição $p(x)$, é denotado como qualquer uma das opções a seguir:

$$
(\exists x \in A)(p(x)) \qquad   (\exists x \in A)p(x)   \qquad   \exists x \in A, p(x)
$${#eq:quantificador-existencial}

ou, quando é claro sobre qual conjunto de valores a proposição está definida, pode-se usar:

$$
(\exists x)(p(x)) \qquad   (\exists x)p(x)   \qquad   \exists x, p(x)
$${#eq:quantificador-existencial-claro}

A leitura da fórmula $(\exists x \in A) p(x)$ é: "existe pelo menos um $x$ tal que $p(x)$" ou "existe $x$ tal que $p(x)$".

O valor-verdade de cada proposição quantificada é:

a) $(\forall x \in A) p(x)$ é **verdadeira**, se $p(x)$ for **verdadeira** para **todos os elementos de $A$**; e
b) $(\exists x \in A) p(x)$ é **verdadeira**, se $p(x)$ for **verdadeira** para **pelo menos um elemento de $A$**.

Portanto:

a) **quantificador universal**: a proposição $(\forall x \in A) p(x)$ é:
    - **verdadeira** se o conjunto verdade for igual ao conjunto $A$
    - **falsa**, caso contrário
b) **quantificador existencial**: a proposição $(\exists x \in A) p(x)$ é:
    - **verdadeira**, se o conjunto verdade for não vazio (ou diferente de $\emptyset$)
    - **falsa**, caso contrário (ou igual a $\emptyset$)

A noção de uma proposição $p(x)$ sobre um conjunto pode ser generalizada para descrever alguma propriedade de elementos $x_1 \in A_1, x_2 \in A_2, ..., x_n \in A_n$, sendo denotada da seguinte forma:

$$
p(x_1, x_2, ..., x_n)
$$ {#eq:proposicao-generalizada}

Por exemplo, para o conjunto universo $N$ valem:

* $(\forall n)(\exists m)(n < m)$ é **verdadeira**: dado **qualquer** valor $n$, **existe pelo menos um** $m$ que satisfaz a desigualdade. Por exemplo: tomando $m = n + 1$ é verdadeiro que $n < n + 1$
* $(\exists m)(\forall n)(n < m)$ é **falsa**: **existe** um número natural maior que **qualquer** outro, o que não é verdade.

