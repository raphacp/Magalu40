class Cachorro:
    def __init__(self, nome, raca):
        self.nome = nome
        self.raca = raca

    def recebe_peso(self, valor):
        self.peso = valor

    def calcula_porte(self):
        if self.peso <= 5:
            self.porte = "P"
        elif self.peso <= 15:
            self_porte = "M"
        else:
            self_porte = "G"


cachorro1 = Cachorro("Minnie", "SRD")
cachorro1.recebe_peso(4)
cachorro1.calcula_porte()
cachorro1.__dict__
