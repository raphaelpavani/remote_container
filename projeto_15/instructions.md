# Projeto 1

## Objetivo de projeto

### Estamos criando um módulo de **login** do nosso aplicativo, e você deve obter as seguintes informações do funcionário.

## Módulo 1 - Gerar registro do funcionário

### Funcionalidades do módulo 1

```python
from datetime import datetime
import random
```



1. Obtenha o nome do usuário

   ```python
   name = input("Por favor, insira o seu nome:")
   ```

   

2. Obtenha a idade do usuário

   ```python
   age = int(input("Por favor, insira sua idade:"))
   ```

   

3. Registre de forma automática a data do cadastro do usuário, usando a data do registro como data de registro

   ```python
   register = datetime.now()
   ```

   

4. Para cada novo funcionário que é registrado na empresa, ele recebe um dos seguintes cartões, que é sorteado de forma aleatória:

```python
cartoes = ['R$50,00','R$250,00','R$120,00']
```

5. Guarde informações sobre a data de aniversário do funcionário. **(dd/mm/aaaa)**
   
   ```python
   birthday = datetime.strptime(
       input("Por favor insira sua data de nascimento dia/mês/ano:"), '%d/%m/%Y')
   ```
   
   

## Módulo 2 - Gerar apresentação do usuário

### Funcionalidades do módulo 2 - Mensagem de boas vindas!


Usando os dados obtidos no módulo 1, exiba as seguintes informações:

1. Olá (nome do usuário), seu registro foi concluído com sucesso no dia(data de cadastro no formato **dd/mm/aaaa**).

Parabéns, houve um sorteio e você ganhou um cartão de compras no valor de (valor sorteado).

```python
print(f'''Olá {name}, o seu registro foi concluído com sucesso no dia {register.day}/{register.month}/{register.year}
          Parabéns, houve um sorteio e você ganhou um cartão de compras no valor de {random.choice(cartoes)}.'''
      )
```

