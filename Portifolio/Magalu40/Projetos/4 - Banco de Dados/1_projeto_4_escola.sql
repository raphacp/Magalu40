-- Criação do banco de dados
CREATE DATABASE projeto_4_escola;

-- Selecionando o banco criado
USE projeto_4_escola;

-- Criação da tabela Aluno
CREATE TABLE Aluno(
CPF VARCHAR(15) NOT NULL,
Nome VARCHAR(100) NOT NULL,
Endereco VARCHAR(255) NOT NULL,
Telefone VARCHAR(30) NOT NULL,
Data_Nasc DATE,
PRIMARY KEY (CPF)
);

-- Criação da tabela Departamento
CREATE TABLE Departamento(
Codigo INT NOT NULL AUTO_INCREMENT,
Nome VARCHAR(255),
PRIMARY KEY (Codigo)
);

-- Criação da tabela Curso
CREATE TABLE Curso(
Codigo INT NOT NULL AUTO_INCREMENT,
Nome VARCHAR(100) NOT NULL,
Descricao VARCHAR(255),
Codigo_Depto INT NOT NULL,
PRIMARY KEY (Codigo),
FOREIGN KEY (Codigo_Depto) REFERENCES Departamento(Codigo)
);

-- Criação da tabela Matricula
CREATE TABLE Matricula(
Codigo_Curso INT NOT NULL,
CPF_Aluno VARCHAR(15) NOT NULL,
Data_Matricula DATE,
PRIMARY KEY (Codigo_Curso, CPF_Aluno),
FOREIGN KEY (Codigo_Curso) REFERENCES Curso(Codigo),
FOREIGN KEY (CPF_Aluno) REFERENCES Aluno(CPF)
);

-- Criação da tabela Professor
CREATE TABLE Professor(
Matricula INT NOT NULL AUTO_INCREMENT,
Nome VARCHAR(100),
Endereco VARCHAR(255),
Telefone VARCHAR(30),
Data_Nasc DATE,
Codigo_Depto INT,
Data_Contratacao DATE,
PRIMARY KEY (Matricula),
FOREIGN KEY (Codigo_Depto) REFERENCES Departamento(Codigo)
);

-- Criação da tabela Disciplina
CREATE TABLE Disciplina(
Codigo INT NOT NULL AUTO_INCREMENT,
Nome VARCHAR(50) NOT NULL,
Qtde_Creditos INT NOT NULL,
Matricula_Prof INT,
PRIMARY KEY (Codigo),
FOREIGN KEY (Matricula_Prof) REFERENCES Professor(Matricula)
);

-- Criação da tabela Cursa
CREATE TABLE Cursa(
CPF_Aluno VARCHAR(15) NOT NULL,
Codigo_Disc INT NOT NULL,
PRIMARY KEY (CPF_Aluno, Codigo_Disc),
FOREIGN KEY (CPF_Aluno) REFERENCES Aluno(CPF),
FOREIGN KEY (Codigo_Disc) REFERENCES Disciplina(Codigo)
);

-- Criação da tabela Compoe
CREATE TABLE Compoe(
Codigo_Curso INT NOT NULL,
Codigo_Disc INT NOT NULL,
PRIMARY KEY (Codigo_Curso, Codigo_Disc),
FOREIGN KEY (Codigo_Curso) REFERENCES Curso(Codigo),
FOREIGN KEY (Codigo_Disc) REFERENCES Disciplina(Codigo)
);

-- Criação da tabela Pre_Req
CREATE TABLE Pre_Req(
Codigo_Disc INT NOT NULL,
Codigo_Disc_Dependencia INT NOT NULL,
PRIMARY KEY (Codigo_Disc, Codigo_Disc_Dependencia),
FOREIGN KEY (Codigo_Disc) REFERENCES Disciplina(Codigo),
FOREIGN KEY (Codigo_Disc_Dependencia) REFERENCES Disciplina(Codigo)
);



