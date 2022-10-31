import emoji
from random import randint

computador = randint(0, 10)
print('\033[31m-=-\033[m' * 20)
print('Sou seu \033[36mcomputador...\033[m')
print('Vou pensar em um Número de 0 até 10. Tente adivinhar...')
print('Será quer você consegue adivinhar?')
print('\033[31m-=-\033[m' * 20)

acertou = False
palpite = 0

while not acertou:
    jogador = int(input('Qual seu Palpite?: '))
    palpite += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente mais uma vez!')
        elif jogador > computador:
            print('Menos... Tente mais uma vez!')
print('Acertou com {} tentativas, Parábens!!' .format(palpite))
print(emoji.emojize(':fox:'))
