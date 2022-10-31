import emoji

print('-=-' * 20)
print('Analisador de Triângulos')
print('-=-' * 20)

t1 = float(input('Primeiro Segmento: '))
t2 = float(input('Segundo Segmento: '))
t3 = float(input('Terceiro Segmento: '))

if t1 < t2 + t3 and t2 < t1 + t3 and t3 < t1 + t2:
    print('Os Segmentos acima podem formar um Triângulo!')
else:
    print('Os Segmentos acima não podem formar um Triângulo!')

print(emoji.emojize(':fox:'))
