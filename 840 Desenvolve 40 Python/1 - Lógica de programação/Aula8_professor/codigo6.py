# Nomear parâmetros

def dividir(a, b):
    return a/b

# print(dividir(3, 5))
# print(dividir(a=3, b=5))
# print(dividir(b=5, a=3))
# print(dividir(3, b=5))

# **kwargs -> keyword args -> argumentos com chave // argumentos nomeados
def minha_funcao(var, **kwargs):
    print(var)
    print(kwargs)

    if "a" in kwargs:
        print(kwargs["a"])

    if "b" in kwargs:
        print(kwargs["b"])

# minha_funcao("oi", a=3, b=5, d=10)

# Função para calcular o preço final de um produto
# com base no valor do produto, frete, desconto, garantia estendida
# -> desconto e garantia serão opcionais com **kwargs

# 0 <= desconto <= 1
# preco = frete + garantia_estendida + valor - valor * desconto
# preco = frete + garantia_estendida + valor*(1-desconto)

def calcular_preco(valor, frete, **kwargs):
    preco = frete

    if "garantia_estendida" in kwargs:
        preco = preco + kwargs["garantia_estendida"]
    
    if "desconto" in kwargs:
        desconto = kwargs["desconto"]
        preco = preco + valor*(1-desconto)
    else:
        preco = preco + valor

    return preco

# print(calcular_preco(500, 50)) # 550
# print(calcular_preco(500, 50, desconto=0.2)) # 450
# print(calcular_preco(500, 50, desconto=0.2, garantia_estendida=70)) # 520
# print(calcular_preco(500, 50, garantia_estendida=70)) # 620

# Passar valores padrão para argumentos
def calcular_preco2(valor, frete, desconto=0, garantia_estendida=0):
    preco = frete + garantia_estendida + valor*(1-desconto)
    return preco

print(calcular_preco2(500, 50)) # 550
print(calcular_preco2(500, 50, 0.2)) # 450
print(calcular_preco2(500, 50, 0.2, 70)) # 520
print(calcular_preco2(500, 50, garantia_estendida=70)) # 620

