# Vamos fazer um programa para verificar quem é o
# assassino de um crime. Para descobrir o assassino,
# a polícia faz um pequeno questionário com 5 perguntas
# onde a resposta só pode ser sim ou não (s/n):

# a. Mora perto da vítima?

# b. Já trabalhou com a vítima?

# c. Telefonou para a vítima?

# d. Esteve no local do crime?

# e. Devia para a vítima?

# Cada resposta sim dá um ponto para o suspeito.
# A polícia considera que os suspeitos com 5 pontos são os assassinos,
# com 4 a 3 pontos são cúmplices e 2 pontos são apenas suspeitos,
# necessitando outras investigações.
# Valores iguais ou abaixo de 1 são liberados.

pergunta_a = input("Mora perto da vítima? ")
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

if pontos == 5:
    print("Assassino")
elif pontos == 3 or pontos == 4:
    print("Cúmplice")
elif pontos == 2:
    print("Suspeito")
else:
    print("Liberado")


