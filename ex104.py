import emoji


def leiaint(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[31mERRO! Digite um Número inteiro válido.\033[31m')
        if ok:
            break
        return valor


n = leiaint('Digite um Número')
print(f'Você acabou de digitar o Número {n} ')
print(emoji.emojize(':fox:'))
