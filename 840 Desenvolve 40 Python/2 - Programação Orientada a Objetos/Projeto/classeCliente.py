import classeLoja
import datetime as dt

class Cliente:
    def __init__(self, nome):
        self.nome = nome
        self.aluguel_ativo = False
#         texto_log = f'''
# ****************************************************************************************************************
# *  LOG
# *  Classe: {__class__.__name__} - {__class__.mro()}
# *  Método: {__class__.__init__.__name__}
# *  Parâmetros recebidos: {self, self.nome}
# *  Data: {dt.datetime.now().strftime('%d/%m/%Y %H:%M:%S')}
# ****************************************************************************************************************
# '''
#         print(texto_log)

    def ver_estoque(self, loja):
        if isinstance(loja, classeLoja.Loja):

            texto_log = f'''
****************************************************************************************************************
*  LOG
*  Classe: {__class__.__name__} - {__class__.mro()}
*  Método: {__class__.ver_estoque.__name__}
*  Parâmetros recebidos: {self.nome, loja.nome}
*  Data: {dt.datetime.now().strftime('%d/%m/%Y %H:%M:%S')}
****************************************************************************************************************
'''
            print(f"O estoque da loja {loja.nome} é de {loja.estoque} bicicleta(s).")
            print(texto_log)
        else:
            raise AttributeError("A loja informada não é um objeto da classe correspondente.")

    
    def alugar_bicicleta(self, loja, qtd, tipo, data_hora):
        # Coloquei uma limitação de 1 aluguel por cliente para simplificar, devido ao tempo curto para desenvolver o projeto
        # Caso dê tempo vou retirar esta trava e fazer melhor.
        assert isinstance(loja, classeLoja.Loja), 'A loja informada não é um objeto da classe correspondente.'
        assert isinstance(qtd, int), 'A quantidade deve ser um número inteiro.'
        assert isinstance(tipo, str), 'O tipo de aluguel deve ser uma string H, D ou S.'
        assert isinstance(data_hora, dt.datetime), 'A data informada não está no padrão correto.'
        if self.aluguel_ativo == False:
            self.loja = loja
            self.qtd = qtd
            self.tipo = str.upper(tipo)
            self.data_aluguel = data_hora
            self.desconto = False
            if self.tipo == 'H' or self.tipo == 'D' or self.tipo == 'S':
                if loja.estoque >= self.qtd:
                    print(f"Aluguel liberado.\nModalidade: {self.tipo}\nQuantidade: {self.qtd} bicicleta(s).")
                    loja.estoque -= self.qtd
                    self.aluguel_ativo = True
                    if self.qtd >= 3:
                        self.desconto = True
                        print(f"Parabéns, você ganhou um desconto de 30% no aluguel de {self.qtd} bicicletas.")
                else:
                    print(f"A loja {loja.nome} não tem bicicletas disponíveis para aluguel. Estoque: {loja.estoque}.")
            else:
                print(f"A loja {loja.nome} só trabalha com aluguel nas modalidades Hora(H), Dia(D) ou Semana(S).")
        else:
            print(f"O cliente {self.nome} já tem {self.qtd} bicicleta(s) alugada(s) na loja {self.loja.nome} e não é possível fazer um novo aluguel.")
        
        
        texto_log = f'''
****************************************************************************************************************
*  LOG
*  Classe: {__class__.__name__} - {__class__.mro()}
*  Método: {__class__.alugar_bicicleta.__name__}
*  Parâmetros recebidos: {self.nome, loja.nome, qtd, tipo, data_hora}
*  Data: {dt.datetime.now().strftime('%d/%m/%Y %H:%M:%S')}
****************************************************************************************************************
'''
        print(texto_log)

    def devolver_bicicleta(self, data_hora):
        assert isinstance(data_hora, dt.datetime), 'A data de devolução informada não está no padrão correto.'
        if self.aluguel_ativo == True:
            self.data_devolucao = data_hora
            valor, duracao, modelo = classeLoja.Loja.calcular_valor(self.tipo, self.data_aluguel, self.data_devolucao)
            if self.qtd >= 3:
                valor = (valor * self.qtd) * 0.7
                print(f"Oba!\nPor ter alugado {self.qtd} bicicletas você ganhou um desconto de 30% e o aluguel ficou em R$ {valor:.0f},00 pelo período de {duracao} {modelo}.")
            else:
                print(f"O aluguel de {self.qtd} bicicletas ficou em R$ {valor},00 pelo período de {duracao} {modelo}.")

            #fiquei na dúvida se aqui deveria remover os atributos ou só zerar.
            self.loja.estoque += self.qtd
            self.loja = ''
            self.qtd = ''
            self.tipo = ''
            self.data_aluguel = ''
            self.desconto = False
            self.data_devolucao = ''
            self.aluguel_ativo = False     
        else:
            print(f"O cliente não tem nenhuma bicicleta alugada.")

        texto_log = f'''
****************************************************************************************************************
*  LOG
*  Classe: {__class__.__name__} - {__class__.mro()}
*  Método: {__class__.devolver_bicicleta.__name__}
*  Parâmetros recebidos: {self.nome, data_hora}
*  Data: {dt.datetime.now().strftime('%d/%m/%Y %H:%M:%S')}
****************************************************************************************************************
'''
        print(texto_log)
        

    def __repr__(self):
        return f'''
    Nome do cliente: {self.nome}'''
