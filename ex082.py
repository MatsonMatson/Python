import emoji


impares = []
pares = []
numeros = []

while True:
    numeros.append(int(input('Digite um Número: ')))
    resp = str(input('Você Deseja Continuar?: [S/N]'))
    if resp == 'Nn':
        break
for i, v in enumerate(numeros):
    if v % 2 == 0:
        pares.append(v)
    else:
        impares.append(v)
print('-=-' * 30)
print(f'A Lista completa é {numeros}')
print(f'A Lista dos Pares é {pares}')
print(f'A Lista dos Impares é {impares}')
print(emoji.emojize(':fox:'))

