# from datetime import datetime
# Programa que cadastra várias pessoas

# Escolha uma opção:
# 1. Cadastrar usuário
# 2. Listar usuários
# 3. Encerrar

usuarios = []
opcao = int(input("\nEscolha uma opção: \n1. Cadastrar usuário \n2. Listar usuários \n3. Encerrar\n"))

while opcao != 3:
    if opcao == 1:
        nome = input("Digite o nome do novo usuário: ")
        email = input("Digite o email do novo usuário: ")

        novo_usuario = {}
        novo_usuario["nome"] = nome
        novo_usuario["email"] = email
        # novo_usuario["data_de_cadastro"] = datetime.now().strftime("%d/%m/%Y")
        usuarios.append(novo_usuario)
    elif opcao == 2:
        for usuario in usuarios:
            print(usuario)

    opcao = int(input("\nEscolha uma opção: \n1. Cadastrar usuário \n2. Listar usuários \n3. Encerrar\n"))