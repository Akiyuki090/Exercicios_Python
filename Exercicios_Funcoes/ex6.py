"""
Reverso do número. Faça uma função que retorne o reverso de um número inteiro informado. Por exemplo: 127 -> 721.
"""

def Reverse():
    num = int(input('Número: '))
    numero = str(num)
    print(numero[::-1])

Reverse()
