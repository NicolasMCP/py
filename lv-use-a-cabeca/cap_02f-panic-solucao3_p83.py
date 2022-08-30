frase_str = "Don't panic!"
frase = list(frase_str)  # frase agora e uma lista, type('list')
print(f"frase_str: {frase_str}")
print(f"frase    : {frase}")

nova_frase = ''.join(frase[1:3])
print(f"pre      : {nova_frase}")
nova_frase = nova_frase + ''.join([frase[5], frase[4], frase[7], frase[6]])

print(f"frase     : {frase}")
print(f"nova_frase: {nova_frase}")
