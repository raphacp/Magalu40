# Cuidado ao "copiar" listas
numeros = [5, 2, 7]
outros_numeros = numeros # Não é cópia, é a mesma lista

# Altera as duas listas:
outros_numeros[0] = 100

print(numeros)
print(outros_numeros)

# Não precisa ter essa preocupação com números e strings
contador = 5
outro_contador = contador

# Altera somente o segundo contador:
outro_contador = outro_contador + 1

print(contador)
print(outro_contador)




