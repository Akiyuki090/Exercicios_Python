'''
Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, 
que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
comprar apenas latas de 18 litros;
comprar apenas galões de 3,6 litros;
misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os valores para cima, 
isto é, considere latas cheias.
'''
def tintas():
    import math


    metragem = float(input('Informe o tamanho do local a ser pintado(m2): '))
    
    if(metragem <= 21.6):
        print(f'Recomendamos a utilização de galões de 3,6 litro.')
        xl = metragem / 6
        total_l = xl/3.6
        print(f'Para pintar uma área de: {metragem} m2, será necessário: {round(xl, 2)} litros de tintas')
        print(f'Então será utilizados: {math.ceil(total_l)} galão(ões), totalizando: R${round((math.ceil(total_l) * 25), 2)}')
    elif(21.6 < metragem <= 108):
        print(f'Recomendamos a utilização de latas de 18 litro.')
        xl = metragem / 6
        total_l = xl/18
        print(f'Para pintar uma área de: {metragem} m2, será necessário: {round(xl, 2)} litros de tintas')
        print(f'Então será utilizado(s): {math.ceil(total_l)} lata(s), totalizando: R${round((math.ceil(total_l) * 80), 2)}')
    else:
        print(f'Recomendamos a utilização de ambas litragens de tintas.')
        xl = metragem / 6
        Litros_folga = xl + ((10/100)*(xl))
        qtd_Litro = math.ceil(Litros_folga / 18)

        Litros_folga_faltando = Litros_folga - (qtd_Litro * 18)
        qtd_Galao = math.ceil(Litros_folga_faltando / 3.6)

        custo = (qtd_Litro * 80) + (qtd_Galao * 25)

        print(f'Para pintar: {metragem} m2 recomendamos utilizar: {qtd_Litro} latas e {qtd_Galao} de galões, totalizando: R${custo}')


tintas()
