import emoji

num = (int(input('Digite um Número: ')), int(input('Digite outro Número: ')),
       int(input('Digite mais um Número: ')), int(input('Digite o último Número: ')))
print(f'Você digitou os números{num}')
print(f'O Valor 9 apareceu {num.count(9)} vezes')
if 3 in num:
    print(f'O Valor 3 apareceu na {num.index(3)+1}º posição')
else:
    print('O Valor 3 não foi digitado em nenhuma posição')
print('Os Valores Pares difitados foram ', end=' ')
for n in num:
    if n % 2 == 0:
        print(n, end=' ')
print(emoji.emojize(':fox:'))