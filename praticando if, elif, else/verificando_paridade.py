#se for par ou impar

numero_escolhido = int(input('Digite um número inteiro:\n'))

calculo = numero_escolhido % 2 #calculo que verifica o restante em inteiro

if calculo == 0: #se o restante for 0
    print(f'O número {numero_escolhido} é par.') #exibe que é par
else: #se for diferente de 0 (1)
    print(f'O número {numero_escolhido} é impar.') #exibe que é ímpar