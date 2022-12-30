"""
Classe Funcionário: Implemente a classe Funcionário. Um empregado tem um nome (um string) e um salário(um double). 
Escreva um construtor com dois parâmetros (nome e salário) e métodos para devolver nome e salário.
Escreva um pequeno programa que teste sua classe.
Aprimore a classe do exercício anterior para adicionar o método aumentarSalario
(porcentualDeAumento) que aumente o salário do funcionário em uma certa porcentagem.
"""

class Funcionario:
    def __init__(self, nome, idade, salario):
        self.nome = nome
        self._idade = idade
        self.salario = salario

    def get_age(self):
        return self._idade

    def set_age(self, novaIdade):
        self._idade = novaIdade

    def verFuncionario(self):
        print(f'Funcionário: {self.nome}, idade: {self._idade} anos, salário: R${self.salario}')

    def aumentaSalario(self, percentual):
        novoSalario = self.salario * (percentual/100)
        self.salario += novoSalario
        print(f'Novo salário de: {self.nome} vai ser: R${self.salario}')

if __name__ == '__main__':
    id1 = Funcionario('Marcio', 21, 2345)
    id1.set_age(22)
    id1.verFuncionario()
    id1.aumentaSalario(50)
    id1.verFuncionario()
