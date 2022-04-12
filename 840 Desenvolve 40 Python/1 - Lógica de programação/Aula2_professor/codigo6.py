numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
operacao = input("Escolha uma operação (+, -, *, /): ")

foi_invalido = False

if operacao == "+":
    resultado = numero1 + numero2
elif operacao == "-":
    resultado = numero1 - numero2
elif operacao == "*":
    resultado = numero1 * numero2
elif operacao == "/":
    resultado = numero1 / numero2
else:
    print("Operador inválido.")
    foi_invalido = True

if not foi_invalido:
    print(f"O resultado da operação é {resultado}")