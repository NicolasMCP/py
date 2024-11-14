# 2. Comparação com Ano Anterior
#    Digamos que você está analisando as vendas de produtos de um ecommerce e quer identificar quais 
#    produtos tiveram no ano de 2020 mais vendas do que no ano de 2019, para reportar isso para a diretoria.
#    Sua resposta pode ser um print de cada produto, qual foi a venda de 2019, a venda de 2020 e 
#    o % de crescimento de 2020 para 2019.
#    Lembrando, para calcular o % de crescimento de um produto de um ano para o outro, podemos fazer: 
#       (venda2020/venda2019 - 1)
#    A lógica da tupla é: (produto, vendas2019, vendas2020)

vendas_produtos = [('iphone', 558147, 951642), 
                   ('galaxy', 712350, 244295), 
                   ('ipad', 573823, 26964), 
                   ('tv', 405252, 787604), 
                   ('máquina de café', 718654, 867660), 
                   ('kindle', 531580, 78830), 
                   ('geladeira', 973139, 710331), 
                   ('adega', 892292, 646016), 
                   ('notebook dell', 422760, 694913), 
                   ('notebook hp', 154753, 539704), 
                   ('notebook asus', 887061, 324831), 
                   ('microsoft surface', 438508, 667179), 
                   ('webcam', 237467, 295633), 
                   ('caixa de som', 489705, 725316), 
                   ('microfone', 328311, 644622), 
                   ('câmera canon', 591120, 994303)]

print(*[f'Produto {produto} em 2019 vendido {venda2019} em 2020 vendido {venda2020} o crescimento foi de {(venda2020 / venda2019 - 1):.1%}' for produto, venda2019, venda2020 in vendas_produtos if venda2020 > venda2019], sep='\n')

