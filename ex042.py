import emoji

cores = {'azul':'033[34m',
            'amarelo':'033[33m',
                'lilas':'033[35m',
                    'vermelho':'033[31m'}

print('-=-' * 20)
print('Analisador de Triângulos')
print('-=-' * 20)

t1 = float(input('Primeiro Segmento: '))
t2 = float(input('Segundo Segmento: '))
t3 = float(input('Terceiro Segmento: '))

if t1 < t2 + t3 and t2 < t1 + t3 and t3 < t1 + t2:
    print('Os Segmentos acima podem formar um Triângulo!', end='')
    if t1 == t2 == t3:
        print('\033[31mEQUÍLATERO\033[m')
    elif t1 != t2 != t3:  # != é 'diferente'
        print('\033[34mESCALENO\033[m')
    else:
        print('\033[35mISÓSCELES\033[m')
else:
    print('Os Segmentos acima não podem formar um Triângulo!')
print(emoji.emojize(':fox:'))