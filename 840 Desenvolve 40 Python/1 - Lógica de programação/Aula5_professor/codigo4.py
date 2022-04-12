usuario = {
    "email": "paulo@email.com",
    "nome":"Paulo Otávio Sestini",
    "cidade": "Votuporanga"
}

if "email" in usuario:
    print(usuario["email"])
else:
    print("Não existe a chave email.")

if "país" in usuario:
    print(usuario["país"])
else:
    print("Não existe a chave país.")