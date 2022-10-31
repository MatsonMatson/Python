import emoji
#V3
print('==' * 10)
print('10 TERMOS DE UMA PA')
print('==' * 10)

termo = int(input('Primeiro Termo: '))
razao = int(input('Razão: '))
decimo = termo
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} '.format(decimo), end='→')
        decimo += razao
        cont +=1
    print(' PAUSA')
    mais = int(input('Quantos termos você quer mostra a mais?: '))
print('Progressão finalizada com {} termos.' .format(total))
print(emoji.emojize(':fox:'))
