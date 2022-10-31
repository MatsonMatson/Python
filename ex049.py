import emoji

num = int(input('Digite um Número para sua tabuada: '))

for c in range(1, 11):
    print('{} X {:1} = {}' .format(num, c, num*c))
print(emoji.emojize(':fox:'))
