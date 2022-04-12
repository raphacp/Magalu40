# Alguns exemplos
# y = x^2
# y = x**2

valores_x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
valores_y = []

for x in valores_x:
    valores_y.append(x**2)

print(valores_x)
print(valores_y)

# Exemplos com nomes

nomes = ['paulo sestini', 'matheus ribeiro', 'edilene gomes', 'paulo ohata']
nomes_maiusculos = []

for nome in nomes:
    nomes_maiusculos.append(nome.title())

print(nomes)
print(nomes_maiusculos)

# Atualizando a mesma lista
nomes = ['paulo sestini', 'matheus ribeiro', 'edilene gomes', 'paulo ohata']

for indice in range(len(nomes)):
    nomes[indice] = nomes[indice].title()

print(nomes)

# Calcular a média de N provas
N = int(input("Quantas notas serão digitadas? "))
notas = []

for contador in range(N):
    nota = float(input(f"{contador+1}. Digite uma nota: "))
    notas.append(nota)

media = sum(notas) / len(notas)
print(f"A média das notas é {media:.2f}")


