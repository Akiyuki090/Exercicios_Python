'''
Criando uma lista de afazeres
'''

with open('lista.txt', '+w') as file:
    while True:
        afazer = input('Qual a tarefa: ')
        if afazer != 'sair':
            file.write(afazer)
            file.write('\n')
        else:
            break
