#calculo de aprovação de empréstimo

RENDA_LIMITE = 2000 #constante para verificar se é maior que 2000
PARCELA = 0.3 #constante para verificar se é maior que %30

valor_renda = int(input('Qual o valor da renda?\n'))
valor_parcela = int(input('Qual o valor da parcela?\n'))

if valor_renda > RENDA_LIMITE and valor_parcela <= PARCELA * valor_renda: #se o valor da renda for maior que o minimo
#e se o valor da parcela vezes o valor da renda é maior ou igual ao valor da parcela definida
    print("Empréstimo aprovado!")
elif valor_renda <= RENDA_LIMITE: #se o valor da renda for menor ou igual ao limite
    print("Empréstimo negado: renda insuficiente.")
else: #se não atender a nenhuma das condicionais acima
    print("Empréstimo negado: parcela acima de 30% da renda.")



