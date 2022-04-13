import classeCliente
import datetime as dt
import math
#from math import ceil

class Loja:
    def __init__(self, nome, estoque):
        if isinstance(estoque, int):
            self.estoque = estoque
        else:
            raise TypeError('Valor de estoque deve ser um número inteiro')
        self.nome = nome
        #self.estoque = estoque
    
    #Transformando o método calcular_valor em estático. Não tenho certeza se seria necessário, usei mais para aprendizado
    @staticmethod
    def calcular_valor(tipo, data_hora_aluguel, data_hora_devolucao):
        valor_hora = 5
        valor_dia = 25
        valor_semana = 100

        duracao_aluguel = data_hora_devolucao - data_hora_aluguel
        duracao_horas = (duracao_aluguel.days * 24) + (duracao_aluguel.seconds / 3600)
        duracao_dias = duracao_horas / 24
        duracao_semanas = (duracao_dias / 7)
        
        texto_log = f'''
****************************************************************************************************************
*  LOG
*  Classe: {__class__.__name__} - {__class__.mro()}
*  Método: {__class__.calcular_valor.__name__}
*  Parâmetros recebidos: {tipo, data_hora_aluguel, data_hora_devolucao}
*  Data: {dt.datetime.now().strftime('%d/%m/%Y %H:%M:%S')}
****************************************************************************************************************
'''
        print(texto_log)

        if tipo == 'H':
            custo_hora = valor_hora * math.ceil(duracao_horas)
            return custo_hora, math.ceil(duracao_horas), 'horas'
        
        elif tipo == 'D':
            custo_dia = valor_dia * math.ceil(duracao_dias)
            return custo_dia, math.ceil(duracao_dias), 'dias'

        elif tipo == 'S':
            custo_semana = valor_semana * math.ceil(duracao_semanas)
            return custo_semana, math.ceil(duracao_semanas), 'semanas'
        
        else:
            print("Tipo de aluguel incorreto. Deve ser H(hora), D(dia) ou S(semana).")
    
    def __repr__(self):
        return f'''
    Nome da loja: {self.nome}
    Estoque da loja {self.nome}: {self.estoque} bicicletas.'''

