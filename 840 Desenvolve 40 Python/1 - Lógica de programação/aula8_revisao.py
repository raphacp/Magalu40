alunos_e_notas = [
    {
        "nome": "Paulo",
        "nota": 8
    },
    {
        "nome": "Rapha",
        "nota": 9
    },
    {
        "nome": "Eduardo",
        "nota": 7.5
    },
    {
        "nome": "Julia",
        "nota": 8.5
    }
]

# alunos_aprovados = []
# for aluno in alunos_e_notas:
#     nota = aluno["nota"]
#     if nota >= 8:
#         alunos_aprovados.append(aluno)

# print(alunos_aprovados)


#Verificando se um valor existe em uma lista
# frutas = ["maçã", "uva", "melão"]

# if "maçã" in frutas:
#     print("Tem maçã.")
# else:
#     print("Não tem maçã.")

# if "pêra" in frutas:
#     print("Tem pêra.")
# else:
#     print("Não tem pêra.")

# numeros = [20, 10, 5, 45]

# if 20 in numeros:
#     print(20)

# if 40 in numeros:
#     print(30)

def buscar_nota_do_aluno(nome_do_aluno, lista_de_alunos):
    for aluno in lista_de_alunos:
        if aluno["nome"] == nome_do_aluno:
            return aluno["nota"]

print(buscar_nota_do_aluno("Rapha", alunos_e_notas))

def buscar_alunos(lista_de_nomes, lista_de_alunos):
    resultado = []
    for aluno in lista_de_alunos:
        if aluno["nome"] in 



prod_caro = {}
mais_caro = 0
for i in range (len(prod_categ)):
    if prod_categ[i]['preco'] > mais_caro:
        prod_caro = prod_categ[i]
        mais_caro = prod_categ[i]['preco']