'''
Faça um programa que carregue uma lista com os modelos de cinco carros (exemplo de modelos: FUSCA, GOL, VECTRA etc).
Carregue uma outra lista com o consumo desses carros, isto é, quantos quilômetros cada um desses carros faz com um litro de combustível.
Calcule e mostre:
O modelo do carro mais econômico;
Quantos litros de combustível cada um dos carros cadastrados consome para percorrer uma distância de 1000 quilômetros e quanto isto custará, 
considerando um que a gasolina custe R$ 2,25 o litro.
'''
import pandas as pd


carros = []
modelo = []
economico = 0

for c in range (1, 2):
    modelo.append(str(input('Digite o modelo de carro: ')))
    modelo.append(float(input('Informe o rendimento do automovel: ')))
    if len(carros) == 0:
        economico = modelo[1]
    else:
        if modelo[1] > economico:
            economico = modelo[1]
    carros.append(modelo[:])
    modelo.clear()


df = pd.DataFrame(carros, columns = ['Modelo', 'Quilometragem', 'Consumo'])
print(df)

for i in carros:
    if i[1] == economico:
        print(f'O modelo: {i[0]}, é o mais economico')
    


