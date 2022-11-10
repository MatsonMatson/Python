from Uteis import  Moeda
import emoji


valor = float(input('Digite o Preço: '))
print(f'A metade de {Moeda.moeada(valor)} é {Moeda.metade(valor, True)}')
print(f'O dobro de {Moeda.moeada(valor)} é {Moeda.dobro(valor, True)}')
print(f'Aumentando em 10%, temos o valor de {Moeda.aumentar(valor, 10, True)}')
print(emoji.emojize(':fox:'))
