import emoji

cores = {'azul':'033[34m',
            'amarelo':'033[33m',
                'lilas':'033[35m',
                    'vermelho':'033[31m'}

n1 = int(input('Primeiro Valor: '))
n2 = int(input('Segundo Valor: '))

if n1 > n2:
    print('O Primeiro Valor é o Maior!')
elif n2 > n1:
    print('O Segundo Valor é o Maior!')
else:
   # n1 = n2 assim tbm funciona
    print('Os dois valores são Iguais!!')

print(emoji.emojize(':fox:'))
