# Operador de unpacking
# *

tupla = ("Olá", "tudo bem?")
print(tupla) # print(("Olá", "tudo bem?"))
print(*tupla) # print("Olá", "tudo bem?")

# Como passar uma quantidade variável de argumentos
# para uma função
print('oi', 'olá', 'tchau', 'como vai', 'palavra')

# Função para somar números
# somar(1, 2) = 3
# somar(1, 2, 3) = 6
# somar(1) = 1
# somar(1, 2, 3, 4) = 10

# *args -> argumentos (arguments)
def somar(*numeros):
    soma = 0
    for numero in numeros:
        soma = soma + numero
    return soma

print(somar(1, 2))
print(somar(1, 2, 3))
print(somar(1))
print(somar(1, 2, 3, 4))
