import funcoes

# define os valores possíveis de cada variável do conjunto de dados
formacoes = 'Ensino Fundamental Completo, Ensino Médio Completo, \
Ensino Superior Incompleto, Ensino Superior Completo, Pós-Graduação'.split(', ')

frequencias = 'Nenhuma, Pouca, Moderada, Intensa'.split(', ')

ambientes = 'Google Docs, Word, Libre Office, FastFormat, Quip, \
Zoho, Only Office, Outros'.split(', ')

problemas = 'Criação de sumários, Criação de lista de figuras, Numeração de páginas, \
Espaçamento do texto, Alinhamento do texto, Criar referências, Fazer citações, \
Criar tabelas, Não compreender a ferramenta, Outros'.split(', ')

opcoes = 'Modelo de documentos, Gerador de Referências, Tutorial interativo da Ferramenta, \
Sugestões de erros, Dicas de formatação, Instruções para citações, \
Compartilhar documento com o orientador, Gerador de Gráficos, \
Criação automática de sumários, Verificação de plágio, Gerador de Tabela de Siglas, \
Gerador de Tabela de Imagens, Outros'.split(', ')

# define contadores para cada valor das variáveis do conjunto de dados
cont_formacoes = {}
cont_frequencias = {}
cont_ambientes = {}
cont_problemas = {}
cont_opcoes = {}

# inicializa os contadores
for formacao in formacoes:
    cont_formacoes[formacao] = 0

for frequencia in frequencias:
    cont_frequencias[frequencia] = 0

for ambiente in ambientes:
    cont_ambientes[ambiente] = 0

for problema in problemas:
    cont_problemas[problema] = 0

for opcao in opcoes:
    cont_opcoes[opcao] = 0

# abre o arquivo do conjunto de dados para leitura
with open('Trabalhos Acadêmicos.csv', encoding='utf-8') as arquivo:
    # processa as linhas do arquivo do conjunto de dados
    for linha in arquivo:
        # quebra cada linha em partes, a partir da vírgula
        registro = linha.split(',')
        # passa para a próxima iteração se for o cabeçalho
        if "Timestamp" in registro[0]:
            continue
        # conta os valores para a variável formação
        for formacao in cont_formacoes:
            if formacao in registro[1]:
                cont_formacoes[formacao] += 1
        # conta os valores para a variável frequência
        for frequencia in cont_frequencias:
            if frequencia in registro[2]:
                cont_frequencias[frequencia] += 1
        # conta os valores para a variável ambiente
        registro_ambientes = [r.strip('"') for r in registro[3].split(';')]
        for ambiente in registro_ambientes:
            if ambiente in cont_ambientes:
                cont_ambientes[ambiente] += 1
            else:
                # considera qualquer valor que não for uma das opções possíveis
                # como opção "Outros"
                cont_ambientes['Outros'] += 1
        # conta os valores para a variável problemas
        registro_problemas = [r.strip('"') for r in registro[4].split(';')]
        for problema in registro_problemas:
            if problema in cont_problemas:
                cont_problemas[problema] += 1
            else:
                cont_problemas['Outros'] += 1
        # conta os valores para a variável opções
        registro_opcoes = [r.strip('"') for r in registro[5].split(';')]
        for opcao in registro_opcoes:
            if opcao in cont_opcoes:
                cont_opcoes[opcao] += 1
            else:
                cont_opcoes['Outros'] += 1

# define as distribuições de probabilidade individuais para cada variável
# do conjunto de dados
pd_formacao = funcoes.ProbDist(cont_formacoes)
pd_ambiente = funcoes.ProbDist(cont_ambientes)
pd_frequencia = funcoes.ProbDist(cont_frequencias)
pd_problema = funcoes.ProbDist(cont_problemas)
pd_opcao = funcoes.ProbDist(cont_opcoes)


# define predicados gerais
def predicado_formacao_esc(k):
    return 'Ensino Superior Completo' in k


def predicado_formacao_efc(k):
    return 'Ensino Fundamental Completo' in k


def predicado_formacao_esi(k):
    return 'Ensino Superior Incompleto' in k


def predicado_opcao_cas(k):
    return 'Criação automática de sumários' in k


def predicado_problema_cs(k):
    return 'Criação de sumários' in k


def predicado_problema_clf(k):
    return 'Criação de lista de figuras' in k


def predicado_problema_np(k):
    return 'Numeração de páginas' in k


def predicado_problema_et(k):
    return 'Espaçamento do texto' in k


def predicado_problema_at(k):
    return 'Alinhamento do texto' in k


def predicado_problema_cr(k):
    return 'Criar referências' in k


def predicado_problema_fc(k):
    return 'Fazer citações' in k


def predicado_problema_ct(k):
    return 'Criar tabelas' in k


