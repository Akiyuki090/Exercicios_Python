"""
Classe Macaco: Desenvolva uma classe Macaco,que possua os atributos nome e bucho (estomago)
e pelo menos os métodos comer(), verBucho() e digerir(). Faça um programa ou teste interativamente, criando pelo menos dois macacos, 
alimentando-os com pelo menos 3 alimentos diferentes e verificando o conteúdo do estomago a cada refeição. 
Experimente fazer com que um macaco coma o outro. É possível criar um macaco canibal?
"""
class Monkey:
    def __init__(self, nome):
        self.nome = nome
        self.bucho = []

    def verMacaco(self):
        print(f'{self.nome} diz olá!!')

    def comer(self):
        resp = str(input('Deseja alimentar seu macaco[s/n]: '))
        if resp == 's':

            comida = str(input('Qual alimento: '))
            self.bucho.append(comida)

            for i in self.bucho:
                print(f'Macaco comeu: {i}')

            if len(self.bucho) >= 3:
                print('Macaco cheio')
        else:
            print('Macaco agradece')

    def verbucho(self):
        for i in self.bucho:
            print(i)

    def digerir(self):
        for i in self.bucho:
            print(f'Macaco esta digerindo {i}')


if __name__ == '__main__':
    Macaco = Monkey('Jorge')
    Macaco.verMacaco()
    Macaco.comer()
    Macaco.verbucho()
    Macaco.comer()
    Macaco.verbucho()
    Macaco.digerir()
    