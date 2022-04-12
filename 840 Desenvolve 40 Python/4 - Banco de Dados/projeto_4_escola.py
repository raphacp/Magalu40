import mysql.connector

conectado = False

# Conecta no banco
def conecta_banco():

    banco = input('Digite o nome do banco: ')
    usuario = input('Digite o nome do usuário do banco: ')
    senha = input('Digite a senha do usuário do banco: ')

    db_projeto = mysql.connector.connect(
    host="localhost",
    user=usuario,
    password=senha,
    # database = banco #Se o banco já existir pode ser usado para conectar direto
)
    global conectado
    conectado = True
    db_cursor = db_projeto.cursor()
    print(f'\nBanco {banco} conectado.')
    return db_projeto, db_cursor, banco


# Cria a conexão e já conecta no banco selecionado
def cria_banco():

    # Criei uma função só p conectar
    # db_projeto = mysql.connector.connect(
    #     host="localhost",
    #     user=usuario,
    #     password=senha,
    #     # database = banco #Se o banco já existir pode ser usado para conectar direto
    # )
    
    db_projeto, db_cursor, banco = conecta_banco()
    db_cursor = db_projeto.cursor()
    db_cursor.execute(f"CREATE DATABASE {banco}")
    print(f"\nO banco {banco} foi criado com sucesso.")
    
    # Tenativa de tratamento de erro. Se der tempo volto aqui p acertar
    # db_cursor.execute("SHOW DATABASES")
    # for x in db_cursor:
    #     print(x)
    #     if banco in x:
    #         print(f"Já existe um banco com o nome {banco}. Por favor selecione outro nome.")
    #     else:    
    #         # db_cursor.execute(f"CREATE DATABASE {banco}")
    #         print(f"O banco {banco} foi criado com sucesso.")

    return db_projeto, db_cursor


# Criar as tabelas
def cria_tabelas(db_projeto, db_cursor):
    db_cursor.execute(f"USE {db_projeto}") # seta o banco

    # Cria as tabelas
    db_cursor.execute("CREATE TABLE Aluno (CPF VARCHAR(15) NOT NULL, Nome VARCHAR(100) NOT NULL, Endereco VARCHAR(255) NOT NULL, Telefone VARCHAR(30) NOT NULL, Data_Nasc DATE, PRIMARY KEY (CPF))")
    db_cursor.execute("CREATE TABLE Departamento (Codigo INT NOT NULL AUTO_INCREMENT, Nome VARCHAR(255), PRIMARY KEY (Codigo))")
    db_cursor.execute("CREATE TABLE Curso (Codigo INT NOT NULL AUTO_INCREMENT, Nome VARCHAR(100) NOT NULL, Descricao VARCHAR(255), Codigo_Depto INT NOT NULL, PRIMARY KEY (Codigo), FOREIGN KEY (Codigo_Depto) REFERENCES Departamento(Codigo))")
    db_cursor.execute("CREATE TABLE Matricula (Codigo_Curso INT NOT NULL, CPF_Aluno VARCHAR(15) NOT NULL, Data_Matricula DATE, PRIMARY KEY (Codigo_Curso, CPF_Aluno), FOREIGN KEY (Codigo_Curso) REFERENCES Curso(Codigo), FOREIGN KEY (CPF_Aluno) REFERENCES Aluno(CPF))")
    db_cursor.execute("CREATE TABLE Professor (Matricula INT NOT NULL AUTO_INCREMENT, Nome VARCHAR(100), Endereco VARCHAR(255), Telefone VARCHAR(30), Data_Nasc DATE, Codigo_Depto INT, Data_Contratacao DATE, PRIMARY KEY (Matricula), FOREIGN KEY (Codigo_Depto) REFERENCES Departamento(Codigo))")
    db_cursor.execute("CREATE TABLE Disciplina (Codigo INT NOT NULL AUTO_INCREMENT, Nome VARCHAR(50) NOT NULL, Qtde_Creditos INT NOT NULL, Matricula_Prof INT, PRIMARY KEY (Codigo), FOREIGN KEY (Matricula_Prof) REFERENCES Professor(Matricula))")
    db_cursor.execute("CREATE TABLE Cursa (CPF_Aluno VARCHAR(15) NOT NULL, Codigo_Disc INT NOT NULL, PRIMARY KEY (CPF_Aluno, Codigo_Disc), FOREIGN KEY (CPF_Aluno) REFERENCES Aluno(CPF), FOREIGN KEY (Codigo_Disc) REFERENCES Disciplina(Codigo))")
    db_cursor.execute("CREATE TABLE Compoe (Codigo_Curso INT NOT NULL, Codigo_Disc INT NOT NULL, PRIMARY KEY (Codigo_Curso, Codigo_Disc), FOREIGN KEY (Codigo_Curso) REFERENCES Curso(Codigo), FOREIGN KEY (Codigo_Disc) REFERENCES Disciplina(Codigo))")
    db_cursor.execute("CREATE TABLE Pre_Req (Codigo_Disc INT NOT NULL, Codigo_Disc_Dependencia INT NOT NULL, PRIMARY KEY (Codigo_Disc, Codigo_Disc_Dependencia), FOREIGN KEY (Codigo_Disc) REFERENCES Disciplina(Codigo), FOREIGN KEY (Codigo_Disc_Dependencia) REFERENCES Disciplina(Codigo))")

    # exibe as tabelas
    print("As tabelas foram criadas com sucesso.")
    db_cursor.execute("SHOW TABLES")
    for x in db_cursor:
        print(x)


