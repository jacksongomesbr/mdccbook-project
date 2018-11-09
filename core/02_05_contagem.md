# Contagem 

Considere o seguinte algoritmo, em pseudocódigo:

```
Algoritmo ordena(A)
n = tamanho(A)
para i de 1 até n - 1
    para j de i + 1 até n
        se (A[i] > A[j]) então
            troca(A, i, j)
```

Os algoritmos `tamanho(lista)` e `troca(lista, i, j)` representam, respectivamente:

* retorna o tamanho da `lista`
* troca os valores dos índices `i` e `j` da `lista`

No algoritmo `ordena(lista)`, quantas vezes é executado o condicional?

Analisamos isso da seguinte forma:

* da **primeira** vez: para $i = 1$, $j = \{2, ..., n\}$, executa $n - 1$ vezes
* da **segunda** vez: para $i = 2$, $j = \{3, ..., n\}$, executa $n - 2$ vezes
* da **terceira** vez: para $i = 3$, $j = \{4, ..., n\}$, executa $n - 3$ vezes
* da **quarta** vez: para $i = 4$, $j = \{5, ..., n\}$, executa $n - 4$ vezes
* da **i-ésima** vez, executa $n - i$ vezes.

Assim, o condicional é executado tantas vezes conforme indica a [@eq:contagem-ordena-inicio], para $n > 0, i = [1, (n-1)]$:

