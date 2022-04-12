# Convertendo entre tupla e lista
# tupla = (1, 2, 3)
# print(tupla)
# lista = list(tupla)
# print(lista)
# tupla = tuple(lista)
# print(tupla)

alunos_e_notas = {
    "paulo": 8,
    "matheus": 7,
    "gabriela": 4.5,
    "amanda": 9,
    "ivan": 4,
    "larissa": 7.5
}

# Construir uma função
# que retorne uma lista de alunos aprovados
# e outra de alunos reprovados
# Critério de aprovação: nota >= 5

def calcular_aprovacao(alunos_e_notas):
    aprovados = []
    reprovados = []
    for aluno in alunos_e_notas:
        nota = alunos_e_notas[aluno]
        if nota >= 5:
            aprovados.append(aluno)
        else:
            reprovados.append(aluno)

    return aprovados, reprovados

aprovados, reprovados = calcular_aprovacao(alunos_e_notas)
print(aprovados)
print(reprovados)