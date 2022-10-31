import emoji
from time import sleep

cores = {'azul': '033[34m',
            'amarelo': '033[33m',
                'lilas': '033[35m',
                    'vermelho': '033[31m',
                        'ciano': '033[36'}

print('\033[35m-=-\033[m' * 15)

preco = float(input('Digite o Preço das Compras R$: '))
sleep(1)

print('''FORMAS DE PAGAMENTO: 
[1]\033[33mÀ Vista Dinheiro/Cheque\033[m
[2]\033[31mÀ Vista Cartão\033[m
[3]\033[34m2x No Cartão\033[m
[4]\033[36m3x Ou Mais No Cartão\033[m''')

escolha = int(input('Qual Método de Pagamento?: '))

print('\033[35m-=-\033[m' * 15)

if escolha == 1:
    sleep(0.5)
    desc = preco - (preco * 10 / 100)
    print('Sua compra de \033[33mR${:.2f}\033[m no final vai custar \033[33mR${:.2f}\033[m' .format(preco, desc))
elif escolha == 2:
    sleep(0.5)
    desc = preco - (preco * 5 / 100)
    print('Sua compra de \033[31mR${:.2f}\033[m no final vai custar \033[31mR${:.2f}\033[m' .format(preco, desc))
elif escolha == 3:
    sleep(0.5)
    print('Sua compra em até 2x se mantem o mesmo valor de \033[34mR${:.2f}\033[m' .format(preco))
else:
    sleep(0.5)
    parcelas = int(input('Quantas Parcelas?'))
    juros = preco + (preco * 20 / 100)
    precoparc = juros / parcelas
    print('Sua compra será parcelada em \033[36m{:.2f}x\033[m de \033[36mR${:.2f}\033[m '.format(parcelas, precoparc))
    print('Sua compra de \033[36mR${:.2f}\033[m no final vai custar \033[31mR${:.2f}\033[m' .format(preco, juros))
print(emoji.emojize(':fox:'))