$$
(n - 1) + (n - 2) + ... + (n - i) 
$$ {#eq:contagem-ordena-inicio} 

Para $n = 5$, por exemplo, temos:

\begin{align*}
(n - 1) + (n - 2) + (n - 3) + (n - 4) = \\
(5 - 1) + (5 - 2) + (5 - 3) + (5 - 4) = \\
4 + 3 + 2 + 1 = \\
10
\end{align*}

O código a seguir, em Python, demonstra esse comportamento:

```python
lista = [1, 2, 3, 4, 5]
n = len(lista)
k = 0
for i in range(n - 1): # range(n) gera n números, de 0...(n-1)
    for j in range(i + 1, n): # range(i, n) gera números de i...(n-1)
        print('Comparando A[%d] > A[%d]' % (i, j)) 
        k = k + 1
print('O condicional executou {} vezes'.format(k))
```

A saída seria algo como o seguinte:

```
Comparando A[0] > A[1]
Comparando A[0] > A[2]
Comparando A[0] > A[3]
Comparando A[0] > A[4]
Comparando A[1] > A[2]
Comparando A[1] > A[3]
Comparando A[1] > A[4]
Comparando A[2] > A[3]
Comparando A[2] > A[4]
Comparando A[3] > A[4]
O condicional executou 10 vezes
```    

## Utilizando a teoria dos conjuntos

Podemos melhorar o raciocínio para interpretar a contagem da quantidade de comparações utilizando a linguagem de conjuntos. Suponha que o conjunto $S$ contenha todas as comparações feitas pelo algoritmo, representadas por uma tupla $(i,j)$ em que $i$ representa o primeiro índice da lista e $j$, o segundo. Considere $n = | S |$. Dividimos o conjunto $S$ em $n-1$ partes (subconjuntos):

* o conjunto $S_1$ de comparações quando $i = 1$
* o conjunto $S_2$ de comparações quando $i = 2$
* o conjunto $S_{n-1}$ de comparações quando $i = n-1$

Assim, descobrimos o número de comparações em cada conjunto $S_i$ e adicionamos para obter o tamanho do conjunto $S$.

**Exemplo:**

Para $n = 5$:

* $S_1 = \{(1,2),(1,3),(1,4),(1,5)\}$; $\left|S_1\right| = n - 1 = 5 - 1 = 4$
* $S_2 = \{<2,3>,<2,4>,<2,5>\}$; $\left|S_2\right| = n - 2 = 5 - 2 = 3$
* $S_3 = \{<3,4>,<3,5>\}$; $\left|S_3\right| = n - 3 = 5 - 3 = 2$
* $S_4 = \{<4,5>\}$; $\left|S_4\right| = n - 4 = 5 - 4 = 1$

## Princípio da adição

Cada conjunto $S_i$ é um **conjunto disjunto** dos demais porque as comparações que cada um contém são diferentes das presentes nos outros conjuntos. Em outras palavras, conjuntos são chamados disjuntos quando não possuem elementos em comum. Assim, $S = \{S_1, S_2, ..., S_m\}$ (com $m = n - 1$) é uma família de conjuntos mutuamente disjuntos. Seguindo esse pensamento podemos estabelecer o **Princípio da adição**:

> **Princípio da adição**
> 
> O tamanho da união de uma família de conjuntos finitos mutuamente disjuntos é a soma dos tamanhos dos conjuntos.

Podemos aplicar o princípio da adição para resolver o problema em questão. Considere que $\left| S \right|$ indique o tamanho do conjunto $S$, então:

\begin{align*}
\left|S_1 \cup S_2 \cup ... \cup S_m\right| = \left|S_1\right| + \left|S_2\right| + ... + \left|S_m\right| 
\end{align*}

ou, usando a notação de união:

\begin{align*}
\left|\bigcup_{i = 1}^m S_i \right| = \sum_{i = 1}^m \left|S_i\right|
\end{align*}

**Exemplo:**

Para $n = 5$:

\begin{align*}
\left|\bigcup_{i = 1}^m S_i \right| = \left|S_1\right| + \left|S_2\right| + \left|S_3\right| + \left|S_4\right| \\
= 4 + 3 + 2 + 1 \\
= 10
\end{align*}

Quando $S = \bigcup_{i = 1}^m S_i$, então temos um $S$ particionado nos conjuntos $S_1, S_2, ..., S_m$ e estes formam uma **partição** de $S$.

**Exemplo:**

* $S = \{1, 2, 3, 4, 5\}$
* O conjunto $P_1=\{\{1\}, \{2, 3\}, \{4, 5\}\}$ é uma partição de $S$
* $S$ pode ser particionado nos conjuntos $\{1\}$, $\{2, 3\}$ e $\{4, 5\}$, elementos de $P_1$, que são chamados **blocos da partição** $P_1$.

Isso permite redefinir o **Princípio da adição**:

> **Princípio da adição** (*redefinido*)
> 
> Se um conjunto finito $S$ foi dividido em _blocos_, então o tamanho de $S$ é a soma do tamanho dos blocos.

## Soma de inteiros consecutivos

Voltando para a [@eq:contagem-ordena-inicio], ela pode ser escrita como:

$$
\sum_{i = 1}^{n - 1}(n - i)
$$

Demonstramos assim, para $n = 5$:

$$
\sum_{i = 1}^{n - 1}(n - i) = (5 - 1) + (5 - 2) + (5 - 3) + (5 - 4) \\
= 4 + 3 + 2 + 1 \\
= 10
$$

Isso mostra que, na prática:

$$
\sum_{i = 1}^{n - 1}(n - i) = 4 + 3 + 2 + 1 \\
= 1 + 2 + 3 + 4 = \sum_{i = 1}^{n - 1}i
$$

Entretanto, podemos tentar encontrar uma forma de reduzir ou simplificar essa equação. Vamos experimentar o seguinte:

1. Somar $n - 1$ números, de $1$ a $n - 1$: $s_1 = 1 + 2 + ... + (n - 1)$
2. Somar $n - 1$ números, de $n - 1$ a $1$: $s_2 = (n - 1) + ... + 2   + 1$
3. Somar $n$ números $n - 1$ vezes: $s_3 = n + n + ... + n$

**Exemplo**, para $n = 5$:

1. $s_1 = 1 + 2 + 3 + 4$
2. $s_2 = 4 + 3 + 2 + 1$
3. $s_3 = 5 + 5 + 5 + 5$

Esses artifícios mostram que $s_3 = s_1 + s_2$ e esse raciocínio leva a algumas conclusões:

1. Podemos escrever $s_3 = n \times (n - 1)$
2. $s_3 = s_1 + s_2$
3. Logo, podemos afirmar que $\frac{s_3}{2} = s_1 = s_2$

A conclusão final desse raciocínio é que:

$$
\sum_{i = 1}^{n - 1}(n - i) = \sum_{1 = 1}^{n - 1}i = \frac{n \times (n - 1)}{2}
$$

Esse artifício foi utilizado por *Carl Friedrich Gauss* e, por fim, fornece uma forma útil para situações que envolvam encontrar a soma de uma série de valores ou variáveis.

**Exemplo**: Para $n = 5$, encontrar $S = 1 + 2 + ... + (n - 1)$:

$$
S = \frac{5 \times (5-1)}{2} = \frac{20}{2} = 10
$$

## Princípio do produto

Seguindo a mesma abordagem para entender o princípio da adição, veja o seguinte algoritmo `multiplica_matrizes()`, que encontra o produto de duas matrizes ($A \times B = C$):

```
Algoritmo multiplica_matrizes(A, B)
r, n = dimensoes(A) # A tem r = linhas, n = colunas
n, m = dimensoes(B) # B tem n = linhas, m = colunas
C = matriz(r, m)    # C tem r = linhas, m = colunas
para i de 1 até r
    para j de 1 até m
        s = 0
        para k de 1 até n
            s = s + A[i][k] * B[k][j]
        C[i][j] = s
retorne C
```

Onde os algoritmos `dimensoes(A)` e `matriz(m,n)` representam, respectivamente:

* as dimensões (linha x coluna) da matriz `A`
* criação de uma matriz com as dimensões `m` x `n`

Quantas multiplicações (`A[i][k] * B[k][j]`) o algoritmo executa ao final de todas as iterações (em termos de `r`, `m`, e `n`)?

Vejamos:

* o laço `para` mais interno (linha 8) executa $n$ multiplicações
* o laço `para` anterior (linha 6), repete o laço mais interno $m$ vezes. Assim, executa $n \times m$ multiplicações

Pensando no contexto de conjuntos, como foi feito na abstração do princípio da adição, temos que para todo $i = 1, ..., r$ o conjunto de multiplicações pode ser dividido em:

* conjunto $S_1$ de multiplicações quando $j = 1$
* conjunto $S_2$ de multiplicações quando $j = 2$
* conjunto $S_j$ de multiplicações para todo $j$.

Seja $T_i$ o conjunto das multiplicações para todo $i$. Este conjunto é a união dos conjuntos $S_j$:

$$
T_i = \bigcup_{j = 1}^m S_j
$$

Usando o princípio da adição, o tamanho de $T_i$ é igual à soma dos tamanhos de cada conjunto $S_j$. A soma de $m$ números, cada um igual a $n$, é $m \times n$, como mostra a [@eq:principio-produto], que define o **Princípio do produto**:

$$
\left| T_i \right| = \left| \bigcup_{j = 1}^m S_j \right| = \sum_{j = 1}^m \left| S_j \right| = \sum_{j = 1}^m n = m \times n
$$ {#eq:principio-produto}

> **Princípio do produto**
>
> O tamanho da união de conjuntos disjuntos $m$, sendo cada um de tamanho $n$, é $m \times n$.

O laço `para` mais externo (linha 5) executa uma vez para cada valor de $i = 1, ..., r$, por isso o podemos afirmar que existem $r$ conjuntos $T_i$. Portanto, pelo princípio do produto, concluímos que o algoritmo do produto entre duas matrizes executa $r \times m \times n$ multiplicações.

## Subconjunto com dois elementos

Voltemos ao algoritmo usado no princípio da adição. Algumas considerações:

* quando $i = 1$, $j = 2, ..., n$
* quando $i = 2$, $j = 3, ..., n$

Para cada número de $i$ e $j$, é feita a comparação entre $A[i]$ e $A[j]$ exatamente uma vez. Desta forma, o número de comparações é o mesmo que o número de subconjuntos de dois elementos do conjunto $\{1, 2, ..., n\}$. Uma questão importante é: **de quantas maneiras diferentes podemos escolher dois elementos desse conjunto?**

Antes de responder essa pergunta é importante apresentar (ou relembrar) o conceito de **par ordenado**: um par ordenado contém um elemento na primeira posição e outro na segunda. Por exemplo, temos o par ordenado $(2, 5)$ -- que é diferente do par ordenado $(5, 2)$, pois a ordem dos elementos é importante aqui.

O problema se torna descobrir a quantidade de pares ordenados que podem ser criados com os elementos do conjunto em questão. 

O raciocínio é este: ao escolhermos determinados primeiro e segundo elemento, existem $n$ maneiras de se escolher o primeiro elemento, e para cada escolha dele, há $n - 1$ maneiras de se escolher o segundo. Numericamente, para $n = 5$, fazemos:

* ao escolher $1$ para primeiro elemento do par são formados os pares $(1, 2), (1, 3), (1, 4), (1, 5)$
* ao escolher $2$ para primeiro elemento do par são formados os pares $(2, 1), (2, 3), (2, 4), (2, 5)$
* ao escolher $3$ para primeiro elemento do par são formados os pares $(3, 1), (3, 2), (3, 4), (3, 5)$
* ao escolher $4$ para primeiro elemento do par são formados os pares $(4, 1), (4, 2), (4, 3), (4, 5)$
* ao escolher $5$ para primeiro elemento do par são formados os pares $(5, 1), (5, 2), (5, 3), (5, 4)$

Se representarmos essas escolhas usando conjuntos ($C_1, ..., C_5$) podemos afirmar que o conjunto $C$ de todas as escolhas é igual à união de $n$ conjuntos de tamanho $n-1$, ou seja:

$$
C = \bigcup_{i=1}^{n} C_i
$$

Pelo princípio do produto, poderíamos concluir que a quantidade de pares ordenados é $n \times (n - 1)$. Portanto, para $n = 5$, teríamos $5 \times (5 - 1) = 20$.

Ao escolher os elementos para formar os pares, entretanto, chegamos ao seguinte raciocínio:

* escolher $2$ e depois $5$, para formar o par $(2,5)$ **ou**
* escolher $5$ e depois $2$, para formar o par $(5,2)$

Essa é uma consideração importante porque as duas escolhas são mutuamente exclusivas.

Portanto, o número de subconjuntos com dois elementos em $\{1, 2, ..., n\}$ é $n \times (n - 1) / 2$. Isso também pode ser representado usando a notação $\binom{n}{2}$, que pode ser lida como **$n$ termos, $2$ a $2$** ou **$n$ escolha $2$**. Assim:

$$
1 + 2 + ... + (n - 1) = \binom{n}{2} = \frac{n \times (n - 1)}{2}
$$

O seguinte programa Python demonstra esses conceitos na prática:

```python
n = 5

S = [i for i in range(1, n + 1)]
print('S = {', ', '.join([str(i) for i in S]), '}')

Pares = []
for i in range(n): 
    for j in range(i + 1, n):
        Pares.append('(%d, %d)' % (i + 1, j + 1))
       
print('Pares = {', ', '.join([i for i in Pares]), '}')
        
print(len(Pares), ' Pares')
```

A saída do programa seria:

    S = { 1, 2, 3, 4, 5 }
    Pares = { (1, 2), (1, 3), (1, 4), (1, 5), (2, 3), (2, 4), (2, 5), (3, 4), (3, 5), (4, 5) }
    10  Pares
    
## Contagem de listas, permutações e conjuntos

Para utilizar os princípios da adição e do produto na prática, considere o seguinte problema:

> Uma senha de um certo sistema de computador deveria ter de quatro a oito caracteres e conter letras minúsculas e/ou maiúsculas. Quantas senhas são possíveis?

Para resolver o problema, o raciocínio pode partir do princípio de que as senhas podem ter quatro, cinco, seis, sete ou oito caracteres. Como o conjunto de todas as senhas é a união dos conjuntos com senhas de tamanho quatro a oito, podemos usar o princípio da adição. 

Considere $P_i$ como o conjunto das senhas com $i$ caracteres e $P$ é o conjunto com todas as senhas.

$$
P = P_4 \cup P_5 \cup P_6 \cup P_7 \cup P_8
$$

Assim:

$$
\left|P\right| =  \sum_{i = 4}^8 \left|P_i\right|
$$

Qual o valor de $\left|P_i\right|$? Para isso precisamos considerar que para uma senha com $i$ letras existem 52 escolhas para a primeira letra, 52 para a segunda e assim por diante. Pelo princípio do produto:

$$
\left|P_i\right| = 52^i
$$

Portanto, o número total de senhas, $\left|P\right|$ é:

$$
\left|P\right| = 52^4 + 52^5 + 52^6 + 52^7 + 52^8
$$

A porcentagem de senhas com quatro letras é obtida como:

$$
\frac{52^4}{\left|P\right|} \times 100
$$

Esse raciocínio é útil para chegar à conclusão de que é mais fácil encontrar uma senha que já sabemos ter quatro caracteres do que entre quatro e oito caracteres e leva a uma redefinição (ou segunda versão) do princípio do produto.

**Princípio do produto (versão 2)**

Se um conjunto $S$ de listas de comprimento $m$ tem as seguintes propriedades:

* existem $i_1$ primeiros elementos diferentes das listas em $S$, e
* para cada $j > 1$ e cada escolha dos $j - 1$ elementos de uma lista em $S$, existem $i_j$ escolhas de elementos na posição $j$ daquelas listas, então, existem $i_1 \times i_2 \times ... \times i_m = \prod_{k = 1}^m i_k$ listas em $S$.

Ao aplicar esse princípio ao problema da contagem das senhas temos: como uma senha com $m$ letras é uma lista com $m$ elementos, e por existirem 52 primeiros elementos diferentes da senha e 52 escolhas para cada outra posição da senha, temos que $i_1 = 52, i_2 = 52, ..., i_m = 52$, assim, o número de senhas de comprimento $m$ é $i_1 \times i_2 \times ... \times i_m = 52^m$.

## Listas e funções

Definição formal de lista:

> Uma **lista** de $k$ coisas escolhidas a partir de $T$ consiste em um primeiro membro de $T$ até o $k$-ésimo membro de $T$. Por exemplo, uma lista de 3 coisas escolhidas de um conjunto $T$ consiste nos elementos $t_1, t_2, t_3$, todos membros de $T$. Os elementos da lista não são, necessariamente, diferentes uns dos outros. Se a lista for escrita em uma ordem diferente, será uma lista diferente.

Definição formal de função:

> Uma **função** de um conjunto $S$ (o *domínio*) para um conjunto $T$ (o *contradomínio*) é um relacionamento entre os elementos de $S$ e $T$. 

Por exemplo:

$$
f(1) = Samuel \qquad f(2) = Maria \qquad f(3) = Sara
$$

indica que $f$ é uma função que descreve uma lista de três nomes. Assim, temos uma definição: **uma lista de $k$ elementos a partir de um conjunto $T$ é uma função de $\{1, 2, ..., k\}$ para $T$**.

**Exemplo:** Quais são as funções do conjunto $\{1, 2\}$ para o conjunto $\{a, b\}$?

Para resolver a questão, precisamos especificar $f_i(1)$ e $f_i(2)$, enumerando-as:

|$f_i(1)$  |$f_i(2)$  |
|----------|----------|
|$f_1(1)=a$|$f_1(2)=b$|
|$f_2(1)=b$|$f_2(2)=a$|
|$f_3(1)=a$|$f_3(2)=a$|
|$f_4(1)=b$|$f_4(2)=b$|

O conjunto de todas as funções do conjunto $\{1, 2\}$ para o conjunto $\{a, b\}$ é a união entre as funções $f_i$ com $f_i(1) = a$ e aquelas com $f_i(1) = b$. O conjunto de funções com $f_i(1) = a$ tem dois elementos, um para cada escolha de $f_i(2)$: 

* o conjunto $f_i(1) = a = \{f_1(2) = b, f_3(2) = a\}$
* o conjunto $f_i(1) = b = \{f_2(2) = a, f_4(2) = b\}$

Pelo princípio do produto, a resposta para a questão é $2 \times 2 = 4$.

O número de funções do conjunto $\{1, 2\}$ para o conjunto $\{a, b, c\}$ é a união dos três conjuntos, um para cada escolha de $f_i(1)$, cada qual possuindo três elementos, um para cada escolha de $f_i(2)$. Assim, pelo princípio do produto, temos: $3 \times 3 = 9$.

O número de funções do conjunto $\{1, 2, 3\}$ para o conjunto $\{a, b\}$ é a união de quatro conjuntos, um para cada escolha de $f_i(1)$ e $f_i(2)$, cada qual possuindo dois elementos, um para cada escolha de $f_i(3)$. Assim, pelo princípio do produto, temos $4 \times 2 = 8$.

Uma função $f$ de um conjunto $S$ para um conjunto $T$ é chamada **um a um**, ou **injetora**, se, para cada $x \in S$ e $y \in S$, com $x \neq y$, $f(x) \neq f(y)$. No exemplo anterior as funções $f_1$ e $f_2$ são injetoras, mas $f_3$ e $f_4$ não são.

Uma função $f$ de um conjunto $S$ para um conjunto $T$ é chamada **sobrejetora** se, para cada elemento $y \in T$ (no contradomínio), existe um $x \in S$, tal que $f(x) = y$. No exemplo anterior, as funções $f_1$ e $f_2$ são sobrejetoras, mas $f_3$ e $f_4$ não são.


## Permutações de $k$ elementos de um conjunto

Uma lista de $k$ elementos distintos de um conjunto $N$ é chamada **permutação de $k$ elementos** de $N$.

Existem $n$ escolhas para o primeiro elemento da lista, para cada uma existem $(n - 1)$ escolhas para o segundo. Para cada escolha dos dois primeiros elementos da lista, há $(n - 2)$ formas de escolher o terceiro elemento, e assim por diante. 

Por exemplo, se $N = \{1, 2, 3, 4\}$, as permutações de $k = 3$ elementos são:

\begin{align}
L = \{123, 124, 132, 134, 142, 143, \\
213, 214, 231, 234, 241, 243, \\
312, 314, 321, 324, 341, 342, \\
412, 413, 421, 423, 431, 432
\}
\end{align}

Ou seja, existem $4 \times 3 \times 2 = 24$ listas com $k = 3$ elementos em $N$. Pelo princípio do produto (versão 2) isso é $n \times (n - 1) \times (n - 2)$. 

Dados os primeiros $i - 1$ elementos da lista, temos $n - (i - 1) = n - i + 1$ escolhas para o $i$-ésimo elemento da lista.

Pelo princípio do produto (versão 2) temos $n \times (n - 1) \times ... \times (n - k + 1)$ maneiras de escolher permutações de $k$ elementos de $N$. De outra forma:

\begin{align}
n \times (n - 1) \times ... \times (n - k + 1) = \prod_{i = 0}^{k-1} (n - i)
\end{align}

**Teorema 2.1**

O número de permutações de $k$ elementos de um conjunto de $n$ elementos é:

\begin{align}
n \times (n - 1) \times ... \times (n - k + 1) = \prod_{i = 0}^{k-1} (n - i) = \frac{n!}{(n-k)!}
\end{align}


## Contando subconjuntos de um conjunto
 
Usamos anteriormente $\binom{n}{3}$, que lemos "$n$ termos, 3 a 3", para representar o número de subconjuntos com três elementos do conjunto $\{1, 2, ..., n\}$.

O número de subconjuntos de $k$ elementos do conjunto $\{1, 2, ..., n\}$ é $\binom{n}{k}$, que lemos como "$n$ termos, $k$ a $k$". 

Como o número de permutações de $k$ elementos de um conjunto com $k$ elementos é $k!$ temos:

\begin{align}
\frac{n!}{(n-k)!} = \binom{n}{k} \times k!
\end{align}

Isso dá o **Teorema 2.2**:

Para inteiros $n$ e $k$, com $0 \leq k \leq n$, o número de subconjuntos de $k$ elementos de um conjunto de $n$ elementos é:

\begin{align}
C_{n,k} = \binom{n}{k} = \frac{n!}{k! \times (n - k)!}
\end{align}

A notação $C_{n, k}$ gera os chamados **coeficientes binomiais**.

## Atividade prática

Estude a relação entre o coeficiente binomial e o Triângulo de Pascal e use esse conhecimento para criar um programa que crie o Triângulo de Sierpinski (use, por exemplo, a cor preta para número ímpar e a cor branca para número par). Exemplo:

![Triângulo de Sierpinski](https://www.mathsisfun.com/images/pascals-triangle-3.gif)
