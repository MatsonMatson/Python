import emoji

aluno = dict()
aluno ['Nome'] = str(input('Nome:'))
aluno ['Média'] = float(input('Digite sua Média: '))
print(f'O nome do Aluno é {aluno["Nome"]}')
print(f'A sua média é {aluno["Média"]}')
if aluno['Média'] >= 7:
    print('Situação APROVADA')
elif aluno['Média'] >= 5:
    print('Situação RECUPERAÇÃO')
else:
    print('Situação REPROVA')
#for k, v in aluno.items():
    #print(f'{k} é igual a {v}')
print(emoji.emojize(':fox:'))
