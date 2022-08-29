# coloca na variável palavra a string garrafas
palavra = "garrafas"
# loop de 99 até 1 diminuindo 1
for quantas in range(99, 0, -1):
    # imprime o refrão
    print(quantas, palavra, "de Cerveja da parede.")
    # imprime o refrão
    print(quantas, palavra, "de Cerveja.")
    # imprime o refrão
    print("Dece redondo...")
    # imprime o refrão
    print("Faça um giro.")
    # verifica se foi a última garrafa
    if quantas == 1:
        # caso seja a última, informa que não tem mais garrafas
        print("Sem mais Garrafas de Cerveja na parede.")
    # caso contrario seque depois deste else
    else:
        # diminui 1 a quantia para apresentar
        novo_num = quantas - 1
        # se for 1 (somente uma garrafa)
        if novo_num == 1:
            # coloca a palavra no plural
            palavra = "garrafa"
        # imprime o refrão
        print(novo_num, palavra, "de Cerveja na parede.")
    # imprime uma linha em branco
    print()
