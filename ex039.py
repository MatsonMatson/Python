import emoji
from datetime import date

cores = {'azul':'033[34m',
            'amarelo':'033[33m',
                'lilas':'033[35m',
                    'vermelho':'033[31m'}

ano = int(input('Ano de Nascimento: '))
atual = date.today().year
idade = atual - ano

print('Quem Nasceu em {} tem {} anos em {}'.format(ano, idade, atual))
if idade == 18:
    print('Você tem que se Alistar \033[31mIMEDIATAMENTE!!\033[m')
elif idade <= 17:
    saldo = 18 - idade
    print('Ainda Faltam \033[31m{}\033[m para você se Alistar' .format(saldo))
    ano = atual + saldo
    print('Seu Alistamento será em \033[31m{}\033[m' .format(ano))
else:
    saldo = idade - 18
    print('Você já deveria ter se alistado há \033[31m{}\033[m' .format(saldo))
    ano = atual - saldo
    print('Seu Alistamento foi em \033[33m{}\033[m' .format(ano))

print(emoji.emojize(':fox:'))
