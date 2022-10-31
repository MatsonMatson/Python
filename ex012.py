preco = float(input('Qual o Preço do produto? R$: '))
desc = preco - (preco * 5 / 100)
print('O produto que custava {}, na promoção com desconto de 5%, vai custar {}' .format(preco, desc))
