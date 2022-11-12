"""
Classe Bomba de Combustível: Faça um programa completo utilizando classes e métodos que:

Possua uma classe chamada bombaCombustível, com no mínimo esses atributos:
tipoCombustivel.
valorLitro
quantidadeCombustivel
Possua no mínimo esses métodos:
abastecerPorValor( ) – método onde é informado o valor a ser abastecido e mostra a quantidade de litros que foi colocada no veículo
abastecerPorLitro( ) – método onde é informado a quantidade em litros de combustível e mostra o valor a ser pago pelo cliente.
alterarValor( ) – altera o valor do litro do combustível.
alterarCombustivel( ) – altera o tipo do combustível.
alterarQuantidadeCombustivel( ) – altera a quantidade de combustível restante na bomba.
OBS: Sempre que acontecer um abastecimento é necessário atualizar a quantidade de combustível total na bomba.
"""
class Bomba:
    def __init__(self, tipoCombustivel, valorLitro, qtdCombustivel):
        self.tipoCombustivel = tipoCombustivel
        self.valorLitro = valorLitro
        self.qtdCombustivel = qtdCombustivel
    
    def abastecerPorValor(self):
        abst = float(input('Quantos reais deseja por: '))
        litros = abst / self.valorLitro
        print(f'Deu um total de {litros} litros')
        self.qtdCombustivel -= litros

    def abastecerPorLitro(self):
        abst = float(input('Quantos litros deseja por: '))
        litros = abst * self.valorLitro
        print(f'Deu um total de {litros} litros')
        self.qtdCombustivel -= litros

    def alterarValor(self):
        x = float(input('Alterou o preço? Informe ae para nós: '))
        self.valorLitro = x

    def alterarCombustivel(self):
        x = str(input('Qual o novo tipo de combustivel: '))
        self.tipoCombustivel = x
    
    def alterarQuantidadeCombustivel(self):
        x = str(input('Qual a nova quantidade de combustivel: '))
        self.qtdCombustivel = x

