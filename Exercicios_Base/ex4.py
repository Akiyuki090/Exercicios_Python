"""
Palíndromo
"""
# operador morsa(:=), operador ternario(a if a else b) 
print(frase := input('Qual a frase: '))
print(palindromo := frase[::-1])
print('É palindromo' if frase == palindromo else 'Não é palindromo')
