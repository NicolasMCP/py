vocais = ['a', 'e', 'i', 'o', 'u']

palavra = input("Digite o texto a procurar vocais. ")

for vocal in vocais:
    if vocal in palavra.lower():
        print(vocal)
