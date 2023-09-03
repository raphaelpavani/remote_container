from datetime import datetime
import random

name = input("Por favor, insira o seu nome:")
age = int(input("Por favor, insira sua idade:"))
register = datetime.now()
cartoes = ['R$50,00', 'R$250,00', 'R$120,00']
birthday = datetime.strptime(
    input("Por favor insira sua data de nascimento dia/mês/ano:"), '%d/%m/%Y')

# MÓDULO 2
print(f'''Olá {name}, o seu registro foi concluído com sucesso no dia {register.day}/{register.month}/{register.year}
          Parabéns, houve um sorteio e você ganhou um cartão de compras no valor de {random.choice(cartoes)}.'''
      )
