# Probabilidade  {#sec:probabilidade}

## Definições iniciais

Experimento

:   Uma ocorrência com um **resultado** incerto. Também pode ser chamado "processo". 

    Exemplos: 

    * rolar um dado
    * um usuário utilizar uma interface com vários botões que podem ser pressionados sem uma ordem pré-estabelecida


Resultado

:   O resultado de um **experimento**; um "estado" particular do mundo (ambiente). Também pode ser chamado "caso". 

    Exemplos: 

    * 4 (como resultado do experimento "rolar um dado"); 
    * usuário pressionou o botão "Sair" (como resultado do experimento "usuário utilizar uma interface com vários botões")


Espaço amostral

:   O conjunto de todos os **resultados** possíveis para um experimento. 

    Exemplos: 
    
    * $lados = \{1, 2, 3, 4, 5, 6\}$; 
    * $botoes = \{\mbox{Salvar}, \mbox{Sair}, \mbox{Cancelar}, \mbox{Ajuda}\}$


Evento

:   Um subconjunto do **espaço amostral**. 

    Exemplos: 
    
    * o evento "dado com face par" é o conjunto dos resultados $\{2, 4, 6\}$
    * o evento "usuário pressionou botão do formulário" é o conjunto dos resultados $botoes = \{\mbox{Salvar}, \mbox{Cancelar}\}$


Probabilidade

:   A probabilidade de um **evento** em relação a um **espaço amostral** é a quantidade de **resultados** no evento dividida pela quantidade de resultados no espaço amostral. Como é uma razão, o valor de uma probabilidade será **sempre** um número entre $0$ (um evento impossível) e $1$ (um evento certo). Entretanto, é importante considerar que é bastante comum encontrar a porcentagem apresentada entre $0$ e $100$, ou seja, é o valor entre $0$ e $1$ multiplicado por $100$.

    Exemplo: 
    
    * a probabilidade do evento "dado com face par" é $3/6 = 1/2 = 0.5$ ou 50 %
    * a probabilidade do evento "usuário pressionou botão do formulário" é o conjunto é $2/4 = 0.5$



## A função $P()$

$P()$ é o nome tradicional para a função **Probabilidade**:

```python
from fractions import Fraction

def P(evento, espaco):
    "A probabilidade de um `evento`, dado o `espaco` amostral"
    return Fraction(len(evento & espaco), len(espaco))
```

O código implementa o conceito "Probabilidade é simplemente uma fração cujo numerador é o número de casos favorávels e cujo denominador é o número de todos os casos possíveis" (Laplace). Os parâmetros `evento` e `espaco` são conjuntos.


## Aquecimento: Rolar um dado

Qual é a probabilidade de rolar um dado e a face superior ser um número par? Consideramos, para isso, um dado com seis faces.

Podemos definir o espaço amostral $A$ (o conjunto das faces do dado), o evento $par$ (o conjunto dos resultados que atendem ao **predicado** "dado com face par") e calcular a probabilidade:

```python
A = {1, 2, 3, 4, 5, 6}
par = {2, 4, 6}
print(P(par, A))
```

Resultado:

    1/2

O tipo do resultado de `P(par, A)` é `Fraction`, portanto o resultado do código também poderia ser `Fraction(1, 2)`. O código utiliza o tipo `Fraction` para que o resultado seja apresentado como fração, não como número real. Obviamente, $1/2 = 0.5$.

*Você pode perguntar*: "por que não usar `len(evento)` ao invés de `len(evento & espaco)`? Isso é necessário porque não podem ser considerados resultados que não estejam presentes no espaço amostral. Veja só:

```python
par = {2, 4, 6, 8, 10, 12}
print(P(par, A))
```

Teria como resultado:

    1/2


Se considerasse apenas `len(evento)`, o retorno seria outro:

```python
Fraction(len(par), len(A))
```

Resultado:

    Fraction(1, 1)



Os "casos favoráveis", da definição de Laplace, resultam da interseção $\mbox{evento} \cap \mbox{espaco}$. No código da função `p()`, considerando que os parâmetros sejam conjuntos, isso é feito usando o operador `&`, por isso `len(evento & espaco)`.


### Sobre o tipo `Fraction` em Python

