import random
import emoji
from random import randint
from time import sleep

numeros = (randint(0, 20), randint(0, 20), randint(0, 20), randint(0, 20), randint(0, 20))
print('Os Valores Sorteado foram: ')
sleep(0.5)
for n in numeros:
    print(f'{n}', end=' ')

print(f'\nO maior valor foi o {max(numeros)}')
print(f'O menor valor foi o {min(numeros)}')
print(emoji.emojize(':fox:'))
