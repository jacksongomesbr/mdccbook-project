# Introdução {#sec:introducao}

## Matemática Discreta

Conforme [@menezes2010matematica] as Diretrizes Curriculares do MEC para os cursos de computação e informática definem que:

> A matemática, para a área de computação, deve ser vista como uma ferramenta a ser usada na definição formal de conceitos computacionais (linguagens, autômatos, métodos etc.). Os modelos formais permitem definir suas propriedades e dimensionar suas instâncias, dadas suas condições de contorno.

Além disso, afirmam:

> Considerando que a maioria dos conceitos computacionais pertencem ao domínio discreto, a **matemática discreta** (ou também chamada álgebra abstrata) é fortemente empregada.

Desta forma, a **Matemática Discreta** preocupa-se com o emprego de técnicas e abordagens da matemática para o entendimento de problemas a serem resolvidos com computação. Mas o que significa ser **discreto**? A matemática, por si, trata também do domínio **contínuo**. Assim, estes domínios são opostos: contínuo e discreto. Para entender isso melhor, observe a [@fig:grafico-x2]:

![Gráfico da $y = x^2$, com $0 \leq x \leq 5$](./graphics/Introducao_4_0.png){#fig:grafico-x2}

[@fig:grafico-x2] representa a função $y = x^2$, com $0 \leq x \leq 5$ em dois gráficos, sendo que o da direita destaca pontos selecionados, que representam 6 amostras (0, 1, 2, 3, 4 e 5).

Aumentando-se o número de amostras em dois instantes, para 10, 100 e 1000 teríamos, como mostra a [@fig:grafico-x2-mais-amostras]:

![Gráfico da $y = x^2$ com mais amostras](./graphics/Introducao_6_0.png){#fig:grafico-x2-mais-amostras}

O que se pode perceber pela [@fig:grafico-x2-mais-amostras] é que quanto mais se aumenta o número de amostras, mais se aproxima de uma curva perfeita. Entretanto, há um certo limite de percepção da perfeição dessa curva, por assim dizer. Por exemplo, embora a quantidade de amostras do gráfico da esquerda seja menor, a diferença para o gráfico da direita, visualmente falando, é pouco perceptível.

Considere outro exemplo: um computador possui uma capacidade de armazenamento virtualmente infinita. "Virtualmente" porque embora se aceite um limite, ele não é conhecido, já que a quantidade de unidades de armazemamento pode ser bastante grande, mas é **contável**. Assim, no contexto da computação, embora algo possa ser considerado finito ou infinito, ele é *contável* ou *discreto* no sentido de que pode ser enumerado ou sequenciado, de forma que não existe um elemento entre quaisquer dois elementos consecutivos da enumeração. 

No exemplo do computador, embora a quantidade de unidades de armazenamento não seja conhecida, ela é contável e enumerável e não se pode afirmar que exista, por um exemplo, um disco rídigo desconhecido entre os array de discos composto por D1 e D2. Outro exemplo: na matemática, o conjunto dos números naturais é contável (ou enumerável), equanto o conjunto dos números reais não é contável. 

Assim, a matemática discreta possui como ênfase os estudos matemáticos baseados em conjuntos contáveis, sejam eles finitos ou infinitos. De forma oposta, a *matemática do continuum* possui ênfase nos conjuntos não contáveis. Um exemplo disso são o cálculo diferencial e integral.

## Teoria dos Conjuntos {#sec:teoria-dos-conjuntos}

Os **conjuntos** são a base da forma de representação de enumerações de elementos em matemática discreta. Por definição um conjunto é:

> uma estrutura que agrupa objetos e constitui uma base para construir estruturas mais complexas.

Segue uma definição mais formal:

> Um *conjunto* é uma coleção de zero ou mais objetos distintos, chamados *elementos* do conjunto, os quais não possuem qualquer ordem associada.

O fato de não haver uma *ordem associada* não significa que os elementos não possam estar ordenados, num dado contexto, conforme algum critério. Apenas indica que, no geral, isso não é obrigatório.

Há duas formas (notações) de representar conjuntos: notação por extensão e notação por compreensão.

**Notação por extensão** é quando todos os elementos do conjunto estão enumerados, representados entre chaves e separados por vírgula. Exemplo: 

$\mbox{Vogais} = \{a, e, i, o, u\}$.

Entende-se que se um conjunto pode ser representado por extensão, então ele é *finito*. Caso contrário, é *infinito*.

**Notação por compreensão** representa conjuntos usando propriedades. Os exemplos a seguir usam uma pequena diferença de notação, mas representam a mesma coisa: 

- $\mbox{Pares} = \{ n \mid n \mbox{ é um número par}\}$
- $\mbox{Pares} = \{ n : n \mbox{ é um número par}\}$

Este conjunto é interpretado como: o conjunto de todos os elementos $n$ tal que $n$ é um número par. A forma geral de representar um conjunto por propriedades é:

$X = \{x : p(x)\}$

Isso quer dizer que $x$ é um elemento de $X$ se a propriedade $p(x)$ for verdadeira.

A notação por propriedades é uma boa forma de representar conjuntos *infinitos*.

Há ainda uma outra forma aceitável de representar conjuntos usando uma representação semelhante à de por extensão. Exemplos:

- $\mbox{Digitos} = \{0, 1, 2, ..., 9\}$
- $\mbox{Pares} = \{0, 2, 4, 6, ...\}$

Embora haja elementos ausentes, substituídos por reticências ($...$) é completamente aceitável e entendível o que se quer informar com a descrição do conjunto.

O número de elementos de um conjunto $A$ é representado por $|A|$ (isso também é chamado "cardinalidade"). Portanto, se $A =\{1,2,3\}$, $|A| = 3$ e $|\emptyset| = 0$.

A seguir, revemos conceitos de algumas relações entre e com conjuntos ou elementos.

### Pertinência

Se um elemento $a$ pertence ao conjunto $A$ isso é representado como: $a \in A$. Caso contrário, se $a$ não pertence a $A$, então representa-se como: $a \not\in A$.

----------------------------------------------------------------------------------
**Exemplos**: Pertence, não pertence
----------------------------------------------------------------------------------
Quanto ao conjunto $\mbox{Vogais} = \{a, e, i, o, u\}$:

a) $a \in \mbox{Vogais}$

b) $h \not\in \mbox{Vogais}$

