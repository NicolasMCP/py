arquivo = open('todos.txt', 'a')
print('Linhas extras.', file=arquivo)
print('Mais uma para teste.', file=arquivo)
arquivo.close()
