# Método de listas (funções)

# Append (adiciona algo no final de uma lista)
frutas = []
print(frutas)
frutas.append("uva")
print(frutas)
frutas.append("morango")
print(frutas)

# Pop (remover algo do final da lista)
frutas.pop()
print(frutas)
frutas.pop()
print(frutas)

# Insert (insere em uma determinada posição)
letras = ['a', 'b', 'c', 'd']
#        ['a', 'b', 'x', 'c', 'd']
letras.insert(2, 'x')
print(letras)

# Pop (com parâmetro / remove por índice)
letras.pop(2)
print(letras)

# Remove (remove pelo valor)
letras.remove('c')
print(letras)

# Remove com valor repetido
outras_letras = ['a', 'b', 'c', 'c']
outras_letras.remove('c') # c b a

print(outras_letras)

# Substituindo por índice
letras = ['a', 'b', 'c']
letras[1] = 'x'
print(letras)

# Index (encontra o índice de um valor)
letras = ['a', 'b', 'c']
indice_da_letra_b = letras.index('b')
letras[indice_da_letra_b] = 'x'
print(letras)

# Sort (ordena a lista)
numeros = [5, 4, 9, 3]
numeros.sort()
print(numeros)


