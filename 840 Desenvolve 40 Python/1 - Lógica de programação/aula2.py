# 14/01/2022
# Pesquisa de satisfação

nota_do_servico = int(input("Dê uma nota de 0 a 10: "))

if nota_do_servico < 5:
    print("Poxa! Que pena que o serviço não foi satisfatório. Vamos melhorar.")
elif nota_do_servico < 8:
    print("Parece que o serviço foi bom, mas não excelente. Vamos melhorar.")
else:
    print("Que bom que o serviço foi muito bom!")

print(f"A nota dada foi {nota_do_servico}. Obrigado pelo feedback!")