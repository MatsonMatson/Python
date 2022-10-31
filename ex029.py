import emoji
from time import sleep

velocidade = float(input('Qual a velocidade do seu Carro? :'))

if velocidade <= 80:
    print('Você está dentro das normas, tenha uma ótima Viagem!')
else:
    print('MULTADO! Você excedeu o limitde de velociade permitido que é de 80Km/h')
    print('Calculando sua Multa!')
    sleep(2)
    multa = (velocidade - 80) * 7
    print('Sua Multa é de R${}' .format(multa))

print('Tenha um Bom Dia! Dirija com Cuidado!')
print(emoji.emojize(':fox:'))
