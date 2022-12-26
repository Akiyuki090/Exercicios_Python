"""
Desenvolva um programa que apresente a soma dos valores pares e dos valores ímpares
"""

lista = []
qtd = int(input('Quantos valores terá sua lista: '))

for i in range(0, qtd):
    valor = int(input('Qual o valor: '))
    lista.append(valor)

print(lista)

x = lambda a: a if a % 2 == 0 else 0
y = lambda a : a if a % 2 != 0 else 0

pares = filter(x, lista)
impares = filter(y, lista)

print(list(pares))
print(list(impares))
