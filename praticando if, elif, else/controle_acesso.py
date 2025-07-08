#controle de acesso do escritório

ENTRADA = 8 #constante que verifica o horário de entrada
SAIDA = 18 #constante que verifica o horário de saida

entrada_funcionario = int(input('Digite a hora atual (formato 24 horas):\n')) #variavel que verifica a entrada do funcionário

if entrada_funcionario < ENTRADA: # se a entrada do funcionário for antes das 8
    print('Acesso negado')
elif ENTRADA <= entrada_funcionario < SAIDA: #se a entrada do funcionário for depois das 8 e as das 18
    print('Acesso permitido')
elif entrada_funcionario >= SAIDA: #se a entrada for as 18 ou depois das 18
    print('Acesso negado')
else:
    print('Ops, talvez tenha dado algo errado. Digite o horario corretamente!') #se nenhuma das condicionais forem atendidas
