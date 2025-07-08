#calculando os dados do usuario

peso = float(input('Digite o peso atual (kg):\n'))
altura = float(input('Digite o altura atual (m):\n'))

imc = peso / (altura**2) #calculo IMC

if imc < 18.5: #se o IMC for menor que esse valor
    print(f'Seu IMC é: {imc:.2f}. Você está abaixo do peso.') #exibe essa mensagem
elif 18.5 <= imc < 25: #se o IMC for maior ou igual ou menor que 25
    print(f'Seu IMC é: {imc:.2f}. Seu peso está dentro da normalidade.') #exibe essa mensagem
elif imc >= 25: #se o IMC for igual ou maior que o 25
    print(f'Seu IMC é: {imc:.2f}. Você está acima do peso') #exibe essa mensagem
else:
    print('Ops, talvez tenha dado algo errado. Tente novamente colocando as informações corretamente') #caso o usuario coloque alguma informação incorreta



