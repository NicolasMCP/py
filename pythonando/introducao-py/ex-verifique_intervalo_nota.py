# Escreva um programa que receba notas de um aluno (0-10), caso a nota
# esteja fora desse intervalo peça para o professor digitar novamente

while True:
    nota = int(input('Digite a nota no intervalo (0-10): '))
    if nota < 0:
        print('A nota não pode ser inferior a Zero, corrija.')
    elif nota > 10:
        print('Você digitou uma nota maior que 10, corrija.')
    else:
        break
print(nota)












