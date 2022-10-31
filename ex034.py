import emoji
from time import sleep

salario = float(input('Qual é o Sálario do Funcionário R$: '))

if salario <= 1250:
    print('Seu Antigo Sálario é R${} e vai passar a receber...' .format(salario))
    newsalario = salario + (salario * 10 / 100)
    print('PROCESSANDO...')
    sleep(2)
    print('Seu Novo Sálario é de {:.2f}' .format(newsalario))
else:
    print('Seu Antigo Sálario é R${} e vai passar a receber...' .format(salario))
    newsalario = salario + (salario * 15 / 100)
    print('PROCESSANDO...')
    sleep(2)
    print('Seu Novo Sálario é de {:.2f}' .format(newsalario))

print(emoji.emojize(':fox:'))
