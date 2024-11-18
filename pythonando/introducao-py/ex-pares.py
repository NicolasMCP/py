# Receba um número e mostre todos os números pares de 0 até o número digitado

top = int(input('Números pares de 0-'))
i = 0
while i < top:
    i += 1
    if i % 2 == 0:
        print(i,end=' ')
print()