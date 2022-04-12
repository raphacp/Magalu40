def obter_dados():
    '''
    Essa função carrega os dados dos alunos e retorna uma lista de dicionários, onde cada dicionário representa um aluno.
    NÃO MODIFIQUE essa função.
    '''
    dados = [
        {
            "nome": "paulo",
            "nota": 8
        },
        {
            "nome": "matheus",
            "nota": 7
        },
        {
            "nome": "gabriela",
            "nota": 4.5
        },
        {
            "nome": "amanda",
            "nota": 9
        },
        {
            "nome": "ivan",
            "nota": 4
        },
        {
            "nome": "larissa",
            "nota": 7.5
        },
    ]
    return dados

def listar_aprovados(dados):
    '''
    O parâmetro "dados" deve ser uma lista de dicionários representando os alunos.
    Essa função deverá retornar uma lista contendo todos os alunos aprovados.    
    '''
    lista_aprovados = []
    for aluno in dados:
        if aluno["nota"] >= 5:
            lista_aprovados.append(aluno)

    return lista_aprovados

def listar_reprovados(dados):
    '''
    O parâmetro "dados" deve ser uma lista de dicionários representando os alunos.
    Essa função deverá retornar uma lista contendo todos os alunos aprovados.    
    '''
    lista_reprovados = []
    for aluno in dados:
        if aluno["nota"] < 5:
            lista_reprovados.append(aluno)

    return lista_reprovados

def menu(dados):
    '''
    O parâmetro "dados" deve ser uma lista de dicionários representando os alunos.
    Essa função deverá, em loop, realizar as seguintes ações:
    - Exibir as seguintes opções:
        1. Listar alunos aprovados
        2. Listar alunos reprovados
        0. Sair
    O loop encerra quando a opção do usuário for 0.
    '''

    mensagem = "1. Listar alunos aprovados\n2. Listar alunos reprovados\n0. Sair\n"
    opcao = int(input(mensagem))

    while opcao != 0:
        if opcao == 1:
            aprovados = listar_aprovados(dados)
            for aluno in aprovados:
                print(aluno)
        elif opcao == 2:
            reprovados = listar_reprovados(dados)
            for aluno in reprovados:
                print(aluno)

        opcao = int(input(mensagem))



# Programa Principal - não modificar!
d = obter_dados()
menu(d)