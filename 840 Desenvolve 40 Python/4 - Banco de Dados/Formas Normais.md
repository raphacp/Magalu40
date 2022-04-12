# Normalização de Banco de Dados

Normalização é uma ferramenta usada no projeto lógico que serve para reestruturar tabelas e atributos, reduzindo assim redundâncias e permitindo o correto crescimento do banco de dados. Por meio dela que bancos com muita movimentação garantem sua integridade após remoção, inserção e alteração dos dados.

# Problemas da Falta de Normalização

<img src="https://spaceprogrammer.com/wp-content/uploads/2017/10/exemplo-tabela-desnormalizada-1.jpg">

**Problemas de Inserção**

- Só é possível inserir um cliente se o mesmo adquirir um produto
- Só é possível inserir um produto se algum cliente adquiri-lo

**Problemas de alteração**

- Para atualizar o telefone do cliente todos os outros registros deverão ser atualizados.
- Para atualizar o preço do produto todos os registros desse mesmo produto deverão ser atualizados.

**Problemas de exclusão**

- Se os produtos adquiridos por algum cliente forem excluídos, os dados cadastrais do mesmo se perderão.

As formas normais são sequenciais, ou seja, se um banco se encontra na terceira forma normal, isso também significa que o mesmo está na segunda e também na primeira. Por isso devemos sempre começar a normalização pela primeira forma normal, para que não hajam problemas mais a frente na nossa normalização.

# 1FN

Podemos dizer que uma tabela se encontra na Primeira Forma Normal se:

- Possui chave primária;
- Não possui grupos repetitivos;

Todos os seus atributos são atômicos, ou seja, não precisa ser decomposto.
Para chegar a primeira forma normal devemos: Determinar o atributo que possui característica de chave primária, tornar todos atributos atômicos, transformar o grupo repetitivo em uma nova tabela, levando a chave primária da tabela na qual estava, para manter a ligação entre a tabela criada e a original. Depois aplicamos também sobre essa nova tabela a primeira forma normal.

#### Aplicação:

**Tabela** (cod_cliente, nome_cliente, tel1, tel2, endereco, cod_produto, nome_produto, preco, quantidade) ✗

**Cliente** (<u>cod_cliente</u>, nome_cliente, tel1, tel2, rua, bairro, cidade, estado) ✓

**Produto** (<u>cod_cliente</u>, <u>cod_produto</u>, nome_produto, preco, quantidade) ✓

# FN2

Podemos dizer que uma tabela se encontra na Segunda Forma Normal se:

- Está na primeira forma normal;
- Não possui dependências parciais da chave primária;

Para chegar a segunda forma normal verifique se a chave primária dessa tabela é composta ou simples. Se for simples, já se encontra na segunda forma normal. Se for composta, verifique se todos os atributos da relação dependem de todos os atributos que compõem a chave primária. Por exemplo, se a chave primária é composta dos atributos A , B e o campo C em questão depende somente de B. Se sim, já está na segunda forma normal. Se não, pegue o atributo (C) que depende parcialmente da chave primária e crie uma nova tabela.

**Aplicação:**

**Cliente** (<u>cod_cliente</u>, nome_cliente, tel1, tel2, rua, bairro, cidade, estado) ✓ (não possui chave primária composta)

**Produto** (<u>cod_cliente</u>, <u>cod_produto</u>, nome_produto, preco, quantidade) ✗

cod_produto ➙ nome_produto, preco (dependência parcial)

cod_cliente, cod_produto ➙ quantidade (dependência total)

Resp: Produto (<u>cod_produto</u>, nome_produto, preco) ✓

Resp: Compra (<u>cod_cliente</u>, <u>cod_produto</u>, quantidade) ✓

# FN3

Podemos dizer que uma tabela se encontra na Terceira Forma Normal se:

- Está na segunda forma normal;
- Se nenhum dos campos foram determinados transitivamente pela chave primária.

Para chegar a terceira forma normal verifique os campos que não são chave primária. Se algum desses campos não chave possuir dependência com outro campo não chave, então essa tabela não se encontra na terceira forma normal. Veja o exemplo abaixo:

Carro (<u>placa</u>, <u>modelo</u>, km_rodados, cod_fabricante, nome_fabricante) ✗

Placa, modelo ➙ km_rodados

Placa, modelo ➙cod_fabricante

Placa, modelo ➙ nome_fabricante

Cod_frabricante ➙ nome_fabricante

Carro (<u>placa</u>, modelo, kmRodados, cod_fabricante) ✓

Fabricante (<u>cod_fabricante</u>, nome_fabricante) ✓

---

# Exercícios

[Tabela Ex 1 ](./tabela-ex-normalizacao.png)

**1)** Considerando a tabela, dê exemplos de problemas causados pela redundância com:

- inserção
- exclusão
- alteração

**2)** Otimize a tabela usando as formas normais e monte o diagrama ER (Modelagem Lógica).

[Tabela Ex 2 ](./tabela-ex2-normalizacao.png)

**3)** Considerando a tabela, dê exemplos de problemas causados pela redundância com:

- inserção
- exclusão
- alteração

**4)** Otimize a tabela usando as formas normais e monte o diagrama ER (Modelagem Lógica).
