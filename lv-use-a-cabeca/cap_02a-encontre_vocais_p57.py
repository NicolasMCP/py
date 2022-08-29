vocais = ['a', 'e', 'i', 'o', 'u']

palavra = "Ana Paula"

for vocal in palavra.lower():
    if vocal in vocais:
        print(vocal)
