'''
Matrizes
'''
n = int(input("tamanho matriz :"))

linha = [0] * n

matriz = [linha] * n

print(matriz)

for l in range(n):
    linha = []
    for c in range(n):
        numero = int(
            input(" Numero que ficara armazenado {},{} :".format(l, c)))
        linha.append(numero)
    matriz[l] = linha

print(matriz)