O tipo `Fraction` do Python é usado para representar valores na forma de frações (racional). Por exemplo:


```python
print(Fraction(0.5))
print(Fraction(0.3))

# usa limit_denominator() para encontrar a fração mais aproximada
print(Fraction(0.3).limit_denominator()) 

print(Fraction(3, 10)) 
print(Fraction(0.3333333))

# limitando o denominador (padrão é max=1000000)
print(Fraction(0.3333333).limit_denominator()) 

# convertendo o valor de Fraction() para float()
print(float(Fraction(0.3333333))) 
```

Resultado:

    1/2
    5404319552844595/18014398509481984
    3/10
    3/10
    6004798902680711/18014398509481984
    1/3
    0.3333333


## Problemas com urnas

Problemas com urnas surgiram por volta do ano 1700, com o matemático *Jacob Bernoulli*. Por exemplo:

* Uma urna contém 23 bolas: 8 brancas, 6 azuis e 9 vermelhas. Selecionamos seis bolas aleatoriamente (cada seleção com a mesma chance de acontecer). Qual é a probabilidade desses três resultados possíveis:

1. todas as bolas são vermelhas
2. 3 são azuis, 2 são vermelhas e 1 é branca
3. 4 são brancas

Então, um resultado é um **conjunto** com 6 bolas, enquanto o espaço amostral é o conjunto de todas as possíveis combinações (também conjuntos) com 6 bolas. Antes de continuar a solução, duas questões:

1. há múltiplas bolas da mesma cor (ex: 8 bolas brancas)
2. um resultado é um **conjunto** de bolas, então a ordem dos seus elementos não importa (diferentemente da **lista** -- ou sequência -- para a qual a ordem importa)

Para resolver a primeira questão, vamos nomear as bolas usando uma letra e um número, assim: 

* as 8 bolas brancas serão chamadas `W1` até `W8`
* as 6 bolas azuis serão chamadas `B1` até `B6`
* as 9 bolas vermelhas serão chamadas `R1` até `R9`

Para resolver a segunda questão teremos que trabalhar com permutações e então encontrar combinações, dividindo o número de permutações por $c!$, onde $c$ é o número de bolas em uma combinação. 

Por exemplo, se eu precisar escolher 2 bolas de 8 disponíveis, há 8 formas de escolher a primeira, e 7 formas de escolher a segunda. Sendo assim, há $8 \times 7 = 56$ permutações, mas $52/2 = 26$ combinações. Tudo isso porque $\{W1, W2\} = \{W2, W1\}$.

Vamos lá. O código a seguir define a função `cross()` e o conteúdo da urna:


```python
def cross(A, B):
    "O conjunto de formas de concatenar os itens de A e B (produto cartesiano)"
    return {a + b
            for a in A for b in B
           }

urna = cross('W', '12345678') | cross('B', '123456') | cross('R', '123456789')
```

Os parâmetros `A` e `B` devem ser iteráveis, ou seja, podem ser conjuntos, listas ou... strings.

O código para definir a variável `urna` utiliza a função `cross()` para gerar três conjuntos, um para cada cor de bola, e depois gera a união entre eles (utilizando o operador `|`).

A variável `urna` é um conjunto de 23 elementos $\{B1, B2, ..., B6, R1, R2, ..., R9, W1, W2, ..., W8\}$.

Agora, vamos definir o espaço amostral, chamado `U6`, o conjunto de todas as combinações com 6 bolas. O código a seguir define a função `combos()`:

```python
import itertools

def combos(items, n):
    "Todas as combinações de n items; cada combinação concatenada em uma string"
    return {' '.join(combo)
            for combo in itertools.combinations(items, n)
           }

U6 = combos(urna, 6)
```

Os parâmetros são:

* `items`: deve ser uma lista ou um conjunto
* `n`: deve ser um número inteiro que representa o tamanho de cada combinação

A função `combos()` utiliza o pacote `itertools` e a função `combinations()` e concatena o resultado dela para gerar um conjunto de strings como resultado final.

A variável `U6` contém o conjunto de todas as combinações (resultados possíveis) com 6 bolas. O tamanho dessa variável é $100947$ (a quantidade de combinações). O código a seguir usa o pacote `random` para apresentar uma amostra de tamanho 10 (função `sample()`) dessa variável.