def predicado_problema_ncf(k):
    return 'Não compreender a ferramenta' in k


def predicado_ambiente_word(k):
    return 'Word' in k


def predicado_ambiente_google_docs(k):
    return 'Google Docs' in k


# resoluções das questões (2 - 7)

# 2: Dado que uma pessoa indique que sua formação acadêmica é Ensino Superior Incompleto
# qual a probabilidade de ela ter problemas com Criar referências, Fazer citações ou Numeração de páginas?

# define um predicado específico para a questão 2:
# o problema ser Criar referências, Fazer citações ou Numeração de páginas
def predicado_q2(k):
    return 'Criar referências' in k or 'Fazer citações' in k or 'Numeração de páginas' in k

# define a distribuição de probabilidade conjunta entre 
# a distribuição de probabilidade de formação
# e a distribuição de probabilidade de problema
pd_formacao_problema = funcoes.joint(pd_formacao, pd_problema, ' - ')

# encontra a probabilidade: 
# P(Problema=Criar referências, Fazer Citações ou Numeração de Páginas | Formacao=Ensino Superior Incompleto)
prob_q2 = funcoes.P(predicado_q2, funcoes.tal_que(predicado_formacao_esi, pd_formacao_problema))

print('Questão 2')
print('-' * 70)
print('''A probabilidade de uma pessoa ter problemas com Criar referências, 
Fazer citações ou Numeração de páginas dado que sua formação acadêmica 
é Ensino Superior Completo é: {:.3}'''.format(prob_q2))
print()
print()


# 3: Dado que uma pessoa indique que utiliza o ambiente Word qual a probabilidade de que o
# problema na edição de trabalhos acadêmicos seja Criação de sumários?

# define a distribuição de probabilidade conjunta entre
# a distribuição de probabilidade de ambiente
# e a distribuição de probabilidade de problema
pd_ambiente_problema = funcoes.joint(pd_ambiente, pd_problema, ' - ')

# encontra a probabilidade:
# P(Problema=Criação de sumários | Ambiente=Word)
prob_q3 = funcoes.P(predicado_problema_cs, funcoes.tal_que(predicado_ambiente_word, pd_ambiente_problema))

print('Questão 3')
print('-' * 70)
print('''A probabilidade de uma pessoa ter problema com Criação de sumários
dado que utiliza o ambiente Word é: {:.3}'''.format(prob_q3))
print()
print()


# 4: Dado que uma pessoa indique que utiliza o ambiente Word e seu problema de edição de
# trabalhos acadêmicos seja Criação de sumários qual a probabilidade de que ela gostaria
# que uma ferramenta de edição fornecesse como ajuda a Criação automática de sumários?

# define a distribuição de probabilidade conjunta entre
# a distribuição de probabilidade de ambiente
# a distribuição de probabilidade de problema
# e a distribuição de probabilidade de opção
pd_ambiente_problema_opcao = funcoes.joint(funcoes.joint(pd_ambiente, pd_problema, ' - '), pd_opcao, ' - ')

# define um predicado específico para a questão 4:
# o ambiente deve ser Word e o problema deve ser Criação de sumários
def predicado_q4(k):
    return predicado_ambiente_word(k) and predicado_problema_cs(k)

# encontra a probabilidade
# P(Opção=Criação automática de sumários | Ambiente=Word & Problema=Criação de sumários)
prob_q4 = funcoes.P(predicado_opcao_cas, funcoes.tal_que(predicado_q4, pd_ambiente_problema_opcao))

print('Questão 4')
print('-' * 70)
print('''A probabilidade de uma pessoa gostar de ajuda com
Criação automática de sumários dado que ela utiliza o ambiente Word e 
tem problema com Criação de sumários é: {:.3}'''.format(prob_q4))
print()
print()


# 5: Dado que uma pessoa indique que sua formação acadêmica é Ensino Fundamental Completo
# qual a probabilidade de ela utilizar Google Docs ou Word como ambiente de edição de trabalhos?

# define a distribuição de probabilidade conjunta entre
# a distribuição de probabilidade de formação
# e a distribuição de probabilidade de ambiente
pd_formacao_ambiente = funcoes.joint(pd_formacao, pd_ambiente, ' - ')

# define um predicado específico para a questão 5:
# o Ambiente é Google Docs ou Word
def predicado_q5(k):
    return predicado_ambiente_google_docs(k) or predicado_ambiente_word(k)

# encontra a probabilidade:
# P(Ambiente=Google Docs ou Word | Formação=Ensino Fundamental Completo)
prob_q5 = funcoes.P(predicado_q5, funcoes.tal_que(predicado_formacao_efc, pd_formacao_ambiente))

