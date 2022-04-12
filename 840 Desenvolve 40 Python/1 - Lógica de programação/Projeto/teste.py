import json
import os.path
import sys

def obter_dados():
    '''
    Essa função carrega os dados dos produtos e retorna uma lista de dicionários, onde cada dicionário 
    representa um produto.
    NÃO MODIFIQUE essa função.
    '''
    with open(os.path.join(sys.path[0], 'dados.json'), 'r') as arq:
        dados = json.loads(arq.read())
    return dados

def valida_entrada():
    mensagem = '''
    1. Listar categorias
    2. Listar produtos de uma categoria
    3. Produto mais caro por categoria
    4. Produto mais barato por categoria
    5. Top 10 produtos mais caros
    6. Top 10 produtos mais baratos
    0. Sair
    '''
    opcao = input(mensagem)
    
    while not opcao.isdigit() or int(opcao) < 0 or int(opcao) > 6:
        print("Opção digitada inválida. Digite novamente.")
        opcao = input(mensagem)
    #print("É dígito")
    opcao = int(opcao)

    return opcao

def menu(dados):

    opcao = valida_entrada()

    while opcao != 0: #Sair  
        #print("Não é zero. Continua.")
        if opcao == 1: #Listar categorias
            print("Olá 1")
        elif opcao == 2: #Listar produtos de uma categoria
            print("Olá 2")
        elif opcao == 3: #Produto mais caro por categoria
            print("Olá 3")
        elif opcao == 4: #Produto mais barato por categoria
            print("Olá 4")
        elif opcao == 5: #Top 10 produtos mais caros
            print("Olá 5")
        elif opcao == 6: #Top 10 produtos mais baratos
            print("Olá 6")
        opcao = valida_entrada()

    print("Tchau, obrigado.")
    
# Programa Principal - não modificar!
d = obter_dados()
menu(d)

