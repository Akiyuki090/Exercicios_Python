"""
Classe Conta de Investimento: Faça uma classe contaInvestimento que seja semelhante a classe contaBancaria, 
com a diferença de que se adicione um atributo taxaJuros. Forneça um construtor que configure tanto o saldo inicial como a taxa de juros. 
Forneça um método adicioneJuros (sem parâmetro explícito) que adicione juros à conta. Escreva um programa que construa uma poupança 
com um saldo inicial de R$1000,00 e uma taxa de juros de 10%. Depois aplique o método adicioneJuros() cinco vezes e imprime o 
saldo resultante.
"""

class ContaInvestimento:
    def __init__(self, nome, saldoinicial=1000):
        self.nome = nome
        self.saldoinicial = saldoinicial
    
    def adicioneJuros(self, juros):
        saldoJuros = self.saldoinicial * (juros/100)
        self.saldoinicial += saldoJuros

    def verConta(self):
        print(f'Nome: {self.nome}, saldo: R${round(self.saldoinicial, 2)}')
    
if __name__ == '__main__':
    acc = ContaInvestimento('Marcus')
    acc.verConta()
    acc.adicioneJuros(5)
    acc.adicioneJuros(5)
    acc.adicioneJuros(5)
    acc.adicioneJuros(5)
    acc.adicioneJuros(5)
    acc.verConta()
