import emoji

total = totmil = menor = cont = 0
barato = ' '
print('\033[31m-\033[m' * 20)
print('\033[36mLOJA SUPER BARATÃO\033[m')
print('\033[31m-\033[m' * 20)

while True:
    produto = str(input('Nome do Produto:'))
    preco = float(input('Preço: R$ '))
    cont += 1
    total += preco
    if preco > 1000:
        totmil += 1
    if cont == 1:
        menor = preco
        barato = produto
    else:
        if preco < menor:
            menor = preco
            barato = produto
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if resp == 'N':
        break
print('{:-^40}'.format('FIM DO PROGRAMA'))
print(f'O total da Compra foi de R${total:.2f}')
print(f'Temos {totmil} Produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {barato} que custa R${menor:2.f}')

print(emoji.emojize(':fox:'))
