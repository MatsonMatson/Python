import emoji
from time import sleep


c = ('\033[m', # 0 Sem Cor
     '\033[0;30;41m', # 1 Vermelho
     '\033[0;30;42m', # 1 Verde
     '\033[0;30;43m', # 1 Amarelo
     '\033[0;30;44m', # 1 Azul
     '\033[0;30;45m', # 1 Roxo
     '\033[7;30m', # 6 Branco
     );


def ajuda(com):
    titulo(f'Acessando o manual do comando \'{com}\'', 4)
    print(c[0], end='')
    help(com)
    print(c[0], end='')
    sleep(1)


def titulo(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor], end='')
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)
    print(c[0], end='')
    sleep(1)


#Programa Principal
comando = ''
while True:
    titulo('SISTEMA DE AJUDA PyHELP', 2)
    comando = str(input("Função ou Biblioteca > "))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)

titulo('ATÉ LOGO', 1)
print(emoji.emojize(':fox:'))
