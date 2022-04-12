# Imprimir as tabuadas de 2 até 10

for N in range(2, 11): # 2, 3, 4, ..., 10
    print(f"\n Tabuada do {N} \n")
    for contador in range(11):
        valor_da_tabuada = N * contador
        print(f"{N} x {contador} = {valor_da_tabuada}")