# Digite um número maior que 0
numero = int(input("Digite um número maior do que 0: "))

while numero <= 0:
    print("Entrada inválida.")
    numero = int(input("Digite um número maior do que 0: "))

print(numero)