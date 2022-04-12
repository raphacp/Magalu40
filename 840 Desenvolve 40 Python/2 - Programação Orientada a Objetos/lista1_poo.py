# 1
# Crie uma classe Quadrado com o atributo lado. Os métodos calcular_area e calcular_perimetro devem criar os 
# atributos lado e perímetro, respectivamente.

""" class Quadrado:
    def __init__(self, lado):
        self.lado = lado

    def calcular_area(self):
        self.area = self.lado * self.lado
        return self.area

    def calcular_perimetro(self):
        self.perimetro = self.lado * 4
        return self.perimetro

quadrado1 = Quadrado(12)

print(f"A área do quadrado é: {quadrado1.calcular_area()}.")
print(f"O perímetro do quadrado é: {quadrado1.calcular_perimetro()}.")
 """
# 2
# Crie uma classe Moto com os atributos marca, modelo, cor e marcha_atual, maior_marcha e ligada. O atributo 
# marcha indica em que marcha a moto encontra-se no momento, sendo represtando de forma inteira: 0 - neutro, 
# 1 - primeira, 2 - segunda, etc. O atributo ligada é um booleano que indica se ela está ligada ou não.
# Crie um método ligar_moto que muda o atributo ligada caso ela esteja desligada. Verifique se a marcha está no 
# neutro para ligá-la.
# Crie os métodos marcha_abaixo e marcha_acima para alterar o valor da marcha da moto. Verifique se a moto está 
# ligada para executar os métodos.

""" class Moto:
    def __init__(self, marca, modelo, cor, maior_marcha):
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.maior_marcha = maior_marcha
        self.marcha_atual = 0
        self.ligada = False
    
    def ligar_moto(self):
        if self.ligada == False:
            if self.marcha_atual == 0:
                self.ligada = True
                print("A moto foi ligada.")
            else:
                print("A moto não está no neutro para ser ligada.")
        else:
            print("A moto já está ligada.")

    def marcha_abaixo(self):
        if self.ligada == True:
            if self.marcha_atual == 0:
                print(f"A moto já está na menor marcha ({self.marcha_atual}).")
            else:
                self.marcha_atual -= 1
                print(f"Marcha reduzida para {self.marcha_atual}.")
        else:
            print("A moto está deligada.")

    def marcha_acima(self):
        if self.ligada == True:
            if self.marcha_atual == self.maior_marcha:
                print(f"A moto já está na maior marcha ({self.maior_marcha}).")
            else:
                self.marcha_atual += 1
                print(f"Marcha aumentada para {self.marcha_atual}.")
        else:
            print("A moto está desligada.")

    def desligar_moto(self):
        if self.ligada == True:
            self.ligada = False
            self.marcha_atual = 0
            print("A moto foi desligada.")
        else:
            print("A moto já está desligada.")
    
    def __repr__(self):
        texto = f'''
        Marca: {self.marca}
        Modelo: {self.modelo}
        Cor: {self.cor}
        Maior marcha: {self.maior_marcha}
        Marcha atual: {self.marcha_atual}
        Ligada: {self.ligada}
        '''
        return texto

moto1 = Moto("honda","biz", "azul", 5)
moto1.ligar_moto()
print(moto1)
moto1.marcha_acima()
moto1.marcha_abaixo()
moto1.desligar_moto() """


# 3
# Crie uma classe Televisao com atributos ligado, numero_canais, canal_atual, volume, min_volume e max_volume. 
# Os atributos min_volume e max_volume devem receber 0 e 100 respectivamente. Crie um metodo ligar_desligar que 
# muda o estado atual da TV para o oposto.
# Crie os métodos abaixar_volume e aumentar_volume.
# Crie os métodos canal_abaixo e canal_acima. Caso esteja no último canal e aumente 1, o canal deve retornar para 
# o menor canal. Caso esteja no primeiro canal e diminua 1, o canal deve retornar para o maior canal.



# 4
# Crie uma classe Microondas, com os atributos ligado e porta_aberta. Os dois atributos devem ser booleanos.
# Crie um método ligar_desligar que deve alterar o atributo ligado para o oposto.
# Crie um método abri_fechar que deve alterar o atributo porta_aberta para o oposto.
# Crie um método esquentar que recebe quanto tempo o microondas deve funcionar. O método só deve ser executado 
# se o microondas estiver ligado e com a tampa fechada.