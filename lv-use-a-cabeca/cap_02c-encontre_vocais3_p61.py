vocais = ['a', 'e', 'i', 'o', 'u']

palavra = input("Digite o texto a procurar vocais. ")
encontradas = []

for letra in palavra.lower():
    if letra in vocais:
        if letra not in encontradas:
            encontradas.append(letra)
for vocal in encontradas:
    print(vocal)
