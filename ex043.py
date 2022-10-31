import emoji
from time import sleep

cores = {'azul':'033[34m',
            'amarelo':'033[33m',
                'lilas':'033[35m',
                    'vermelho':'033[31m'}

print('-=-' * 20)
print('Calculadora de IMC')
print('-=-' * 20)

kg = float(input('Qual é o seu Peso?: '))
altura = float(input('Qual a sua Altura?: '))

imc = kg / altura**2

print('Seu IMC é de {:.2f}' .format(imc))
sleep(1)

if imc < 16:
    print("\033[35mMagreza grave\033[m")
elif imc < 17:
    print("\033[35mMagreza moderada\033[m")
elif imc < 18.5:
    print("\033[34mMagreza leve\033[m")
elif imc < 25:
    print("\033[34mSaudável\033[m")
elif imc < 30:
    print("\033[33mSobrepeso\033[m")
elif imc < 35:
    print("\033[31mObesidade Grau I\033[m")
elif imc < 40:
    print("\033[31mObesidade Grau II (severa)\033[m")
else:
    print("\033[31mObesidade Grau III (mórbida)\033[m")

print(emoji.emojize(':fox:'))
