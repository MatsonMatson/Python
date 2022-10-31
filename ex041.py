import emoji
from datetime import date

cores = {'azul':'033[34m',
            'amarelo':'033[33m',
                'lilas':'033[35m',
                    'vermelho':'033[31m'}

nasc = int(input('Ano de Nascimento: '))
atual = date.today().year
idade = atual - nasc

if idade <= 9:
    print('O Atleta tem \033[31m{}\033[m anos.' .format(idade))
    print('\033[31mATLETA MIRIM\033[m')
elif idade <= 14:
    print('O Atleta tem \033[33m{}\033[m anos.' .format(idade))
    print('\033[33mATLETA INFANTIL\033[m')
elif idade <= 19:
    print('O Atleta tem \033[35m{}\033[m anos.'.format(idade))
    print('\033[35mATLETA JÚNIO\033[m')
elif idade <= 25:
    print('O Atleta tem \033[33m{}\033[m anos.'.format(idade))
    print('\033[33mATLETA JÚNIOR\033[m')
else:
    print('O Atleta tem \033[31m{}\033[m anos.'.format(idade))
    print('\033[31mMASTER\033[m')

print(emoji.emojize(':fox:'))
