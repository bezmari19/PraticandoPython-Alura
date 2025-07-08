#calculo pedagio

distancia = int(input('Digite a distancia percorrida:\n'))

if distancia < 100: #se a distancia percorrida for menor que 100km
    print(f'A distancia percorrida foi {distancia}. Valor: R$10,00') #exibe o valor correspondente e confirma o que foi digitado pelo usuário
elif 100 <= distancia < 200: #se a distancia for entre 100 e 200
    print(f'A distancia percorrida foi {distancia}. Valor: R$20,00') #exibe o valor correspondente e confirma o que foi digitado pelo usuário
elif distancia > 200: #se a distancia percorrida for maior que 200
    print(f'A distancia percorrida foi: {distancia}. Valor: R$30,00') #exibe o valor correspondente e confirma o que foi digitado pelo usuário