import emoji
from time import sleep


num = int(input('Digite seu Número para Fatorar: '))
c = num
f = 1
print('Calculando {}! = ' .format(num), end='')
sleep(1)
while c > 0:
    print('{}' .format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print('{}' .format(f))
print(emoji.emojize(':fox:'))
