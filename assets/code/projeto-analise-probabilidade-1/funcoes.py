from fractions import Fraction
from math import factorial
import random
import itertools

def cross(A, B):
    "O conjunto de formas de concatenar os itens de A e B (produto cartesiano)"
    return {a + b
            for a in A for b in B
           }

def combos(items, n):
    "Todas as combinações de n items; cada combinação concatenada em uma string"
    return {' '.join(combo)
            for combo in itertools.combinations(items, n)
           }

def escolha(n, c):
    "Número de formas de escolher c itens de uma lista com n items"
    return factorial(n) // (factorial(c) * factorial(n - c))

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
        return ProbDist({o: espaco[o] for o in espaco if predicado(o)})
    else:
        return {o for o in espaco if predicado(o)}


class ProbDist(dict):
    "Uma distribuição de probablidade; um mapeamento {resultado: probabilidade}"
    def __init__(self, mapping=(), **kwargs):
        self.update(mapping, **kwargs)
        total = sum(self.values())
        if total != 0:
            for outcome in self:
                self[outcome] = self[outcome]/total
                assert self[outcome] >= 0

def joint(A, B, sep=''):
    """A probabilidade conjunta de duas distribuições de probabilidade independentes.
    Resultado é todas as entradas da forma {a+sep+b: P(a)*P(b)}"""
    return ProbDist({a + sep + b: A[a] * B[b]
                    for a in A
                    for b in B})

## predicados
def soma_eh_primo(r): return eh_primo(sum(r))

def eh_primo(n): return n > 1 and not any(n % i == 0 for i in range(2, n))

def eh_par(n): return n % 2 == 0

