-- Consultas do projeto 4
-- 1 Produza um relatório que contenha os dados dos alunos matriculados em todos os cursos oferecidos pela escola
-- 2 Produza um relatório com os dados de todos os cursos, com suas respectivas disciplinas, oferecidos pela escola
-- 3 Produza um relatório que contenha o nome dos alunos e as disciplinas em que estão matriculados
-- 4 Produza um relatório com os dados dos professores e as disciplinas que ministram
-- 5 Produza um relatório com os nomes das disciplinas e seus pré-requisitos
-- 6 Produza um relatório com a média de idade dos alunos matriculados em cada curso
-- 7 Produza um relatório com os cursos oferecidos por cada departamento

USE projeto_4_escola;

-- 1 Produza um relatório que contenha os dados dos alunos matriculados em todos os cursos oferecidos pela escola
# SELECT c.Nome Curso, a.*
SELECT c.Nome Curso, a.Nome Aluno, a.CPF, a.Endereco, a.Telefone, a.Data_Nasc #Resolvi colocar os campos manualmente só p poder trocar a ordem e o nome vir antes do CPF
FROM Aluno a, Curso c, Matricula m 
WHERE m.CPF_Aluno = a.CPF AND m.Codigo_Curso = c.Codigo 
ORDER BY c.Nome ASC, a.Nome ASC

