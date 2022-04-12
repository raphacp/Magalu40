verdadeiro = True
falso = False

# Comparações
print(3 < 5)
print(3 > 5)
print(5 == 5)
print(5 > 5)
print(5 >= 5)
print(5 <= 5)
print(3 != 4) # Diferente

print("paulo" == "paulo") # True
print("paulo" == "matheus") # False

# Conjunções lógicas / operadores lógicos
# and, or, not

# and -> Só é verdade se as duas condições forem verdade
print(True and True) # True
print(True and False) # False
print(False and True) # False
print(False and False) # False

# Checar se um número está entre 3 e 10
numero = 11
print(numero > 3 and numero < 10)

# or -> Só é verdade se PELO MENOS uma condição for verdade
print(True or True) # True
print(True or False) # True
print(False or True) # True
print(False or False) # False

# not -> Inverter o valor lógico
print(not True)
print(not False)

# Checar se um número NÃO está entre 3 e 10
numero = 5
print(not(numero > 3 and numero < 10))

# Ou exclusivo -> Verdade se apenas um dos dois for verdade
print(True ^ True)
print(True ^ False)
print(False ^ True)
print(False ^ False)