```python
import random

print(random.sample(U6, 10))
```

Resultado:

    ['W2 W3 W6 R7 W1 W8',
     'B4 R9 W5 B2 R4 R5',
     'W5 R6 R3 W8 W7 R5',
     'W4 W5 R6 W7 R5 B6',
     'B1 W5 R8 W8 R4 W7',
     'B4 R9 B1 B5 R3 B2',
     'W2 W6 R7 R3 W8 B2',
     'W1 R3 W8 R4 R5 B6',
     'B4 R9 W1 B2 B3 B6',
     'R9 W3 W5 R3 B2 B3']


**Mas...** será que o $100.947$ é a quantidade correta de formas de escolher 6 de 23 bolas? Bem, o raciocínio é esse:

* Escolha uma de 23 (sobram 22)
* Escolha uma de 22 (sobram 21)
* ...
* Escolha seis de 18

Como não ligamos para a ordem (enfim, é um **conjunto**), então dividimos por $6!$. Isso dá:

\begin{align}
23 \mbox{ escolha } 6 = \frac{23 \times 22 \times 21 \times 20 \times 19 \times 18}{6!} = 100947
\end{align}

Note que $23 \times 22 \times 21 \times 20 \times 19 \times 18 = 23!/(23-6)!$, então, podemos generalizar:

\begin{align}
n \mbox{ escolha } c = \frac{n!}{c!\times(n - c)!} = \binom{n}{c}
\end{align}

Podemos traduzir isso para código, definindo a função `escolha()`:

```python
from math import factorial

def escolha(n, c):
    "Número de formas de escolher c itens de uma lista com n items"
    return factorial(n) // (factorial(c) * factorial(n - c))
```

Os parâmetros são:

* `n`: tamanho da lista
* `c`: quantos itens da lista (tamanho da combinação)

O código utiliza o pacote `math` e a função `factorial()` para encontrar o resultado do binomial. Em Python, o operador `/` é utilizado para uma divisão resultando em um número real, enquanto `//` resulta em um número inteiro.

Por exemplo:

```python
escolha(23, 6)
```

Resulta em `100947`.

Agora temos uma API que permite resolver vários problemas. Relembrando:

* `P(evento, espaco)`: calcula a probabilidade de um `evento` dado um `espaco` 
* `escolha(n, c)`: calcula o número de forma de escolher `c` itens de uma lista com `n` itens

Os problemas a seguir estão no contexto urna do enunciado anterior.

**Problema 1: qual a probabilidade de selecionar 6 bolas vermelhas?**

O problema considera a mesma definição da `urna` apresentada anteriormente. A resolução envolve o código a seguir.

```python
red6 = {s for s in U6 if s.count('R') == 6}
prob_red6 = P(red6, U6)
```

O código define o conjunto `red6`, que resulta de um **filtro** na variável `U6`: utiliza a função `count(n)` para identificar quais os elementos de `U6` possuem 6 ocorrências da letra `R`, ou seja, 6 bolas vermelhas.

O resultado desse raciocínio: a probabilidade de escolher 6 bolas vermelhas é `4/4807 = 0.0008` (0.08 %) ou `len(red6) / len(U6) = 84 / 100.947` (`len(red6) = 84` indica que há 84 escolhas possíveis).

**Por que 84 escolhas possíveis?** Por que há 9 bolas vermelhas na urna, então estamos querendo saber quantas são as formas de escolher 6 delas:

```python
escolha(9, 6)
```

O resultado é `84`.

Portanto, a probabilidade de selecionar 6 bolas vermelhas da urna é `escolha(9, 6)` dividido pelo tamanho do espaço amostral:

```python
P(red6, U6) == Fraction(escolha(9, 6), len(U6))
```

O código verifica se o valor de `P(red6, U6)` é igual a `Fraction(escolha(9, 6), len(U6))`. O resultado é: `True`.

**Importante:** Reveja a definição da modelagem do problema e do raciocínio da sua resolução quantas vezes forem necessárias para fixar o entendimento.


**Problema 2: qual a probabilidade de escolher 3 azuis, 2 brancas e 1 vermelha?**

