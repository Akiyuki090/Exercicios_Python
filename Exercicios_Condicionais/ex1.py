'''
O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:
                      Até 5 Kg           Acima de 5 Kg

File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg

Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção,
porém não há limites para a quantidade de carne por cliente. 
Se compra for feita no cartão Tabajara o cliente receberá ainda um desconto de 5% sobre o total da compra. 
Escreva um programa que peça o tipo e a quantidade de carne comprada pelo usuário e gere um cupom fiscal, contendo as 
informações da compra: tipo e quantidade de carne, preço total, tipo de pagamento, valor do desconto e valor a pagar.
'''

print('*' * 30)
print('PROMOÇÕES'.center(30))
print('*' * 30)

d = [ ["Filé duplo", 4.9, 5.8],
     ["Alcatra", 5.9, 6.8],
     ["Picanha", 6.9, 7.8]]
     
print ("{:<15} {:<20} {:<15}".format('Carne','Até 5kg','Mais de 5kg'))

for v in d:
    carne, ate5, mais5 = v
    print ("{:<15} {:<20} {:<15}".format( carne, ate5, mais5))

print('Digite a opção de escolha do cliente:')
while True:
    value = int(input('Digite [1] para FIlé, [2] para Alcatra e [3] para Picanha: '))
    if(value != 1 and value != 2 and value != 3):
        break
    else:

        if(value == 1):
            qtd = float(input('Informe quantos kg deseja: '))
            if(qtd < 5):
                valor = qtd * 4.9
                print(f'O valor a ser pago é: R${valor}')
                pag = str(input('Qual o meio de pagamento: '))
                if(pag == 'cartao'):
                    print('Desconto adicionado')
                    desc = valor - (valor * 0.05)
                    print(f'Pagamento final: R${desc}')

                    print('-' * 30)
                    print('NOTA FISCAL'.center(30))
                    print('-' * 30)
                    print(f'O cliente comprou: {qtd}KG de Filé duplo, totalizando: R${valor}, o meio de pagamento foi: {pag} portanto o valor a ser pago é: R${round(desc,2)}')
                else:
                    print('Sem desconto')
                    desc = valor
                    print('-' * 30)
                    print('NOTA FISCAL'.center(30))
                    print('-' * 30)
                    print(f'O cliente comprou: {qtd}KG de Filé duplo, totalizando: R${valor}, o meio de pagamento foi: {pag}')
            else:
                valor = qtd * 5.8
                print(f'O valor a ser pago é: R${valor}')
                pag = str(input('Qual o meio de pagamento: '))
                if(pag == 'cartao'):
                    print('Desconto adicionado')
                    desc = valor - (valor * 0.05)
                    print(f'Pagamento final: R${desc}')

                    print('-' * 30)
                    print('NOTA FISCAL'.center(30))
                    print('-' * 30)
                    print(f'O cliente comprou: {qtd}KG de Filé duplo, totalizando: R${valor}, o meio de pagamento foi: {pag} portanto o valor a ser pago é: R${round(desc,2)}')

                else:
                    print('Sem desconto')
                    desc = valor
                    print('-' * 30)
                    print('NOTA FISCAL'.center(30))
                    print('-' * 30)
                    print(f'O cliente comprou: {qtd}KG de Filé duplo, totalizando: R${valor}, o meio de pagamento foi: {pag} ')
        
        elif(value == 2):
            qtd = float(input('Informe quantos kg deseja: '))
            if(qtd < 5):
                valor = qtd * 5.9
                print(f'O valor a ser pago é: R${valor}')
                pag = str(input('Qual o meio de pagamento: '))
                if(pag == 'cartao'):
                    print('Desconto adicionado')
                    desc = valor - (valor * 0.05)
                    print(f'Pagamento final: R${desc}')

                    print('-' * 30)
                    print('NOTA FISCAL'.center(30))
                    print('-' * 30)
                    print(f'O cliente comprou: {qtd}KG de Alcatra, totalizando: R${valor}, o meio de pagamento foi: {pag} portanto o valor a ser pago é: R${round(desc,2)}')
                else:
                    print('Sem desconto')
                    desc = valor
                    print('-' * 30)
                    print('NOTA FISCAL'.center(30))
                    print('-' * 30)
                    print(f'O cliente comprou: {qtd}KG de Alcatra, totalizando: R${valor}, o meio de pagamento foi: {pag}')
            else:
                valor = qtd * 6.9
                print(f'O valor a ser pago é: R${valor}')
                pag = str(input('Qual o meio de pagamento: '))
                if(pag == 'cartao'):
                    print('Desconto adicionado')
                    desc = valor - (valor * 0.05)
                    print(f'Pagamento final: R${desc}')

                    print('-' * 30)
                    print('NOTA FISCAL'.center(30))
                    print('-' * 30)
                    print(f'O cliente comprou: {qtd}KG de Alcatra, totalizando: R${valor}, o meio de pagamento foi: {pag} portanto o valor a ser pago é: R${round(desc,2)}')

                else:
                    print('Sem desconto')
                    desc = valor
                    print('-' * 30)
                    print('NOTA FISCAL'.center(30))
                    print('-' * 30)
                    print(f'O cliente comprou: {qtd}KG de Alcatra, totalizando: R${valor}, o meio de pagamento foi: {pag} ')

        else:
            qtd = float(input('Informe quantos kg deseja: '))
            if(qtd < 5):
                valor = qtd * 6.9
                print(f'O valor a ser pago é: R${valor}')
                pag = str(input('Qual o meio de pagamento: '))
                if(pag == 'cartao'):
                    print('Desconto adicionado')
                    desc = valor - (valor * 0.05)
                    print(f'Pagamento final: R${desc}')

                    print('-' * 30)
                    print('NOTA FISCAL'.center(30))
                    print('-' * 30)
                    print(f'O cliente comprou: {qtd}KG de Picanha, totalizando: R${valor}, o meio de pagamento foi: {pag} portanto o valor a ser pago é: R${round(desc,2)}')
                else:
                    print('Sem desconto')
                    desc = valor
                    print('-' * 30)
                    print('NOTA FISCAL'.center(30))
                    print('-' * 30)
                    print(f'O cliente comprou: {qtd}KG de Picanha, totalizando: R${valor}, o meio de pagamento foi: {pag}')
            else:
                valor = qtd * 7.8
                print(f'O valor a ser pago é: R${valor}')
                pag = str(input('Qual o meio de pagamento: '))
                if(pag == 'cartao'):
                    print('Desconto adicionado')
                    desc = valor - (valor * 0.05)
                    print(f'Pagamento final: R${desc}')

                    print('-' * 30)
                    print('NOTA FISCAL'.center(30))
                    print('-' * 30)
                    print(f'O cliente comprou: {qtd}KG de Picanha, totalizando: R${valor}, o meio de pagamento foi: {pag} portanto o valor a ser pago é: R${round(desc,2)}')

                else:
                    print('Sem desconto')
                    desc = valor
                    print('-' * 30)
                    print('NOTA FISCAL'.center(30))
                    print('-' * 30)
                    print(f'O cliente comprou: {qtd}KG de Picanha, totalizando: R${valor}, o meio de pagamento foi: {pag} ')
    
    op = str(input('Deseja continuar[s/n]: '))
    if(op == 'n'):
        break
print('Volte sempre')
