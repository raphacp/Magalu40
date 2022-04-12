# Listas e indexação

numeros = [10, 20, 30, 40, 50]
texto = ["uva", "banana", "gato", "bola"]
frutas = []

# print(numeros)
# print(texto)

# print(numeros[0])
# print(texto[1])

#Indexação negativa
# print(numeros[-1])
# print(texto[-2])

#Intervalo e salto (slice)
#print(numeros[1:4])
#print(numeros[0:4:2])

#Omitir valores nos intervalos
# print(numeros[1:])  # pega da segunda posição p frente
# print(numeros[:3])  # pega do começo até o 4
# print(numeros[:])   # pega a lista toda
# print(numeros[::2]) # pega tudo pulando de 2 em 2
# print(numeros[::-1]) # Inverte a lista somente no print. O .reverse inverte a lista mesmo.

# print(sorted(texto))
# print(texto)

# Não está copiando os valores para a variável, na verdade ele está só apontando para a mesma variável. Se mudar uma a outra muda também
# outros_numeros = numeros

# print(numeros)
# print(outros_numeros)

# #se alterar uma variável a outra tb muda pois as 2 apontam para o mesmo local
# numeros[0] = 100

# print(numeros)
# print(outros_numeros)

# # Utilizando o método copy ele realmente copia a variável e elas ficam independentes
# outros_numeros = numeros.copy()

# # alterando uma a outra não é alterada
# numeros[0] = 500

# print(numeros)
# print(outros_numeros)

# Append adiciona elemento no final da lista

# print(frutas)/
# frutas.append("laranja")
# print(frutas)
# frutas.append("maçã")
# print(frutas)

# Pop remove elemento do final da lista

# print(frutas)
# frutas.pop()
# print(frutas)
# frutas.pop()
# print(frutas)

# # Insert insere em uma determinada posição
letras = ["a", "b", "c","d"]
print(letras)
letras.insert(2, "x")
print(letras)

# # Pop remove pelo índice
# letras.pop(2)
# print(letras)

# # Remove remove pelo valor. A primeira ocorrência
# letras.remove("c")
# print(letras)

# Percorrer listas

# os 2 for fazem a mesma coisa, mas o primeiro vai pelo índice e o outro pelo valor
# for i in range(len(numeros)):
#     print(numeros[i])

# for i in numeros:
#     print(i)

# numero = 50
# print(f"O número é: {numero:03d}") #f-string Insere 0

# # Lista dentro de lista
# lista = [5, 2, 7, [10, 20]]
# print(lista[3][1])

