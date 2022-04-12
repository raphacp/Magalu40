def somar(a, b):
    resultado = a + b
    return resultado

def pedir_e_somar():
    num1 = int(input("informe um numero: "))
    num2 = int(input("informe outro numero: "))
    resultado = somar(num1, num2)
    return resultado

#print(somar(3, 5))
print(pedir_e_somar())