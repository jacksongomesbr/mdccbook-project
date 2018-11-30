# Bayes, Bayes, Baby

O capítulo anterior apresentou conceitos fundamentais de Probabilidade e uma das principais ferramentas, o *Teorema de Bayes*. Este capítulo contribui com o anterior, trazendo uma leitura e uma aplicação prática.

## Dados

Considere um conjunto de dados com informações sobre pessoas (sexo, idade e renda familiar):

```
sexo;idade;rendafamiliar
F;20;2000
M;19;3000
M;19;3000
M;20;2500
M;21;3000
```

O conjunto de dados está no formato CSV. Cada linha do conjunto de dados, com exceção da primeira, que representa o cabeçalho, representa um indivíduo (uma pessoa) no conjunto de dados. A partir desse conjunto de dados, vamos fazer algumas análises.

Imagine que uma nova pessoa respondeu a pesquisa, mas não se sabe nada dela. Qual a probabilidade de essa nova pessoa ser do sexo masculino? Para resolver essa questão, vamos utilizar as ferramentas anteriores. A primeira delas é a distribuição de probabilidade, enumerando o conjunto de dados e a quantidade de ocorrências de cada sexo.

```python
PDSexo = ProbDist(
    Sexo_M=4,
    Sexo_F=1
)
```

O valor de `PDSexo` é um dicionário com duas chaves, `Sexo_F` e `Sexo_M`, e seus valores indicam que:

* frequência do sexo feminino (`Sexo_F`): $1/5 =  0.2$
* probabilidade de ser do sexo masculino (`Sexo_M`): $4/5 = 0.8$

Na sequência, definimos dois predicados:

```python
def sexo_m(r): 
    return 'Sexo_M' in r

def sexo_f(r): 
    return 'Sexo_F' in r
```

Os predicados representados pelas funções `sexo_m()` e `sexo_f()` são aplicados ao dicionário `PDSexo` e retornam `True` se a chave correspondente estiver presente no dicionário.

Assim, podemos calcular a probabilidade de um novo indivíduo ser do sexo masculino usando a função `P()`, o predicado `sexo_m()` e `PDSexo`:

```python
P(sexo_m, PDSexo)
```

O resultado é: `0.8`.

O que $0,8$ (ou $80\%$) quer dizer? Chamamos isso de **probabilidade independente**, pois estamos considerando que a **variável** "sexo" não depende de outra variável do conjunto de dados. Variável? Isso, esse é o termo usado, mas, para simplificar, é uma coluna no conjunto de dados.

Outra forma de enxergar isso é perceber que a frequência (aqui diretamente relacionada à probabilidade) é $\frac{4}{5} = 0.8$:

\begin{align}
A = \mbox{conjunto das pessoas do sexo masculino} \\
S = \mbox{conjunto das pessoas} \\
P(Sexo=M) = P(A) = \frac{\mid A \mid}{\mid S \mid} = \frac{4}{5} = 0.8
\end{align}

Perceba que se fôssemos fazer uma manchete disso, ficaria mais interessante algo como:

> **8 em cada 10 pessoas são homens**

Ao invés de

> **4 de 5 pessoas são homens**

Claro, a relação se mantém. Verifique.

Imagine que você continuou olhando para os dados e ficou curioso. De repente, vem a pergunta: **e como fazer para a idade?**. Talvez sua pergunta venha do fato de que tentou imaginar que seria pouco produtivo gerar a probabilidade de cada idade possível. Considerando idades entre 20 e 59 anos, por exemplo, não seria difícil gerar as probabilidades individuais para cada idade, mas isso não seria prático.

Nesses casos, a técnica é usar uma **categorização** da variável "idade". Assim:

* até 20 anos: categoria A
* 21 a 30 anos: categoria B
* 31 a 50 anos: categoria C
* 51 anos ou mais: categoria D

Isso começa a deixar a situação mais interessante, pois podemos encontrar as quantidades das idades conforme as categorias e gerar a distribuição de probabilidade:

```python
PDIdades = ProbDist(
    Idade_A=4,
    Idade_B=1,
    Idade_C=0,
    Idade_D=0
)
```

O valor de `PDIdades` significa que:

* probabilidade de a idade estar na categoria A: $4/5 = 0.8$
* probabilidade de a idade estar na categoria B: $1/5 = 0.2$
* probabilidade de a idade estar na categoria C: $0/5 = 0.0$
* probabilidade de a idade estar na categoria D: $0/5 = 0.0$

Alguns predicados:

```python
def idade_A(r):
    return 'Idade_A' in r

def idade_B(r):
    return 'Idade_B' in r

def idade_C(r): 
    return 'Idade_C' in r

def idade_D(r): 
    return 'Idade_D' in r
```

Com estas ferramentas podemos responder a pergunta: qual a probabilidade de uma pessoa estar na categoria de idade B (faixa de 21 a 30 anos):

```python
P(idade_B, PDIdades)
```

O resultado é $0.2$.

O raciocínio é o mesmo se usarmos a contagem:

\begin{align}
A = \mbox{conjunto das pessoas com idade entre 21 e 30 anos (faixa B)} \\
S = \mbox{conjunto de todas as pessoas} \\
P(Idade=B) = P(A) = \frac{\mid A \mid}{\mid S \mid} = \frac{1}{5} = 0.2
\end{align}

Ou seja, 2 em cada 10 pessoas estão na faixa de idade B (21 a 30 anos).

Suponha que alguém tenha se questionado como responder a pergunta: dado que uma pessoa está na faixa etária B, qual a probabilidade de ser homem? Para responder isso, criamos uma **distribuição de probabilidade conjunta**:

```python
PDSexoIdade = joint(PDSexo, PDIdades, ' ')
```

O valor de `PDSexoIdade` é:

    {
        'Sexo_F Idade_A': 0.16,
        'Sexo_F Idade_B': 0.04,
        'Sexo_F Idade_C': 0.0,
        'Sexo_F Idade_D': 0.0,
        'Sexo_M Idade_A': 0.64,
        'Sexo_M Idade_B': 0.16,
        'Sexo_M Idade_C': 0.0,
        'Sexo_M Idade_D': 0.0
     }

Daí respondemos a pergunta calculando:

```python
P(sexo_m, tal_que(idade_B, PDSexoIdade))
```

O resultado é, aproximadamente, $0.8$; então a resposta para a pergunta anterior é $80\%$. 

Outra informação importante é que a distribuição de probabilidade conjunta (resultado da função `joint()`) representa a distribuição de probabilidade de dois eventos ocorrerem sequencialmente, por isso usamos `joint(PDSexo, PDIdades)`. 

> O que seria `joint(PDIdades, PDSexo)`? Por que os valores são iguais?

Com base nessas informações podemos interpretar o resultado da seguinte forma:


```python
PA = P(sexo_m, PDSexoIdade)
PE = P(idade_B, PDSexoIdade)
prob = PA * PE / PE
```

O valor de `prob` é `0.8000000000000002` ou, aproximadamente, $0.8$.

Perceba que há um padrão nesse tipo de pergunta: "dado que" é chamado de **evidência** e representa a informação dada no enunciado (ex.: "dado que uma pessoa está na faixa etária B"). 

Em outras palavras, essa técnica para encontrar a probabilidade de um evento dada a ocorrência \[anterior\] de uma evidência é chamada **probabilidade condicional** ou **Teorema de Bayes**.

Usando o Teorema de Bayes na sua forma clássica temos:


```python
# Evidência
PE = P(idade_B, PDSexoIdade)
print('P(E) = P(Idade=B) = %.1f%%' % (PE * 100))

# Hipótese A (Sexo = F)
PA = P(sexo_f, PDSexoIdade)
print('P(A) = P(Sexo=F) = %.1f%%' % (PA * 100))

# Hipótese B (Sexo = M)
PB = P(sexo_m, PDSexoIdade)
print('P(B) = P(Sexo=M) = %.1f%%' % (PB * 100))

# Evidência, dada Hipótese A
PEA = P(idade_B, tal_que(sexo_f, PDSexoIdade))
print('P(E|A) = P(Idade=B|Sexo=F) = %.1f%%' % (PEA * 100))

# Evidência, dada Hipótese B
PEB = P(idade_B, tal_que(sexo_m, PDSexoIdade))
print('P(E|B) = P(Idade=B|Sexo=M) = %.1f%%' % (PEB * 100))

# Outra forma de encontrar P(E)
PE2 = PEA * PA + PEB * PB
print('P(E) = P(Idade=B) = %.1f%%' % (PE2 * 100))

# probabilidade desejada (Sexo = M), dada a Evidência -> P(B|E)
PBE = P(sexo_m, tal_que(idade_B, PDSexoIdade))
print('P(B|E) = P(Sexo=M|Idade=B) = %.1f%%' % (PBE * 100))

# outra forma de encontrar P(B|E)
PBE2 = PEB * PB / PE
print('P(B|E) = P(Sexo=M|Idade=B) = %.1f%%' % (PBE2 * 100))

# outra forma de encontrar P(B|E)
PBE3 = PB * PE / PE
print('P(B|E) = P(Sexo=M|Idade=B) = %.1f%%' % (PBE3 * 100))
```

Os resultados seriam:


    P(E) = P(Idade=B) = 20.0%
    P(A) = P(Sexo=F) = 20.0%
    P(B) = P(Sexo=M) = 80.0%
    P(E|A) = P(Idade=B|Sexo=F) = 20.0%
    P(E|B) = P(Idade=B|Sexo=M) = 20.0%
    P(E) = P(Idade=B) = 20.0%
    P(B|E) = P(Sexo=M|Idade=B) = 80.0%
    P(B|E) = P(Sexo=M|Idade=B) = 80.0%
    P(B|E) = P(Sexo=M|Idade=B) = 80.0%
    

**Exercícios**

* dado que uma pessoa é do sexo feminino, qual a probabilidade da sua renda estar na faixa B? (considere as faixas: A (até 1000), B (1001 a 3000), C (3001 a 5000) e D (acima de 5000)

* dado que uma pessoa está na faixa etária B, qual a probabilidade da sua renda estar na faixa A?
