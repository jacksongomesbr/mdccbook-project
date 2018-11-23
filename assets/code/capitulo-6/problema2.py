import funcoes

# definição do modelo da urna
urna = funcoes.cross('W', '12345678') | funcoes.cross('B', '123456') | funcoes.cross('R', '123456789')

# possibilidades de resultados/escolhas com 6 bolas
U6 = funcoes.combos(urna , 6)

# eventos em que há 3 bolas azuis, 2 bolas brancas e 1 bola vermelha
b3w2r1 = {s for s in U6 if s.count('B') == 3 and s.count('W') == 2 and s.count('R') == 1}

# a probabilidade de ocorrer o evento
prob_b3w2r1 = funcoes.P(b3w2r1, U6)

print(prob_b3w2r1)
print(float(prob_b3w2r1))
