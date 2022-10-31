import emoji
from time import sleep

cores = {'limpa':'\033[m',
            'azul':'\033[34m',
              'amarelo':'\033[33m',
                'lilas':'\033[35m',
                   'vermelho':'\033[31m'}

casa = float(input('Valor da Casa: R$ '))
salario = float(input('Sálario do Comprador: R$ '))
anos = int(input('Quantos Anos de Financiamento? '))

meses = anos * 12
prestacao = casa / meses
minimo = salario * 30 /100

print('Para Pagar uma casa de \033[0:31mR${}\033[m em \033[0:31m{}\033[m anos, a prestação será de \033[0:31mR${:.2f}\033[m ' .format(casa, anos, prestacao))
print('\033[0:34mCalculando as Prestações\033[0:34m')
sleep(2)
#if prestacao > salario * 30 / 100:
  #  print('Infeizmente seu empréstimo foi Negado!')
#else:
#    print('Parábens, seu empréstimo foi Aceito!')

#tem outro jeito de fazer

if prestacao <= minimo:
    print('Infeizmente seu empréstimo foi Negado!')
else:
    print('Parábens, seu empréstimo foi Aceito!')
print(emoji.emojize(':fox:'))
