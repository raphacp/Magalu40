# Enunciado
# Crie um sistema de empréstimo de bibliotecas, que envolverá duas classes principais (Cliente, Loja).
# Cliente pode:
# • Ver as bicicletas disponíveis na Loja
# • Alugar bicicletas por hora (R$5/hora)
# • Alugar bicicletas por dia (R$25/dia)
# • Alugar bicicletas por semana (R$100/semana)
# • Aluguel para família, uma promoção que 3 ou mais empréstimos (de qualquer tipo) com 30% de desconto no valor 
# total

# Loja pode:
# • Calcular a conta quando o cliente decidir devolver a bicicleta
# • Mostrar o estoque de bicicletas
# • Receber pedidos de aluguéis por hora, diários ou semanais validando a possibilidade com o estoque e modo de 
# aluguel existente

# Por questão de simplicidade vamos assumir que:
# • Cada empréstimo segue apenas um modelo de cobrança (hora, dia ou semana)
# • O cliente pode decidir livremente quantas bicicletas quer alugar
# • Os pedidos de aluguéis só podem ser efetuados se houver bicicletas suficientes disponíveis
# • Não se preocupem quanto a dinheiro em caixa das Lojas nem dos Clientes

# Ao projetar seus objetos você deve se atentar ao que cada classe será responsável por fazer. Entenda o que cada 
# elemento pode fazer e em seguida, abstraia o problema para desenhar as classes e seus métodos. Note que nem tudo 
# que um objeto pode fazer é necessariamente um método desse objeto.
# Utilize a biblioteca datetime para trabalhar com tempo no seu programa.
# Você provavelmente vai querer testar o funcionamento e relação dessas classes. Para isso use um terceiro arquivo 
# que usa pelo menos três instâncias de Cliente e duas de Loja e testa a integração e funcionamento das duas 
# classes. Para facilitar o fluxo das chamadas, use prints em cada método que funcionem como logs. Um bom log 
# consiste em informar de onde ele vem (classe que printou o log), o que ele está fazendo (qual método), com 
# quais informações (os parâmetros recebidos) e o momento que ocorreu. Faça validações, e gere erros caso alguma 
# validação falhe (raise), note que é comum logarmos (neste caso, com o print) quando algum erro ocorreu em nosso 
# sistema.



#usar o datetime como um atributo do aluguel


#criar um arquivo __init__.py
#ele pode ser vazio, não precisa de código, só p n dar algum erro. Alguns programas mais novos não dá erro, outros sim

# %%write_file './classeLoja.py'

# class Loja:
#     def __init__(self) -> None:
#         pass


        

