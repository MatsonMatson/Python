import emoji

pesomaior = 0
pesomenor = 0
for c in range(1, 6):
    peso = float(input('Qual é o Peso da {}º pessoa?: ' .format(c)))
    if peso == 1:
        pesomaior = c
        pesomenor = c
    else:
        if peso > pesomaior:
            pesomaior = peso
        if peso < pesomenor:
            pesomenor = peso
    
print('O maior Peso lido foi {}Kg' .format(pesomaior))
print('O menor Peso lido foi {}Kg' .format(pesomenor))

print(emoji.emojize(':fox:'))