-- ************ RESULTADO ************
-- Curso,Aluno,CPF,Endereco,Telefone,Data_Nasc
-- Alemão,"Alexandre Humberto Pinhão de Cerqueira Usago",55775324274,"063 Douglas Stravenue",+55-11-94512-1245,1983-11-21
-- Alemão,"Dionísio Cirilo Weiss Lole",34123567630,"057 Felicia Plains Apt. 273",+1-084-098-0852,1980-01-04
-- Alemão,"Edson Coso",71841727055,"1531 Brown Motorway",+1-320-216-2073x6487,1975-05-21
-- Alemão,"Gisele Rosatto",73645095255,"085 Christopher Manors",+1-132-406-7601,2003-03-17
-- Alemão,"Helena Gois Creti",66497186863,"0721 Ho Flat Apt. 522",+55-11-98844-2645,1976-09-28
-- Alemão,"Ivanete Mirela Tsuyupeka",62923232666,"0685 Jackson Ferry Apt. 908",+55-63-97788-8877,1992-12-01
-- Alemão,"Joelma de Brandão",71491051654,"14956 Brown Knolls",+1-308-457-3135x0137,2004-07-07
-- Alemão,"Jorge Walter Mili Alkenumi Júnior",84432343161,"2382 Trevor Shore Suite 669",+1-699-041-8342x500,1964-12-13
-- Alemão,"Josilda Nair Lyphornson",22558877441,"03367 Briggs Wall",+1-046-659-3776x382,2009-04-17
-- Alemão,"Paula Eztrern",70789700852,"144 Hicks Ports",+1-292-141-1784x1818,1982-10-07
-- Alemão,"Roberval da Cunha de Tavares",69242576334,"22953 Michael Mountains Suite 782",+1-629-612-7735x0573,1932-01-14
-- Alemão,"Victor de Medeiros d"Ávila Ecifoson",43926298300,"19899 Amber Groves Suite 120",+1-502-017-3863x00019,1980-09-04
-- "Ciência da Computação","Abílio Jânio Joepa",69737674648,"14263 Garcia Mission Apt. 814",+1-280-314-4845x866,2004-06-09
-- "Ciência da Computação","Ali de Magalhães",65867072600,"22319 Lynch Summit",+1-624-303-3807x7302,1979-05-18
-- "Ciência da Computação","Brenda de Junqueira",71140376253,"144 Hogan Loaf",+1-306-897-1768x3145,1939-08-04
-- "Ciência da Computação","Danielle Kiean Durirna",01861002026,"1729 Travis Port Suite 555",+1-436-204-0218x93143,1942-05-22
-- "Ciência da Computação","David Meynyorn",69386999246,"139 Hutchinson Junctions",+1-268-776-5272x81605,2005-04-12
-- "Ciência da Computação","Eduardo Nepanegi",79369087553,"237 Mark Park Apt. 909",+1-680-479-7414x295,1939-08-09
-- "Ciência da Computação","Humberto Mike de Uchôa",27048779600,"17858 Heidi Underpass",+1-454-626-5519x56950,2001-06-16
-- "Ciência da Computação","Jackson Jorge Suwoga",69036323845,"13850 Good Motorway",+1-262-563-8517,2004-01-16
-- "Ciência da Computação","Jonas Fred Rangel",72618080077,"2311 Ann Courts Apt. 922",+1-665-515-9977x273,1982-12-22
-- "Ciência da Computação","Josiel de Alvim",17780734413,"05422 Grant Skyway",+1-083-864-2840x9744,1976-04-20
-- "Ciência da Computação","Lili Terezinha da Silva",67554824469,"2272 Bell Walk",+1-627-528-4315,1958-05-01
-- "Ciência da Computação","Manoel Charles de Trindade Penedo",02928272625,"0939 Jeff Trail Suite 414",+1-150-081-6101,1978-08-29
-- "Ciência da Computação","Mel Naves de Vasconcelos",58157960405,"06390 Ashley Forks Apt. 050",+55-11-98989-8989,1966-07-05
-- "Ciência da Computação","Paulo de Holanda do Espírito Santo Júnior",50677305777,"2076 Earl Fork Suite 238",+1-517-869-1890x06854,2009-11-06
-- "Ciência da Computação","Quésia Amoã",71262459124,"081 Figueroa Corners Apt. 472",+1-113-947-0116,1979-06-23
-- "Ciência da Computação","Samara Risme do Vale",21985524001,"1757 John Inlet Suite 690",+1-442-899-0937x509,1987-10-06
-- "Ciência da Computação","Selma Fortes",56966642339,"0633 Patrick Drives Apt. 420",+55-11-91616-1677,1948-10-09
-- "Ciência da Computação","Sheila Ocuã",11122233344,"012 Elizabeth Stravenue Apt. 349",+55-22-97777-1212,1994-01-29
-- "Ciência da Computação","Thiago Leandro do Rio de Souza",86120095098,"23836 Morales Avenue Apt. 703",+1-712-156-1000x894,2007-06-01
-- "Ciência da Computação","Willian Martin Arno",50466400847,"05839 Thompson Rue",+1-084-892-5501x680,1938-08-31
-- "Engenharia Elétrica","Abílio Jânio Joepa",69737674648,"14263 Garcia Mission Apt. 814",+1-280-314-4845x866,2004-06-09
-- "Engenharia Elétrica","Bento Frias",51010052012,"060 Stewart Branch",+55-86-96667-7776,2004-07-10
-- "Engenharia Elétrica","Itamar de Carvalho Júnior",77219049451,"0934 Lee Valley",+1-145-545-9941x096,1932-01-14
-- "Engenharia Elétrica","Jonas Fred Rangel",72618080077,"2311 Ann Courts Apt. 922",+1-665-515-9977x273,1982-12-22
-- "Engenharia Elétrica","Melanie Vânia de Camargo da Rocha",67688504928,"0787 Stephens Plaza",+55-11-93333-0011,2000-03-19
-- "Engenharia Elétrica","Ney de Toledo Sanches",72543077858,"1624 Amber Point Suite 348",+1-366-174-2909x7141,1956-02-18
-- "Engenharia Elétrica","Quésia Amoã",71262459124,"081 Figueroa Corners Apt. 472",+1-113-947-0116,1979-06-23
-- "Engenharia Elétrica","Simão de Fraga Neto",70071141059,"079 Suzanne Stream",+55-11-97667-5455,1963-07-08
-- "Engenharia Elétrica","Terezinha Bise de Araújo Finanatiov",33799787085,"1892 Cory Village",+1-469-353-6174x2359,1961-04-20
-- Espanhol,"Ana de Moreira",38863042693,"193 Anthony Tunnel",+1-475-436-9174x158,1942-04-17
-- Espanhol,"Bartolomeu Otaviano de Ferraz",77681335684,"2353 Andrew Inlet Suite 652",+1-671-746-2629x546,2000-04-18
-- Espanhol,"Gisele Rosatto",73645095255,"085 Christopher Manors",+1-132-406-7601,2003-03-17
-- Espanhol,"Isaías Hamilton da Silva",68685648444,"138 Smith Streets Apt. 492",+1-255-321-3202x867,1931-11-03
-- Espanhol,"Joelma de Brandão",71491051654,"14956 Brown Knolls",+1-308-457-3135x0137,2004-07-07
-- Espanhol,"Mário Frederico Ovrilso",67984297641,"137 Goodwin Parks",+1-252-863-7092x9337,1997-04-07
-- Espanhol,"Mateus Rodrigues Guedes Npo",48989553908,"205 Sarah Loop",+1-517-737-7246,1936-08-09
-- Espanhol,"Milene Selma dos Pinhais de Moura Banhos",32112035216,"18266 Chelsea Mountains",+1-468-874-6602x132,1970-11-21
-- Espanhol,"Mônica Fabiana Prates",61731914601,"068 Ruth Ridges",+55-69-91111-6666,1965-08-13
-- Espanhol,"Paula Eztrern",70789700852,"144 Hicks Ports",+1-292-141-1784x1818,1982-10-07
-- Espanhol,"Wendy Tatiana Mercado de Menezes",43424140187,"10518 Anthony Freeway",+1-167-077-3027x220,1938-04-29
-- Espanhol,"Yasmin Banhos",57428313254,"2117 Randy Lights",+1-556-408-9360,1977-08-16
-- Espanhol,"Zara de Angola",62491568861,"219 Gonzalez Valley",+1-581-097-0378,1992-07-09
-- Estatística,"Abigail Dlantroz",10468536559,"256 Crawford Throughway",+1-777-030-3784x73761,1993-12-28
-- Estatística,"Ana Moreno",59349278470,"0669 Hill Heights Apt. 171",+55-11-92233-4455,1981-02-07
-- Estatística,"Bárbara Felícia Robitako",31914223344,"160 Leslie Rue Apt. 353",+1-344-733-4444x1671,1984-03-08
-- Estatística,"Beatriz Sônia Ublavi da Rocha",60803816994,"21627 David Neck",+1-577-835-7565x573,1981-01-23
-- Estatística,"Gisele de Meireles",66809234064,"05951 Jenkins Crossing Suite 446",+1-088-816-9973x2987,1972-11-24
-- Estatística,"Leandro Augusto de Paranhos Amernma Tristão",22233344455,"028 Kenneth Locks",+55-11-91413-1213,2000-09-16
-- Estatística,"Quirino Martinez da Silva Neienason",68879822993,"0789 Meza Fork",+55-11-91212-1179,1961-07-04
-- Estatística,"Reinaldo Murilo da Silva",99141819171,"09633 Baker Square",+1-154-623-3842x183,1930-03-26
-- Estatística,"Robson Drynom Freire Júnior",85095067979,"05080 Travis Shores",+1-082-745-7709x4741,2005-08-04
-- Estatística,"Rogério Lowimirnian",35467646557,"167 Jeremy Throughway Suite 209",+1-396-537-7355,1947-06-10
-- Estatística,"Sandra Paulínia Canam",20297772132,"1752 Monica Ranch",+1-440-687-8070,1963-02-13
-- Estatística,"Xerxes do Paraná",57585758579,"1100 Daniel Gardens Apt. 024",+1-171-628-8431x350,1993-04-25
-- Finanças,"Albino Nicolas de Gimenes",92871102507,"247 Vaughn Shores",+1-741-371-8090x165,2009-06-27
-- Finanças,"Ângelo Izcunarn",55740561385,"21067 Laurie Pike",+1-550-416-5992,2004-08-07
-- Finanças,"Bárbara Felícia Robitako",31914223344,"160 Leslie Rue Apt. 353",+1-344-733-4444x1671,1984-03-08
-- Finanças,"Damares Célia de Martins Eclaovi da Silva",35487538954,"1908 Kevin Roads Suite 490",+1-472-989-2332x1398,1995-09-26
-- Finanças,"Leni Xaetreu",68334973043,"13734 Margaret Point",+1-254-970-1261,2001-05-03
-- Finanças,"Quirino Martinez da Silva Neienason",68879822993,"0789 Meza Fork",+55-11-91212-1179,1961-07-04
-- Finanças,"Sandro Waei Mendes de Britto",76027731386,"08924 Raymond Run Suite 652",+1-135-928-1213,1938-03-01
-- Finanças,"Úrsula de Angola Heijira",67633622240,"1356 Watson Estate",+1-251-042-1324x74675,1954-02-09
-- Francês,"Bete Rute Pede",64114550732,"069 Brittany Points Suite 047",+55-92-98080-7070,1982-12-02
-- Francês,"Elano Augusto Irnsitli",47301802039,"2024 Huff Union Apt. 574",+1-511-445-0713x65770,1981-05-11
-- Francês,"Eustáquio Itysson",65529569832,"12544 Byrd Extensions Suite 786",+1-194-494-9092,1982-08-09
-- Francês,"Oliver Pires Nago",65178894431,"12373 Henry Streets",+1-192-776-1029x206,1933-07-02
-- Francês,"Roberval de Amorim Drouzcos",23673275870,"176 Annette Run",+1-443-253-1363x736,1932-04-01
-- Francês,"Rosana Talita de Alvarenga",66932271437,"1338 Heidi Glen Suite 479",+1-208-995-2035x0440,1954-11-19
-- Francês,"Viviane Larissa de Sampaio",65880245234,"132 Jessica Forge",+1-199-656-5893x5963,1998-04-19
-- "Gestão Comercial","Ana Dilma Phachuzsay",40550794562,"1946 Glenn Spur",+1-492-068-3719x2665,1997-06-19
-- "Gestão Comercial","Carlos dos Santos Júnior",37175290824,"1909 Kimberly Inlet",+1-473-912-7616x111,1955-03-08
-- "Gestão Comercial","Fabiana Dina de Melo",74836413320,"0860 Melinda Drive",+1-135-526-1698x670,1965-04-11
-- "Gestão Comercial","Ingrid de Angola Barroso",66230920635,"133 Peck Streets Suite 250",+1-203-609-6202x9171,1939-02-19
-- "Gestão Comercial","Ismael de Soares Júnior",30424283347,"180 Michelle Stream",+1-462-851-0359,1943-10-02
-- "Gestão Comercial","Israel de Assunção Pimenta",33355599988,"04462 Lisa Ferry",+1-076-939-0979x819,1960-10-03
-- "Gestão Comercial","José Mourão",52201370078,"06127 Woods Plains Suite 176",+55-11-99000-0099,1997-01-03
-- "Gestão Comercial","Karin Luciana de Antunes Pinhão",87807846899,"2391 Tyler Crest Suite 791",+1-713-808-6087x888,1957-07-19
-- "Gestão Comercial","Marcelo de Barbosa",15234516524,"16736 Kelly Crest Suite 119",+1-419-551-1054x5276,1996-05-28
-- "Gestão Comercial","Neila da Silva",65305868797,"072 Hall Mountain Apt. 224",+55-11-95050-4039,1947-08-31
-- "Gestão Comercial","Olímpia de Chaves Sasenabu",72192402457,"15416 Mitchell Common Suite 092",+1-334-299-9934,1995-02-18
-- "Gestão Comercial","Otaviano Marcelo de Carvalho",72453777190,"08396 James Grove Suite 681",+1-131-998-5104x74347,1944-07-09
-- "Gestão de RH","Antônio Oeulu",82744591292,"23751 Cox Terrace Apt. 161",+1-693-275-7418x39092,1996-03-23
-- "Gestão de RH","Dionísio Kim de Oliveira Fragoso Júnior",70088350049,"14316 Wilson Spring",+1-288-466-3628x503,1967-08-27
-- "Gestão de RH","Edu Arnaldo Mineiro Cuminnas Towateho",96246606245,"24779 Cheryl Ferry",+1-756-239-9210x20911,1965-04-22
-- "Gestão de RH","Eliomar Suzanne de Moura",12345678977,"030 Michael Curve Suite 017",+55-13-91111-0004,1981-06-20
-- "Gestão de RH","Gisele do Amaral de Malta",53392688143,"062 James Shore",+55-11-91615-0102,1983-07-14
-- "Gestão de RH","Joyce Aparecida da Silva",42238546431,"1983 Butler Stravenue Apt. 453",+1-499-706-7459,1951-01-16
-- "Gestão de RH","Karina dos Santos",70439025450,"1432 Sarah Curve",+1-289-520-9893,1990-05-26
-- "Gestão de RH","Laerte Ederson Moreno",59116065123,"21391 Cory Oval Apt. 436",+1-568-572-5795x75520,1954-10-26
-- "Gestão de RH","Marciano de Bezerra Buarque Oeyser",62626255555,"1121 Phyllis Gateway",+1-187-288-6080x3141,1950-02-21
-- "Gestão de RH","Marielle da Serra",81056839422,"237 Richardson Ford Suite 476",+1-684-625-2006,2008-12-29
-- "Gestão de RH","Otávio Gilmar de Alves Nirnofezsen Inau Júnior",52365057644,"20778 John Ramp",+1-526-762-4872x8157,1964-04-11
-- "Gestão de RH","Raiane da Luz Gutierrez de Borges",74174171444,"044 Rachel Falls Suite 789",+1-067-145-4362x6407,1968-07-25
-- "Gestão de RH","Roberta de Oliveira Ximenes",74305831946,"23149 Jessica Ranch Apt. 613",+1-667-191-4271x344,1965-05-12
-- "Gestão de RH","Soraya Brides Liuviã",98598598598,"101 Kelly Isle",+1-165-321-9382x226,1939-04-22
-- "Gestão de RH","Suely Daniela Cavalcante",54052809516,"210 Austin Bridge",+1-538-141-7604x105,1959-10-29
-- Inglês,"Alfredo Anderson de Barros",10130986185,"250 Carroll Road",+1-770-767-4254,2001-02-01
-- Inglês,"Altair de Pereira Isbi Muchol",44445555665,"161 Monica Way",+1-361-446-5011,1970-03-18
-- Inglês,"Ana de Barbosa",94558854373,"24762 Tina Cliff Suite 930",+1-741-938-9637x9318,1937-05-20
-- Inglês,"Avelino Abirner Neto",97934358114,"2488 Davis Mills",+1-764-358-8611,1938-07-18
-- Inglês,"Bianca Maria dos Santos",05020555555,"0206 Sanford Ford",+55-61-94444-3311,1993-03-04
-- Inglês,"Brenda de Junqueira",71140376253,"144 Hogan Loaf",+1-306-897-1768x3145,1939-08-04
-- Inglês,"Daniela Rute de Tozetto",21212121212,"159 Bailey Cove",+1-340-310-5929x8290,1945-03-01
-- Inglês,"David Meynyorn",69386999246,"139 Hutchinson Junctions",+1-268-776-5272x81605,2005-04-12
-- Inglês,"Dionísio Cirilo Weiss Lole",34123567630,"057 Felicia Plains Apt. 273",+1-084-098-0852,1980-01-04
-- Inglês,"Edson Coso",71841727055,"1531 Brown Motorway",+1-320-216-2073x6487,1975-05-21
-- Inglês,"Hamilton Gunoi Martinez",25361027740,"177 Davis Fields",+1-449-235-2333x560,1975-09-15
-- Inglês,"Humberto Mike de Uchôa",27048779600,"17858 Heidi Underpass",+1-454-626-5519x56950,2001-06-16
-- Inglês,"Ismael de Soares Júnior",30424283347,"180 Michelle Stream",+1-462-851-0359,1943-10-02
-- Inglês,"Israel de Assunção Pimenta",33355599988,"04462 Lisa Ferry",+1-076-939-0979x819,1960-10-03
-- Inglês,"Jackson Jorge Suwoga",69036323845,"13850 Good Motorway",+1-262-563-8517,2004-01-16
-- Inglês,"João Cléber da Silva",68752234762,"04476 Cheryl Camp Apt. 802",+1-079-376-9912,1953-09-24
-- Inglês,"Juliano de Diniz Esluyer Anuneson",75993583815,"23381 Roy Hollow Apt. 749",+1-668-107-5214,1985-11-09
-- Inglês,"Kauê Albafriov",91183350638,"24622 Rodgers Rapid Apt. 751",+1-726-416-1130x3829,1958-11-03
-- Inglês,"Meire Amanda de Osório da Silva",28736531478,"1791 Caldwell Centers Suite 237",+1-460-452-2517x411,1961-02-28
-- Inglês,"Moisés Fontes de Machado",45614050170,"20184 Crawford Mews Apt. 328",+1-507-130-4354,1975-05-28
-- Inglês,"Ney de Toledo Sanches",72543077858,"1624 Amber Point Suite 348",+1-366-174-2909x7141,1956-02-18
-- Inglês,"Olímpia de Chaves Sasenabu",72192402457,"15416 Mitchell Common Suite 092",+1-334-299-9934,1995-02-18
-- Inglês,"Olímpia Estrada das Neves",70930328207,"230 Joshua Squares",+1-654-362-4649x8722,2007-07-01
-- Inglês,"Otaviano Marcelo de Carvalho",72453777190,"08396 James Grove Suite 681",+1-131-998-5104x74347,1944-07-09
-- Inglês,"Otto Marlon Iboman da Silva",54584006209,"0620 Christensen Fords",+55-34-95050-4040,1957-10-01
-- Inglês,"Poliana Yasmin Naves Lielua",01437901196,"05301 Stevenson Corner",+1-083-114-1939x21255,1981-09-20
-- Inglês,"Roberto de Nogueira",10299761377,"250 Lucero Mews Suite 311",+1-773-579-0923x905,1962-04-07
-- Inglês,"Roberval da Cunha de Tavares",69242576334,"22953 Michael Mountains Suite 782",+1-629-612-7735x0573,1932-01-14
-- Inglês,"Simão de Fraga Neto",70071141059,"079 Suzanne Stream",+55-11-97667-5455,1963-07-08
-- Inglês,"Terezinha Bise de Araújo Finanatiov",33799787085,"1892 Cory Village",+1-469-353-6174x2359,1961-04-20
-- Inglês,"Úrsula dos Santos Behere do Espírito Santo",89495598768,"2438 Maria Extensions",+1-715-955-8150x249,1937-04-20
-- Letras,"Alan Siumyde Muu da Silva",66581596036,"1337 Rios Coves",+1-206-537-3712,1945-02-26
-- Letras,"Caio Geli Gomes",64828219030,"11950 Johnson Mission Apt. 583",+1-189-102-9525x579,2008-03-13
-- Letras,"Cíntia Regina Schneider Teles",99622109983,"2489 Barton Cliffs Suite 644",+1-767-558-2046x80568,1941-06-04
-- Letras,"Elano Akizoho de Souza Terceiro",01712609174,"1650 Thompson Manors",+1-375-414-0428x2935,1958-05-23
-- Letras,"Isaías Hamilton da Silva",68685648444,"138 Smith Streets Apt. 492",+1-255-321-3202x867,1931-11-03
-- Letras,"Laura Yoripe",12141618201,"02576 Lewis Falls Suite 987",+55-11-5525-1414,1974-12-09
-- Letras,"Milene Selma dos Pinhais de Moura Banhos",32112035216,"18266 Chelsea Mountains",+1-468-874-6602x132,1970-11-21
-- Letras,"Nádia Rauson Efro",64179320731,"221 Dawn Hill Apt. 047",+1-621-441-7900x765,1991-08-26
-- Letras,"Susan Olmo de Souza Rangel",18590127865,"16686 Williams Center",+1-385-549-8323x9389,2008-08-19
-- Letras,"Valéria Natália de Soares do Paraná",06169933554,"0438 Cole Mount",+1-066-815-7844x2771,1961-01-12
-- Marketing,"Dionísio Kim de Oliveira Fragoso Júnior",70088350049,"14316 Wilson Spring",+1-288-466-3628x503,1967-08-27
-- Marketing,"Guiomar Verônica de Oliveira Naves",64477543628,"119 Carpenter Fords",+1-187-635-8902x728,1964-11-05
-- Marketing,"João Cléber da Silva",68752234762,"04476 Cheryl Camp Apt. 802",+1-079-376-9912,1953-09-24
-- Marketing,"José Décio Zyvo",67282946839,"134 Gina Causeway",+1-231-484-1774x84631,1930-01-28
-- Marketing,"Karina dos Santos",70439025450,"1432 Sarah Curve",+1-289-520-9893,1990-05-26
-- Marketing,"Lúcio Baltazar da Silva",16922268394,"17127 Ashley Ranch",+1-424-210-7863,1964-10-10
-- Marketing,"Meire Amanda de Osório da Silva",28736531478,"1791 Caldwell Centers Suite 237",+1-460-452-2517x411,1961-02-28
-- Marketing,"Ney Adílson Gomo",60540596536,"06709 Pitts Fields",+55-81-99999-0001,1930-04-28
-- Marketing,"Olímpia Estrada das Neves",70930328207,"230 Joshua Squares",+1-654-362-4649x8722,2007-07-01
-- Marketing,"Raiane da Luz Gutierrez de Borges",74174171444,"044 Rachel Falls Suite 789",+1-067-145-4362x6407,1968-07-25
-- Marketing,"Selena Mayra de Souza Ugiza Gutierrez",85285287414,"165 Reed Ports Suite 314",+1-367-126-5660,1934-04-30

