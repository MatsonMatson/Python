import emoji
from random import randint
from time import sleep
from operator import itemgetter
jogos = {'Jogador 1º': randint(1, 6),
         'Jogador 2º': randint(1, 6),
         'Jogador 3º': randint(1, 6),
         'Jogador 4º': randint(1, 6)}
ranking = dict()
print('Valores Sorteado:')
for k, v in jogos.items():
    print(f'{k} tirou {v} no dado')
    sleep(0.5)
ranking = sorted(jogos.items(), key=itemgetter(1), reverse=True)
print('-=-' * 20)
print('=====RANKING DOS JOGADORES=====')
for i, v in enumerate(ranking):
    print(f'{i+1}º Lugar: {v[0]} com {v[1]}')
    sleep(0.5)
print(emoji.emojize(':fox:'))
