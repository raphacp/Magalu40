# Dicionários

# Dicionários são relações entre chaves e valores

# notas = [5, 2, 10, 3, 4]
# print(notas[2])

alunos_e_notas = {
    "paulo": 8,
    "matheus": 9,
    "gabriela": 4.5,
    "amanda": 9,
    "ivan": 4,
    "larissa": 7.5
}

print(alunos_e_notas)

# Obter valor por meio de chave
print(alunos_e_notas["paulo"])
print(alunos_e_notas["matheus"])

# Adicionar chaves e valores novos
alunos_e_notas["carlos"] = 10

print(alunos_e_notas)

# Podemos checar se chaves existem
if "josé" in alunos_e_notas:
    print(alunos_e_notas["josé"])
else:
    print("a chave josé não existe")

if "paulo" in alunos_e_notas:
    print(alunos_e_notas["paulo"])
else:
    print("a chave paulo não existe")

# Loop no dicionário
alunos_com_nota_9 = []

for aluno in alunos_e_notas:
    nota = alunos_e_notas[aluno] # alunos_e_notas["paulo"]
    if nota == 9:
        alunos_com_nota_9.append(aluno)

print(alunos_com_nota_9)

