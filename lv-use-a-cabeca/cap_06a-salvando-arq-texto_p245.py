todos = open('todos.txt', 'a')
print('Jogue fora o lixo.', file=todos)
print('Alimente o gato.', file=todos)
print('Preparar declaração de imposto.', file=todos)
todos.close()