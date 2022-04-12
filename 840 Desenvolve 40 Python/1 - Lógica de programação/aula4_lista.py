# 1
# Crie uma lista qualquer e faça um programa que imprima cada elemento da lista usando o for.

""" numeros = [5, 9, 10, 54, 1]

for i in numeros:
    print(i)

#ou
for i in range(len(numeros)): #se for usar o range tem q usar o índice da lista (len)
    print(numeros[i]) """

# 2
# Faça um programa que imprima todos os itens de uma lista usando while e compare com o exercício 1.

""" numeros = [5, 9, 10, 54, 1]
contador = 0

while contador < len(numeros):
    print(numeros[contador])
    contador += 1 """

# 3
# Faça um programa que peça para o usuário digitar um número n e imprima uma lista com todos os 
# números de 0 a n-1.
# Exemplo: se o usuário digitar 5, o programa deve imprimir [0, 1, 2, 3, 4]

""" lista_numeros = []
numero = int(input("Digite um número: "))

for i in range(0, numero):
    lista_numeros.append(i)

print(lista_numeros) """

# 4
# Faça um programa que olhe todos os itens de uma lista e diga quantos deles são pares.

""" lista_numeros = [2, 5, 8, 22, 15, 4, 9]
lista_pares = []

for i in range(0, len(lista_numeros)):
    if lista_numeros[i] % 2 == 0:
        lista_pares.append(lista_numeros[i])

print(lista_pares)
print(len(lista_pares)) """

# 5
# Faça um programa que imprima o maior número de uma lista, sem usar a função max().

""" lista_numeros = [7, 5, 8, 22, 15, 4, 9]
maior = 0

for i in range(0, len(lista_numeros)):
    if lista_numeros[i] > maior:
        maior = lista_numeros[i]

print(maior) """

# 6
# Agora usando a função max() faça um programa que imprima os três maiores números de uma lista.
# Dica: Use o método próprio de listas .remove().

""" lista_numeros = [7, 5, 8, 22, 15, 4, 9]
maiores = []

for i in range(0, 3):
    maiores.append(max(lista_numeros))
    lista_numeros.remove(max(lista_numeros))

print(maiores) """

# 7
# Faça um programa que, dadas duas listas de mesmo tamanho, crie uma nova lista com cada elemento 
# igual a soma dos elementos da lista 1 com os da lista 2, na mesma posição.
# Exemplo:
# Dadas lista1 = [1, 4, 5] e lista2 = [2, 2, 3], então lista3 = [1+2, 4+2, 5+3] = [3, 6, 8]

""" numeros_1 = [3, 7, 9, 2]
numeros_2 = [2 ,6, 8, 20]
numeros_3 = []

for i in range(0, len(numeros_1)):
    numeros_3.append(numeros_1[i] + numeros_2[i])

print(numeros_3) """

# 8
# Faça um programa que pede para o usuário digitar 5 números e, ao final, imprime uma lista com os 
# 5 números digitados pelo usuário (sem converter os números para int ou float).
# Exemplo: Se o usuário digitar 1, 5, 2, 3, 6, o programa deve imprimir a lista ['1','5','2','3','6']

""" lista_numeros = []

for i in range(0, 5):
    lista_numeros.append(input("Digite um número: "))

print(f'Os números digitados foram: {lista_numeros}') """

# 9
# Pegue a lista gerada no exercício anterior e transforme cada um dos itens dessa lista em um float.
# OBS: Não é para alterar o programa anterior, mas sim a lista gerada por ele.

""" lista_numeros = []

for i in range(5):
    lista_numeros.append(input("Digite um número: "))

# print(f'Os números digitados foram: {lista_numeros}')

for i in range(0, len(lista_numeros)):
    lista_numeros[i] = float(lista_numeros[i])
print(f'Os números digitados foram: {lista_numeros}') """

# 10
# Faça um programa que peça as 4 notas bimestrais e mostre a média aritmética delas, usando listas.

