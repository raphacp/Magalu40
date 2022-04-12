# Imprimir a tabuada do N

# N x 0
# N x 1
# N x 2
# ...
# N x 10

N = int(input("Digite o valor de N: "))

for contador in range(11): # 0, 1, 2, ... 10
    valor_da_tabuada = N * contador
    print(f"{N} x {contador} = {valor_da_tabuada}")