-- 2 Produza um relatório com os dados de todos os cursos, com suas respectivas disciplinas, oferecidos pela escola

SELECT c.Codigo, c.Nome Curso, c.Descricao, d.Nome Disciplina, d.Codigo, d.Qtde_Creditos
FROM Curso c, Compoe co, Disciplina d
WHERE co.Codigo_Curso = c.Codigo AND co.Codigo_Disc = d.Codigo 
ORDER BY c.Codigo ASC, d.Codigo ASC

-- ************ RESULTADO ************
-- Codigo,Curso,Descricao,Disciplina,Codigo,Qtde_Creditos
-- 1,Estatística,"Cálculos e conceitos matemáticos relacionados à estatísticas.","Cálculo 1",1,2
-- 1,Estatística,"Cálculos e conceitos matemáticos relacionados à estatísticas.","Cálculo 2",2,3
-- 1,Estatística,"Cálculos e conceitos matemáticos relacionados à estatísticas.",Probabilidade,3,4
-- 1,Estatística,"Cálculos e conceitos matemáticos relacionados à estatísticas.","Equações Lineares",4,5
-- 2,Finanças,"Fundamentos e noções básicas sobre finanças e mercado de capitais.","Matemática Financeira",5,3
-- 2,Finanças,"Fundamentos e noções básicas sobre finanças e mercado de capitais.","Admin. e Contabilidade",6,2
-- 2,Finanças,"Fundamentos e noções básicas sobre finanças e mercado de capitais.","Mercado de Capitais",7,4
-- 3,"Ciência da Computação","Lógica de Programação com linguagem Python e cálculos matemáticos básicos, Banco de Dados e técnicas/ferramentas de Data Science e IA.","Cálculo 1",1,2
-- 3,"Ciência da Computação","Lógica de Programação com linguagem Python e cálculos matemáticos básicos, Banco de Dados e técnicas/ferramentas de Data Science e IA.",Probabilidade,3,4
-- 3,"Ciência da Computação","Lógica de Programação com linguagem Python e cálculos matemáticos básicos, Banco de Dados e técnicas/ferramentas de Data Science e IA.",Python,8,3
-- 3,"Ciência da Computação","Lógica de Programação com linguagem Python e cálculos matemáticos básicos, Banco de Dados e técnicas/ferramentas de Data Science e IA.","Data Science e IA",9,5
-- 3,"Ciência da Computação","Lógica de Programação com linguagem Python e cálculos matemáticos básicos, Banco de Dados e técnicas/ferramentas de Data Science e IA.","Banco de Dados",10,6
-- 4,"Engenharia Elétrica","Técnicas para projetar e implementar instalações e circuitos elétricos.","Cálculo 1",1,2
-- 4,"Engenharia Elétrica","Técnicas para projetar e implementar instalações e circuitos elétricos.","Circuitos Elétricos",11,3
-- 4,"Engenharia Elétrica","Técnicas para projetar e implementar instalações e circuitos elétricos.","Instalações Elétricas",12,4
-- 5,Marketing,"Conceitos e técnicas para Marketing, trabalhando com ferramentas de propaganda e publicidade.","Elementos do Marketing",13,3
-- 5,Marketing,"Conceitos e técnicas para Marketing, trabalhando com ferramentas de propaganda e publicidade.","Mapeamento do Público",14,4
-- 5,Marketing,"Conceitos e técnicas para Marketing, trabalhando com ferramentas de propaganda e publicidade.","Criação e Melhorias",15,5
-- 5,Marketing,"Conceitos e técnicas para Marketing, trabalhando com ferramentas de propaganda e publicidade.","Mídias Sociais",16,6
-- 6,"Gestão de RH","Psicologia e prática para trabalhar com Recursos Humanos, buscando e explorando habilidades das pessoas.","Admin. e Contabilidade",6,2
-- 6,"Gestão de RH","Psicologia e prática para trabalhar com Recursos Humanos, buscando e explorando habilidades das pessoas.","Introd. Psicologia",20,2
-- 6,"Gestão de RH","Psicologia e prática para trabalhar com Recursos Humanos, buscando e explorando habilidades das pessoas.","Gestão de Competências",21,3
-- 6,"Gestão de RH","Psicologia e prática para trabalhar com Recursos Humanos, buscando e explorando habilidades das pessoas.","Identif. Realoc. de Talentos",22,4
-- 7,"Gestão Comercial","Administração e desenvolvimento de propagandas, vendas, gestão de projetos comerciais e liderança de equipe.","Admin. e Contabilidade",6,2
-- 7,"Gestão Comercial","Administração e desenvolvimento de propagandas, vendas, gestão de projetos comerciais e liderança de equipe.","Elementos do Marketing",13,3
-- 7,"Gestão Comercial","Administração e desenvolvimento de propagandas, vendas, gestão de projetos comerciais e liderança de equipe.","Comportam. do Consumidor",17,3
-- 7,"Gestão Comercial","Administração e desenvolvimento de propagandas, vendas, gestão de projetos comerciais e liderança de equipe.","Comércio exterior",18,4
-- 7,"Gestão Comercial","Administração e desenvolvimento de propagandas, vendas, gestão de projetos comerciais e liderança de equipe.","Gestão de Projetos",19,5
-- 8,Letras,"Conhecimento e exploração profunda na literatura brasileira e básica na literatura mundial.","Concepções de Linguagem",23,2
-- 8,Letras,"Conhecimento e exploração profunda na literatura brasileira e básica na literatura mundial.","Gêneros Literários",24,3
-- 8,Letras,"Conhecimento e exploração profunda na literatura brasileira e básica na literatura mundial.","Variação Linguística",25,4
-- 8,Letras,"Conhecimento e exploração profunda na literatura brasileira e básica na literatura mundial.","Literaturas na Educação Básica",26,5
-- 9,Inglês,"Gramática, leitura, audição e conversação do idioma na teoria e prática.","Inglês Básico",27,2
-- 9,Inglês,"Gramática, leitura, audição e conversação do idioma na teoria e prática.","Inglês Intermediário",28,3
-- 9,Inglês,"Gramática, leitura, audição e conversação do idioma na teoria e prática.","Inglês Avançado",29,4
-- 10,Espanhol,"Gramática, leitura, audição e conversação do idioma na teoria e prática.","Espanhol Básico",30,2
-- 10,Espanhol,"Gramática, leitura, audição e conversação do idioma na teoria e prática.","Espanhol Intermediário",31,3
-- 10,Espanhol,"Gramática, leitura, audição e conversação do idioma na teoria e prática.","Espanhol Avançado",32,4
-- 11,Alemão,"Gramática, leitura, audição e conversação do idioma na teoria e prática.","Alemão Básico",33,2
-- 11,Alemão,"Gramática, leitura, audição e conversação do idioma na teoria e prática.","Alemão Intermediário",34,3
-- 11,Alemão,"Gramática, leitura, audição e conversação do idioma na teoria e prática.","Alemão Avançado",35,4
-- 12,Francês,"Gramática, leitura, audição e conversação do idioma na teoria e prática.","Francês Básico",36,2
-- 12,Francês,"Gramática, leitura, audição e conversação do idioma na teoria e prática.","Francês Intermediário",37,3
-- 12,Francês,"Gramática, leitura, audição e conversação do idioma na teoria e prática.","Francês Avançado",38,4