De forma semelhante ao problema anterior, primeiro é necessário criar um modelo que representa o ennciado (o evento), ou seja: no espaço amostral, quais os possíveis resultados têm três bolas azuis, duas brancas e uma vermelha? Para isso, temos o código:

```python
b3w2r1 = {s for s in U6 if s.count('B') == 3 and s.count('W') == 2 and s.count('R') == 1}

prob_b3w2r1 = P(b3w2r1, U6)
```

O código encontra os resultados que têm três letras "B", duas "W" e 1 "R" e, a partir dele, encontra a probabilidade desejada. O resultado é: $240/4807 = 0.05$ ou 5 %.

Podemos encontrar o mesmo resultado contando de quantas formas podemos escolher 3 de 6 azuis, 2 de 8 brancas, 1 de 9 vermelhas e dividindo o resultado pelo tamanho do espaço amostral. Assim, o código a seguir verifica essa igualdade:

```python
P(b3w2r1, U6) == Fraction(escolha(6, 3) * escolha(8, 2) * escolha(9, 1), len(U6))
```

O resultado é `True`.

O raciocínio seguinte também é válido:

* há 6 bolas azuis, então...
    * há 6 formas de encontrar a primeira bola azul
    * há 5 formas de encontrar a segunda azul
    * há 4 formas de encontrar a terceira azul
* há 8 bolas brancas, então...
    * há 8 formas de encontrar a primeira bola branca
    * há 7 formas de encontrar a segunda branca
* há 9 bolas vermelhas, então...
    * há 9 formas de encontrar a bola vermelha

Como $\{B1, B2, B3\} = \{B3, B2, B1\}$ e $\{W1, W2\} = \{W2, W1\}$, teríamos:

\begin{align}
\frac{(6 \times 5 \times 4) \times (8 \times 7) \times (9)}{3! \times 2! \times |A|}
\end{align}

Ou, em código:

```python
 P(b3w2r1, U6) == Fraction((6 * 5 * 4) * (8 * 7) * 9, 
                           factorial(3) * factorial(2) * len(U6))
```

O resultado é `True`.

**Problema 3: Qual a probabilidade de termos exatamente 4 bolas brancas?**

Podemos encontrar a resposta usando os mesmos raciocínios anteriores:

```python
w4 = {s for s in U6 if
      s.count('W') == 4}

prob_w4 = P(w4, U6)
```

O resultado é `350/4807 = 0.07` ou `7.3%`. Para checar o resultado, temos:

```python
P(w4, U6) == Fraction(escolha(8, 4) * escolha(15, 2), len(U6))
```

O resultado é `True`.

Ou, de outra forma:

```python
P(w4, U6) == Fraction((8 * 7 * 6 * 5) * (15 * 14), factorial(4) * factorial(2) * len(U6))
```

O resultado é `True`.

Esse último raciocínio, em particular, é interpretado assim:

* há 8 bolas brancas, então...
    * 8 escolhas para a primeira bola
    * 7 escolhas para a segunda
    * 6 escolhas para a terceira
    * 5 escolhas para a segunda
* há $23 - 8 = 15$ bolas não brancas, então...
    * 15 escolhas para as outras bolas restantes (não brancas)
    * 14 escolhas para as outras bolas restantes (não brancas restantes)

Ou seja:

\begin{align}
\frac{(8 \times 7 \times 6) \times (15 \times 14)}{4! \times 2! \times |A|}
\end{align}

## Revisando a função P, com eventos mais gerais

Até o momento, para calcular a probabilidade de um dado com face par, usamos:

```
par = {2, 4, 6}
```

Entretanto, embora seja fácil enumerar um conjunto pequeno, é difícil enumerar um conjunto maior. Assim o código a seguir apresenta uma redefinição da função `P()` e a função `tal_que()`:


```python
def P(evento, espaco):
    """A probabilidade de um evento, dado um espaco amostral. 
    evento pode ser um conjunto ou um predicado"""
    if callable(evento):
        evento = tal_que(evento, espaco)
    return Fraction(len(evento & espaco), len(espaco))

def tal_que(predicado, colecao):
    "O subconjunto de elementos da colecao para os quais o predicado é verdadeiro"
    return {e for e in colecao if predicado(e)}
```

O código da função `P()` verifica se o parâmtro `evento` é uma função (aqui chamamos de "predicado"). Se sim, então executa a função `tal_que()` usando o predicado.