print('Questão 5')
print('-' * 70)
print('''A probabilidade de uma pessoa utilizar Google Docs ou Word
dado que sua formação acadêmica é Ensino Fundamental Completo é: {:.3}'''.format(prob_q5))
print()
print()


# 6: Dado que uma pessoa indique que sua formação acadêmica é Ensino Superior Incompleto
# ou Ensino Superior Completo qual a probabilidade de ela não utilizar nem Google Docs e nem Word?

# define predicados específicos para a questão 6:
# a Formação é Ensino Superior Incompleto ou Ensino Superior Completo
def predicado_q6a(k):
    return predicado_formacao_esi(k) or predicado_formacao_esc(k)

# o Ambiente não é Google Docs e nem Word
def predicado_q6b(k):
    return not predicado_ambiente_google_docs(k) and not predicado_ambiente_word(k)

# encontra a probabilidade:
# P(Ambiente=~Google Docs e ~Word | Formação=Ensino Superior Completo ou Ensino Superior Incompleto)
prob_q6 = funcoes.P(predicado_q6b, funcoes.tal_que(predicado_q6a, pd_formacao_ambiente))

print('Questão 6')
print('-' * 70)
print('''A probabilidade de uma pessoa não utilizar Google Docs e nem Word
dado que sua formação acadêmica é Ensino Fundamental Completo ou
Ensino Fundamental Incompleto é: {:.3}'''.format(prob_q6))
print()
print()


# 7: Dado que uma pessoa indique que utilize o ambiente Word qual os dois problemas
# com maiores probabilidades -- e quais seriam elas?

# encontra as probabilidades individuais de cada problema:
# P(Problema=Criação de Sumários | Ambiente=Word)
prob_problema_cs = funcoes.P(predicado_problema_cs, funcoes.tal_que(predicado_ambiente_word, pd_ambiente_problema))

# P(Problema=Criação de lista de figuras | Ambiente=Word)
prob_problema_clf = funcoes.P(predicado_problema_clf, funcoes.tal_que(predicado_ambiente_word, pd_ambiente_problema))

# P(Problema=Numeração de páginas | Ambiente=Word)
prob_problema_np = funcoes.P(predicado_problema_np, funcoes.tal_que(predicado_ambiente_word, pd_ambiente_problema))

# P(Problema=Espaçamento do texto | Ambiente=Word)
prob_problema_et = funcoes.P(predicado_problema_et, funcoes.tal_que(predicado_ambiente_word, pd_ambiente_problema))

# P(Problema=Alinhamento do texto | Ambiente=Word)
prob_problema_at = funcoes.P(predicado_problema_at, funcoes.tal_que(predicado_ambiente_word, pd_ambiente_problema))

# P(Problema=Criar referências | Ambiente=Word)
prob_problema_cr = funcoes.P(predicado_problema_cr, funcoes.tal_que(predicado_ambiente_word, pd_ambiente_problema))

# P(Problema=Fazer citações | Ambiente=Word)
prob_problema_fc = funcoes.P(predicado_problema_fc, funcoes.tal_que(predicado_ambiente_word, pd_ambiente_problema))

# P(Problema=Criar tabelas | Ambiente=Word)
prob_problema_ct = funcoes.P(predicado_problema_ct, funcoes.tal_que(predicado_ambiente_word, pd_ambiente_problema))

# P(Problema=Não compreender a ferramenta | Ambiente=Word)
prob_problema_ncf = funcoes.P(predicado_problema_ncf, funcoes.tal_que(predicado_ambiente_word, pd_ambiente_problema))

# define um array com as probabilidades individuais de cada problema
prob_problemas_associados_word = [
    prob_problema_cs, 
    prob_problema_clf, 
    prob_problema_np, 
    prob_problema_et,
    prob_problema_at, 
    prob_problema_cr, 
    prob_problema_fc, 
    prob_problema_ct, 
    prob_problema_ncf
]

# ordena o array de forma decrescente, obtendo o índice
prob_ordenados = [i[0] for i in sorted(enumerate(prob_problemas_associados_word), reverse=True, key=lambda x:x[1])]

# obtém o primeiro e o segundo índice (relacionados ao primeiro maior e segundo maior problema, respectivamente)
p1_idx = prob_ordenados[0]
p2_idx = prob_ordenados[1]

# obtém o nome do problema e sua probabilidade associada ao primeiro maior e segundo maior problema, respectivamente
prob_1 = (problemas[p1_idx], prob_problemas_associados_word[p1_idx])
prob_2 = (problemas[p2_idx], prob_problemas_associados_word[p2_idx])

print('Questão 7')
print('-' * 70)
print('''Os problemas com maior probabilidade, dado que a pessoa utiliza
o ambiente Word são: 
* {}: {:.3}
* {}: {:.3}'''.format(prob_1[0], prob_1[1], prob_2[0], prob_2[1]))
print()
print()