-- 3 Produza um relatório que contenha o nome dos alunos e as disciplinas em que estão matriculados

SELECT a.Nome, d.Nome Disciplina
FROM Aluno a, Disciplina d, Cursa c
WHERE c.CPF_Aluno = a.CPF AND c.Codigo_Disc = d.Codigo
ORDER BY a.Nome ASC, d.Nome ASC

-- ************ RESULTADO ************
-- Nome,Disciplina
-- "Abigail Dlantroz","Cálculo 1"
-- "Abílio Jânio Joepa","Cálculo 1"
-- "Abílio Jânio Joepa",Probabilidade
-- "Alan Siumyde Muu da Silva","Gêneros Literários"
-- "Albino Nicolas de Gimenes","Mercado de Capitais"
-- "Alexandre Humberto Pinhão de Cerqueira Usago","Alemão Intermediário"
-- "Alfredo Anderson de Barros","Inglês Intermediário"
-- "Ali de Magalhães",Python
-- "Altair de Pereira Isbi Muchol","Inglês Básico"
-- "Ana de Barbosa","Inglês Intermediário"
-- "Ana de Moreira","Espanhol Básico"
-- "Ana Dilma Phachuzsay","Admin. e Contabilidade"
-- "Ana Moreno","Cálculo 1"
-- "Ângelo Izcunarn","Admin. e Contabilidade"
-- "Antônio Oeulu","Gestão de Competências"
-- "Avelino Abirner Neto","Inglês Intermediário"
-- "Bárbara Felícia Robitako","Admin. e Contabilidade"
-- "Bárbara Felícia Robitako","Equações Lineares"
-- "Bartolomeu Otaviano de Ferraz","Espanhol Intermediário"
-- "Beatriz Sônia Ublavi da Rocha","Cálculo 1"
-- "Bento Frias","Circuitos Elétricos"
-- "Bete Rute Pede","Francês Básico"
-- "Bianca Maria dos Santos","Inglês Básico"
-- "Brenda de Junqueira","Data Science e IA"
-- "Brenda de Junqueira","Inglês Intermediário"
-- "Caio Geli Gomes","Variação Linguística"
-- "Carlos dos Santos Júnior","Elementos do Marketing"
-- "Cíntia Regina Schneider Teles","Variação Linguística"
-- "Damares Célia de Martins Eclaovi da Silva","Admin. e Contabilidade"
-- "Daniela Rute de Tozetto","Inglês Avançado"
-- "Danielle Kiean Durirna","Cálculo 1"
-- "David Meynyorn","Data Science e IA"
-- "David Meynyorn","Inglês Avançado"
-- "Dionísio Cirilo Weiss Lole","Alemão Básico"
-- "Dionísio Cirilo Weiss Lole","Inglês Básico"
-- "Dionísio Kim de Oliveira Fragoso Júnior","Introd. Psicologia"
-- "Dionísio Kim de Oliveira Fragoso Júnior","Mídias Sociais"
-- "Edson Coso","Alemão Intermediário"
-- "Edson Coso","Inglês Básico"
-- "Edu Arnaldo Mineiro Cuminnas Towateho","Gestão de Competências"
-- "Eduardo Nepanegi","Data Science e IA"
-- "Elano Akizoho de Souza Terceiro","Concepções de Linguagem"
-- "Elano Augusto Irnsitli","Francês Básico"
-- "Eliomar Suzanne de Moura","Admin. e Contabilidade"
-- "Eustáquio Itysson","Francês Avançado"
-- "Fabiana Dina de Melo","Comércio exterior"
-- "Gisele de Meireles","Equações Lineares"
-- "Gisele do Amaral de Malta","Gestão de Competências"
-- "Gisele Rosatto","Alemão Avançado"
-- "Gisele Rosatto","Espanhol Avançado"
-- "Guiomar Verônica de Oliveira Naves","Mapeamento do Público"
-- "Hamilton Gunoi Martinez","Inglês Avançado"
-- "Helena Gois Creti","Alemão Básico"
-- "Humberto Mike de Uchôa","Inglês Avançado"
-- "Humberto Mike de Uchôa",Python
-- "Ingrid de Angola Barroso","Comportam. do Consumidor"
-- "Isaías Hamilton da Silva","Concepções de Linguagem"
-- "Isaías Hamilton da Silva","Espanhol Básico"
-- "Ismael de Soares Júnior","Comportam. do Consumidor"
-- "Ismael de Soares Júnior","Inglês Básico"
-- "Israel de Assunção Pimenta","Gestão de Projetos"
-- "Israel de Assunção Pimenta","Inglês Intermediário"
-- "Itamar de Carvalho Júnior","Cálculo 1"
-- "Ivanete Mirela Tsuyupeka","Alemão Intermediário"
-- "Jackson Jorge Suwoga","Banco de Dados"
-- "Jackson Jorge Suwoga","Inglês Básico"
-- "João Cléber da Silva","Inglês Intermediário"
-- "João Cléber da Silva","Mapeamento do Público"
-- "Joelma de Brandão","Alemão Intermediário"
-- "Joelma de Brandão","Espanhol Avançado"
-- "Jonas Fred Rangel","Banco de Dados"
-- "Jonas Fred Rangel","Cálculo 1"
-- "Jorge Walter Mili Alkenumi Júnior","Alemão Avançado"
-- "José Décio Zyvo","Mapeamento do Público"
-- "José Mourão","Comércio exterior"
-- "Josiel de Alvim",Python
-- "Josilda Nair Lyphornson","Alemão Básico"
-- "Joyce Aparecida da Silva","Introd. Psicologia"
-- "Juliano de Diniz Esluyer Anuneson","Inglês Intermediário"
-- "Karin Luciana de Antunes Pinhão","Admin. e Contabilidade"
-- "Karina dos Santos","Elementos do Marketing"
-- "Karina dos Santos","Identif. Realoc. de Talentos"
-- "Kauê Albafriov","Inglês Avançado"
-- "Laerte Ederson Moreno","Gestão de Competências"
-- "Laura Yoripe","Concepções de Linguagem"
-- "Leandro Augusto de Paranhos Amernma Tristão","Cálculo 2"
-- "Leni Xaetreu","Mercado de Capitais"
-- "Lili Terezinha da Silva",Python
-- "Lúcio Baltazar da Silva","Mapeamento do Público"
-- "Manoel Charles de Trindade Penedo","Cálculo 1"
-- "Marcelo de Barbosa","Elementos do Marketing"
-- "Marciano de Bezerra Buarque Oeyser","Admin. e Contabilidade"
-- "Marielle da Serra","Introd. Psicologia"
-- "Mário Frederico Ovrilso","Espanhol Básico"
-- "Mateus Rodrigues Guedes Npo","Espanhol Intermediário"
-- "Meire Amanda de Osório da Silva","Inglês Intermediário"
-- "Meire Amanda de Osório da Silva","Mapeamento do Público"
-- "Mel Naves de Vasconcelos","Data Science e IA"
-- "Melanie Vânia de Camargo da Rocha","Instalações Elétricas"
-- "Milene Selma dos Pinhais de Moura Banhos","Espanhol Intermediário"
-- "Milene Selma dos Pinhais de Moura Banhos","Gêneros Literários"
-- "Moisés Fontes de Machado","Inglês Básico"
-- "Mônica Fabiana Prates","Espanhol Básico"
-- "Nádia Rauson Efro","Gêneros Literários"
-- "Neila da Silva","Comércio exterior"
-- "Ney Adílson Gomo","Elementos do Marketing"
-- "Ney de Toledo Sanches","Circuitos Elétricos"
-- "Ney de Toledo Sanches","Inglês Básico"
-- "Olímpia de Chaves Sasenabu","Elementos do Marketing"
-- "Olímpia de Chaves Sasenabu","Inglês Intermediário"
-- "Olímpia Estrada das Neves","Inglês Intermediário"
-- "Olímpia Estrada das Neves","Mapeamento do Público"
-- "Oliver Pires Nago","Francês Intermediário"
-- "Otaviano Marcelo de Carvalho","Comportam. do Consumidor"
-- "Otaviano Marcelo de Carvalho","Inglês Avançado"
-- "Otávio Gilmar de Alves Nirnofezsen Inau Júnior","Gestão de Competências"
-- "Otto Marlon Iboman da Silva","Inglês Intermediário"
-- "Paula Eztrern","Alemão Básico"
-- "Paula Eztrern","Espanhol Básico"
-- "Paulo de Holanda do Espírito Santo Júnior","Data Science e IA"
-- "Poliana Yasmin Naves Lielua","Inglês Básico"
-- "Quésia Amoã","Data Science e IA"
-- "Quésia Amoã","Instalações Elétricas"
-- "Quirino Martinez da Silva Neienason","Admin. e Contabilidade"
-- "Quirino Martinez da Silva Neienason","Cálculo 2"
-- "Raiane da Luz Gutierrez de Borges","Criação e Melhorias"
-- "Raiane da Luz Gutierrez de Borges","Gestão de Competências"
-- "Reinaldo Murilo da Silva",Probabilidade
-- "Roberta de Oliveira Ximenes","Identif. Realoc. de Talentos"
-- "Roberto de Nogueira","Inglês Intermediário"
-- "Roberval da Cunha de Tavares","Alemão Básico"
-- "Roberval da Cunha de Tavares","Inglês Intermediário"
-- "Roberval de Amorim Drouzcos","Francês Básico"
-- "Robson Drynom Freire Júnior",Probabilidade
-- "Rogério Lowimirnian","Equações Lineares"
-- "Rosana Talita de Alvarenga","Francês Básico"
-- "Samara Risme do Vale",Python
-- "Sandra Paulínia Canam","Cálculo 2"
-- "Sandro Waei Mendes de Britto","Matemática Financeira"
-- "Selena Mayra de Souza Ugiza Gutierrez","Elementos do Marketing"
-- "Selma Fortes",Python
-- "Sheila Ocuã",Probabilidade
-- "Simão de Fraga Neto","Circuitos Elétricos"
-- "Simão de Fraga Neto","Inglês Básico"
-- "Soraya Brides Liuviã","Identif. Realoc. de Talentos"
-- "Suely Daniela Cavalcante","Identif. Realoc. de Talentos"
-- "Susan Olmo de Souza Rangel","Concepções de Linguagem"
-- "Terezinha Bise de Araújo Finanatiov","Circuitos Elétricos"
-- "Terezinha Bise de Araújo Finanatiov","Inglês Avançado"
-- "Thiago Leandro do Rio de Souza","Banco de Dados"
-- "Úrsula de Angola Heijira","Admin. e Contabilidade"
-- "Úrsula dos Santos Behere do Espírito Santo","Inglês Básico"
-- "Valéria Natália de Soares do Paraná","Concepções de Linguagem"
-- "Victor de Medeiros d"Ávila Ecifoson","Alemão Intermediário"
-- "Viviane Larissa de Sampaio","Francês Básico"
-- "Wendy Tatiana Mercado de Menezes","Espanhol Intermediário"
-- "Willian Martin Arno","Data Science e IA"
-- "Xerxes do Paraná","Equações Lineares"
-- "Yasmin Banhos","Espanhol Básico"
-- "Zara de Angola","Espanhol Básico"

