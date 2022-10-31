import emoji

cont = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco',
            'Seis', 'Sete', 'Oito', 'Nove', 'Dez',
            'Onze', 'Doze', 'Treze', 'Quatorze/Catorze', 'Quinze',
            'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')

while True:
    num = int(input('Digite um número entre 0 e 20: '))
    if 0 <= num <= 20:
        break
    print('Tente Novamente: ', end=' ')
print(f'Você digitou o Número {cont[num]}')
print(emoji.emojize(':fox:'))

