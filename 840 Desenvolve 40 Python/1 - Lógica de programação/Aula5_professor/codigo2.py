usuarios = [
    {
        "nome": "paulo",
        "email": "paulo@email.com"
    },
    {
        "nome": "matheus",
        "email": "matheus@email.com"
    }
]

for usuario in usuarios:
    print(usuario["nome"], usuario["email"])

usuarios = {
    "nome": ["paulo", "matheus"],
    "email": ["paulo@email.com", "matheus@email.com"]
}

#    nome        email

#    paulo       matheus
#    paulo@email matheus@email

print(usuarios["email"])