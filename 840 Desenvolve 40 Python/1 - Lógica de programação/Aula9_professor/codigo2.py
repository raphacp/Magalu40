alunos_e_notas = [
    {
        "nome": "paulo",
        "nota": 8
    },
    {
        "nome": "matheus",
        "nota": 7
    },
    {
        "nome": "gabriela",
        "nota": 4.5
    },
    {
        "nome": "amanda",
        "nota": 9
    },
    {
        "nome": "ivan",
        "nota": 4
    },
    {
        "nome": "larissa",
        "nota": 7.5
    },
]

# Encontrar os alunos aprovados
alunos_aprovados = []
for aluno in alunos_e_notas:
    nota = aluno["nota"]
    if nota >= 5:
        alunos_aprovados.append(aluno)

print(alunos_aprovados)


# Checar se algo está numa lista
frutas = ["maçã", "uva", "melão"]

if "maçã" in frutas:
    print("tem maçã")
else:
    print("não tem maçã")

if "pera" in frutas:
    print("tem pera")
else:
    print("não tem pera")

numeros = [10, 5, 20]

if 20 in numeros:
    print(20)

if 30 in numeros:
    print(30)

# Funções

def obter_aprovados(listas_de_alunos):

    alunos_aprovados = []
    for aluno in listas_de_alunos:
        nota = aluno["nota"]
        if nota >= 5:
            alunos_aprovados.append(aluno)

    return alunos_aprovados

aprovados = obter_aprovados(alunos_e_notas)

print(aprovados)


outros_alunos = [
    {
        "nome": "amanda",
        "nota": 8
    },
    {
        "nome": "paulo",
        "nota": 4
    }
]

print(obter_aprovados(outros_alunos))

def buscar_nota_do_aluno(nome_do_aluno, lista_de_alunos):
    for aluno in lista_de_alunos:
        if aluno["nome"] == nome_do_aluno:
            return aluno["nota"]

print(buscar_nota_do_aluno("amanda", alunos_e_notas))

def buscar_alunos(lista_de_nomes, lista_de_alunos):
    resultado = []
    for aluno in lista_de_alunos:
        if aluno["nome"] in lista_de_nomes:
            resultado.append(aluno)
    return resultado


print(buscar_alunos(["paulo", "amanda"], alunos_e_notas))