from time import sleep
import emoji


def area(lar, comp):
    print('-=-' * 10)
    a = lar * comp
    print(f'A área do terreno é de {a}m2')
    print('-=-' * 10)


print('   CONTROLE DE TERRENO   ')
print('-=-' * 10)
lar = float(input('Digite a Largura(m): '))
comp = float(input('Digite o Comprimento (m): '))
print('A área do terreno está sendo calculada...')
sleep(0.5)
area(lar, comp)
print(emoji.emojize(':fox:'))
