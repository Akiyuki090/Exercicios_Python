'''
Especificação   Código  Preço
Cachorro Quente 100     R$ 1,20
Bauru Simples   101     R$ 1,30
Bauru com ovo   102     R$ 1,50
Hambúrguer      103     R$ 1,20
Cheeseburguer   104     R$ 1,30
Refrigerante    105     R$ 1,00

Faça um programa que leia o código dos itens pedidos e as quantidades desejadas. 
Calcule e mostre o valor a ser pago por item (preço * quantidade) e o total geral do pedido. 
Considere que o cliente deve informar quando o pedido deve ser encerrado.
'''

print("Produto         Codigo  Custo"
      "\n-------------------------------"
      "\nCachorro Quente 100     R$ 1.20"
      "\nBauru Simples   101     R$ 1.30"
      "\nBauru com ovo   102     R$ 1.50"
      "\nHamburguer      103     R$ 1.20"
      "\nCheeseburguer   104     R$ 1.30"
      "\nRefrigerante    105     R$ 1.00\n")

guardavalor = []
while True:
    codigo = int(input('Qual o código: '))
    qtd = int(input('Quantidade: '))
    stri = str(input('Deseja continuar[s/n]: '))

    if codigo == 100:
        valor = (qtd * 1.2)
        guardavalor.append(valor)
        print(f'O valor: R$ {sum(guardavalor)}')

    elif codigo == 101:
        valor = (qtd * 1.30)
        guardavalor.append(valor)
        print(f'O valor: R$ {sum(guardavalor)}')

    elif codigo == 102:
        valor = (qtd * 1.50)
        guardavalor.append(valor)
        print(f'O valor: R$ {sum(guardavalor)}')

    elif codigo == 103:
        valor = (qtd * 1.20)
        guardavalor.append(valor)
        print(f'O valor: R$ {sum(guardavalor)}')

    elif codigo == 104:
        valor = (qtd * 1.30)
        guardavalor.append(valor)
        print(f'O valor: R$ {sum(guardavalor)}')

    elif codigo == 105:
        valor = (qtd * 1)
        guardavalor.append(valor)
        print(f'O valor: R$ {sum(guardavalor)}')

    else:
        print('Produto não informado')

    if stri == 'n':
        break
