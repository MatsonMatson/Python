from Uteis import  Moeda
import emoji


valor = float(input('Digite o Preço: '))
print(f'A metade de R${valor} é R${Moeda.metade(valor)}')
print(f'O dobro de R${valor} é R${Moeda.dobro(valor)}')
print(f'Aumentando em 10%, temos o valor de R${Moeda.aumentar(valor, 10)}')
print(emoji.emojize(':fox:'))

