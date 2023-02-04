'''
Lista com n pessoas que armazene o nome, sexo e idade.
Mostre as mulheres cadastradas e a media de idades de todos na lista
'''
pessoas = {}
grupo = []
somaidade = 0

while True:
    pessoas['Nome'] = str(input('Informe o nome: '))
    pessoas['Sexo'] = str(input('Informe o sexo[m/f]: '))
    pessoas['Idade'] = int(input('Informe a idade: '))
    somaidade =+ pessoas['Idade']
    grupo.append(pessoas.copy())
    pessoas.clear()
    stri = str(input('Novo cadastro[s/n]: '))
    if stri == 'n':
        break

for i in grupo:
    if i['Sexo'] == 'f':
        nome = i['Nome']
        print(f'As mulheres: {nome}')

print(grupo)  
print(f'Foram cadastradas {len(grupo)} pessoas')
print(f'A média de idade no grupo é de: {somaidade/len(grupo)}')
