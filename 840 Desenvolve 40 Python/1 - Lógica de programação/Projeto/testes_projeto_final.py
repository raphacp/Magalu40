# Você foi contratado pelo Magazine Luiza para desenvolver um sistema que irá auxiliá-los a escolher os produtos
# que irão receber desconto na próxima Black Friday.
# Para isso, você terá acesso a uma API que fornece alguns dados dos produtos: um ID (identificador único), o 
# preço e a categoria do produto. Uma função pronta irá retornar para você o conjunto de dados já em formato 
# adequado: uma lista de dicionários, onde cada dicionário representa um produto.
# Você deverá implementar as funções para listar todas as categorias, listar todos os produtos de uma categoria, 
# identificar o produto mais barato e o mais caro de uma categoria e o top 10 de produtos mais baratos e mais 
# caros de toda a base de dados.
# Você pode baixar a base de dados clicando aqui e o código pronto para auxiliá-lo clicando aqui. Renomeie a 
# base de dados para dados.json.
# Leia atentamente os comentários no código fornecido. Não modifique a função já pronta e respeite os parâmetros 
# e retorno solicitados nos comentários de cada função que você irá desenvolver.
# Atente-se ao prazo de entrega. Você pode entregar o seu exercício fazendo o upload do arquivo .py finalizado.

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

def listar_categorias(dados):
    '''
    O parâmetro "dados" deve ser uma lista de dicionários representando os produtos.
    Essa função deverá retornar uma lista contendo todas as categorias dos diferentes 
    produtos. Cuidado para não retornar categorias repetidas.
    '''
    print("Listando as categorias.\n")

    categorias = []
    for categoria in dados:
        if categoria["categoria"] not in categorias:
            categorias.append(categoria["categoria"])
    return categorias

##### FEITO #####

def listar_por_categoria(dados, categoria):
    '''
    O parâmetro "dados" deve ser uma lista de dicionários representando os produtos.
    O parâmetro "categoria" é uma string contendo o nome de uma categoria.
    Essa função deverá retornar uma lista contendo todos os produtos pertencentes à categoria dada.
    '''
    print(f"Listando os produtos da categoria \"{categoria.upper()}\".\n")
    
    produtos_categoria = []
    for produto in dados:
        if produto["categoria"] == categoria:
            produtos_categoria.append(produto)
    return produtos_categoria

##### FEITO #####

def produto_mais_caro(dados, categoria):
    '''
    O parâmetro "dados" deve ser uma lista de dicionários representando os produtos.
    O parâmetro "categoria" é uma string contendo o nome de uma categoria.
    Essa função deverá retornar um dicionário representando o produto mais caro da 
    categoria dada.
    '''
    print("Listando o produto mais caro.\n")
    lista_categoria = listar_por_categoria(dados, categoria)
    produto_caro = {}
    caro = 0
    for produto in lista_categoria:
        if float(produto["preco"]) > caro:
            produto_caro = produto
            caro = float(produto["preco"])
    return produto_caro

##### FEITO #####

def produto_mais_barato(dados, categoria):
    '''
    O parâmetro "dados" deve ser uma lista de dicionários representando os produtos.
    O parâmetro "categoria" é uma string contendo o nome de uma categoria.
    Essa função deverá retornar um dicionário representando o produto mais caro da 
    categoria dada.
    '''
    print("Listando o produto mais barato.\n")
    lista_categoria = listar_por_categoria(dados, categoria)
    produto_barato = {}
    valor = float(lista_categoria[0]['preco'])
    for produto in lista_categoria:
        if float(produto["preco"]) < valor:
            produto_barato = produto
            valor = float(produto["preco"])
    return produto_barato

##### FEITO #####

def produto_mais_caro_geral(dados):
    '''
    O parâmetro "dados" deve ser uma lista de dicionários representando os produtos.
    Essa função deverá retornar um dicionário representando o produto mais caro.
    '''

    produto_caro = {}
    caro = 0
    indice = 0
    for produto in dados:
        if float(produto["preco"]) > caro:
            produto_caro = produto
            caro = float(produto["preco"])
            indice = dados.index(produto)
    return produto_caro, indice

def top_10_caros(dados):
    '''
    O parâmetro "dados" deve ser uma lista de dicionários representando os produtos.
    Essa função deverá retornar uma lista de dicionários representando os 10 produtos 
    mais caros.
    '''
    print("Listando os 10 produtos mais caros.\n")

    produtos = dados.copy()
    mais_caros = []
    caro = 0

    for i in range (10):
        mais_caro, indice = produto_mais_caro_geral(produtos)
        mais_caros.append(mais_caro)
        produtos.pop(indice)
       
    return mais_caros

def produto_mais_barato_geral(dados):
    '''
    O parâmetro "dados" deve ser uma lista de dicionários representando os produtos.
    Essa função deverá retornar um dicionário representando o produto mais barato.
    '''
    produto_barato = {}
    valor = float(dados[0]['preco'])
    indice = 0
    for produto in dados:
        if float(produto["preco"]) < valor:
            produto_barato = produto
            valor = float(produto["preco"])
            indice = dados.index(produto)
    return produto_barato, indice

def top_10_baratos(dados):
    '''
    O parâmetro "dados" deve ser uma lista de dicionários representando os produtos.
    Essa função deverá retornar uma lista de dicionários representando os 10 produtos 
    mais caros.
    '''
    print("Listando os 10 produtos mais baratos.\n")

    produtos = dados.copy()
    mais_baratos = []

    for i in range (10):
        mais_barato, indice = produto_mais_barato_geral(produtos)
        mais_baratos.append(mais_barato)
        produtos.pop(indice)
       
    return mais_baratos

def menu(dados):
    '''
    O parâmetro "dados" deve ser uma lista de dicionários representando os produtos.
    Essa função deverá, em loop, realizar as seguintes ações:
    - Exibir as seguintes opções:
        1. Listar categorias
        2. Listar produtos de uma categoria
        3. Produto mais caro por categoria
        4. Produto mais barato por categoria
        5. Top 10 produtos mais caros
        6. Top 10 produtos mais baratos
        0. Sair
    - Ler a opção do usuário.
    - No caso de opção inválida, imprima uma mensagem de erro.
    - No caso das opções 2, 3 ou 4, pedir para o usuário digitar a categoria desejada.
    - Chamar a função adequada para tratar o pedido do usuário e salvar seu retorno.
    - Imprimir o retorno salvo. 
    O loop encerra quando a opção do usuário for 0.
    '''

    mensagem = '''
    1. Listar categorias
    2. Listar produtos de uma categoria
    3. Produto mais caro por categoria
    4. Produto mais barato por categoria
    5. Top 10 produtos mais caros
    6. Top 10 produtos mais baratos
    0. Sair
    '''

    categoria = ""
    opcao = input(mensagem)
    
    #while not (opcao.isdigit()) or int(opcao) < 0 or int(opcao) > 6:
    while opcao.isdigit():
        opcao = int(opcao)
        while opcao != 0: #Sair
            if opcao not in range(0, 7):
                print(f"Opção digitada inválida. Digite novamente.")
                opcao = input(mensagem)
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
        print(f"Opção digitada inválida. Digite novamente.")
        opcao = input(mensagem)

    print("Tchau, obrigado.")
# Programa Principal - não modificar!
d = obter_dados()
menu(d)

