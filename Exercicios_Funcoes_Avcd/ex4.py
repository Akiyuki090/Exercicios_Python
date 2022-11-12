'''
Maiores que 0
'''
maior = lambda x: x > 0

lista = [0, -2, -6, -8, 10, 20, -100, 0, 990, 3, -9, 12]

print(list(filter( maior, lista)))
