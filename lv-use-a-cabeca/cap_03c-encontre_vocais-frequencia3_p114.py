vocais = ['a', 'e', 'i', 'o', 'u']

palavra = input("Digite o texto a procurar vocais. ")
encontradas = {}

for letra in palavra.lower():
    if letra in vocais:
        if letra not in encontradas:
            encontradas[letra] = 0
        encontradas[letra] += 1
for chave, valor in sorted(encontradas.items()):
    print(chave, ">>--->", valor)
