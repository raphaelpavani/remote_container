# ​​# DESAFIO 🥇

# Calcule quantos dias faltam até o seu aniversário
from datetime import datetime
data_aniversario = datetime.strptime(
    input("Digite a data do aniversário:"), '%d/%m/%Y')
print(f'Os dias são: {(data_aniversario - datetime.now()).days}')
