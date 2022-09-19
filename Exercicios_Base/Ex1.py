'''
Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda,
8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
salário bruto.
quanto pagou ao INSS.
quanto pagou ao sindicato.
o salário líquido.
calcule os descontos e o salário líquido
'''

def calcula_salario():
    salario_Hora = float(input('Quanto você recebe por hora: '))
    horas = float(input('Quantas horas por dia você trabalha: '))

    # Calculando salario mensal descontando sabados e domingos, e considerando o mês com 30 dias:
    salario_Bruto = ((20 * horas) * salario_Hora)
    print(f'Seu salário mensal bruto é de: R${salario_Bruto}')

    # Imposto de renda:
    Imposto = salario_Bruto * (11/100)
    print(f'Foi descontado: R${Imposto} para o imposto de renda')

    # INSS:
    inss = salario_Bruto * (8/100)
    print(f'Foi descontado: R${inss} para o INSS')

    # Sindicato:
    sindicato = salario_Bruto * (5/100)
    print(f'Foi descontado: R${sindicato} para o sindicato')

    # Salario líquido:
    salario_Liquido = salario_Bruto - Imposto - inss - sindicato
    print(f'Salário final: R${salario_Liquido}')

    # Descontos:
    descontos = Imposto + inss + sindicato
    print(f'Descontos totais: R${round(descontos,2)}')


calcula_salario()
