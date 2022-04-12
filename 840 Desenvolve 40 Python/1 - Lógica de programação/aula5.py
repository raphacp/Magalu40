# Dicionário
#Diferente da lista o dicionário não usa indíce. Devemos nos preocupar com chaves ou invés da posição

# usuario_lista = ["Paulo Sestini", "paulo@email.com", "Votuporanga"]
# usuarios = [
#     {
#         "nome": "paulo",
#         "email": "paulo@email.com"
#     },
#     {
#         "nome": "matheus",
#         "email": "matheus@email.com"
#     }
# ]
# for usuario in usuarios:
#     print(usuario["nome"], usuario["email"])

# usuarios = {
#     "email": "paulo@email.com",
#     "nome": "Paulo Sestini",
#     "cidade": "Votuporanga"
# }

# print(usuarios["nome"])
# print(usuarios["email"])
# print(usuarios["cidade"])
# print(usuarios)

#Diferente de uma variável qualquer, o dicionário cria um novo campo caso ele não exista usando o =
# usuarios["telefone"] = 2158978547
# print(usuarios)


# for chave in usuarios:
#     print("Chave:",chave, "\nValor:", usuarios[chave])

# chaves = list(usuarios.keys())
# valores = list(usuarios.values())
# print(chaves)
# print(valores)

# if "email" in usuarios:
#     print(usuarios["email"])
# else:
#     print("Não existe a chave email.")

# if "pais" in usuarios:
#     print(usuarios["pais"])
# else:
#     print("Não existe a chave país.")

# alunos = {
#     'paulo': {
#         'nota': 8,
#         'presença': 80
#     },
#     'matheus':{
#         'nota': 9,
#         'presença': 70
#     }
# }

# Fica tipo uma matriz
#
#   aluno   nota    presença
#   paulo   8           80
#   matheus 9           70
#

# print(alunos['paulo'])
# print(alunos['matheus']["presença"])

# alunos['matheus']['média'] = 8.7

# print(alunos)


# Programa que cadastra uma pessoa

# usuario = {}
# nome = input("Digite o nome do usuário: ")
# email = input("Digite o email do usuário: ")
# cidade = input("Digite a cidade do usuário: ")

# usuario['nome'] = nome
# usuario['email'] = email
# usuario['cidade'] = cidade

# print(usuario)
# for campo in usuario:
#     print(usuario[campo])


# Programa que cadastra várias pessoas

#Escolha uma opção:
#1. Cadastrar usuário
#2. Listar usuários
#3. Encerrar

from datetime import datetime


usuarios = []
opcao = int(input("\nEscolha uma opção: \n1. Cadastrar usuário \n2. Listar usuários \n3. Encerrar\n"))

while opcao != 3:
    if opcao == 1:
        nome = input('Digite o nome do novo usuário: ')
        email = input('Digite o email do novo usuário: ')
        
        novo_usuario = {}
        novo_usuario['nome'] = nome
        novo_usuario['email'] = email
        novo_usuario['data de cadastro'] = datetime.now().strftime("%d/%m:%Y %H:%M:%S")
        usuarios.append(novo_usuario)
    elif opcao == 2:
        for usuario in usuarios:
            print(usuario)

    opcao = int(input("\nEscolha uma opção: \n1. Cadastrar usuário \n2. Listar usuários \n3. Encerrar\n"))


