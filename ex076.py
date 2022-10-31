import emoji

lista = ('Macarrão', 10.50,
         'Feijão', 7.25,
         'Arroz', 6.75,
         'Coca-Cola', 7.50,
         'Molho de Tomate', 4.25,
         'Milho em Lata', 3.25,
         'Ervilhas em Lata', 3.25,
         'Preseunto Kg', 25.50,
         'Queijo Mussarela Kg', 26.50,
         'Chocolate ao Leite', 12.35,
         'Chocolate Amargo', 20.00,
         'Fanta Laranja', 5.75)
print('\033[31m-=-\033[m' * 30)
print('\033[36mLISTAS DE PREÇOS\033[m')
for pos in range(0, len(lista)):
    if pos % 2 == 0:
        print(f'{lista[pos]:.<30}', end=' ')
    else:
        print(f'R%{lista[pos]:>7}')

print('\033[31m-=-\033[m' * 30)
print(emoji.emojize(':fox:'))
