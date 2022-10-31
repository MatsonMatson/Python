import emoji

num = int(input('Digite um Número: '))
total = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[34m', end=' ')
    else:
        print('\033[31m', end=' ')
    print('{} ' .format(c), end=' ')
print('O Número {} foi divisível {} vezes' .format(num, total))
if total == 2:
    print('E por isso ele é PRIMO!')
else:
    print('E por isso ele não é PRIMO!')
print(emoji.emojize(':fox:'))