-- 4 Produza um relatório com os dados dos professores e as disciplinas que ministram
-- SELECT p.Matricula, p.Nome Professor, p.Endereco, p.Telefone, p.Data_Nasc, p.Data_Contratacao, p.Codigo_Depto Cod_Departamento, d.Nome Disciplina, d.Codigo
-- FROM Professor p, Disciplina d
-- WHERE d.Matricula_Prof = p.Matricula
-- ORDER BY p.Nome ASC, d.Nome ASC

SELECT p.Matricula, p.Nome Professor, p.Endereco, p.Telefone, p.Data_Nasc, p.Data_Contratacao, p.Codigo_Depto Cod_Departamento, d.Nome Disciplina, d.Codigo
FROM Professor p
INNER JOIN Disciplina d ON d.Matricula_Prof = p.Matricula
ORDER BY p.Nome ASC, d.Nome ASC

-- ************ RESULTADO ************
-- Matricula,Professor,Endereco,Telefone,Data_Nasc,Data_Contratacao,Cod_Departamento,Disciplina,Codigo
-- 11,"Áureo de Palhares Neiol","0214 Ramos Bypass Apt. 986",+55-51-92929-5550,1951-02-26,2017-08-24,3,"Alemão Avançado",35
-- 11,"Áureo de Palhares Neiol","0214 Ramos Bypass Apt. 986",+55-51-92929-5550,1951-02-26,2017-08-24,3,"Alemão Básico",33
-- 11,"Áureo de Palhares Neiol","0214 Ramos Bypass Apt. 986",+55-51-92929-5550,1951-02-26,2017-08-24,3,"Alemão Intermediário",34
-- 17,"Bella Biwo","03836 Lydia Creek Apt. 778",+1-060-465-8808x51762,1932-08-15,2016-06-23,1,"Matemática Financeira",5
-- 17,"Bella Biwo","03836 Lydia Creek Apt. 778",+1-060-465-8808x51762,1932-08-15,2016-06-23,1,"Mercado de Capitais",7
-- 4,"Cléber de Vasconcelos","0134 Murray Walk",+55-11-4224-2626,1957-08-09,2020-10-05,9,Python,8
-- 19,"Décio de Leão do Amaral Terceiro","04312 Haley Island",+1-065-022-0820,1981-04-06,2016-06-03,3,"Inglês Básico",27
-- 19,"Décio de Leão do Amaral Terceiro","04312 Haley Island",+1-065-022-0820,1981-04-06,2016-06-03,3,"Inglês Intermediário",28
-- 14,"Flaviana Supugeko de Arantes","031 Cook Ville Suite 523",+55-21-90909-4444,1996-05-07,2016-07-30,2,"Gestão de Competências",21
-- 14,"Flaviana Supugeko de Arantes","031 Cook Ville Suite 523",+55-21-90909-4444,1996-05-07,2016-07-30,2,"Identif. Realoc. de Talentos",22
-- 6,"Gabriela da Silva de Macedo","0165 Drew Junction Suite 552",+1-026-402-2651,1930-10-06,2020-05-17,2,"Comércio exterior",18
-- 6,"Gabriela da Silva de Macedo","0165 Drew Junction Suite 552",+1-026-402-2651,1930-10-06,2020-05-17,2,"Gestão de Projetos",19
-- 1,"Gabriela Genir Marinho","000 Wright Motorway Suite 352",+1-006-414-8797,1954-12-08,2016-12-13,1,"Cálculo 2",2
-- 8,"Gabriela Maria Ribohi Valente","01932 Garcia Expressway Suite 183",+1-037-591-5560x81884,1954-04-20,2021-05-24,9,Probabilidade,3
-- 7,"Heitor Raul de Meireles Rilia","0181 Ronald Brooks",+1-032-081-6436,1950-02-02,2019-02-06,3,"Francês Avançado",38
-- 7,"Heitor Raul de Meireles Rilia","0181 Ronald Brooks",+1-032-081-6436,1950-02-02,2019-02-06,3,"Francês Básico",36
-- 7,"Heitor Raul de Meireles Rilia","0181 Ronald Brooks",+1-032-081-6436,1950-02-02,2019-02-06,3,"Francês Intermediário",37
-- 13,"João Osvaldo de Oliva do Prado","02794 Carr Mountains",+55-11-97887-8007,1942-05-15,2020-10-08,1,"Circuitos Elétricos",11
-- 13,"João Osvaldo de Oliva do Prado","02794 Carr Mountains",+55-11-97887-8007,1942-05-15,2020-10-08,1,"Instalações Elétricas",12
-- 9,"Lúcio Ceilson","015 Johnson Stravenue Suite 582",+1-019-168-1103x30298,1973-04-25,2021-07-06,1,"Admin. e Contabilidade",6
-- 18,"Márcio de Oliveira Negrão","041 Lin Lock",+1-061-832-1376x6059,1930-02-21,2021-06-15,2,"Comportam. do Consumidor",17
-- 18,"Márcio de Oliveira Negrão","041 Lin Lock",+1-061-832-1376x6059,1930-02-21,2021-06-15,2,"Introd. Psicologia",20
-- 10,"Marco Yumoma Neto","01627 Lopez Path Suite 161",+1-024-173-1193x0353,1969-05-22,2016-04-18,2,"Concepções de Linguagem",23
-- 10,"Marco Yumoma Neto","01627 Lopez Path Suite 161",+1-024-173-1193x0353,1969-05-22,2016-04-18,2,"Gêneros Literários",24
-- 10,"Marco Yumoma Neto","01627 Lopez Path Suite 161",+1-024-173-1193x0353,1969-05-22,2016-04-18,2,"Literaturas na Educação Básica",26
-- 10,"Marco Yumoma Neto","01627 Lopez Path Suite 161",+1-024-173-1193x0353,1969-05-22,2016-04-18,2,"Variação Linguística",25
-- 2,"Marli de Holanda Opinvic","00183 Charles Mountain",+1-008-628-9256x246,1963-01-15,2016-04-07,2,"Criação e Melhorias",15
-- 2,"Marli de Holanda Opinvic","00183 Charles Mountain",+1-008-628-9256x246,1963-01-15,2016-04-07,2,"Elementos do Marketing",13
-- 2,"Marli de Holanda Opinvic","00183 Charles Mountain",+1-008-628-9256x246,1963-01-15,2016-04-07,2,"Mapeamento do Público",14
-- 2,"Marli de Holanda Opinvic","00183 Charles Mountain",+1-008-628-9256x246,1963-01-15,2016-04-07,2,"Mídias Sociais",16
-- 20,"Moacyr Arthur Góis","05983 Michael Spring Suite 047",+55-19-90001-8889,1986-02-28,2021-09-05,9,"Banco de Dados",10
-- 16,"Romildo Ademar da Silva Fragoso Júnior","0377 Joshua Circle",+1-051-279-6304x91019,1942-11-25,2017-09-05,9,"Equações Lineares",4
-- 15,"Ronaldo Severino Berrea Bozuga","03656 Ward Plaza Apt. 978",+1-047-466-1919x28434,1931-01-12,2017-09-14,3,"Espanhol Avançado",32
-- 15,"Ronaldo Severino Berrea Bozuga","03656 Ward Plaza Apt. 978",+1-047-466-1919x28434,1931-01-12,2017-09-14,3,"Inglês Avançado",29
-- 5,"Selena Caroline Cavalcante da Silva","0137 Shelton Rest Apt. 273",+1-013-001-8838,1935-01-04,2016-11-09,1,"Cálculo 1",1
-- 12,"Sílvia Rosimeire Franco","022 Thomas Ridges Apt. 464",+55-11-91010-2020,1940-04-04,2019-12-03,9,"Data Science e IA",9
-- 3,"Walter Mário de Muniz","00626 Jonathan Hollow Apt. 314",+55-11-99999-8888,1958-03-21,2016-09-25,3,"Espanhol Básico",30
-- 3,"Walter Mário de Muniz","00626 Jonathan Hollow Apt. 314",+55-11-99999-8888,1958-03-21,2016-09-25,3,"Espanhol Intermediário",31


