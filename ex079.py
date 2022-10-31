import emoji

numeros = list()

while True:
    n = int(input('Digite um Valor: '))
    if n not in numeros:
        numeros.append(n)
        print('Valor Adicionado com Sucesso...')
    else:
        print('Valor Duplicado!, Não foi adicionado...')
    r = str(input('Você quer continuar? [S/N]'))
    if r in 'Nn':
        break
print('\033[31m-=-\033[m' * 15)
print(f'Você digitou os números {numeros}')
print(emoji.emojize(':fox:'))