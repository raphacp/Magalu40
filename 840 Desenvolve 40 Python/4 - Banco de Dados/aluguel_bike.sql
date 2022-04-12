create database Aluguel_Bike;

use aluguel_bike;

create table Loja (
CNPJ varchar(14) not null,
Nome VARCHAR(60) NOT NULL,
Endereco VARCHAR(120) NOT NULL,
Telefone varchar(15) not null,
Email varchar(40) not null,
PRIMARY KEY (CNPJ)
);

create table Cliente (
CPF varchar(15) not null,
Nome VARCHAR(60) NOT NULL,
Endereco VARCHAR(120) NOT NULL,
Telefone varchar(15) not null,
Email varchar(40) not null,
PRIMARY KEY (CPF)
);

-- Esqueci de colocar a foreign key. Adicionei ela depois mas fiquei com medo de não estar certo
#create table Bicicleta (
#SN varchar(30),
#CNPJ_Loja varchar(14),
#Marca varchar(30),
#Tipo varchar(30)
#);

#alter table Bicicleta add FOREIGN KEY (CNPJ_Loja) REFERENCES Loja(CNPJ)

create table Bicicleta (
SN varchar(30),
CNPJ_Loja varchar(14),
Marca varchar(30),
Tipo varchar(30),
primary key (SN),
FOREIGN KEY (CNPJ_Loja) REFERENCES Loja(CNPJ)
);

ALTER TABLE Bicicleta ADD Disponibilidade BOOL;
ALTER TABLE Bicicleta ADD Cor varchar(50);
ALTER TABLE Bicicleta ADD Aro int;

create table Aluguel (
Id int not null auto_increment primary key,
DataInicio datetime,
DataFinal datetime,
Tipo enum("Hora", "Dia", "Semana"),
CNPJ_Loja varchar(14),
CPF_Cliente varchar(15),
FOREIGN KEY (CNPJ_Loja) REFERENCES Loja(CNPJ),
FOREIGN KEY (CPF_Cliente) REFERENCES Cliente(CPF)
);

create table Bicicletas_Aluguel (
Id_Aluguel int,
SN_Bicicleta varchar(30),
foreign key (Id_Aluguel) references Aluguel(Id),
foreign key (SN_Bicicleta) references Bicicleta(SN)
);