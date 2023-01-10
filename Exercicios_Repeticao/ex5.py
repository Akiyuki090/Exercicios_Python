"""
Verifique se em determinada frase existem números, se sim guarde-os em uma lista separada.
"""
frase = input("Frase: ")
lista = frase.split(" ")
numeros = []
frases = []

print(lista)

for i in lista:
    if str.isnumeric(i) == True:
        numeros.append(i)
    else:
        frases.append(i)

print(numeros)
print(frases)
