import emoji

print('-' * 15)
print('Sequência de Fiobonacci')
print('-' * 15)
n = int(input('Quantos você quer mostrar?: '))
t1 = 0
t2 = 1
print('~' * 30)
print('{} 👉 {}' .format(t1, t2), end='')
cont = 3
while cont <= n:
    t3 = t1 + t2
    print(' 👉 {}' .format(t3), end='')
    t1 = t2
    t2 =t3
    cont += 1
print('👉 FIM')
print(emoji.emojize(':fox:'))