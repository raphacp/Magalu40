# Faça um programa que pergunte quanto você ganha por hora
# e o número de horas trabalhadas no mês e depois, calcule
# e mostre o total do seu salário no referido mês.

valor_por_hora = float(input("Quanto você ganha por hora? "))
horas_trabalhadas = float(input("Quantas horas você trabalhou no mês? "))

salario = valor_por_hora*horas_trabalhadas

print(f"O seu salário neste mês é de R${salario:.2f}.")

