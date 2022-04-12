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

    banco_de_dados.append(novo_usuario)

def lista_usuarios(banco_de_dados):
    for usuario in banco_de_dados:
        print(usuario)

def pedir_dados():
    nome = input("Digite o nome do novo usuário: ")
    email = input("Digite o email do novo usuário: ")

    return nome, email

usuarios = []
opcao = int(input("\nEscolha uma opção: \n1. Cadastrar usuário \n2. Listar usuários \n3. Encerrar\n"))

while opcao != 3:
    if opcao == 1:
        nome, email = pedir_dados()
        cadastrar(usuarios, nome, email)
    elif opcao == 2:
        lista_usuarios(usuarios)

    opcao = int(input("\nEscolha uma opção: \n1. Cadastrar usuário \n2. Listar usuários \n3. Encerrar\n"))