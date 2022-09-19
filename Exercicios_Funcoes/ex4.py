"""
Exercicio para criar uma lista com x elementos, que armazene seu nome de uma cidade e sua temperatura, e depois uma função para pegar uma 
cidade e converter sua temperatura em kelvin ou farenheit.
"""

cidade = list()
temp = []

while True:
    temp.append(str(input('Informe o nome da cidade: ')))
    temp.append(float(input('Informe a temperatura: ')))

    cidade.append(temp[:])
    temp.clear()

    st = str(input('Deseja continuar[s/n]: '))
    if st == 'n':
        break
print(cidade)

temps = str(input('Ver temperaturas em kelvin ou farenheit[k/f]: '))

if temps == 'k':
    def kelvin():
        temp1 = []
        for i in cidade:
            t = i[1]
            temp1.append(t)
            print(temp1)
            k = lambda t: 273 - t
            kv = list(map(k, temp1))
            print(f'Temperaturas em kelvin: {kv}')
    kelvin()

elif temps == 'f':
    def farenheit():
        temp1 = []
        for i in cidade:
            t = i[1]
            temp1.append(t)
            print(temp1)
            f = lambda t: ((1.8*t) + 32)
            fh = list(map(f, temp1))
            print(f'Temperaturas em farenheit: {fh}')
    farenheit()

else:
    print('Temperatura inválida')
