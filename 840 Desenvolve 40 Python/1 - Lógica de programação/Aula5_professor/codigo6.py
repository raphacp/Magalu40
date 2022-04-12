# Programa que cadastra uma pessoa
usuario = {}
nome = input("Digite o nome do usuário: ")
email = input("Digite o email do usuário: ")
cidade = input("Digite a cidade do usuário: ")

usuario["nome"] = nome
usuario["email"] = email
usuario["cidade"] = cidade

# print(usuario["nome"])
# print(usuario["email"])
# print(usuario["cidade"])

for campo in usuario:
    print(usuario[campo])