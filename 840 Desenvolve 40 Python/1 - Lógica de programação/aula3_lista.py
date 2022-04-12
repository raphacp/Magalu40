# 1
# Faça um programa que peça ao usuário um número e imprima todos os números de um até o número dado.
# Exemplo: digite: 5
# imprime: 1 2 3 4 5

""" numero = int(input("Digite um número: "))

for i in range(1, numero+1):
    print(i) """

# 2
# Peça ao usuário para digitar um número e imprima o fatorial de n.

""" numero = int(input("Digite um número para calcularmos o seu fatorial: "))
fatorial = 1

for i in range(1, numero+1):
    fatorial = fatorial * i

print(f"O fatorial de {numero} é {fatorial}") """


# 3
# Peça ao usuário para digitar um número N e some todos os números de 1 a N utilizando o laço de 
# repetição while.

""" numero = int(input("Digite um número: "))

contador = 1
soma = 0

while contador <= numero:
    #print(contador)
    soma = soma + contador
    contador = contador + 1
print(soma) """

# 4
# Faça um programa que imprima a tabuada do 9 (de 9*1 a 9*10) usando loops.

""" for i in range(11):
    valor_da_tabuada = 9 * i
    print(f"9 x {i} = {valor_da_tabuada}") """

# 5
# Faça um programa, usando loops, que peça para um usuário digitar um número e que só finaliza 
# quando o usuário digitar 0. Ao final imprima a soma de todos os números digitados.

""" numero = int(input("Digite um número: "))
soma = 0

while numero != 0:
    soma = soma + numero
    #print("O número digitado está incorreto. Tente novamente.")
    numero = int(input("\nO número digitado está incorreto. Digite outro número: "))

print(f"Você acertou! A soma dos números digitados é {soma}.") """

# 6
# Faça um programa que sorteia um número N e peça para o usuário adivinhar o número sorteado. 
# A cada resposta errada, o seu programa deve imprimir um aviso dizendo que a resposta está errada e 
# pedir novamente uma resposta ao usuário.
# Para a realização desse exercício, utilize alguma função da biblioteca random (e.g. randint()).

""" import random

numero_sorteado = random.randint(0, 5)
numero = int(input("Advinhe o número sorteado (0 a 5): "))

while numero_sorteado != numero:
    print(f"A resposta está errada. Tente novamente. {numero_sorteado}/{numero}")
    numero_sorteado = random.randint(0, 5)
    numero = int(input("Advinhe o número sorteado (0 a 5): "))

print("A resposta está correta!") """

# 7
# Faça um programa que peça para o usuário digitar a idade, o salário e o sexo de uma pessoa até que as 
# entradas digitadas sejam válidas.
# a. Idade: entre 0 e 150;
# b. Salário: maior que 0;
# c. Sexo: M, F ou Outro.

""" idade = int(input("Digite a idade: "))
while idade < 0 or idade > 150:
    idade = int(input("O valor digitado está incorreto. A idade deve ser entre 0 e 150. Digite a idade: "))

salario = float(input("Digite o salário: "))
while salario <= 0:
    salario = float(input("O valor digitado está incorreto. O salário deve ser maior que 0. Digite o salário: "))

sexo = input("Digite o sexo: ")
while sexo != "M" and sexo != "F" and sexo != "Outro":
    sexo = input("O valor digitado está incorreto. O sexo deve ser M, F ou Outros. Digite o sexo: ") """


# 8
# Desafio! - Calcule a soma de até mil termos da série 1 + 1/2 + 1/4 + 1/8 + 1/16 + ...
# Dica: Use três variáveis:
# • um contador, que começa em zero;
# • uma variável para a soma de todos os termos, que também começa em zero;
# • uma variável para cada termo, que começa em 1 e a cada loop é dividida por 2.
# A repetição da soma de mil termos pode ser feita com a função while contador < 1000.

""" contador = 0
soma = 0
termo = 1

while contador < 1000:
    soma = soma + termo
    contador += 1
    termo = termo / 2

print(f"A soma dos termos é {soma}") """


# 9
# Super Desafio! - Calcule a soma de mil termos dos inversos dos fatoriais: 
# 1/(1!) + 1/(2!) + 1/(3!) + 1/(4!) + ...
# Dica: Assim como no exercício anterior use três variáveis: um contador; uma variável para a soma; 
# e uma variável para os termos. Lembre-se de que 4! = 4*3*2*1 que também é igual a 4*3!.

# numero = int(input("Digite um número para calcularmos o seu fatorial: "))

contador = 1
soma = 0
termo = 1
fatorial = 1

# def fatorial_fun(numero):
#     fatorial = 1
#     for i in range(1, numero+1):
#         fatorial = fatorial * i
#         return fatorial

while contador < 1000:
    for i in range(1, contador+1):
        fatorial = fatorial * i
    # fatorial_resultado = fatorial_fun(contador)
    termo = 1 / (fatorial)
    soma = soma + termo
    contador += 1
    fatorial = 1

print(f"A soma dos termos é {soma}")

#Resposta do exercício

""" contador = 1
soma = 0
valor = 1 
fatorial = 1

while contador < 1000:
  fatorial *= contador
  valor = 1/fatorial
  soma += valor
  contador +=1 

print(soma) """
