from turtle import Turtle
t = Turtle()
t.speed(1)

while True:
    distancia = int(input('Distância a percorrer:\n'))
    direcao = input(
        'Para qual direção devemos ir? - Para frente(f) para trás(t):')
    rotacao = input(
        'Para direita(d), para a esquerda(e), não rotacionar(n):')
    continua = input("Deseja continuar andando? (s)im ou (n)ao")
    if continua == 's':
        continue
    else:
        continua == 'n'
    break

    t.forward(distancia)
    t.right(distancia)
    t.forward(distancia)
