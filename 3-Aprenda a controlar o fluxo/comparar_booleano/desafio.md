# Desafio 🥇 da aula 4 - Comparações c/ Operadores

### Quero que você defina as seguintes variáveis, inicialmente todas como False, a ideia aqui não é de se importar com os valores dentro dessas variáveis, mas sim como montar condicionais.

```python
possui_passaporte = False

passagem_comprada = False

menor_de_idade = False
```

### E Crie as seguintes condições usando o que acabou de ver e imprima o resultado na tela. Tente fazer cada condição e depois veja a solução no final deste aula.

1. Uma pessoa só pode viajar se possuir passaporte e tiver a passagem comprada e não for menor de idade

   ```python
   if (possui_passaporte == True and passagem_comprada == True) and menor_de_idade == False:
       print("Pode viajar 1")
   ```

   

2. Uma pessoa só pode viajar se possuir passaporte ou tiver a passagem comprada e não for menor de idade

   ```python
   if (possui_passaporte == True or passagem_comprada == True) and menor_de_idade == False:
       print("Pode viajar 2")
   ```

   

3. Uma pessoa só pode viajar se não possuir passaporte ou tiver a passagem comprada e não for menor de idade

   ```python
   if (possui_passaporte == False or passagem_comprada == True) and menor_de_idade == False:
       print("Pode viajar 3")
   ```

   

4. Uma pessoa não pode viajar se não possuir passaporte ou não tiver a passagem comprada e for menor de idade

   ```python
   if (possui_passaporte == False or passagem_comprada == False) and menor_de_idade == True:
       print("Pode viajar 4")
   ```

   ## Solução completa:

   ```python
   possui_passaporte = False
   
   passagem_comprada = False
   
   menor_de_idade = False
   
   if (possui_passaporte == True and passagem_comprada == True) and menor_de_idade == False:
       print("Pode viajar 1")
   if (possui_passaporte == True or passagem_comprada == True) and menor_de_idade == False:
       print("Pode viajar 2")
   if (possui_passaporte == False or passagem_comprada == True) and menor_de_idade == False:
       print("Pode viajar 3")
   if (possui_passaporte == False or passagem_comprada == False) and menor_de_idade == True:
       print("Pode viajar 4")
   ```
