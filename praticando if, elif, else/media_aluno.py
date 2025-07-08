#calculando a media final do aluno

nota1 = float(input('Digite a primeira nota do aluno:\n'))
nota2 = float(input('Digite a segunda nota do aluno:\n'))
nota3 = float(input('Digite a terceira nota do aluno:\n'))

media_final = (nota1 + nota2 + nota3) / 3 #calculo média final do aluno

if media_final >= 7: #se a nota for maior ou igual a 7
    print(f'Sua nota é: {media_final:.1f}. Aprovado!')
elif 5 <= media_final < 7: #se a nota for maior ou igual a 5, ou menor ue 7
    print(f'Sua nota é: {media_final:.1f}. Recuperação')
elif media_final < 5: #se a nota for menor que 5
    print(f'Sua nota é: {media_final:.1f}. Reprovado!')
else:
    print('Ops, algo deu errado! Tente novamente') #se houver algum erro

