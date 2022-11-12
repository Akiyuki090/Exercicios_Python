'''
Desenvolva um programa que converta todas as temperaturas desta lista em Celsius ([22.5, 40, 13, 29, 34]) para Fahrenheit
'''
tempCelsius = [22.5, 40, 13, 29, 34]

FRHT = lambda x: 1.8 * x + 32

print(list(map(FRHT, tempCelsius)))
