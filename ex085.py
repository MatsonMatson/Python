import emoji

num = [[], []]
valor = 0
for c in range(1, 8):
    valor = int(input('Digite o Valor: '))
    if valor % 2 == 0:
        num[0].append(valor)
    else:
        num[1].append(valor)
print('-=-' * 20)
num[0].sort()
num[1].sort()
print(f'Os valores pares digitado são {num[0]}')
print(f'Os valores impares digitados são {num[1]} ')
print(emoji.emojize(':fox:'))
