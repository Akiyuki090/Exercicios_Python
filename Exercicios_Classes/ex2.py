'''
Classe Conta Corrente: Crie uma classe para implementar uma conta corrente. 
A classe deve possuir os seguintes atributos: número da conta, nome do correntista e saldo. 
Os métodos são os seguintes: alterarNome, depósito e saque; No construtor, saldo é opcional, com valor default zero e 
os demais atributos são obrigatórios.
'''

class Conta_Corrente:
    def __init__(self, numero, nome, saldo = 0):
        self.numero = numero
        self.nome = nome
        self.saldo = saldo
    
    def alterarNome(self):
        novo = str(input('Novo nome: '))
        self.nome = novo

    def depósito(self):
        deposito = float(input('Quanto deseja colocar: R$ '))
        self.saldo += deposito

    def saque(self):
        saque = float(input('Quanto deseja sacar: R$ '))
        if saque > self.saldo:
            print(f'Saldo indisponível. {self.saldo}')
        else:
            self.saldo -= saque

    def Ver(self):
        print(self.nome)
        print(self.numero)
        print(self.saldo)
