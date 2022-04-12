# Calcule a potência a^b
# Exemplo: 2^3 = 8
# 2^3 = 2*2*2 = 8

a = int(input("Digite o valor de a: "))
b = int(input("Digite o valor de b: "))

# 1*2*2*2 = 2*2*2 = 8
resultado = 1

#0, 1, 2, ... b-1
# b = 3 -> 0, 1, 2
for contador in range(b):
    resultado = resultado * a

print(resultado)