-- 5 Produza um relatório com os nomes das disciplinas e seus pré-requisitos
-- #*#*#*#*# Fiquei em dúvida com o enunciado, se deveria trazer só as disciplinas que tem pré-requisito ou todas. Então fiz as 2 formas
-- Só as disciplinas que possuem pré-requisito
CREATE VIEW Disciplina_Pre_Req AS
SELECT d.Codigo, d.Nome Disciplina, pr.Codigo_Disc_Dependencia Pre_Requisito
FROM Disciplina d
INNER JOIN Pre_Req pr
ON pr.Codigo_Disc = d.Codigo

SELECT dpr.Codigo, dpr.Disciplina, dpr.Pre_Requisito, d.Nome Disciplina
FROM Disciplina_Pre_Req dpr
INNER JOIN Disciplina d
ON dpr.Pre_Requisito = d.Codigo
ORDER BY d.Codigo ASC

-- ************ RESULTADO DISCIPLINAS COM PRÉ-REQUISITO ************
-- Codigo,Disciplina,Pre_Requisito,Disciplina
-- 2,"Cálculo 2",1,"Cálculo 1"
-- 7,"Mercado de Capitais",5,"Matemática Financeira"
-- 9,"Data Science e IA",8,Python
-- 12,"Instalações Elétricas",11,"Circuitos Elétricos"
-- 15,"Criação e Melhorias",13,"Elementos do Marketing"
-- 18,"Comércio exterior",13,"Elementos do Marketing"
-- 19,"Gestão de Projetos",6,"Admin. e Contabilidade"
-- 22,"Identif. Realoc. de Talentos",20,"Introd. Psicologia"
-- 26,"Literaturas na Educação Básica",24,"Gêneros Literários"
-- 28,"Inglês Intermediário",27,"Inglês Básico"
-- 29,"Inglês Avançado",28,"Inglês Intermediário"
-- 31,"Espanhol Intermediário",30,"Espanhol Básico"
-- 32,"Espanhol Avançado",31,"Espanhol Intermediário"
-- 34,"Alemão Intermediário",33,"Alemão Básico"
-- 35,"Alemão Avançado",34,"Alemão Intermediário"
-- 37,"Francês Intermediário",36,"Francês Básico"
-- 38,"Francês Avançado",37,"Francês Intermediário"

