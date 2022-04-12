# 14/01/2022

# 1 
# Faça um programa que peça a idade do usuário e imprima se ele é maior ou menor de 18 anos.

""" idade = int(input("Digite a sua idade: "))

if idade < 18:
    print("Você é menor de 18 anos.")
else:
    print("Você é maior de 18 anos.") """

# 2 
# Faça um programa que peça um número e mostre se ele é positivo ou negativo.

""" numero = float(input("Digite um número: "))

if numero >= 0:
    print(f"O número digitado ({numero}) é positivo")
else:
    print(f"O número digitado ({numero}) é negativo") """

# 3 
# Faça um programa que peça dois números e mostre o maior deles.

""" numero1 = float(input("Digite um número: "))
numero2 = float(input("Digite outro número: "))

if numero1 > numero2:
    print(f"O maior número digitado é: {numero1}.")
else:
    print(f"O maior número digitado é: {numero2}.") """

# 4 
# Faça um programa que leia a validade das informações:
# a. Idade: entre 0 e 150;
# b. Salário: maior que 0;
# c. Sexo: M, F ou Outro;
# O programa deve imprimir uma mensagem de erro para cada informação inválida.

""" idade = int(input("Digite a idade: "))
salario = float(input("Digite o salário: "))
sexo = input("Digite o sexo: ")

if idade < 0 or idade > 150:
    print("O valor digitado está incorreto. A idade deve ser entre 0 e 150.")

if salario <= 0:
    print("O valor digitado está incorreto. O salário deve ser maior que 0.")

# if sexo != "M":
#     if sexo != "F":
#         if sexo != "Outro":
#             print("O valor digitado está incorreto. O sexo deve ser M, F ou Outros.")

if sexo != "M" and sexo != "F" and sexo != "Outro":
            print("O valor digitado está incorreto. O sexo deve ser M, F ou Outros.") """

# 5 
# Escreva um programa que peça a nota de 3 provas de um aluno e verifique se ele passou ou não de ano.
# Obs.: O aluno irá passar de ano se sua média for maior que 6.

""" nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

media = (nota1 + nota2 + nota3) / 3

if media < 6:
    print(f"Poxa! Você não passou de ano. Sua média foi: {media}.")
else:
    print(f"Parabéns! Você passou de ano. Sua média foi: {media}.") """

# 6 
# Vamos fazer um programa para verificar quem é o assassino de um crime. Para descobrir o assassino, 
# a polícia faz um pequeno questionário com 5 perguntas onde a resposta só pode ser sim ou não:
# a. Mora perto da vítima?
# b. Já trabalhou com a vítima?
# c. Telefonou para a vítima?
# d. Esteve no local do crime?
# e. Devia para a vítima?
# Cada resposta sim dá um ponto para o suspeito. A polícia considera que os suspeitos com 5 pontos são 
# os assassinos, com 4 a 3 pontos são cúmplices e 2 pontos são apenas suspeitos, necessitando outras 
# investigações. Valores iguais ou abaixo de 1 são liberados.

""" pergunta_a = input("Mora perto da vítima? ")
pergunta_b = input("Já trabalhou com a vítima? ")
pergunta_c = input("Telefonou para a vítima? ")
pergunta_d = input("Esteve no local do crime? ")
pergunta_e = input("Devia para a vítima? ")
pontos = 0

if pergunta_a == "s":
    pontos = pontos + 1

if pergunta_b == "s":
    pontos = pontos + 1

if pergunta_c == "s":
    pontos = pontos + 1

if pergunta_d == "s":
    pontos = pontos + 1

if pergunta_e == "s":
    pontos = pontos + 1

print(f"Sua pontuação foi: {pontos}.")

if pontos <= 1:
    print("Ufa! Você não é um suspeito e está liberado.")
elif pontos <= 2:
    print("Opa! Você é um suspeito e investigaremos mais sobre você.")
elif pontos <= 4:
    print("Xiii! Você é cúmplice do crime.")
elif pontos <= 5:
    print("Perdeu Perdeu! Você é o assasino. Já para a cadeia")
 """

# 7 
# Desafio 3 - Um hospital quer fazer o diagnóstico de gripe ou dengue a partir de um questionário de 
# sintomas, tendo as perguntas abaixo, faça um programa que faça o diagnóstico deste hospital:
# a. Sente dor no corpo?
# b. Você tem febre?
# c. Você tem tosse?
# d. Está com congestão nasal?
# e. Tem manchas pelo corpo?
# Para o diagnóstico ele tem a seguinte tabela:
# A     B   C	D	E	Resultado
# Sim   Sim	Não	Não	Sim	Dengue
# Sim	Sim	Sim	Sim	Não	Gripe
# Não	Sim	Sim	Sim	Não	Gripe
# Sim	Não	Não	Não	Não	Sem doenças
# Não	Não	Não	Não	Não	Sem doenças

""" perg_a = input("Sente dor no corpo (s/n)? ")
perg_b = input("Você tem febre (s/n)? ")
perg_c = input("Você tem tosse (s/n)? ")
perg_d = input("Está com congestão nasal (s/n)? ")
perg_e = input("Tem manchas pelo corpo (s/n)? ")

if perg_a == "s" and perg_b == "s" and perg_c == "n" and perg_d == "n" and perg_e == "s":
    print("Você está com Dengue.")
if perg_b == "s" and perg_c == "s" and perg_d == "s":
    print("Você está com Gripe.")
if perg_b == "n" and perg_c == "n" and perg_d == "n" and perg_e == "n":
    print("Você está sem doença.") """



