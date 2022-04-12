# Funções

---

## Exercícios
- Exercícios recomendados: 1, 2, 5, 7, 12, 14
- Exercícios pra explicação: 3, 9
- Exercícios pra resolver em sala: 8

## O que é uma função?
- uma maneira de "chamar" diversas linhas de código sem ter que reescrevê-las todas as vezes
- toda função tem o seguinte formato:
	- `<nome_da_funcão>(<argumentos da função>)`
	- se isso parece familiar, é porque é! estamos usando diversas funções desde o primeiro dia de aula
	- exemplos: `print()`, `input()`

## Pra que usamos funções?
- otimização da escrita de código
- ou seja: é uma maneira de repetir várias linhas de código que já foram escritas sem precisar escrever todas novamente
- além disso, deixa o código mais limpo pra leitura, pois chamamos uma função por seu *indicador*, assim como fazíamos com as variáveis, ao invés de inserir as linhas de código correspondentes

## Como criar uma função?
- toda função, para poder ser utilizada, precisa antes ser **definida**.
	- a palavra chave utilizada para isso é a palavra `def`
	- a definição é uma "instrução", ou seja, descreve o mecanismo de ação da função criada
	- fórmula geral:
	```
	def nome_da_funcao(argumento1, argumento2, ...):
		# linhas de código (corpo da função)
		return # não-obrigatório
	```

### Como usar uma função?
- damos o nome de "chamada" da função o ato de escrever a função no código para que execute suas operações
	- ex.: `print(42)` é uma chamada de função
		- "função print, venha aqui e faça o que estou mandando (imprimir 42)"

### Argumentos (ou parâmetros) de uma função
- uma função *pode* ter **argumentos**, ou seja, variáveis que serão passadas *dentro dos parênteses* e para utilização interna
	- ex.: uma função `soma()` pode ter como argumentos dois número, `a` e `b`: `soma(a,b)`

#### Escopo de uma função
- vamos tomar como exemplo a função `imprime_42()`, implementada a seguir:
	 ```
	 def imprime_42():
	 	numero = 42
		print(numero)
	 ```
- o que acontece se tentarmos imprimir a variável `numero` fora do corpo da função?
	 ```
	 def imprime_42():
	 	numero = 42
		print(42)
	 
	 imprime_42()
	 print(numero)
	 ```
- o código acima jogará um erro!
	- as variáveis "dentro" do corpo de uma função *só pertencem a ela*, ou seja, só são usadas pela própria função e depois são destruídas.
	- assim, só é possível acessar o valor das variáveis definidas numa função no corpo da própria função.
	- na prática, isso significa que se quisermos o valor de alguma das variáveis definidas dentro de uma função, precisamos adotar outra estratégia

### Retorno de uma função
- uma função *pode* ter um **retorno**, ou seja, um valor que é "devolvido" à chamada da função.
	- ex.: a função `soma(a, b)` retorna `a + b`. assim, se chamarmos a função como `soma(1,3)` ela retornará o valor `4`
- o **retorno** é denotado pela palavra chave `return`
	- ex.: 
	 ```
	 def soma(a,b):
	 	soma = a + b
		return soma
	 ```

## Na prática
- vamos ver um exemplo da aula anterior: sistema de cadastro e listagem de usuários em um banco de dados
	- podemos fazer com que cada uma das opções dadas pelo usuário (1, 2) invoque uma função diferente
		- `cadastrar(usuarios, nome, email)`
		- `listar_usuarios()`
		- [código](codigos/cola.py)
- no entanto, note que as funções acima não retornaram nada! além disso, a função `listar_usuarios()` não recebeu nenhum argumento
	- a presença de argumentos ou de retorno **não é mandatória**, o que nos dá flexibilidade quanto aos tipos de funções que podemos criar
	- [exemplo de funções com argumentos e retorno](codigos/retorno.py)

## Funções dentro de funções
- no corpo de uma função, podemos chamar livremente outras funções, desde que passemos os argumentos adequados, caso necessário
	- exemplo: [integrando duas funções](codigos/integracao.py)
- obs.: podemos, claro, fazer isso com qualquer função que já conhecemos, como `print()`, `input()`, etc.