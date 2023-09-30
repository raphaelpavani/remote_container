estilos = ['Hip-Hop', 'Rock', 'Rap', 'Pop']
print("Desafio 1:")
for estilo in estilos:
    if estilo == 'Rap':
        continue
    print(estilo)
print("\nDesafio 2: ")
for estilo in estilos:
    if estilo == 'Rock':
        break
    print(estilo)