""" notas = []
soma = 0
media = 0

for i in range(4):
    notas.append(float(input("Digite a nota: ")))
    soma = soma + notas[i]

media = soma / len(notas)
print(f"A média do aluno é: {media:.2f}") """

# 11
# Crie uma lista de 10 números e imprima:
# a. uma lista com os 4 primeiros números;
# b. uma lista com os 5 últimos números;
# c. uma lista contendo apenas os elementos das posições pares;
# d. uma lista contendo apenas os elementos das posições ímpares;
# e. a lista inversa da lista sorteada (isto é, uma lista que começa com o último elemento da lista 
#    sorteada e termina com o primeiro);
# f. uma lista inversa dos 5 primeiros números;
# g. uma lista inversa dos 5 últimos números.

""" numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista_a = []
lista_b = []
lista_c = []
lista_d = []
lista_e = []
lista_f = []
lista_g = []

print(numeros)

# a. uma lista com os 4 primeiros números;
for i in range(0, 4):
    lista_a.append(numeros[i])
print(f"Os 4 primeiros números são: {lista_a}")

# b. uma lista com os 5 últimos números;
for i in range(5, len(numeros)):
    lista_b.append(numeros[i])
print(f"Os 5 últimos números são: {lista_b}")

# c. uma lista contendo apenas os elementos das posições pares;
for i in range(0, len(numeros), 2):
    lista_c.append(numeros[i])
print(f"Os números em posições pares são: {lista_c}")

# d. uma lista contendo apenas os elementos das posições ímpares;
for i in range(1, len(numeros), 2):
    lista_d.append(numeros[i])
print(f"Os números em posições ímpares são: {lista_d}")

# e. a lista inversa da lista sorteada (isto é, uma lista que começa com o último elemento da lista 
#    sorteada e termina com o primeiro);
lista_e = numeros.copy()
lista_e.reverse()
print(f"A lista invertida é: {lista_e}")

# f. uma lista inversa dos 5 primeiros números;
for i in range(0, 5):
    lista_f.append(numeros[i])
lista_f.reverse()
print(f"A lista inversa dos 5 primeiros números é: {lista_f}")

# g. uma lista inversa dos 5 últimos números.
for i in range(5, len(numeros)):
    lista_g.append(numeros[i])
lista_g.reverse()
print(f"A lista inversa dos 5 últimos números é: {lista_g}") """

## Resposta professor:

""" import random
numeros = random.sample(range(100), 10) # retorna uma lista de 10 elementos escolhidos aleatoriamente entre 0 e 99.
print("Lista completa:", numeros)
# a.  uma lista com os 4 primeiros números;
print("4 primeiros números:", numeros[:4])
# b.  uma lista com os 5 últimos números;
print("5 últimos números:", numeros[-5:])
# c.  uma lista contendo apenas os elementos das posições pares;
print("Posições pares:", numeros[::2])
# d.  uma lista contendo apenas os elementos das posições ímpares;
print("Posições ímpares:", numeros[1::2])
# e.  a lista inversa da lista sorteada (isto é, uma lista que começa com o último elemento da lista sorteada e termina com o primeiro);
print("Lista invertida:", numeros[::-1])
# f.  uma lista inversa dos 5 primeiros números;
print("Lista invertida dos 5 primeiros:", numeros[4::-1])
# g.  uma lista inversa dos 5 últimos números.
print("Lista invertida dos 5 ultimos:", numeros[:-6:-1]) """

# 12
# Faça um programa que sorteia 10 números entre 0 e 100 e conte quantos números sorteados são maiores que 50.
# Obs.: Precisa usar a biblioteca random

""" import random

numeros = []
contador = 0

for i in range(10):
    numeros.append(random.randint(0, 100))
    if numeros[i] > 50:
        contador +=1

print("Os números sorteados foram: ", numeros)
print(f"{contador} números são maiores que 50.") """

##Resposta professor:

