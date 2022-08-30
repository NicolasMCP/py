vocais = ['a', 'e', 'i', 'o', 'u']

palavra = input("Digite o texto a procurar vocais. ")
encontradas = {}
encontradas['a'] = 0
encontradas['e'] = 0
encontradas['i'] = 0
encontradas['o'] = 0
encontradas['u'] = 0

for letra in palavra.lower():
    if letra in vocais:
        encontradas[letra] += 1
for chave, valor in sorted(encontradas.items()):
    print(chave, ">>--->", valor)
