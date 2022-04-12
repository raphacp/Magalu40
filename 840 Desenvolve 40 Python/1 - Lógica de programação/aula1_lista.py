# 12/01/2022
# 1 Faça um programa que mostre a mensagem "Olá, mundo!" na tela.
""" print ("Olá, mundo!") """

# 2 Faça um programa que peça um número e mostre a mensagem "O número informado foi [número]".
""" numero = int(input("Digite um número: "))
print("O número informado foi:",numero) """

# 3 Faça um programa que peça um número para o usuário (string), converta-o para float e depois 
#   imprima-o na tela. Você consegue fazer a mesma coisa, porém convertendo para int?
""" numero = float(input("Digite um número: "))
print("O número informado foi:",numero)
print("O número informado foi:", int(numero)) """

# 4 Faça um programa que peça dois números inteiros e imprima a soma deles.
""" numero1 = int(input("Digite um número: "))
numero2 = int(input("Digite outro número: "))
soma = numero1 + numero2
print("A soma dos números é:",soma) """

# 5 Faça um programa que peça as 4 notas bimestrais de um aluno e mostre a média aritmética delas.
""" nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
nota4 = float(input("Digite a quarta nota: "))

media = (nota1 + nota2 + nota3 + nota4)/4
print("A sua média foi:", media) """

# 6 Faça um programa que peça o raio de um círculo, calcule e mostre sua área.
# Obs: Fórmula da área de um círculo: A = 3,14*(r**2), onde r é o raio.
""" raio = float(input("Digite o raio do círculo: "))
area = 3.14*(raio**2)
print("A área do círculo é: ", area) """

# 7 Faça um programa que pergunte quanto você ganha por hora e o número de horas trabalhadas 
# no mês e depois, calcule e mostre o total do seu salário no referido mês.
""" valor_hora = float(input("Digite o valor da hora: "))
qtd_hora = float(input("Digite a quantidade de horas trabalhadas no mês: "))
salario = valor_hora * qtd_hora

print(f"O total do seu salário no mês é de {salario} reais") """

# 8 Faça um programa que peça a temperatura em graus Fahrenheit (F), transforme e mostre a temperatura 
# em graus Celsius (°C).
# °C = (5 * (F-32) / 9)
# Obs: Tente também fazer um programa que faça o inverso: peça a temperatura em graus Celsius e a 
# transforme em graus Fahrenheit.
""" temperatura_fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))
temperatura_celsius = float(input("Digite a temperatura em Celsius: "))

temperatura_fahrenheit_celsius = (5 * (temperatura_fahrenheit-32) / 9)
temperatura_celsius_fahrenheit = ((temperatura_celsius * 9) / 5) + 32

print(f"A temperatura {temperatura_fahrenheit} ºF, corresponde à {temperatura_fahrenheit_celsius:.2f} ºC")
print(f"A temperatura {temperatura_celsius} ºC, corresponde à {temperatura_celsius_fahrenheit:.2f} ºF") """

# 9 Faça um programa que peça o dia, o mês e o ano para o usuário e imprima a data completa no formato 
# dd/mm/aaaa.
""" dia = int(input("Digite o dia: "))
mes = int(input("Digite o mês: "))
ano = int(input("Digite o ano: "))

print(f"A data que você digitou foi {dia}/{mes}/{ano}.") """

# 10 Faça um programa que peça 2 números inteiros e um número real, calcule e mostre:
# a) o produto do dobro do primeiro com metade do segundo.
# b) a soma do triplo do primeiro com o terceiro.
# c) o terceiro elevado ao cubo.

""" num_inteiro1 = int(input("Digite um número inteiro: "))
num_inteiro2 = int(input("Digite outro número inteiro: "))
num_real = float(input("Digite um número real: "))

questao_a = (num_inteiro1 * 2) * (num_inteiro2 / 2)
questao_b = (num_inteiro1 * 3) + num_real
questao_c = num_real ** 3

print(f"O produto do dobro de {num_inteiro1} com metade de {num_inteiro2} é igual a {questao_a}.")
print(f"A soma do triplo de {num_inteiro1} com {num_real} é igual a: {questao_b}.")
print(f"{num_real} elevado ao cubo é igual a {questao_c}.") """

# 11 Faça um programa que peça o peso e altura de uma pessoa e calcule seu IMC (Índice de Massa Corporal).
# Obs: IMC = Peso/Altura**2

""" peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))

imc = peso/(altura**2)

print(f"Seu IMC é {imc:.1f}.") """

# 12 Faça um programa que peça um valor monetário e aumente-o em 15%. Seu programa deve imprimir 
# a mensagem “O novo valor é [valor]”.

""" valor = float(input("Informe um valor monetário: "))

aumento = valor * 1.15

print (f"O novo valor é {aumento}.") """

# 13 Faça um programa que peça um valor monetário e diminua-o em 15%. Seu programa deve imprimir 
# a mensagem “O novo valor é [valor]”.

""" valor = float(input("Informe um valor monetário: "))

aumento = valor * 0.85

print (f"O novo valor é {aumento}.") """


# 14 Desafio 1 - Peça para o usuário digitar uma velocidade inicial (em m/s), uma posição inicial (em m) 
# e um instante de tempo (em s) e imprima a posição de um projétil nesse instante de tempo.
# Use a fórmula matemática:
# y(t) = y(0) + v(0)*t + (g*(t**2)/2)
# Onde, 
# y(0) é a posição inicial
# v(0) é a velocidade inicial
# t é o instante de tempo
# g é a aceleração da gravidade (-10m/s²)
# y(t) é a posição final

""" #g = -10 * -10
#print(g)

velocidade_inicial = int(input("Digite a velocidade inicial em m/s: "))
posicao_inicial = int(input("Digite a posição inicial em m: "))
instante_de_tempo = int(input("Digite um instante de tempo em s: "))

posicao = posicao_inicial + velocidade_inicial * instante_de_tempo + (-10 ** 2 * (instante_de_tempo ** 2) / 2)

print(f"A posição do projétil nesse instante de tempo é {posicao}.") """

# 15 Desafio 2 - Faça um programa que informe a data e a hora para o usuário. Para isso use a 
# função datetime.now() do módulo datetime.

""" from datetime import datetime

#print(datetime.now())
data_atual = datetime.now().strftime('%d/%m/%Y %H:%M')

print(f"\nA data atual é: {data_atual}.\n") """



