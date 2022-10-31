import emoji

pessoas = list()
dados = list()
men = mai = totpessoas = 0

while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso Kg: ')))
    if len(pessoas) == 0:
        men = mai = dados[1]
    else:
        if dados[1] > mai:
            mai = dados[1]
        if dados[1] < men:
            men = dados[1]
    pessoas.append(dados[:])
    dados.clear()
    resp = str(input('Quer Continuar?: [S/N]'))
    if resp in 'N/n':
        break
print('-=-' * 20)
print(f'Você cadastrou ao todo {len(pessoas)}')
print(f'O Maior peso obtido foi o de {mai}Kg. Peso de ', end='')
for p in pessoas:
    if p[1] == mai:
        print(f'[{p[0]}]', end='')
print()
print(f'O Menor peso obtido foi o de {men}Kg. Peso de ', end='')
for p in pessoas:
    if p[1] == men:
        print(f'[{p[0]}]', end='')
print()
print(emoji.emojize(':fox:'))
