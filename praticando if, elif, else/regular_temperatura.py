TEMPERATURA_EXIGIDA = 25 #Constante que verifica o limite permetido da temperatura

temperatura = int(input('Digite a temperatura atual:\n')) #variavel que verifica a temperatura do ambiente

if temperatura < TEMPERATURA_EXIGIDA: #se a temperatura for menor que o limite
    print('Cautela: está abaixo do limite permitido') #exibe essa mensagem
elif temperatura == TEMPERATURA_EXIGIDA: #se a temperatura for a mesma que o limite
    print('Seguro: Está no limite permitido') #exibe essa mensagem
else: #se não for nenhuma das duas condicionais (ou seja, maior que a temepratura limite)
    print('Alerta! A temperatura está acima do limite permitido')  #exibe a mensagem de alerta