resposta_cartao = input("Tem cartão? (s/n)")
resposta_permissao = input("Tem permissão? (s/n)")

tem_cartao = (resposta_cartao == "s")
tem_permissao = (resposta_permissao == "s")

if tem_cartao or tem_permissao:
    print("Entrada liberada.")
else:
    print("Entrada bloqueada.")

