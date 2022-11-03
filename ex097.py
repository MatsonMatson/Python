import emoji


def escreva(msg):
    tam = len(msg) + 2
    print('~' * tam)
    print(f'{  msg}')
    print('~' * tam)


#programa principal
escreva(str(input('Digite uma Mensagem: ')))
print(emoji.emojize(':fox:'))
