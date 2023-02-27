import numpy as np


# Entrada de dados da matriz A
matrizA_Linha = int(input('Informe a quantidade de linhas da matriz A: '))
matrizA_Coluna = int(input('Informe a quantidade de colunas da matriz A: '))

MatrizA = []
for i in range(matrizA_Linha):
    linha = []
    for j in range(matrizA_Coluna):
        valor = int(input(f"Digite o valor para a posição ({i},{j}): "))
        linha.append(valor)
    MatrizA.append(linha)

for r in MatrizA:
    print(r)

# Entrada de dados da matriz B
matrizB_Linha = int(input('Informe a quantidade de linhas da matriz B: '))
matrizB_Coluna = int(input('Informe a quantidade de colunas da matriz B: '))

MatrizB = []
for i in range(matrizB_Linha):
    linha = []
    for j in range(matrizB_Coluna):
        valor = int(input(f"Digite o valor para a posição ({i},{j}): "))
        linha.append(valor)
    MatrizB.append(linha)

for r in MatrizB:
    print(r)

# Verificação das dimensões das matrizes
if matrizA_Coluna != matrizB_Linha:
    print('As matrizes não podem ser divididas. Verifique suas dimensões.')
else:
    # Código para divisão de matrizes
    determinante = np.linalg.det(MatrizB)
    print(determinante)

    if determinante == 0:
        print('Não é possível calcular a inversa da matriz B, pois seu determinante é zero')
    else:
        inversa_B = np.linalg.inv(MatrizB)
        matriz_resultado = np.dot(MatrizA, inversa_B)

        for r in matriz_resultado:
            print(r)