# Exibe os bancos
def exibe_bancos(db_projeto, db_cursor):

    db_cursor.execute("SHOW DATABASES")
    for x in db_cursor:
        print(x)

# # exibe as tabelas
# db_cursor.execute("SHOW TABLES")
# for x in db_cursor:
#     print(x)


# Inserir uma linha
# sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
# val = ("John", "Highway 21")
# mycursor.execute(sql, val)
# mydb.commit()
# print(mycursor.rowcount, "record inserted.")

# Inserir várias linhas
# sql = "INSERT INTO aluno VALUES (%s, %s, %s, %s, %s, %s)"
# val = [
#   (0, "Raphael Prado_1", "Rio de Janeiro", "rapha@email.com", "2187458954", 1),
#   (0, "Raphael Prado_2", "Rio de Janeiro", "rapha@email.com", "2187458954", 1),
#   (0, "Raphael Prado_3", "Rio de Janeiro", "rapha@email.com", "2187458954", 1),
# ]
# db_cursor.executemany(sql, val)
# db_projeto.commit()
# print(db_cursor.rowcount, "was inserted.")

# Select
# db_cursor.execute("SELECT * FROM Aluno")
# myresult = db_cursor.fetchall()
# for x in myresult:
#     print(x)


def solicita_valida_entrada():
    mensagem = '''
    1. Criar Banco de Dados no MySQL
    2. Cria as tabelas
    3. Conectar
    4. Exibe os bancos do seu ambiente
    5. Insere os dados nas tabelas
    0. Sair
    '''
    opcao = input(mensagem)
    
    while not opcao.isdigit() or int(opcao) < 0 or int(opcao) > 5:
        print("Opção digitada inválida. Digite novamente.")
        opcao = input(mensagem)
    opcao = int(opcao)

    return opcao

def menu():
    opcao = solicita_valida_entrada()
    while opcao != 0: # Sair
        if opcao == 1: # Criar Banco de Dados no MySQL
            # banco = input('Digite o nome do banco: ')
            # usuario = input('Digite o nome do usuário do banco: ')
            # senha = input('Digite a senha do usuário do banco: ')
            db_projeto, db_cursor = cria_banco()
            
        elif opcao == 2: # Cria as tabelas
            cria_tabelas(db_projeto, db_cursor)

            
        elif opcao == 3: # Conectar
            db_projeto, db_cursor, banco = conecta_banco()

            # try: # If
            #     len(matriz_gerada) == 0
            # except: # Caso ela não exista ainda
            #     print("Você deve executar a opcão 1 primeiro.")
            # else:
            #     print("\nEstatísticas da execução:")

                
        elif opcao == 4: # Exibe os bancos
            if conectado == False:
                db_projeto, db_cursor, banco = conecta_banco()
                exibe_bancos(db_projeto, db_cursor)
            else:
                exibe_bancos(db_projeto, db_cursor)

            # try:
            #     arq = open(caminho_log)
            # except: #FileNotFoundError:
            #     print('Erro: Arquivo de log não encontrado.\nExecute a opção 1 ao menos 1 vez.')
            # else:
            #     with open(caminho_log, encoding='UTF-8') as log:
            #         print(log.read())

        elif opcao == 5: # Conectar
            db_projeto, db_cursor, banco = conecta_banco()
            
        opcao = solicita_valida_entrada()

    print("Tchau, obrigado.\n")
    db_cursor.close()
    db_projeto.close()

menu()