<!-- -->

Quanto ao conjunto $B = \{x : x \mbox{ é brasileiro}\}$:

a) $\mbox{Pele} \in B$

b) $\mbox{Bill Gates} \not\in B$
----------------------------------------------------------------------------------


### Conjuntos importantes

O **conjunto vazio** é um conjunto sem elementos, representado como $\{\}$ ou $\emptyset$. Exemplos:

- o  conjunto de todos os brasileiros com mais de 300 anos;
- o conjunto dos números que são, simultaneamente, ímpares e pares.

O **conjunto unitário** é um conjunto constituído por um único elemento. Exemplos:

- o conjunto constituído pelo jogador de futebol Pelé;
- o conjunto de todos os números que são, simultaneamente, pares e primos, ou seja: $P = \{2\}$;
- um conjunto unitário cujo elemento é irrelevante: $1 = \{*\}$.

O **conjunto universo**, normalmente denotado por $U$, contém todos os conjuntos considerados em um dado contexto.

Outros conjuntos importantes:

- $N$: o conjunto dos números naturais (inteiros positivos e o zero)
- $Z$: o conjunto dos números inteiros (inteiros negativos, positivos e o zero)
- $Q$: o conjunto dos números racionais (os que podem ser representados na forma de fração)
- $I$: o conjunto dos números irracionais
- $R$: o conjunto dos números reais

### Alfabetos, palavras e linguagens

Em computação, e mais especificamente em linguagens de programação, um conceito importante é o que define o conjunto de elementos ou termos-chave da linguagem. 