""" numeros = random.sample(range(101), 10)
maior_que_50 = 0
for n in numeros:
    if n > 50:
        maior_que_50 += 1
print("números > 50 =", maior_que_50) """

# 13
# Faça um programa que sorteie 10 números entre 0 e 100 e imprima:
# a. o maior número sorteado;
# b. o menor número sorteado;
# c. a média dos números sorteados;
# d. a soma dos números sorteados.
# Obs.: Precisa usar a biblioteca random

""" import random

numeros = []

for i in range(10):
    numeros.append(random.randint(0, 100))

print("Os números sorteados são: ", numeros)
print("Lista dos números soretados ordenados: ",sorted(numeros))
print(f"O maior número é: {max(numeros)}")
print(f"O menor número é: {min(numeros)}")
print(f"A média dos números é: {sum(numeros) / len(numeros)}")
print(f"A soma dos números é: {sum(numeros)}") """

# 14
# Super Desafio - Faça um programa que pede para o usuário digitar o CPF e verifica se ele é válido. 
# Para isso, primeiramente o programa deve multiplicar cada um dos 9 primeiros dígitos do CPF pelos 
# números de 10 a 2 e somar todas as respostas. O resultado deve ser multiplicado por 10 e dividido 
# por 11. O resto dessa divisão deve ser igual ao primeiro dígito verificador (10º dígito). Em seguida, 
# o programa deve multiplicar cada um dos 10 primeiros dígitos do CPF pelos números de 11 a 2 e repetir 
# o procedimento anterior para verificar o segundo dígito verificador.
# Exemplo:
# Se o CPF for 286.255.878-87 o programa deve fazer primeiro:
# x = (2*10 + 8*9 + 6*8 + 2*7 + 5*6 + 5*5 + 8*4 + 7*3 + 8*2)
# Em seguida, o programa deve testar se x*10%11 == 8 (o décimo número do CPF). Se sim, o programa deve 
# calcular:
# x = (2*11 + 8*10 + 6*9 + 2*8 + 5*7 + 5*6 + 8*5 + 7*4 + 8*3 + 8*2)
# e verificar se x*10%11 == 7 (o décimo primeiro número do CPF).

""" cpf = ""
lista_cpf = []
x = 0
y = 0
multiplicador_x = 10
multiplicador_y = 11

while len(lista_cpf) != 11:
    cpf = input("Digite o número do CPF (somente números): ")
    #transformando a variável em lista
    lista_cpf = list(cpf)

#transformando a lista em int
for i in range(0, len(lista_cpf)):
    lista_cpf[i] = int(lista_cpf[i])
#print(f'Os números digitados foram: {lista_cpf}')

for i in range(0, 9):
    x = x + (lista_cpf[i] * multiplicador_x)
    multiplicador_x -= 1

if ((x * 10)%11) == lista_cpf[9]:
    #print((x * 10)%11)
    for i in range(0, 10):
        y = y + (lista_cpf[i] * multiplicador_y)
        multiplicador_y -= 1
    if ((y * 10)%11) == lista_cpf[10]:
        #print((y * 10)%11)
        print(f"\nO CPF {cpf} é válido.")
    else:
        print(f"O CPF {cpf} não é válido.")

else:
    print(f"O CPF {cpf} não é válido.")

print("\nFIM\n") """

## Resposta do professor:

""" CPF = list(input("Digite o seu CPF(apenas dígitos): "))  # Convertemos para uma lista de dígitos
for i in range(len(CPF)):
    CPF[i] = int(CPF[i])  # Convertemos a lista para inteiros
print(CPF)

soma = 0

for i in range(9):
    soma = soma + CPF[i]*(10-i)

if soma*10 % 11 == CPF[9]:
    soma = 0
    for i in range(10):
        soma = soma + CPF[i] * (11 - i)
    if soma*10 % 11 == CPF[10]:
        print("CPF Válido")
    else:
        print("CPF Inválido")
else:
    print("CPF Inválido") """
