'''
Fatorial
'''
def fat():
    entrada = int(input('Insira um valor: '))
    aux = 1
    resultado = entrada
    while aux < entrada:
        resultado = resultado * aux
        aux += 1
    print(resultado)

fat()