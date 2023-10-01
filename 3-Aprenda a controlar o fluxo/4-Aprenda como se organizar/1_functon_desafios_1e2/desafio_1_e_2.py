def gerar_nome_completo(nome, sobrenome):
    print(f'Seja bem-vindo(a) {nome} {sobrenome}')


def calcular_valores(price, qtd_product=1):
    result = str(price*qtd_product)
    print(f'O produto do preço pela quantidade é: {result.format(2)}')


nome = input("Digite seu primeiro nome:\n")
sobrenome = input("Digite seu sobrenome:\n")
gerar_nome_completo(nome, sobrenome)

price = float(input("Insira o preço do produto:\n"))
qtd_product = float(input("Insira a quantidade do produto:\n"))
calcular_valores(price, qtd_product)
