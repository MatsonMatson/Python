import emoji

n1 = int(input('Primeiro Valor:'))
n2 = int(input('Segundo Valor: '))
n3 = int(input('Terceiro Valor: '))

menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n2 and n3 < n2:
    menor = n3

maior = n1
if n2 > n2 and n2 > n3:
    maior = n2
if n3 > n2 and n3 >n2:
    maior = n3

print('O Maior Número é o {}' .format(maior))
print('O Menor Número é o {}' .format(menor))
print(emoji.emojize(':fox:'))
