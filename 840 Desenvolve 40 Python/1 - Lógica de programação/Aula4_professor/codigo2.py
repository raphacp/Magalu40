# Indexação

numeros = [10, 20, 30, 40, 50]
#           0   1   2   3   4
#          -5  -4  -3  -2  -1

# Primeiro elemento da lista -> índice 0
print(numeros[0])
print(numeros[1])
...
print(numeros[4])

# Indexação negativa
print(numeros[-1])
print(numeros[-2])
...
print(numeros[-5])

# Selecionar intervalos (slice)
print(numeros[1:4])
print(numeros[0:4])
print(numeros[0:4:2])

# Omitir valores nos intervalos
print(numeros[2:]) # Pega do 2 pra frente
print(numeros[:3]) # Pega até o 2 (antes do 3)
print(numeros[:])  # Pega tudo
print(numeros[::2]) # Pula de 2 em 2 (lista inteira)
print(numeros[::-1]) # Inverter a lista

idade = 35
idades = [35, 50, 60, 40]

print(idades[::-1])


