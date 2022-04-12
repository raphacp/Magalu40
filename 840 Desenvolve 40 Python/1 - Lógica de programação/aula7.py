##### Função dentro de função

# def somar(a, b):
#     resultado = a + b
#     return resultado

# def pedir_e_somar():
#     num1 = int(input("Digite um número: "))
#     num2 = int(input("Digite outro número: "))
#     resultado = somar(num1, num2)
#     return resultado

# #print(somar(3, 5))
# print(pedir_e_somar())

##### Recursão. A função chama ela mesma
# def fatorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * fatorial(n-1)

# print(fatorial(4))


##### Tuplas
# Tipo uma lista mas é imutável

# numeros = (1, 2, 3)
# print(numeros)

# ### Unpacking de tuplas (desempacotar)
# a, b, c = numeros
# print(a)
# print(b)
# print(c)

# #var1 = 30
# #var2 = 40

# var1, var2 = 30, 40
# # var1, _ = 30, 40 # Quando se quer pegar apensas um valor da tupla, é convenção colocar um _ para indicar 
# # q vc está ignorando aquele valor
# print(var1)
# print(var2)

# # Caso exista uma lista dentro da tupla é possível alterar a lista.
# tupla = (1, 2, 3, ['a', 'b'])
# print(tupla)
# tupla[3][0] = 'x'
# print(tupla)
# tupla = (1, 2, ['a', 'b']) # quando se atribui um novo valor p tupla, o python na verdade cria uma nova tupla e não muda a antiga. A antiga é descartada
# print(tupla)


# alunos_e_notas = {
#     "paulo": 8,
#     "matheus": 7,
#     "gabriela": 4.5,
#     "amanda": 9,
#     "ivan": 4,
#     "larissa": 7.5
# }

# def calcular_aprovacao(alunos_e_notas):
#     aprovados = []
#     reprovados = []
#     for aluno in alunos_e_notas:
#         nota = alunos_e_notas[aluno]
#         if nota >= 5:
#             aprovados.append(aluno)
#         else:
#             reprovados.append(aluno)
    
#     return aprovados, reprovados

# aprovados, reprovados = calcular_aprovacao(alunos_e_notas)
# print("Aprovados: ", aprovados)
# print("Reprovados: ", reprovados)


##### Criar uma função recebendo uma tupla de tamanho variável
# def somar(*numeros):
#     soma = 0
#     for numero in numeros:
#         soma = soma + numero
#     return soma

# print(somar(1, 2))
# print(somar(1, 2, 3))
# print(somar(1))
# print(somar(1, 2, 3, 4))

##### Extensão do .append()
##### Append que adiciona vários elementos de uma vez

# def adicionar_na_lista(lista, *args):
#     print(lista)
#     print(args)
#     for elemento in args:
#         lista.append(elemento)

# numeros = [1, 2, 3]
# adicionar_na_lista(numeros, 4, 5, 6)

# print(numeros)

# Passagem de parâmetros opcionais

# def dividir(a, b):
#     print(a)
#     print(b)
#     return a / b

#print(dividir(3, 5))
#print(dividir(a=3, b=5))
#print(dividir(b=5, a=3))
#print(dividir(3, b=5)) # pode passar o primeiro por posição e o segundo por nome
#print(dividir(b=5, 3)) #Não pode passar o primeiro por nome e o segundo por posição

# kwargs -> keyword args -> argumentos com chave // argumentos nomeados

# def minha_funcao(var, **kwargs):
#     print(var)
#     print(kwargs)

#     if "a" in kwargs:
#         print(kwargs["a"])
#     if "b" in kwargs:
#         print(kwargs["b"])

# print(minha_funcao("oi", a=1, b=2, d=5))

# 0 <= desconto <= 1
#preço = frete + garantia_estendida + valor - valor * desconto
#preço = frete + garantia_estendida + valor * (1-desconto)

def calcular_preco(valor, frete, **kwargs):
    preco = frete
    if "garantia_estendida" in kwargs:
        preco = preco + kwargs['garantia_estendida']
    if 'desconto' in kwargs:
        desconto = kwargs["desconto"]
        preco = preco + valor*(1-desconto)
    else:
        preco = preco + valor
    return preco

#print(calcular_preco(500, 50)) #550
#print(calcular_preco(500, 50, desconto=0.2)) #450
#print(calcular_preco(500, 50, desconto=0.2, garantia_estendida=70)) # 520
#print(calcular_preco(500, 50, garantia_estendida=70)) # 620

#### passar valores padrão para argumentos
def calcular_preco2(valor, frete, desconto=0, garantia_estendida=0):
    preco = frete + garantia_estendida + valor * (1-desconto)
    return preco

#print(calcular_preco2(500, 50)) #550
#print(calcular_preco2(500, 50, 0.2)) #450
#print(calcular_preco2(500, 50, 0.2, 70)) # 520
#print(calcular_preco2(500, 50, garantia_estendida=70)) # 620
