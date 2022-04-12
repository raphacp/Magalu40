import classeLoja
import classeCliente
import datetime as dt

loja_1 = classeLoja.Loja("Rapha's Bike", 10)
print(loja_1)

loja_2 = classeLoja.Loja("Pedro Bike", 20)
print(loja_2)

cliente_1 = classeCliente.Cliente("Rapha")
print(cliente_1)

cliente_2 = classeCliente.Cliente("Eduardo")
print(cliente_2)

cliente_3 = classeCliente.Cliente("Paula")
print(cliente_3)

cliente_1.ver_estoque(loja_1)
cliente_1.ver_estoque(loja_2)

cliente_2.ver_estoque(cliente_2)

cliente_1.alugar_bicicleta(loja_1, 4, 's', dt.datetime(2021, 2, 11, 17, 34))

cliente_1.alugar_bicicleta(loja_2, 2, 's', dt.datetime(2021, 2, 11, 17, 34))

cliente_2.alugar_bicicleta(cliente_1, 4, 's', dt.datetime(2021, 2, 11, 17, 34))

cliente_2.alugar_bicicleta(loja_2, '4', 'd', dt.datetime(2021, 2, 11, 17, 34))

cliente_2.alugar_bicicleta(loja_2, 4, 5, dt.datetime(2021, 2, 11, 17, 34))

cliente_2.alugar_bicicleta(loja_2, 4, 'd', 2021/2/11)

cliente_2.alugar_bicicleta(loja_2, 4, 'd', dt.datetime(2021, 2, 11, 17, 34))

cliente_3.alugar_bicicleta(loja_1, 11, 'h', dt.datetime(2021, 2, 11, 17, 34))

cliente_3.alugar_bicicleta(loja_1, 1, 'a', dt.datetime(2021, 2, 11, 17, 34))

cliente_3.alugar_bicicleta(loja_1, 2, 'h', 2021/2/11)

cliente_3.alugar_bicicleta(loja_2, 1, 'h', dt.datetime(2021, 2, 11, 17, 34))

cliente_1.devolver_bicicleta(dt.datetime(2021, 12, 25, 17, 34, 1))

cliente_2.devolver_bicicleta(2021/12/25)

cliente_2.devolver_bicicleta(dt.datetime(2021, 12, 25, 17, 34, 1))

cliente_3.devolver_bicicleta(dt.datetime(2021, 12, 25, 17, 34, 1))

