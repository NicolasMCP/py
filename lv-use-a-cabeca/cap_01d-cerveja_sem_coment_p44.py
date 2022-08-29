palavra = "garrafas"
for quantas in range(99, 0, -1):
    print(quantas, palavra, "de Cerveja da parede.")
    print(quantas, palavra, "de Cerveja.")
    print("Dece redondo...")
    print("Faça um giro.")
    if quantas == 1:
        print("Sem mais Garrafas de Cerveja na parede.")
    else:
        novo_num = quantas - 1
        if novo_num == 1:
            palavra = "garrafa"
        print(novo_num, palavra, "de Cerveja na parede.")
    print()
