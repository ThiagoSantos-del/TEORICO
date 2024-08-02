class Animal:
    nome = str
    coracao = bool
    racional = bool
    consciecia = bool

    def __init__(self,nome,racional):
        self.nome = nome
        self.coracao = True
        self.racional = racional
        self.consciecia = False

class Humano(Animal):
    Racionalidade = bool
    consciencia = bool


class Cachorro(Animal):
    tamanho=0
    cor=''
    raca=''

    def __init__(self, nome, raca):
        self.nome = nome
        self.raca = raca
        self.coracao = True
        self.racional = True
        self.consciecia = True

    def latir(self):
        print('au-au')

cao = Cachorro('Lulu' ,'Pinscher')
cao_2 = Cachorro('Mel' ,'Vira-Lata')
pessoa = Humano('Pedro','Indio')
print(cao)
print(pessoa)