Um **alfabeto** um conjunto finito cujos elementos são denominados *símbolos* ou *caracteres*.

Uma **palavra** (cadeia de caracteres ou sentença) sobre um alfabeto é uma sequência finita de símbolos justapostos.

Uma **linguagem [formal]** é um conjunto de palavras sobre um alfabeto.


----------------------------------------------------------------------------------
**Exemplos**: alfabeto, palavra
----------------------------------------------------------------------------------
a) Os conjuntos $\emptyset$ e $\{a, b, c\}$ são alfabetos

b) O conjunto $N$ não é um alfabeto

c) $\epsilon$ é uma palavra vazia

d) $\Sigma$ é geralmente usada para representar um alfabeto

e) $\Sigma^*$ é o conjunto de todas as palavras possíveis sobre o alfabeto $\Sigma$

f) $\epsilon$ é uma palavra do alfabeto $\emptyset$

g) $\{a, b\}^* = \{\epsilon, a, b, aa, ab, ba, bb, aaa, ...\}$
----------------------------------------------------------------------------------

### Continência, subconjunto e igualdade de conjuntos

A *continência* permite introduzir os conceitos de *subconjunto* e *igualdade de conjunto*.

Se todos os elementos de um conjunto $A$ também são elementos de um conjunto $B$, então $A$ está *contido* em $B$, o que é representado por: $A \subseteq B$. Isso também é lido como $A$ é *subconjunto* de $B$.

Se $A \subseteq B$, mas há $b \in B$ tal que $b \not\in A$, então pode-se dizer que $A$ está *contido propriamente* em $B$, ou que $A$ é *subconjunto próprio* de $B$. Isso é denotado por: $A \subset B$.

A negação de *subconjunto* e *subconjunto próprio* é, respectivamente:

- $A \not\subseteq B$ e
- $A \not\subset B$

----------------------------------------------------------------------------------
**Exemplos**: continência, subconjunto
----------------------------------------------------------------------------------
a) $\{a, b\} \subseteq \{b, a\}$

b) $\{a, b\} \subset \{a, b, c\}$, e $\{a, b\} \subseteq \{a, b, c\}$
----------------------------------------------------------------------------------

A *igualdade de conjuntos* é um conceito baseado em pertinência: se os elementos de $A$ também são elementos de $B$ e vice-versa, então $A = B$. Formalmente, uma condição para $A = B$ é que $A \subseteq B$ e $B \subseteq A$.

----------------------------------------------------------------------------------
**Exemplo**
----------------------------------------------------------------------------------
$\{1, 2, 3\} = \{3, 3, 3, 2, 2, 1\}$
----------------------------------------------------------------------------------

É importante notar que pertinência ($\in$) é usada entre elementos e conjuntos, enquanto continência ($\subset$ e $\subseteq$) é usada entre conjuntos.

Por definição, um conjunto qualquer é subconjunto de si mesmo, e $\emptyset$ é subconjunto de qualquer conjunto. 

----------------------------------------------------------------------------------
**Exemplo**
----------------------------------------------------------------------------------
Seja $A = \{1, 2\}$ então os subconjuntos de $A$ são: $\emptyset$, $\{1\}$, $\{2\}$ e $\{1, 2\}$.
----------------------------------------------------------------------------------

## Conjuntos, Tuplas e Listas

Uma **Tupla** (ou ênupla) é uma sequência ordenada de $n$ elementos (ou componentes). As principais diferenças para **conjunto** são:

* uma ênupla pode conter um elemento mais de uma vez;  e
* os elementos são, obrigatoriamente, ordenados, ou seja, cada elemento está em uma posição diferente.

A notação utilizada é $X = (c_1, c_2, ..., c_n)$ onde:

* $X$ é uma ênupla com $n$ componentes
* $c_1$ é o primeiro componente da ênupla
* $c_n$ é o último componente da ênupla
* $c_i$ é o i-ésimo componente da ênupla

**Exemplos:** 

