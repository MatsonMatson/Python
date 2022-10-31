import emoji

print('==' * 10)
print('10 TERMOS DE UMA PA')
print('==' * 10)

termo = int(input('Primeiro Termo: '))
razao = int(input('Razão: '))
decimo = termo + (10 - 1) * razao

for c in range(termo, decimo + razao, razao):
    print('{} '.format(c), end='→')
print(emoji.emojize(':fox:'))