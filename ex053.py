import emoji

frase = str(input('Digite uma Frase: ')).strip().upper()
palavra = frase.split()
junto = ''.join(palavra)
inverso = ''
print('Você digitou a frase "{}"' .format(frase))

for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]
print('O inverso de {} é {}' .format(junto, inverso))
if inverso == junto:
    print('Temos um Palíndromo!')
else:
    print('A frase não é um Palíndromo!')
print(emoji.emojize(':fox:'))

