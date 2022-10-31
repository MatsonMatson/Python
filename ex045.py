import emoji
from time import sleep
from random import randint

cores = {'azul': '033[34m',
            'amarelo': '033[33m',
                'lilas': '033[35m',
                    'vermelho': '033[31m',
                        'ciano': '033[36'}

print('''SUAS OPÇÕES: 
[0]\033[33mPEDRA\033[m
[1]\033[31mPAPEL\033[m
[2]\033[34mTESOURA\033[m''')

sleep(1)
itens = ('PEDRA', 'PAPEL', 'TESOURA')
jogador = int(input('Qual é a sua Jogada? '))
computador = randint(0, 2)
sleep(1)
print('\033[35m-=-\033[m' * 15)
print('O Computador jogou \033[35m{}\033[m' .format(itens[computador]))
print('O Jogador jogou \033[36m{}\033[m' .format(itens[jogador]))
print('\033[35m-=-\033[m' * 15)
sleep(1)

if computador == 0:
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR VENCE')
    elif jogador == 2:
        print('COMPUTDAOR VENCE')
    else:
        print('JOGADA INVÁLIDA')
elif computador == 1:
    if jogador == 0:
        print('COMPUTDAOR VENCE')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR VENCE')
    else:
        print('JOGADA INVÁLIDA')
elif computador == 2:
    if jogador == 0:
        print('JOGADOR VENCE')
    elif jogador == 1:
        print('COMPUTDAOR VENCE')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('JOGADA INVÁLIDA')
print(emoji.emojize(':fox:'))
