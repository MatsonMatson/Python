import emoji
from time import sleep


viagem = float(input('Qual é a distância da sua Viagem?: '))

if viagem <= 200:
    print('Você está preste a começar a sua viagem de {}km.' .format(viagem))
    print('PROCESSANDO O VALOR...')
    sleep(2)
    valor = viagem * 0.50
    print('O Valor da sua Passagem é de R${:.2f}' .format(valor))
else:
    print('Você está preste a começar a sua viagem de {}km.' .format(viagem))
    print('PROCESSANDO O VALOR...')
    sleep(2)
    desc = viagem * 0.45
    print('O Valor da sua Passagem é de R${:.2f}' .format(desc))

print('Tenha uma Ótima Viagem!')
print(emoji.emojize(':fox:'))
