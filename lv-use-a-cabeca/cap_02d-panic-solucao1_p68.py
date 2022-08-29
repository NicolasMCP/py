frase_str = "Don't panic!"
frase = list(frase_str)  # frase agora e uma lista, type('list')
print(f"frase_str : {frase_str}")
print(f"frase     : {frase}")

for x in range(4):
    frase.pop()          # apaga último objeto da lista
frase.pop(0)             # apaga objeto (0) primeiro da lista
frase.remove("'")        # apaga apóstrofo
print(f"pre insert: {frase}")
frase.insert(2, frase.pop(3))
print(f"pos insert: {frase}")
frase.append(frase.pop(4))  # apaga o 'p' e insere no final

nova_frase = ''.join(frase)
print(f"frase     : {frase}")
print(f"nova_frase: {nova_frase}")
