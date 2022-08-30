str = "Marvin, the Paranoid Android"
letras = list(str)
for letra in letras[:6]:
    print('\t', letra)
print()
for letra in letras[-7:]:
    print('\t'*2, letra)
print()
for letra in letras[12:20]:
    print('\t'*3, letra)
