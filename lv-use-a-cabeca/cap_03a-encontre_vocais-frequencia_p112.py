vocais = ['a', 'e', 'i', 'o', 'u']

palavra = input("Digite o texto a procurar vocais. ")
encontradas = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}

for letra in palavra.lower():
    if letra in vocais:
        encontradas[letra] += 1
for vocal in sorted(encontradas):
    print(vocal, ">>--->", encontradas[vocal])
