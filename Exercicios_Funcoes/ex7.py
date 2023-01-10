"""
Lista com N nomes e idades, caso as idades sejam maiores que 18, mostre de maior
"""
temp = list()
pessoas = list()

while True:
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    temp.append(nome)
    temp.append(idade)
    pessoas.append(temp[:])
    temp.clear()
    resp = str(input('Novo cadastro[s/n]: '))
    if resp == 'n':
        break

for c, i in pessoas:
    print(f"{c} = {i}")

def maioridade():
    for i in pessoas:
        idades = i[1]
        if idades >= 18:
            x = "Maior de idade"
            i[1] = x
        else:
            y = "Menor de idade"
            i[1] = y
    
    print(pessoas)  

maioridade()
