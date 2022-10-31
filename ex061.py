import emoji
#V2
print('==' * 10)
print('10 TERMOS DE UMA PA')
print('==' * 10)

termo = int(input('Primeiro Termo: '))
razao = int(input('Razão: '))
decimo = termo
cont = 1

while cont <=10:
    print('{} '.format(decimo), end='→')
    decimo += razao
    cont +=1
print(emoji.emojize(':fox:'))