A função `tal_que()` aceita dois parâmetros:

* `predicado`: uma expressão que retorna um valor booleano
* `colecao`: o iterável (conjunto ou lista, por exemplo) sobre o qual o predicado será aplicado

O retorno da função é um conjunto com os elementos de `colecao` que satisfazem `predicado` (ou seja, o tornam `True`).

Vamos verificar como isso se comporta. O código a seguir define a função `eh_par()`, um predicado:

```python
def eh_par(n):
    return n % 2 == 0
```

O resultado de `P(eh_par, A)` é `1/2`. Então, aplicando esse conceito, temos o conjunto `D12` (um conjunto com 12 números inteiros, de 1 a 12):

```python
D12 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}

pares = tal_que(eh_par, D12)
```

O resultado é que `pares` é igual a o conjunto $\{2, 4, 6, 8, 10, 12\}$, ou seja, os elementos de `D12` que satisfazem ao predicado (são pares). A probabilidade é calculada assim:

```python
P(eh_par, D12)
```

O resultado é `1/2`, ou seja, a probabilidade de que um número entre 1 e 12 seja par é $0.5$ ou 50%.

Isso permite coisas interessantes. Por exemplo, como determinar a probabilidade de que a soma de três dados é um número primo?

```python
A3 = {(a1, a2, a3) for a1 in A for a2 in A for a3 in A}

def soma_eh_primo(r): 
    return eh_primo(sum(r))

def eh_primo(n): 
    return n > 1 and not any(n % i == 0 for i in range(2, n))

P(soma_eh_primo, A3)
```

O resultado é `73/216 = 0.34` ou 34%.


## Problemas com cartas

Considerando as cartas de um baralho, definimos o problema assim:

* 4 naipes: 
    * copas (C) (ou *hearts* - H)
    * ouro (O) (ou *diamond* - D)
    * paus (P) (ou *clubs* - C) e
    * espadas (E) (ou *spades* - S)
* 13 graus: 1 (Ás), 2, 3, 4, 5, 6, 7, 8, 9, 10 (ou T), 11 (J), 12 (Q), 13 (K)

O baralho possui 52 cartas. O código a seguir define o problema:

```python
naipes = 'SHDC'
graus = 'A23456789TJQK'
baralho  = cross(graus, naipes)
```

O resultado de `len(baralho)` é 52.

Quais as jogadas (mãos) com 5 cartas?

```python
jogadas5 = combos(baralho, 5)
```

Então podemos verificar que `len(jogadas5) == escolha(52, 5)` e podemos apresentar uma amostra do conjunto:

```python
random.sample(jogadas, 5)
```

Resulta em:

    ['3C 3H 8H 2H AC',
     '8C KS 5C 2H 3S',
     'JS 6C JD KH JC',
     '7H 7C 9D 9H KH',
     '5S TC 5D 5C 4C']


**Problema 1: Qual a probabilidade de dar *flush* (5 cartas do mesmo naipe)?**

```python
def flush(jogada):
    return any(jogada.count(n) == 5 for n in naipes)

prob_flush = P(flush, jogadas)
```

O resultado, o valor de `prob_flush`, é: `33/16660 = 0.002` ou 0.2%.


**Problema 2: Qual a probabilidade de dar *four of a kind* (4 cartas iguais, mesmo com naipes diferentes) ?**

```python
def four_kind(jogada):
    return any(jogada.count(g) == 4 for g in graus)

prob_fk = P(four_kind, jogadas)
```

O resultado, o valor de `prob_fk`, é: `1/4165 =  0.0002` ou 0.02%.


    Fraction(1, 4165)

Curioso sobre as jogadas do Pôker?  Veja: https://pt.wikipedia.org/wiki/Tabela_de_jogadas_do_p%C3%B4quer.


## Fermat e Pascal: Apostas, Triângulos e o nascimento da Probabilidade

