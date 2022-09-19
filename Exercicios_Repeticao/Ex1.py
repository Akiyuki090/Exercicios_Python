"""
Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido por eles.
"""
def teste1():
    num1 = int(input("Informe um valor: "))
    num2 = int(input("Informe um outro valor: "))

    x = num1

    while x < num2:
        print(x)
        x += 1


def teste2():
    num1 = int(input("Informe um valor: "))
    num2 = int(input("Informe um outro valor: "))

    for c in range(num1 + 1 , num2):
        print(c)


teste1()
