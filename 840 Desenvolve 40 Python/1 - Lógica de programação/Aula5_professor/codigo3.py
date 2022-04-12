usuario = {
    "email": "paulo@email.com",
    "nome":"Paulo Otávio Sestini",
    "cidade": "Votuporanga"
}

for chave in usuario:
    print(chave)
    print(usuario[chave])

chaves = list(usuario.keys())
valores = list(usuario.values())
print(chaves)
print(valores)