-- TODAS AS DISCIPLINAS
CREATE VIEW Disciplina_Pre_Req_Full AS
SELECT d.Codigo, d.Nome Disciplina, pr.Codigo_Disc_Dependencia Pre_Requisito
FROM Disciplina d
LEFT JOIN Pre_Req pr
ON pr.Codigo_Disc = d.Codigo

SELECT dprf.Codigo, dprf.Disciplina, dprf.Pre_Requisito, d.Nome Disciplina
FROM Disciplina_Pre_Req_Full dprf
LEFT JOIN Disciplina d
ON dprf.Pre_Requisito = d.Codigo
ORDER BY d.Codigo ASC

-- ************ RESULTADO TODAS AS DISCIPLINAS ************
-- Codigo,Disciplina,Pre_Requisito,Disciplina
-- 1,"Cálculo 1",NULL,NULL
-- 2,"Cálculo 2",1,"Cálculo 1"
-- 3,Probabilidade,NULL,NULL
-- 4,"Equações Lineares",NULL,NULL
-- 5,"Matemática Financeira",NULL,NULL
-- 6,"Admin. e Contabilidade",NULL,NULL
-- 7,"Mercado de Capitais",5,"Matemática Financeira"
-- 8,Python,NULL,NULL
-- 9,"Data Science e IA",8,Python
-- 10,"Banco de Dados",NULL,NULL
-- 11,"Circuitos Elétricos",NULL,NULL
-- 12,"Instalações Elétricas",11,"Circuitos Elétricos"
-- 13,"Elementos do Marketing",NULL,NULL
-- 14,"Mapeamento do Público",NULL,NULL
-- 15,"Criação e Melhorias",13,"Elementos do Marketing"
-- 16,"Mídias Sociais",NULL,NULL
-- 17,"Comportam. do Consumidor",NULL,NULL
-- 18,"Comércio exterior",13,"Elementos do Marketing"
-- 19,"Gestão de Projetos",6,"Admin. e Contabilidade"
-- 20,"Introd. Psicologia",NULL,NULL
-- 21,"Gestão de Competências",NULL,NULL
-- 22,"Identif. Realoc. de Talentos",20,"Introd. Psicologia"
-- 23,"Concepções de Linguagem",NULL,NULL
-- 24,"Gêneros Literários",NULL,NULL
-- 25,"Variação Linguística",NULL,NULL
-- 26,"Literaturas na Educação Básica",24,"Gêneros Literários"
-- 27,"Inglês Básico",NULL,NULL
-- 28,"Inglês Intermediário",27,"Inglês Básico"
-- 29,"Inglês Avançado",28,"Inglês Intermediário"
-- 30,"Espanhol Básico",NULL,NULL
-- 31,"Espanhol Intermediário",30,"Espanhol Básico"
-- 32,"Espanhol Avançado",31,"Espanhol Intermediário"
-- 33,"Alemão Básico",NULL,NULL
-- 34,"Alemão Intermediário",33,"Alemão Básico"
-- 35,"Alemão Avançado",34,"Alemão Intermediário"
-- 36,"Francês Básico",NULL,NULL
-- 37,"Francês Intermediário",36,"Francês Básico"
-- 38,"Francês Avançado",37,"Francês Intermediário"