* $X = (1, 1, 2, 3)$
* $X = (1_1, 1_2, 2_3, 3_4)$
* $Y = (3_1, 2_2, 1_3)$

As mesmas relações de pertinência entre conjuntos e elementos podem ser aplicadas entre ênuplas e seus componentes.

Uma **Lista** é uma estrutura de dados que implementa o conceito matemático de **Tupla**, então podemos afirmar para $\mbox{Vogais} = (a, e, i, o, u)$:

* $\mbox{Vogais}$  é uma lista com $5$ elementos
* $a$ é a primeira vogal
* $u$ é a última vogal

## Exercícios

**Questão 1**. Para cada conjunto abaixo: a) descreva de forma alternativa (usando outra forma de notação); e b) diga se é finito ou infinito.

a) todos os números inteiros maiores que 10
b) $\{1, 3, 5, 7, 9, 11, ...\}$
c) todos os países do mundo (Terra)
d) a linguagem de programação Python


**Questão 2**. Para $A = \{1\}$, $B = \{1, 2\}$ e $C = \{\{1\}, 1\}$, marque as afirmações corretas:

a) $A \subset B$
b) $A \subseteq B$
c) $A \in B$
d) $A = B$
e) $A \subset C$
f) $A \subseteq C$
g) $A \in C$
h) $A = C$
i) $1 \in A$
j) $1 \in C$
k) $\{1\} \in A$
l) $\{1\} \in C$
m) $\emptyset \not\in C$
n) $\emptyset \subset C$

**Questão 3**. Sejam $a = \{x \mid 2x = 6 \}$ e $b = 3$. É correto afirmar que $a = b$? Por que?

**Questão 4**. Quais todos os subconjuntos dos seguintes conjuntos?

a) $A = \{a, b, c\}$
b) $B = \{a, \{b, c\}, D\}$, dado que $D = \{1, 2\}$

**Questão 5**. O conjunto vazio está contido em qualquer conjunto, inclusive nele próprio? Justifique.

**Questão 6**. Todo conjunto possui um subconjunto próprio? Justifique.

**Questão 7**. Sejam $A = \{0,1,2,3,4,5\}$, $B = \{3,4,5,6,7,8\}$, $C = \{1,3,7,8\}$, $D=\{3,4\}$, $E=\{1,3\}$, $F=\{1\}$ e $X$ um conjunto desconhecido. Para cada item abaixo, determine quais dos conjuntos $A$, $B$, $C$, $D$, $E$ ou $F$ podem ser iguais a $X$:

a) $X \subseteq A$ e $X \subseteq B$
b) $X \not\subset B$ e $X \subseteq C$
c) $X \not\subset A$ e $X \not\subset C$
d) $X \subseteq B$ e $X \not\subset C$

**Questão 8**. Sejam $A$ um subconjunto de $B$ e $B$ um subconjunto de $C$. Suponha que $a \in A$, $b \in B$, $c \in C$, $d \not\in A$, $e \not\in B$, $f \not\in C$. Quais das seguintes afirmações são verdadeiras?

a) $a \in C$
b) $b \in A$
c) $c \not\in A$
d) $d \in B$
e) $e \not\in A$
f) $f \not\in A$

**Questão 9**. Bancos de dados relacionais costumam representar conjuntos de dados organizados em tabelas, colunas e registros. É possível considerar alguma semelhança entre o conceito de tabela e o conceito de conjunto? Há recursos de consulta (em linguagem SQL, por exemplo) que permitam identificar, ainda que parcialmente, relações entre tabelas e registros (ou valores) como as expressadas nesse capítulo entre elementos e conjuntos? Explique.

**Questão 10**. Escolha uma linguagem de programação e demonstre seus recursos para lidar com conjuntos e listas. Utilizando código-fonte (e a sintaxe da linguagem de programação) demonstre e explique as diferenças conceituais e demonstre recursos da linguagem que permitam identificar as relações de pertinência, continência, subconjunto e igualdade. 

