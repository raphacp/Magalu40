# Funções

# def imprime_nome():
#     print('Rapha')

# imprime_nome()

# def soma_dois(num):
#     somou_dois = num + 2
#     return somou_dois

# x = soma_dois(42)
# print(x)

import random

def media_aleatorios(n):
    nums_aleatorios = []
    indice = 0
    while indice < n:
        num_sorteado = random.randint(0, 100)
        nums_aleatorios.append(num_sorteado)
        indice += 1

    media = sum(nums_aleatorios)/len(nums_aleatorios)
    print(nums_aleatorios)
    print(sum(nums_aleatorios))
    print(len(nums_aleatorios))
    return media

media = media_aleatorios(5)
print(media)
