USE escola;

INSERT INTO turma(Serie, Letra, Periodo) VALUES (3, "E", "Integral");
INSERT INTO turma VALUES (NULL, 1, "A", "Vespertino", "C-36");
INSERT INTO Turma VALUES(0, 2, "D", "Noturno", "F-'4");
INSERT INTO Turma VALUES(NULL, 2, "D", "Noturno", NULL);
UPDATE Turma SET Sala = "A-12" WHERE Id = 3;
UPDATE Turma SET Sala = "B-22" WHERE Id = 1;
UPDATE Turma SET Sala = "F-14" WHERE Id = 2;

SELECT * FROM 	Turma;
DELETE FROM TURMA WHERE Id = 8;

INSERT INTO Aluno VALUES(0, "Raphael Prado", "Rio de Janeiro", "rapha@email.com", "2187458954", 1);
INSERT INTO Aluno VALUES(0, "Karen Arent", "São Paulo", "karen@email.com", "219215458954", 2);
INSERT INTO Aluno VALUES(0, "Eduardo Silva", "Minas Gerais", "eduardo@email.com", "213456458954", 2);
INSERT INTO Aluno VALUES(0, "André Nunes", "Minas Gerais", "andre@email.com", "213456458954", 3);
INSERT INTO Aluno VALUES(0, "Givaldo Pereira", "Paraná", "givaldo@email.com", "213456458954", 3);

SELECT * FROM ALUNO;
SELECT * FROM ALUNO WHERE endereco = "Minas Gerais";
SELECT * FROM ALUNO WHERE endereco LIKE "M%";
SELECT * FROM ALUNO WHERE endereco LIKE "%R%";

INSERT INTO PROFESSOR VALUES ('12345678956', "Chico", "Copacabana", "Integral");
INSERT INTO PROFESSOR VALUES ('45345678956', "Antônio", "Barra", "Integral");
INSERT INTO PROFESSOR VALUES ('89345678956', "Silva", "Vitória", "Matutino");

SELECT * FROM PROFESSOR;

INSERT INTO Turma_Professor VALUES ("12345678956", 1, "07:00:00");
INSERT INTO Turma_Professor VALUES ("12345678956", 2, "13:00:00");
INSERT INTO Turma_Professor VALUES ("12345678956", 3, "18:00:00");
INSERT INTO Turma_Professor VALUES ("45345678956", 3, "08:00:00");
INSERT INTO Turma_Professor VALUES ("45345678956", 2, "10:00:00");
INSERT INTO Turma_Professor VALUES ("89345678956", 1, "10:00:00");
INSERT INTO Turma_Professor VALUES ("89345678956", 3, "07:00:00");

SELECT * FROM Turma_Professor;

-- Exemplos do professor
-- SELECT p.NOME, t.Serie, t.Letra FROM Professor p, Turma t, professor_turma pf WHERE p.CPF = pf.CPF_Professor AND t.id = pf.Id_Turma;
-- SELECT ALUNO.Nome, TURMA.Serie, TURMA.Letra FROM ALUNO, TURMA WHERE TURMA.Id = ALUNO.Id_Turma;