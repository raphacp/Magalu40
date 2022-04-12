# Utilizando um contador para fazer algo várias vezes

# Faça um programa que aceite a nota de N provas e calcula a média
# media = soma_das_notas / N

N = int(input("Informe quantas notas serão digitadas: "))

soma_das_notas = 0

contador = 1
while contador <= N:
    nota = float(input(f"{contador}. Digite uma nota: "))
    soma_das_notas = soma_das_notas + nota
    contador = contador + 1

media = soma_das_notas / N

print(f"A média das provas é {media:.2f}.")

