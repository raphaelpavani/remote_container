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
