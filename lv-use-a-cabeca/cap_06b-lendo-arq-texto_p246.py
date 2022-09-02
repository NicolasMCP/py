arquivo = open('todos.txt')
for linha in arquivo:
    print(linha, end='')
arquivo.close()
