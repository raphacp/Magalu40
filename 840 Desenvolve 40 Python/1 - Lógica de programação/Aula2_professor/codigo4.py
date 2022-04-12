tem_cartao = input("Tem cartão de autorização? (s/n)")
tem_permissao = input("Tem permissão do supervisor? (s/n)")

if tem_cartao == "s" or tem_permissao == "s":
    print("Entrada liberada.")
else:
    print("Entrada bloqueada.")

