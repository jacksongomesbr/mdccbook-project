import funcoes

# definição do modelo da urna
urna = funcoes.cross('W', '12345678') | funcoes.cross('B', '123456') | funcoes.cross('R', '123456789')

# possibilidades de resultados/escolhas com 6 bolas
U6 = funcoes.combos(urna , 6)


red6 = {s for s in U6 if s.count('R') == 6}
prob_red6 = funcoes.P(red6 , U6)

print(len(red6) / len(U6))
print(float(prob_red6))
