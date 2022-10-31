import emoji

resp = 'S'
soma = quant = media = maior = menor = 0
while resp in 'Ss':
    num = int(input('Digite um Número: '))
    soma += num
    quant += 1
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = str(input('Quer Continuar? [S/N]')).upper().strip()[0]
media = soma / quant
print('Você digitou {} números e a média foi de {}' .format(quant, media))
print('o Maior valor foi {} e o Menor foi {}' .format(maior, menor))
print(emoji.emojize(':fox:'))
