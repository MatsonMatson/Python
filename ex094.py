import emoji

pessoa = dict()
galera = list()
soma = media = 0
while True:
    pessoa ['Nome'] = str(input('Nome: '))
    while True:
        pessoa ['Sexo'] = str(input('Sexo: [M/F]')).upper()[0]
        if pessoa['Sexo'] in 'MF':
            break
        print('ERRO! Por Favor, digite apenas M ou F.')
    pessoa['Idade'] = int(input('Idade: '))
    soma += pessoa['Idade']
    galera.append(pessoa.copy())
    while True:
        resp = str(input('Quer Continuar?: [S/N]')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resp == 'N':
        break
print('-=-' * 20)
print(f'Ao todo temos {len(galera)} pessoas cadastradas.')
media = soma / len(galera)
print(f'A Média de idade é de {media:5.2f} anos.')
print('As mulheres cadastrada foram ', end='')
for p in galera:
    if pessoa['Sexo'] in 'F':
        print(f'{p["Nome"]}', end='')
print()
print('Lista das pessoas que estão acima da média: ')
for p in galera:
    if p['Idade'] >= media:
        print('  ', end='')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
print('<<<ENCERRADO>>>')
print(emoji.emojize(':fox:'))
