# IMPORTANTE:
# Solução só por curiosidade para quem solicitou,
# este conteúdo não foi abordado em aula.

from datetime import datetime # Incluímos a biblioteca datetime
agora = datetime.now() # Chamamos a função now() da biblioteca datetime

# Separamos cada pedaço que precisamos
ano = agora.year
mes = agora.month
dia = agora.day
hora = agora.hour
minuto = agora.minute
segundo = agora.second

# Imprimimos o resultado 
# (Obs: o sep="" quer dizer que o print não vai inserir um espaço entre cada uma das saídas)
print(dia, "/", mes, "/", ano, " ", hora, ":", minuto, ":", segundo, sep="")
