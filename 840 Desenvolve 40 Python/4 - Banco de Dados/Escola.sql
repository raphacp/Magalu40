CREATE DATABASE Escola;

USE Escola;

CREATE TABLE Turma (
	Id INT NOT NULL AUTO_INCREMENT,
	Serie INT NOT NULL,
    Letra CHAR(1),
    Periodo ENUM("Matutino", "Vespertino", "Noturno", "Integral"),
    Sala VARCHAR(5),
	PRIMARY KEY (id)
);

CREATE TABLE Aluno (
	N_Matricula INT NOT NULL AUTO_INCREMENT,
	Nome VARCHAR(255) NOT NULL,
    Endereco VARCHAR(255) NOT NULL,
    Email VARCHAR(255),
    Contato_Responsavel VARCHAR(25) NOT NULL,
    TurmaID INT NOT NULL,
	PRIMARY KEY (N_Matricula),
    FOREIGN KEY (TurmaID) REFERENCES Turma(Id)
);

CREATE TABLE Professor (
	CPF VARCHAR(11) NOT NULL,
	Nome VARCHAR(255) NOT NULL,
    Endereco VARCHAR(255) NOT NULL,
	Disponibilidade ENUM("Matutino", "Vespertino", "Noturno", "Integral"),
	PRIMARY KEY (CPF)
);

CREATE TABLE Turma_Professor (
	CPF_Professor VARCHAR(11) NOT NULL,
	Id_Turma INT NOT NULL,
    Horarios TIME DEFAULT '00:00:00',
    FOREIGN KEY (CPF_Professor) REFERENCES Professor(CPF),
    FOREIGN KEY (Id_Turma) REFERENCES Turma(Id)
);