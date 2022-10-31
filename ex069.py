import emoji

tot18 = totH = tot20 = 0

while True:
    idade = int(input('Qual é sua Idade?: '))
    sexo = ' '
    while sexo is not 'MF':
        sexo = str(input('Qual é o seu Sexo? [M/F]')).strip().upper()[0]
    if idade >= 18:
        tot18 += 1
    if sexo == 'M':
        totH += 1
    if sexo == 'F' and idade >= 20:
        tot20 += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if resp == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {tot18}')
print(f'Ao todo temos {totH} Homens cadastrado.')
print(f'E temos {tot20} Mulheres com menos de 20 Anos')
print(emoji.emojize(':fox:'))