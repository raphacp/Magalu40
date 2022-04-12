quer_salvar = input("Deseja salvar o arquivo? (s/n) ")
quer_backup = input("Deseja fazer um backup? (s/n) ")

if quer_salvar == "s" and quer_backup == "s":
    print("Salvando e gerando backup...")
elif quer_salvar == "s" and quer_backup == "n":
    print("Salvando...")
elif quer_salvar == "n" and quer_backup == "s":
    print("Gerando backup...")
else:
    print("Nenhuma operação feita.")

print("Concluido.")