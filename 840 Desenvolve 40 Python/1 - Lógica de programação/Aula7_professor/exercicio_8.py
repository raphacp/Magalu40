# Faça uma função que recebe um número n de entrada, 
# sorteia n números aleatórios entre 0 e 100 e 
# retorna a média deles.

import random

def media_aleatorios(n):
    nums_aleatorios = []

    indice = 0
    while indice < n:
        num_sorteado = random.randint(0, 100)

        nums_aleatorios.append(num_sorteado)
        indice = indice + 1
    
    soma = 0
    for num_aleatorio in nums_aleatorios:
        soma = soma + num_aleatorio

    #soma = sum(num_aleatorios)

    # num_elementos = 0
    # for elemento in nums_aleatorios:
    #     num_elementos = num_elementos + 1

    media = soma / len(nums_aleatorios)
    return media

x = int(input("Digite quantos números quer sortear: "))

media = media_aleatorios(x)

print(media)