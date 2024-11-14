# Exemplo:
# Digamos que você está analisando as vendas do Banco de Dados de um e-commerce.
# Em um determinado dia, você extraiu as vendas do Banco de Dados e elas vieram nesse formato:

vendas = [
    ('20/08/2020', 'iphone x', 'azul', '128gb', 350, 4000),
    ('20/08/2020', 'iphone x', 'prata', '128gb', 1500, 4000),
    ('20/08/2020', 'ipad', 'prata', '256gb', 127, 6000),
    ('20/08/2020', 'ipad', 'prata', '128gb', 981, 5000),
    ('21/08/2020', 'iphone x', 'azul', '128gb', 397, 4000),
    ('21/08/2020', 'iphone x', 'prata', '128gb', 1017, 4000),
    ('21/08/2020', 'ipad', 'prata', '256gb', 50, 6000),
    ('21/08/2020', 'ipad', 'prata', '128gb', 4000, 5000),
]

# - Qual foi o faturamento de IPhone no dia 20/08/2020?

faturamento = 0
for data, produto, cor, capacidade, unidades, valor_unitario in vendas:
    if produto == 'iphone x' and data == '20/08/2020':
        faturamento += unidades * valor_unitario

# print('O faturamento de IPhone no dia 20/08/2020 foi de {}'.format(faturamento))
print(f'O faturamento de IPhone no dia 20/08/2020 foi de {faturamento}')


# - Qual foi o produto mais vendido (em unidades) no dia 21/08/2020?

mais_produto = ''
mais_unidades = 0
mais_cor = ''
for data, produto, cor, capacidade, unidades, valor_unitario in vendas:
    if data == '21/08/2020' and unidades > mais_unidades:
        mais_unidades = unidades
        mais_produto = produto
        mais_cor = cor
print(f'O produto mais vendido foi o \'{mais_produto}\' na cor \'{cor}\' do qual foram vendidas {mais_unidades} unidades\n')


