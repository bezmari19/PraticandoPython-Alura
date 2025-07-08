# Qual vendeu mais?

macas = int(input('Quantas maças foram vendidas?\n')) #variável que recebe o numero de maças
bananas = int(input('Quantas bananas foram vendidas?\n')) #variável que recebe o número de bananas

if macas > bananas: #se o número de maças vendidas for maior que o número de bananas
    print('As maças tiveram mais vendas.') #exibe ao usuario a seguinte mensagem
elif macas < bananas: #se o número de bananas vendidas for maior que o número de maças
    print('As bananas tiveram mais vendas.') #exibe a seguinte mensagem ao usuario
else: #se não for nenhuma das duas primais condicionais (espera-se que sejam iguais)
    print('As vendas tiveram empate') #exibe a seguinte mensagem