'''
função lambda slice
'''

nome = str(input('Qual seu nome: '))

first = lambda x: x.split()[0]
last =  lambda x: x.split()[-1]

print(f'Primeiro nome: {first(nome)}, ultimo nome: {last(nome)}')
