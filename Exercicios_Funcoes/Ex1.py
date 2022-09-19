'''
Faça um programa com uma função chamada somaImposto. A função possui dois parâmetros formais: taxaImposto, que é a quantia de imposto sobre
vendas expressa em porcentagem e custo, que é o custo de um item antes do imposto. A função “altera” o valor de custo para incluir o imposto
sobre vendas.
'''
def somaImposto(taxaImposto, custo):
    altera = custo + ((custo* 10)/100)
    print(f'O valor final do produtto é: R${altera}')

somaImposto(15, 789)
