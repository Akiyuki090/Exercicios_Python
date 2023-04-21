'''
Vereficar se é igual ao anterior
'''
lista = []

while True:
    lista.append(int(input('Digite um valor: ')))
    resp = str(input('Quer continuar[s/n]: '))
    if resp == 'n':
        break

print(lista)

for i in range(len(lista)):
    for j in range(i+1, len(lista)):
        if lista[j] == lista[i]:
            print(f"O item {lista[j]} é igual ao item {lista[i]} na posição {i}.")
