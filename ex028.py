import emoji
from random import randint
from time import sleep

computador = randint (0, 5)
print('-=-' * 20)
print('Vou pensar em um Número de 0 até 5. Tente adivinhar...')
print('-=-' * 20)

jogador = int(input('Em que número eu pensei?: '))

print('PROCESSANDO...')
sleep(2)

if jogador == computador:
    print('PARABÉNS! Você me venceu dessa vez.')
else:
    print('GANHEI! Eu pensei no Número {} e não no {}' .format(computador, jogador))
print('Quem sabe na próxima!!')

print(emoji.emojize(':fox:'))
