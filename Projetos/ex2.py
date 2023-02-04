'''
Encontrar senha
'''

from random import *
import os


password = input('Sua senha: ')

repo = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','ç','@', 1,2,3,4,5,6,7,8,9,0]
print(len(repo))
pasw = ""

while pasw != password:
    pasw = ""
    for i in range(len(password)):
        teste = repo[randint(0, 37)]
        pasw = str(teste)+str(pasw)
        print(pasw)
        print('Verificando senha ... Aguarde')
        os.system('cls')
print(f'Senha: {pasw}')

