"""
Fatorial
"""
import math

num = int(input('Informe um numero: '))
print(math.factorial(num))

def fatorial():
    num = int(input('Informe um valor: '))

    fatorial = 1
    while(num > 1):
        fatorial = fatorial * num
        num = num - 1
    print(fatorial)


fatorial()
