# Tupla
# Tipo uma lista, mas é imutável

numeros = (1, 2, 3)
print(numeros)

# Unpacking "desempacotar"

a, b, c = numeros
print(a)
print(b)
print(c)

# var1 = 30
# var2 = 40

var1, var2 = (30, 40)
print(var1)
print(var2)

var1, var2 = 30, 40
print(var1)
print(var2)

tupla = (1, 2, 3, ['a', 'b'])
tupla[3][0] = 'x'
print(tupla)
