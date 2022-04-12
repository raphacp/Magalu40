# demonstrando que podemos chamar uma função "dentro" da outra

# essa função conta os caracteres em um texto e retorna esse valor
def conta_chars(texto):
    qtd_chars = 0

    for char in texto:
        qtd_chars += char

# essa função imprime texto numa formatação pré-definida
def imprime_texto(texto):
    # na linha abaixo, note que chamamos a outra função!
    contagem_de_chars = conta_chars(texto)

    print(f'o texto informado tem {contagem_de_chars} caracteres.')
