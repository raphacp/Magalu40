# Exercício 1
Faça uma função que receba uma lista de números inteiros e retorne, utilizando retorno multiplo,
uma lista só com os números pares da lista original e outra com somente os números ímpares

# Exercício 2
Faça uma função com *args que receba strings e retorne a concatenação

Exemplo:
```
chamada: concatenar("Olá", "tudo", "bem?")
retorno: "Olátudobem?"
```
Obs. 1 : Para concatenar strings é só usar +

Exemplo: `"ab" + "cd" = "abcd"`

Obs. 2 : Pode fazer como se fosse uma soma de números começando com `soma = 0`, porém começando com `concatenacao = ""`


# Exercício 3
Faça uma função para calcular o salário de um funcionário com a seguinte especificação:
- A função deve receber dois parâmetros obrigatórios, `valor_hora` e `horas`, indicando respectivamente o valor recebido por hora e a quantidade de horas trabalhadas no mês
- A função deve receber, por meio dos `**kwargs`, o parâmetro opcional `bonus`, que é o bônus que o funcionário recebeu no mês
- Caso o parâmetro `bonus` seja passado, ele deve ser somado ao salário final do mês
