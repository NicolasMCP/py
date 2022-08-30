vocais = set('aeiou')

palavra = input("Digite o texto a procurar vocais. ")
encontradas = vocais.intersection(set(palavra))

for vocal in sorted(encontradas):
    print(vocal)
