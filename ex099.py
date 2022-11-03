import emoji
from time import sleep


def maior(*num):
    cont = maior = 0
    print('-=-' * 10)
    print('Analisando os valoes passados...')
    for valor in num:
        print(f'{valor} ', end='', flush=True)
        sleep(0.5)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
        print(f'Foram informado {cont} valores ao todo.')
        print(f'O maior valor informado foi o {maior}.')


#programa principal
maior(9, 5, 2, 3, 1, 5, 11)
maior(0, 4, 7, 9, 2, 10,)
maior(5, 4, 3, 8)
maior(1, 5)
print(emoji.emojize(':fox:'))
