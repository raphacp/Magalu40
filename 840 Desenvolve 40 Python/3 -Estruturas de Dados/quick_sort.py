def particiona(lista, i_menor, i_maior):
    i = i_menor - 1
    pivo = lista[i_maior]

    for j in range(i_menor, i_maior):
        if lista[j] <= pivo:
            i += 1
            lista[i], lista[j] = lista[j], lista[i]

    lista[i+1], lista[i_maior] = lista[i_maior], lista[i+1]

    return i+1

def quick_sort(lista, i_menor, i_maior):
    if len(lista) == 1:
        return lista

    if i_menor < i_maior:
        indice = particiona(lista, i_menor, i_maior)
        
        quick_sort(lista, i_menor, indice-1)
        quick_sort(lista, indice+1, i_maior)

vetor = [3,1,2]
quick_sort(vetor, 0, len(vetor)-1)
vetor
