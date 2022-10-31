import emoji

print('=' * 30)
print('{:^20}'.format('BANCO MONKY'))
print('=' * 30)

valor = int(input('Qual valor você deseja sacar? R$: '))
total = valor
ced = 50
totced = 0
while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        print(f'Total de {totced} Cédulas de R${ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 1
        elif ced == 1:
            ced =1
            break
print(emoji.emojize(':fox:'))