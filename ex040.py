import emoji
from time import sleep

cores = {'azul':'033[34m',
            'amarelo':'033[33m',
                'lilas':'033[35m',
                    'vermelho':'033[31m'}

n1 = float(input('Primeira Nota: '))
n2 = float(input('Segunda Nota: '))

media = (n1 + n2)/2

if media <=5:
    print('Quem tirou as Notas {} e {} tem sua média de...' .format(n1, n2))
    sleep(1)
    print(media)
    print('Infelizmente você foi...')
    sleep(0.5)
    print('\033[31mREPROVADO\033[m')
elif media <= 6.9:
    print('Quem tirou as Notas {} e {} tem sua média de...'.format(n1, n2))
    sleep(1)
    print(media)
    print('Infelizmente você está de...')
    sleep(0.5)
    print('\033[33mRECUPERAÇÃO\033[m')
else:
    print('Quem tirou as Notas {} e {} tem sua média de...'.format(n1, n2))
    sleep(1)
    print(media)
    print('Parábens você foi...')
    sleep(0.5)
    print('\033[34mAPROVADO\033[m')

print(emoji.emojize(':fox:'))
