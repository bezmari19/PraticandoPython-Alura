#calculo pedagio

distancia = int(input('Digite a distancia percorrida:\n'))

if distancia < 100:
    print(f'A distancia percorrida foi {distancia}. Valor: R$10,00')
elif 100 <= distancia < 200:
    print(f'A distancia percorrida foi {distancia}. Valor: R$20,00')
elif distancia > 200:
    print(f'A distancia percorrida foi: {distancia}. Valor: R$30,00')