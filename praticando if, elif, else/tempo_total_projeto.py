# quanto tempo tem o projeto?
diasA = int(input('Quantos dias para o primeiro projeto?\n')) #variavel que lê os dias pro primeiro projeto
diasB = int(input('Quantos dias para o segundo projeto?\n')) #variavel que lê os dias pro segundo projeto
diasC = int(input('Quantos dias para o terceiro projeto?\n')) #variavel que lê os dias pro terceiro projeto

if diasA < 0 or diasB < 0 or diasC < 0: #se um dos dias dos projetos for menor que zero (negativo)
    print('Erro: Os números não podem ser negativos') #exibe o erro
else:
    print(f'O total de dias para as atividades é de: {diasA+diasB+diasC}.') #se forem numeros positivos (maiores que zero) exibe a soma de dias