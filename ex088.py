from random import randint
from time import sleep
import emoji

num = randint(1, 60)
cont = 0
lista = list()
jogos = list()
print('-=-' * 30)
print('    JOGO DA MEGA SENA   ')
print('-=-' * 30)
quant = int(input('Quantos Jogos você quer que eu Sorteie?: '))
tot = 0
while tot <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print('-=' * 3, f'Sorteando {quant} JOGOS ', '=-' * 3)
for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
    sleep(1)
print('-=' * 5, '< BOA SORTE! >', '=-' * 5)
print(emoji.emojize(':fox:'))