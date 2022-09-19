def soma():
    a = int(input('Digite um valor: '))
    b = int(input('Digite outro valor: '))
    r = a + b
    print(f'O resultado da soma é: {r}')


def sub():
    a = int(input('Digite um valor: '))
    b = int(input('Digite outro valor: '))
    r = a - b
    print(f'O resultado da diferença é: {r}')

def mult():
    a = int(input('Digite um valor: '))
    b = int(input('Digite outro valor: '))
    r = a * b
    print(f'O resultado da multiplicação é: {r}')

def div():
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    assert b != 0
    r = a / b
    print(f'O resultado da divisão é: {r}')

def raiz():
    from math import sqrt


    a = int(input('Digite a raiz que deseja calcular: '))
    r = sqrt(a)
    print(f'O resultado da raiz é: {round(r, 3)}')

