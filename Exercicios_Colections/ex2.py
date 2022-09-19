'''
Sua organização acaba de contratar um estagiário para trabalhar no Suporte de Informática, com a intenção de fazer um levantamento nas
sucatas encontradas nesta área. A primeira tarefa dele é testar todos os cerca de 200 mouses que se encontram lá, testando e 
anotando o estado de cada um deles, para verificar o que se pode aproveitar deles.
Foi requisitado que você desenvolva um programa para registrar este levantamento.
O programa deverá receber um número indeterminado de entradas, cada uma contendo: um número de identificação do mouse o tipo de defeito:
necessita da esfera;
necessita de limpeza; a.necessita troca do cabo ou conector; a.quebrado ou inutilizado Uma identificação igual a zero encerra o programa.
'''
import pandas as pd


mouse = []
lista_M = []

while True:
    mouse.append(str(input('Número de identificação: ')))
    mouse.append(str(input('Qual o defeito: ')))
    lista_M.append(mouse[:])
    mouse.clear()
    cmd = str(input('Cadastrar novo mouse? [s/n]: '))
    if cmd == 'n':
        break

df = pd.DataFrame(lista_M, columns= ['Identificação', 'Defeito'])
print(df)
print(f'Forma cadastrados ao total: {len(lista_M)} mouses, restam: {200 - len(lista_M)}')
