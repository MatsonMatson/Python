import emoji
import math
from time import sleep

cores = {'azul':'033[34m',
            'amarelo':'033[33m',
                'lilas':'033[35m',
                    'vermelho':'033[31m'}

num = int(input('Digite um Número: '))

print('\033[35m-=-\033[m' * 15)

print('''Escolha uma das Bases para Conversão: ')
[1] para \033[0:33mBINÁRIO\033[m
[2] para \033[0:31mOCTADECIMAL\033[m
[3] para \033[0:34mHEXADECIMAL\033[m''')

print('\033[35m-=-\033[m' * 15)
sleep(2)
escolha = int(input('Digite o Número de sua escolha!'))

if escolha == 1:
    convertido = bin(num)[2:] #fatiamento de string, deixando apenas os números certos
    print('O \033[31m{}\033[m convertido em \033[31m{}\033[m é igual a \033[31m{}\033[m ' .format(num, escolha, convertido))
elif escolha == 2:
    convertido = oct(num)[2:] #fatiamento de string, deixando apenas os números certos
    print('O \033[31m{}\033[m convertido em \033[31m{}\033[m é igual a \033[31m{}\033[m ' .format(num, escolha, convertido))
else:
    convertido = hex(num)[2:] #fatiamento de string, deixando apenas os números certos
    print('O \033[31m{}\033[m convertido em \033[31m{}\033[m é igual a \033[31m{}\033[m '.format(num, escolha,convertido))
print(emoji.emojize(':fox:'))
