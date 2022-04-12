# from datetime import datetime
# Programa que cadastra várias pessoas

# Escolha uma opção:
# 1. Cadastrar usuário
# 2. Listar usuários
# 3. Encerrar

def cadastrar(banco_de_dados, nome, email):
    novo_usuario = {}
    novo_usuario["nome"] = nome
    novo_usuario["email"] = email
    # novo_usuario["data_de_cadastro"] = datetime.now().strftime("%d/%m/%Y")
    banco_de_dados.append(novo_usuario)

def listar(lista_de_usuarios):
    for usuario in lista_de_usuarios:
        print(usuario)

usuarios = []
opcao = int(input("\nEscolha uma opção: \n1. Cadastrar usuário \n2. Listar usuários \n3. Encerrar\n"))

while opcao != 3:
    if opcao == 1:
        nome = input("Digite o nome do novo usuário: ")
        email = input("Digite o email do novo usuário: ")

        cadastrar(usuarios, nome, email)

    elif opcao == 2:
        listar(usuarios)

    opcao = int(input("\nEscolha uma opção: \n1. Cadastrar usuário \n2. Listar usuários \n3. Encerrar\n"))