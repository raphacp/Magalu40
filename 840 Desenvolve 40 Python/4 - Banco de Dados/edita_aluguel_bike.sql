-- Popular as tabelas de banco aluguel_bike

USE aluguel_bike;

-- Cliente (
-- CPF varchar(15) not null,
-- Nome VARCHAR(60) NOT NULL,
-- Endereco VARCHAR(120) NOT NULL,
-- Telefone varchar(15) not null,
-- Email varchar(40) not null,

INSERT INTO CLIENTE VALUES ("012345678995", "Pedro", "São Gonçalo", "2112345698", "pedro@email.com");
INSERT INTO CLIENTE VALUES ("023345678995", "Andrea", "Niterói", "2134345698", "andrea@email.com");
INSERT INTO CLIENTE VALUES ("034345678995", "Carla", "Barra", "2114345698", "carla@email.com");
INSERT INTO CLIENTE VALUES ("555345678995", "Humberto", "Copa", "2114345698", "raphasbike@email.com");

SELECT * FROM Cliente;

-- Loja (
-- CNPJ varchar(14) not null,
-- Nome VARCHAR(60) NOT NULL,
-- Endereco VARCHAR(120) NOT NULL,
-- Telefone varchar(15) not null,
-- Email varchar(40) not null,

INSERT INTO LOJA VALUES ("01234567000158", "Rapha's Bike", "São Gonçalo", "2199345698", "raphasbike@email.com");
INSERT INTO LOJA VALUES ("75634567000158", "Maria Cicle", "Friburgo", "2199345656", "mariacicle@email.com");
INSERT INTO LOJA VALUES ("11111111111111", "Aula", "Friburgo", "2199345656", "aula@email.com");

SELECT * FROM LOJA;

-- Bicicleta (
-- SN varchar(30),
-- CNPJ_Loja varchar(14),
-- Marca varchar(30),
-- Tipo varchar(30),
-- Disponibilidade Bool,
-- primary key (SN),
-- FOREIGN KEY (CNPJ_Loja) REFERENCES Loja(CNPJ)

INSERT INTO BICICLETA VALUES ("123456789AB", "01234567000158", "Caloi", "Street", NULL);
INSERT INTO BICICLETA VALUES ("483456789AB", "01234567000158", "Monark", "BMX", NULL);
INSERT INTO BICICLETA VALUES ("A33456789OL", "75634567000158", "Monark", "Mountain", NULL);
INSERT INTO BICICLETA VALUES ("F33456789RR", "75634567000158", "Caloi", "BMX", NULL);
INSERT INTO BICICLETA VALUES ("569456789AB", "01234567000158", "Caloi", "Street", NULL);

UPDATE BICICLETA SET Disponibilidade = TRUE WHERE SN = "123456789AB";
UPDATE BICICLETA SET Disponibilidade = FALSE WHERE SN = "483456789AB";
UPDATE BICICLETA SET Disponibilidade = TRUE WHERE SN = "A33456789OL";
UPDATE BICICLETA SET Disponibilidade = FALSE WHERE SN = "F33456789RR";

SELECT * FROM Bicicleta;

-- Aluguel (
-- Id int not null auto_increment primary key,
-- DataInicio datetime,
-- DataFinal datetime,
-- Tipo enum("Hora", "Dia", "Semana"),
-- CNPJ_Loja varchar(14),
-- CPF_Cliente varchar(15),

INSERT INTO ALUGUEL VALUES (0, "2022-03-21 10:15:28.000000", "2022-03-21 15:18:57.000000", "Hora", "01234567000158", "012345678995");
INSERT INTO ALUGUEL VALUES (NULL, "2022-03-22 10:15:28", "2022-03-24 15:18:57", "Dia", "01234567000158", "023345678995");
INSERT INTO ALUGUEL VALUES (NULL, "2022-03-22 08:15:28", "2022-03-30 18:18:57", "Semana", "75634567000158", "034345678995");
INSERT INTO ALUGUEL VALUES (NULL, "2022-03-31 12:28:54", NULL, "Dia", "75634567000158", "034345678995");

SELECT * FROM ALUGUEL;

-- Bicicletas_Aluguel (
-- Id_Aluguel int,
-- SN_Bicicleta varchar(30),
-- foreign key (Id_Aluguel) references Aluguel(Id),
-- foreign key (SN_Bicicleta) references Bicicleta(SN)

INSERT INTO Bicicletas_Aluguel VALUES ("1", "123456789AB");
INSERT INTO Bicicletas_Aluguel VALUES ("2", "F33456789RR");
INSERT INTO Bicicletas_Aluguel VALUES ("4", "F33456789RR");

SELECT * FROM Bicicletas_Aluguel;

-- **5)** Crie uma consulta com LEFT, RIGHT e INNER JOIN para buscar todas as bicicletas de todas as lojas, garanta que em seu banco você 
-- possui ao menos uma loja sem bicicletas. Como vieram os resultados? Quais as diferênças entre os JOINS? Por quê houveram (ou não houveram) 
-- diferenças?

-- SELECT a.Nome, t.Serie, t.Letra
-- FROM aluno a
-- INNER JOIN turma t
-- ON a.Id_Turma = t.Id
-- WHERE t.Serie = 1;

-- Exercício 5
SELECT * #SELECT b.SN, l.nome Loja, l.CNPJ
FROM bicicleta b
RIGHT JOIN loja l
ON b.CNPJ_Loja = l.CNPJ;

-- Exercício 6
-- SELECT * FROM bicicleta b WHERE b.disponibilidade = FALSE;
SELECT * FROM bicicleta b
right JOIN bicicletas_aluguel ba ON b.SN = ba.SN_Bicicleta
right JOIN aluguel a ON a.id = ba.id_aluguel
WHERE a.DataFinal IS NULL; 

-- Exercício 7
SELECT email FROM Cliente WHERE email IS NOT NULL
UNION
SELECT email FROM Loja WHERE email IS NOT NULL;

SELECT email FROM Cliente WHERE email IS NOT NULL
UNION ALL
SELECT email FROM Loja WHERE email IS NOT NULL;

-- Exercício 8
CREATE OR REPLACE VIEW alugueis_ativos_cliente AS
SELECT c.*, a.*
FROM Cliente c
INNER JOIN Aluguel a ON c.cpf = a.cpf_cliente
WHERE a.DataFinal IS NULL;

SELECT * FROM alugueis_ativos_cliente;

CREATE OR REPLACE VIEW alugueis_ativos_loja AS
SELECT l.*, a.*
FROM Loja l
INNER JOIN Aluguel a ON l.cnpj = a.cnpj_loja
WHERE a.DataFinal IS NULL;

SELECT * FROM alugueis_ativos_loja WHERE cnpj = '75634567000158';

CREATE OR REPLACE VIEW bicicleta_disp_loja AS
SELECT l.*, b.*
FROM Bicicleta b
INNER JOIN Loja l ON l.cnpj = b.cnpj_loja
WHERE b.disponibilidade = TRUE;

SELECT * FROM bicicleta_disp_loja WHERE cnpj = '01234567000158';

SELECT MAX(nome)
FROM cliente;

SELECT MIN(DataInicio)
FROM Aluguel;

SELECT cnpj_loja, SUM(aro), AVG(aro)
FROM bicicleta
GROUP BY cnpj_loja, aro;

SELECT l.nome, b.cor, COUNT(*) AS Contagem
FROM loja l
INNER JOIN bicicleta b ON b.cnpj_loja = l.cnpj
-- WHERE b.disponibilidade = TRUE
GROUP BY l.nome, b.cor;

SELECT b.aro, COUNT(*) AS Contagem
FROM bicicleta b
-- WHERE b.disponibilidade = TRUE
GROUP BY b.aro;

SELECT CAST(NOW() AS YEAR) AS Ano;
SELECT CAST('2022-01-02' AS DATETIME);

