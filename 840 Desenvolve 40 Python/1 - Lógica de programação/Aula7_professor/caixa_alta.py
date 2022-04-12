# função que recebe uma lista de palavras e retorna uma lista contendo as mesmas palavras da lista anterior, mas escritas em caixa alta

def caixa_alta(palavras):
    palavras_caps = []

    for palavra in palavras:
        palavra_caps = palavra.upper()
        palavras_caps.append(palavra_caps)

    return palavras_caps
