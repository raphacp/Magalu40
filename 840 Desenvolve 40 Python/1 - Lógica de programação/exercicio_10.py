'''
Faça uma função que recebe duas listas e retorna a soma item a item dessas listas.

Exemplo: Se a função receber as listas [1,4,3] e [3,5,1], 
então a função deve retornar [1+3, 4+5, 3+1] = [4, 9, 4].
'''

def soma_itens(lista1, lista2):
    lista_de_somas = []
  
    indice = 0
    while indice < len(lista1):
        soma_dos_itens = lista1[indice] + lista2[indice]
        lista_de_somas.append(soma_dos_itens)
        indice = indice + 1

    return lista_de_somas

lista1 = [1,4,3]
lista2 = [3,5,1]

lista_com_somas = soma_itens(lista1, lista2)

print(lista_com_somas)