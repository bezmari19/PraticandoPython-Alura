#limite para despesas do usuario

LIMITE = 3000 #coonstante que verifica o limite do orçamento

total_despesas = float(input('Digite o total de despesas do mês (R$):\n')) #variavel que verifica o valor total das despesas

if total_despesas < LIMITE: #se o total for menor que o limite
    print(f'Seu saldo em conta ficará: {LIMITE - total_despesas:.2f}. Parabéns, você economizou!') #exibe o parabéns e o quanto sobrou no orçamento
elif total_despesas == LIMITE: #se o valor for igual ao limite
    print('Você usou todo o orçamento. Tente economizar da próxima vez!') #exibe uma mensagem que fala ao usuario que ele usou tudo e da a dica de economia
else: #qualquer uma que não seja as duas primeiras (espera-se que seja valor maior que o orçamento)
    print('Atenção! Você ultrapassou o limite do orçamento.') #exibe o alerta que ultrapassou o limite