Considere um jogo de apostas, consistindo do fato de jogar uma moeda. Dois jogadores: **H** aposta em cara; e **T** aposta em coroa. Ganha o jogador que conseguir 10 acertos primeiro. O que fazer se o jogo for interrompido quando H tiver acertado 8 e T, acertado 7? Como dividir o pote de dinheiro? Fermat e Pascam trocaram correspondências sobre esse problema, o que pode ser lido [aqui](http://mathforum.org/isaac/problems/prob1.html).

Podemos resolver o problema com as ferramentas definidas anteriormente. Primeiro, alguns predicados:

```python
def ganhar_jogo_incompleto(h_pontos, t_pontos):
    "A probabilidade de que H vai ganhar o jogo não terminado, dados os pontos necessários para H e T ganharem."
    def h_ganha(r): return r.count('h') >= h_pontos
    return P(h_ganha, continuacoes(h_pontos, t_pontos))

def continuacoes(h_pontos, t_pontos):
    "Todas as continuações possíveis quando H precisa de `h_pontos` e T precisa de `t_pontos`"
    rodadas = ['ht' for _ in range(h_pontos + t_pontos - 1)]
    return set(itertools.product(*rodadas))
```

O valor de `continuacoes(2, 3)` (os possíveis retornos restantes para os jogadores) contém:


    {('h', 'h', 'h', 'h'),
     ('h', 'h', 'h', 't'),
     ('h', 'h', 't', 'h'),
     ('h', 'h', 't', 't'),
     ('h', 't', 'h', 'h'),
     ('h', 't', 'h', 't'),
     ('h', 't', 't', 'h'),
     ('h', 't', 't', 't'),
     ('t', 'h', 'h', 'h'),
     ('t', 'h', 'h', 't'),
     ('t', 'h', 't', 'h'),
     ('t', 'h', 't', 't'),
     ('t', 't', 'h', 'h'),
     ('t', 't', 'h', 't'),
     ('t', 't', 't', 'h'),
     ('t', 't', 't', 't')}

O resultado de `ganhar_jogo_incompleto(2, 3)` é `11/16 = 0.6875` ou a probabilidade de H ganhar o joogo é 68,75%.

O resultado confirma o encontrado por Pascal e Fermat.


## Resultados não equiprováveis: Distribuições de probabilidade

Até aqui, lidamos com casos em que a probabilidade de um retorno no espaço amostral é a mesma (uniforme). No mundo real, isso não é sempre verdade. Por exemplo, a probabilidade de uma criança ser uma menina não é exatamente 1/2 (50%), e a probabilidade é um pouco diferente para uma segunda criança. Uma pesquisa encontrou as seguintes contagens de famílias com dois filhos na Dinamarca (**GB** significa uma família em que o primeiro filho é uma garota e o segundo filho é um menino):

```
GG: 121801     GB: 126840
BG: 127123     BB: 135138
```

Vamos introduzir mais três definições:

* **Frequência**: um número que descreve o quão frequente um resultado ocorre. Pode ser uma contagem, como 121801, ou uma razão, como 0,515
* **Distribuição**: um mapeamento de resultado para frequência, para cada resultado no espaço amostral.
* **Distribuição de Probabilidade**: uma distribuição que foi *normalizada* de tal forma que a soma das frequências é 1

Definimos a classe `ProbDist` (um subtipo do `dict` do Python):


```python
class ProbDist(dict):
    "Uma distribuição de probablidade; um mapeamento {resultado: probabilidade}"
    def __init__(self, mapping=(), **kwargs):
        self.update(mapping, **kwargs)
        total = sum(self.values())
        for outcome in self:
            self[outcome] = self[outcome]/total
            assert self[outcome] >= 0
```

Também redefinimos as funções `P()` e `tal_que()`:


```python
def P(evento, espaco):
    """A probabilidade de um evento, dado um espaço amostral de resultados equiprováveis.
    evento: uma coleção de resultados, ou um predicado.
    espaco: um conjunto de resultados ou a distribuicao de probabilidade na forma de pares {resultado: frequencia}.
    """
    if callable(evento):
        evento = tal_que(evento, espaco)
    if isinstance(espaco, ProbDist):
        return sum(espaco[o] for o in espaco if o in evento)
    else:
        return Fraction(len(evento & espaco), len(espaco))
    
def tal_que(predicado, espaco):
    """Os resultados no espaço amostral para os quais o predicado é verdadeiro.
    Se espaco é um conjunto, retorna um subconjunto {resultado, ...}
    Se espaco é ProbDist, retorna um ProbDist{resultado, frequencia}"""
    if isinstance(espaco, ProbDist):
        return ProbDist({o:espaco[o] for o in espaco if predicado(o)})
    else:
        return {o for o in espaco if predicado(o)}
    
```

Aqui está a distribuição de probabilidade para as famílias Dinamarquesas com dois filhos:

```python
DK = ProbDist(GG=121801, GB=126840, BG=127123, BB=135138)
```

O resultado, o valor de `DK`:


    {'BB': 0.2645086533229465,
     'BG': 0.24882071317004043,
     'GB': 0.24826679089140383,
     'GG': 0.23840384261560926}


Vamos entender o resultado em partes. Para isso, alguns predicados:

```python
def primeiro_menina(r): return r[0] == 'G'
def primeiro_menino(r): return r[0] == 'B'
def segundo_menina(r): return r[1] == 'G'
def segundo_menino(r): return r[1] == 'B'
def duas_meninas(r): return r == 'GG'
def dois_meninos(r): return r == 'BB'
```

O resultado de `P(primeiro_menina, DK)` é `0.4866706335070131`.

O resultado de `P(segundo_menina, DK)` é `0.4872245557856497`.

Isso indica que a probabilidade de uma criança ser menina está entre 48% e 49%, mas isso é um pouco diferente entre o primeiro e o segundo filhos:

```python
P(segundo_menina, tal_que(primeiro_menina, DK)), P(segundo_menina, tal_que(primeiro_menino, DK))
```

O resultado é: `(0.4898669165584115, 0.48471942072973107)`.

E, para:

```python
P(segundo_menino, tal_que(primeiro_menina, DK)), P(segundo_menino, tal_que(primeiro_menino, DK))
```

O resultado é `(0.5101330834415885, 0.5152805792702689)`.

Isso diz que é mais provável que o sexo do segundo filho seja igual ao do primeiro cerca de 50%.

## Mais problemas de Urnas: M&Ms e Bayes

Outro problema de urna (Allen Downey):

> O M&M azul foi introduzido em 1995. Antes disso, a mistura de cores em um pacote de M&Ms era formado por: 30% marrom, 20% amarelo, 20% vermelho, 10% verde, 10% laranja, 10% tostado. Depois, ficou: 24% azul, 20% verde, 16% laranja, 14% amarelo, 14% vermelho, 13% marrom. Um amigo meu possui dois pacotes de M&Ms e ele me diz que um é de 1994 e outro é de 1996. Ele não me diz qual é qual, mas me dá um M&M de cada pacote. Um é amarelho e outro é verde. Qual a probabilidade de que o M&M amarelo seja do pacote de 1994?

Para resolver esse problema, primeiro representamos as distribuições de probabilidade de cada pacote:

```python
bag94 = ProbDist(brown=30, yellow=20, red=20, green=10, orange=10, tan=10)
bag96 = ProbDist(blue=24, green=20, orange=16, yellow=14, red=13, brown=13)
```

A seguir, definimos `MM` como a *probabilidade conjunta* -- o espaço amostral para escolher um M&M de cada pacote. O resultado `yellow green` significa que um M&M amarelo foi selecionado do pacote de 1994 e um verde, do pacote de 1996.

```python
def joint(A, B, sep=''):
    """A probabilidade conjunta de duas distribuições de probabilidade independentes. 
    Resultado é todas as entradas da forma {a+sep+b: P(a)*P(b)}"""
    return ProbDist({a + sep + b: A[a] * B[b]
                    for a in A
                    for b in B})

MM = joint(bag94, bag96, ' ')
```

O resultado é:

    {
        'brown blue': 0.07199999999999998,
        'brown brown': 0.03899999999999999,
        'brown green': 0.059999999999999984,
        'brown orange': 0.04799999999999999,
        'brown red': 0.03899999999999999,
        'brown yellow': 0.041999999999999996,
        'green blue': 0.023999999999999994,
        'green brown': 0.012999999999999998,
        'green green': 0.02,
        'green orange': 0.015999999999999997,
        'green red': 0.012999999999999998,
        'green yellow': 0.013999999999999999,
        'orange blue': 0.023999999999999994,
        'orange brown': 0.012999999999999998,
        'orange green': 0.02,
        'orange orange': 0.015999999999999997,
        'orange red': 0.012999999999999998,
        'orange yellow': 0.013999999999999999,
        'red blue': 0.04799999999999999,
        'red brown': 0.025999999999999995,
        'red green': 0.04,
        'red orange': 0.031999999999999994,
        'red red': 0.025999999999999995,
        'red yellow': 0.027999999999999997,
        'tan blue': 0.023999999999999994,
        'tan brown': 0.012999999999999998,
        'tan green': 0.02,
        'tan orange': 0.015999999999999997,
        'tan red': 0.012999999999999998,
        'tan yellow': 0.013999999999999999,
        'yellow blue': 0.04799999999999999,
        'yellow brown': 0.025999999999999995,
        'yellow green': 0.04,
        'yellow orange': 0.031999999999999994,
        'yellow red': 0.025999999999999995,
        'yellow yellow': 0.027999999999999997
    }

Primeiro, o predicado que trata "um é amarelho e o outro é verde":

```python
def yellow_and_green(r): 
    return 'yellow' in r and 'green' in r
```

O resultado de `tal_que(yellow_and_green, MM)` é:

    {'green yellow': 0.25925925925925924, 'yellow green': 0.7407407407407408}

Agora podemos responder a pergunta: dado que tivemos amarelo e verde (mas não sabemos sabemos qual vem de qual pacote), qual é a probabilidade de que o amarelo tenha vido do pacote de 1994?

```python
def yellow94(r): return r.startswith('yellow')
```

O resultado de `P(yellow94, tal_que(yellow_and_green, MM))` é `0.7407407407407408`. Então, há 74% de chance de que o amarelo tenha vindo do pacote de 1994.

A forma de resolver o problema foi semelhante ao que já vínhamos fazendo: criar um espaço amostral, usar P para escolher a probabilidade do evento em questão, dado que sabemos sobre o retorno. 

Poderíamos usar o *Teorema de Bayes*, mas por que? Porque queremos saber a probabilidade de um evento dada uma evidência, que não está imediatamente disponível; entretanto, a probabilidade da evidência dado o evento está disponível.

Antes de ver as cores dos M&Ms, há duas hipóteses, A e B, ambas com igual probabilidade:

```
A: primeiro M&M do pacote de 1994, segundo do pacote de 1996
B: primeiro M&M do pacote de 1996, segundo do pacote de 1994
```

\begin{align}
P(A) = P(B) = 0.5
\end{align}

Então, temos uma evidência:

```
E: primeiro M&M amarelo, depois verde
```

Queremos saber a probabilidade da hipótese A, dada a evidência E: $P(A \mid E)$.

Isso não é fácil de calcular (exceto numerando o espaço amostral), mas o Teorema de Bayes diz:

\begin{align}
P(A \mid E) = \frac{P(E \mid A) \times P(A)}{P(E)} 
\end{align}


As quantidades do lado direito são mais fáceis de calcular:

\begin{align}
P(E \mid A) &= P(Yellow94) \times P(Green96) &= 0.20 \times 0.20 &= 0.04 \\
P(E \mid B) &= P(Yellow96) \times P(Green94) &= 0.10 \times 0.14 &= 0.014 \\
P(A) &= 0.5 \\
P(B) &= 0.5 \\
P(E) &= P(E \mid A) \times P(A) + P(E \mid B) \times P(B) \\
&= 0.04 \times 0.5 + 0.014 \times 0.5 = 0.027
\end{align}

O resultado final:

\begin{align}
P(A \mid E) &= \frac{P(E \mid A) \times P(A)}{P(E)} \\
&= \frac{0.4 \times 0.5}{0.027} \\
&= 0.7407407407
\end{align}

Então é isso. Você tem uma escolha: O Teorema de Bayes permite fazer menos cálculos, mas usa mais álgebra; é melhor custo-benefício se você estiver trabalhando com lápis e papel. Por outro lado, enumerar o espaço amostrar usa menos álgebra, pelo custo de requerer mais cálculos; é melhor custo-benefício se você estiver usando um computador. Idependentemente da abordagem utilizada, é importante conhecer o Teorema de Bayes e como ele funciona.

**Mais importante ainda: você comeria M&Ms de 20 anos?**
