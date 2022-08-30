vocais = ['a', 'e', 'i', 'o', 'u']

palavra = input("Digite o texto a procurar vocais. ")
encontradas = {}

for letra in palavra.lower():
    if letra in vocais:
        if letra in encontradas:
            encontradas[letra] += 1
        else:
            encontradas[letra] = 1
for chave, valor in sorted(encontradas.items()):
    print(chave, ">>--->", valor)
