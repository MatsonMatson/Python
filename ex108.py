from Uteis import  Moeda
import emoji


valor = float(input('Digite o Preço: '))
print(f'A metade de {Moeda.moeada(valor)} é {Moeda.moeada(Moeda.metade(valor))}')
print(f'O dobro de {Moeda.moeada(valor)} é {Moeda.moeada(Moeda.dobro(valor))}')
print(f'Aumentando em 10%, temos o valor de {Moeda.moeada(Moeda.aumentar(valor, 10))}')
print(emoji.emojize(':fox:'))
