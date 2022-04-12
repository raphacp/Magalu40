#Crie um programa que peça a quantidade de notas a serem digitadas e calcule a média

""" N = int(input("Informe a quantidade de notas que serão digitadas: "))
soma_das_notas = 0
contador = 0

while contador < N:
    nota = float(input(f"Digite a nota {contador+1}: "))
    soma_das_notas = soma_das_notas + nota
    contador = contador + 1

media = soma_das_notas / N

print(f"A média das provas é {media:.2f}.") """


# Tabuada de 7

""" for contador in range(11):
    valor_da_tabuada = 7 * contador
    print(f"7 x {contador} = {valor_da_tabuada}") """

# Tabuada de 2 até 10

""" for N in range(2, 11):
    print(f"\nTabuada do {N}:\n")
    for contador in range(11):
        valor_da_tabuada = N * contador
        print(f"{N} x {contador} = {valor_da_tabuada}")
    print("\n***** FIM *****") """

# for contador in range(10):
#     print(contador)

# for contador in range(3, 7):
#     print(contador)

# for contador in range(0, 11, 2):
#     print(contador)

# Calcule a potência a^b
#Exemplo 2^3 = 8
#2^3 = 2*2*2 = 8

""" a = int(input("Digite o valor de a: "))
b = int(input("Digite o valor de b: "))

resultado = 1

for i in range(b):
    resultado = resultado * a

print(f"O resultado da potência de {a}^{b} é {resultado}.") """

# Fatorial de N
# Fatorial de 5 = 5! = 5*4*3*2*1
# Fatorial de N = N! = N * (N-1) * (N-2) * ...

# Gerando números aleatórios
import random
print (random.randint(0, 10))
