import emoji
from datetime import datetime

dados = {}
dados ['Nome'] = str(input('Nome: '))
nasc = int(input('Ano de Nascimento: '))
dados ['Idade'] = datetime.now().year - nasc
dados ['CTPS'] = int(input('Carteira de Trabalho [0 se não tiver]: '))
if dados['CTPS'] != 0:
    dados['Contratação'] = int(input('Carteira de Trabalho [0 se não tiver]: '))
    dados['Salário'] = float(input('Salário: '))
    dados['Aposentadoria'] = dados['Idade'] + ((dados['Contratação'] + 35) - datetime.now().year)
print('-=-' * 20)
for k, v in dados.items():
    print(f' - {k} tem o valor {v}')
print(emoji.emojize(':fox:'))
