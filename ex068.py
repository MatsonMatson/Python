import emoji
from time import sleep
from random import randint

v = 0

while True:
    jogador = int(input('Diga um Valor: '))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = ' '
    sleep(0.5)
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar?: [P/I]')).strip().upper()
    print(f'Você jogou {jogador} e o Computador {computador} e o total foi de {total}')
    sleep(1)
    if tipo == 'P':
        if total % 2 == 0:
            print('Você Venceu!')
            v += 1
        else:
            print('Você Perdeu!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você Venceu!')
            v += 1
        else:
            print('Você Perdeu!')
            break
    print('Vamos Jogar Novamente...')
print(f'GAME OVER! Você venceu {v} vezes...')
print(emoji.emojize(':fox:'))
