# Extensão do .append()
# Append que adiciona vários elementos de uma vez

def adicionar_na_lista(lista, *args):
    print(lista)
    print(args)
    for elemento in args:
        lista.append(elemento)

numeros = [1, 2, 3]
adicionar_na_lista(numeros, 4, 5, 6)

print(numeros)