"""
Jogo da forca
"""
from random import choice


vocabulario = ["esquistossomose", "naftalina", "ribonucleico","idiossincratico", "fagocitose", "quinquagesimo"]
palavra = choice(vocabulario)

chances = 5
alfabeto = list("abdcefghijklmnopqrstuvwxyz")
tentativas = []

while True:
    print(tentativas)
    print("Chances: ", chances)

    for letra in palavra:
        if letra in tentativas:
            print(letra, end=' ')
        else:
            print('_', end=' ')

    palpite = input( "\nDigite seu palpite ou 'SAIR' para sair do programa! ").lower()

    if palpite == 'sair':
        break

    elif palpite not in alfabeto or palpite == '':
        chances -= 1
        print('Ta feio a coisa, sabe nem escrever fiote.... Só pela burrada perde 1 vida ae!!!\n')
        continue

    elif palpite in tentativas:
        print('É, tu não é burro mas tem alzheimer, sorte sua não perder uma vida...\n')
        continue

    tentativas.append(palpite)
    
    if palpite in palavra:
        print('Fez uma pra Deus ver, aleluia !!! \n')

    else:
        print('Ta errando demais, ter nascido ja não basta! \n')
        chances -= 1

    if chances == 0:
        print('Você é a vergonha da profission!!! \n')
        print(f'A palavra era: {palavra}')
        break

    elif set(palavra).issubset(set(tentativas)):
        print('Até que enfim venceu na vida!! \n')
        break
