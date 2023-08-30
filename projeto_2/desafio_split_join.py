# ​Desafio 1: Transforme a frase1 em uma lista de palavras e guarde o resultado em uma variável chamada palavras1
# frase1 = 'Desafio manipulação de strings'
# frase2 = 'jhonatan,rafael,carol,camilla'
frase1 = 'Desafio manipulação de strings'
frase2 = 'jhonatan,rafael,carol,camilla'
palavra_1 = frase1.split()
# Desafio 2: Transforme a frase2 em uma lista de palavras e guarde o resultado em uma variável chamada palavras2
palavra_2 = frase2.split(',')
# Desafio 3: Pegue o palavras1 e transforme elas no seguinte string: "Desafio,manipulação,de,strings". Imprima o resultado no console.
print(','.join(palavra_1))
# Desafio 4: Pegue o palavras2 e transforme elas no seguinte string: frase2 = "jhonatan & rafael & carol & camilla". Imprima o resultado no console.
frase2 = ' & '.join(palavra_2)
print(frase2)
