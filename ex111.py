import emoji
from Uteis import Moeda
from Uteis import Dados

valor = Dados.leiaDinheiro('Digite o preço: R$')
Moeda.resumo(valor)
print(emoji.emojize(':fox:'))
