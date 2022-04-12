class Animal:
    # lista estática de animais criados
    animais = []

    def __init__(self, nome):
        self.nome = nome
        # criamos o animal e o colocaremos na lista estática
        Animal.animais.append(self)

    def fala(self):
        print(self.nome, 'faz barulho.')

    @staticmethod
    def falatorio():
        for a in Animal.animais:
            a.fala()

class Cachorro(Animal):
    # redefinindo o __init__
    def __init__(self, nome, raca):
        # pedaço novo de código
        self.raca = raca
        # chamando a __init__ da classe mãe para fazer o resto do trabalho
        super().__init__(nome)

    def fala(self):
        print(self.nome, 'faz au au.')

class Gato(Animal):
    def fala(self):
        print(self.nome, 'faz miau.')

class Dinossauro(Animal):
    pass
    # pass é um comando "vazio": ele não faz nada, apenas evita erro por não colocarmos nada dentro da classe

cachorrinho = Cachorro('Bidu', "Fox")
gatinho = Gato('Mingau')
dino = Dinossauro('Horácio')

cachorrinho.fala()
gatinho.fala()
dino.fala()

# o cachorrinho é cachorro?
print(isinstance(cachorrinho, Cachorro))
# o gatinho é gato?
print(isinstance(gatinho, Gato))
# o cachorrinho é gato?
print(isinstance(cachorrinho, Gato))
# o gatinho é cachorro?
print(isinstance(gatinho, Cachorro))
# o cachorrinho é animal?
print(isinstance(cachorrinho, Animal))
# o gatinho é animal?
print(isinstance(gatinho, Animal))

Animal.falatorio()
print(Animal.animais[0])