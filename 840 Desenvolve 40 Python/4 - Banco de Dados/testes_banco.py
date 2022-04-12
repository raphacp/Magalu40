# https://www.w3schools.com/python/python_mysql_insert.asp

import mysql.connector

# Cria conexão
# db_escola = mysql.connector.connect(
#   host="localhost",
#   user="root",
#   password="Cedes010"
# )
# print(db_escola)

# Cria a conexão e já conecta no banco selecionado
db_escola = mysql.connector.connect(
host="localhost",
user="root",
password="Cedes010",
database = "escola"
)
print(db_escola)

# Não sei o q faz
db_cursor = db_escola.cursor()

# # exibe os bancos
# db_cursor.execute("SHOW DATABASES")
# for x in db_cursor:
#     print(x)

# # exibe as tabelas
# db_cursor.execute("SHOW TABLES")
# for x in db_cursor:
#     print(x)

# Criar tabela
# mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")
# mycursor.execute("CREATE TABLE customers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")

# Alterar tabela
# mycursor.execute("ALTER TABLE customers ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")


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
# db_escola.commit()
# print(db_cursor.rowcount, "was inserted.")

# Deletar 1 linha
# sql = "DELETE FROM Aluno WHERE N_Matricula = 9"
# db_cursor.execute(sql)
# db_escola.commit()
# print(db_cursor.rowcount, "record(s) deleted")

# Deletar várias linhas
# sql = "DELETE FROM Aluno WHERE N_Matricula = %s"
# val = [[10], [11]]
# db_cursor.executemany(sql, val)
# db_escola.commit()
# print(db_cursor.rowcount, "record(s) deleted")

# Select
# db_cursor.execute("SELECT * FROM Aluno")
# myresult = db_cursor.fetchall()
# for x in myresult:
#     print(x)


db_cursor.close()
db_escola.close()
