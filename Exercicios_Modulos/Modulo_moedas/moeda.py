def aumenta(n):
    valor = float(input('Digite um preço: '))
    print(f'Aumentando o valor em {n}%, temos: {valor + (valor * (n/100))}')

def diminui(n):
    valor = float(input('Digite um preço: '))
    print(f'Diminuindo o valor em {n}%, temos: {valor - (valor * (n/100))}')

def dobro():
    valor = float(input('Digite um preço: '))
    print(f'Dobrando o valor: {valor * 2}')

def metade():
    valor = float(input('Digite um preço: '))
    print(f'Dobrando o valor: {valor / 2}')
