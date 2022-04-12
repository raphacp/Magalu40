# Quero guardar informações de um usuário:
# -> nome
# -> email
# -> cidade

usuario_lista = ["Paulo Sestini", "paulo@email.com", "Votuporanga"]

# Dicionário
usuario = {
    "email": "paulo@email.com",
    "nome":"Paulo Otávio Sestini",
    "cidade": "Votuporanga"
}

print(usuario["nome"])
print(usuario["email"])
print(usuario["cidade"])
print(usuario)

usuario["telefone"] = 123456789

print(usuario)

usuario["telefone"] = 987654321
print(usuario)

usuario.pop("telefone")
print(usuario)

dicionario_novo = {'país': 'Brasil', 'estado': 'São Paulo'}
usuario.update(dicionario_novo)
print(usuario)