-- 6 Produza um relatório com a média de idade dos alunos matriculados em cada curso
##### Com o que foi passado na última aula consegui fazer assim, mas a conta não está muito exata pois não leva em consideração o mês, apenas o ano
SELECT c.Nome Curso, AVG(CAST(NOW() AS YEAR) - CAST(a.Data_Nasc AS YEAR)) AS Media_Idade
FROM Aluno a, Curso c, Matricula m 
WHERE m.CPF_Aluno = a.CPF AND m.Codigo_Curso = c.Codigo
GROUP BY c.Nome 
ORDER BY c.Nome ASC

-- ************ RESULTADO ************
-- Curso,Media_Idade
-- Alemão,40.3333
-- "Ciência da Computação",45.2500
-- "Engenharia Elétrica",46.3333
-- Espanhol,49.9231
-- Estatística,46.1667
-- Finanças,41.2500
-- Francês,56.0000
-- "Gestão Comercial",55.7500
-- "Gestão de RH",52.6667
-- Inglês,54.4839
-- Letras,53.3000
-- Marketing,61.2727

##### Pesquisando um pouco na internet achei a função TIMESTAMPDIFF() que dá p fazer de uma forma mais elegante. Achei ela melhor do que a DATEDIFF().
CREATE OR REPLACE VIEW idade_alunos_curso AS
SELECT c.Nome Curso, a.nome Aluno, a.Data_Nasc Nascimento, CURDATE(), TIMESTAMPDIFF(YEAR, a.Data_Nasc, CURDATE()) AS Idade
FROM Aluno a, Curso c, Matricula m 
WHERE m.CPF_Aluno = a.CPF AND m.Codigo_Curso = c.Codigo
ORDER BY c.Nome ASC

#SELECT curso, AVG(Idade) AS Media_Idade -- Sem arredondamento
SELECT curso, CAST(AVG(Idade) AS SIGNED) AS Media_Idade -- Com arredondamento
FROM idade_alunos_curso
GROUP BY Curso
ORDER BY Curso;

-- SELECT * FROM idade_alunos_curso;

-- ************ RESULTADO ************
-- *** SEM ARREDONDAMENTO
-- Curso,Media_Idade
-- Alemão,39.5833
-- "Ciência da Computação",44.3500
-- "Engenharia Elétrica",45.6667
-- Espanhol,49.0769
-- Estatística,45.5833
-- Finanças,40.6250
-- Francês,55.1429
-- "Gestão Comercial",55.0833
-- "Gestão de RH",51.8667
-- Inglês,53.8387
-- Letras,52.6000
-- Marketing,60.4545

-- *** COM ARREDONDAMENTO
-- Curso,Media_Idade
-- Alemão,40
-- "Ciência da Computação",44
-- "Engenharia Elétrica",46
-- Espanhol,49
-- Estatística,46
-- Finanças,41
-- Francês,55
-- "Gestão Comercial",55
-- "Gestão de RH",52
-- Inglês,54
-- Letras,53
-- Marketing,60


-- 7 Produza um relatório com os cursos oferecidos por cada departamento
SELECT d.Codigo Id_Depto, d.Nome Departamento, c.Codigo Id_Curso, c.Nome Curso, c.Descricao
FROM Departamento d
INNER JOIN Curso c
ON c.Codigo_Depto = d.Codigo
ORDER BY d.Codigo

-- ************ RESULTADO ************
-- Id_Depto,Departamento,Id_Curso,Curso,Descricao
-- 1,Exatas,1,Estatística,"Cálculos e conceitos matemáticos relacionados à estatísticas."
-- 1,Exatas,2,Finanças,"Fundamentos e noções básicas sobre finanças e mercado de capitais."
-- 1,Exatas,4,"Engenharia Elétrica","Técnicas para projetar e implementar instalações e circuitos elétricos."
-- 2,Humanas,5,Marketing,"Conceitos e técnicas para Marketing, trabalhando com ferramentas de propaganda e publicidade."
-- 2,Humanas,6,"Gestão de RH","Psicologia e prática para trabalhar com Recursos Humanos, buscando e explorando habilidades das pessoas."
-- 2,Humanas,7,"Gestão Comercial","Administração e desenvolvimento de propagandas, vendas, gestão de projetos comerciais e liderança de equipe."
-- 2,Humanas,8,Letras,"Conhecimento e exploração profunda na literatura brasileira e básica na literatura mundial."
-- 3,Idiomas,9,Inglês,"Gramática, leitura, audição e conversação do idioma na teoria e prática."
-- 3,Idiomas,10,Espanhol,"Gramática, leitura, audição e conversação do idioma na teoria e prática."
-- 3,Idiomas,11,Alemão,"Gramática, leitura, audição e conversação do idioma na teoria e prática."
-- 3,Idiomas,12,Francês,"Gramática, leitura, audição e conversação do idioma na teoria e prática."
-- 9,TI,3,"Ciência da Computação","Lógica de Programação com linguagem Python e cálculos matemáticos básicos, Banco de Dados e técnicas/ferramentas de Data Science e IA."
