"""
Tabuada
"""

def tabuada1():
    num = int(input('Informe um valor: '))

    for c in range(1, 11):
        print(f'{c} * {num} = {c * num}')


def tabuada2():
    num = int(input('Informe um valor: '))

    x = 0

    while x < 11:
        print(f'{x} * {num} = {x * num}')
        x += 1

tabuada2()
