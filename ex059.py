import emoji
from time import sleep

n1 = float(input('Primeiro Valor: '))
n2 = float(input('Segundo Valor: '))
opcao = 0
print('\033[31m-=-\033[m' * 10)
while opcao != 5:
    print('''    [1] SOMAR
    [2] MULTIPLICAR
    [3] MAIOR
    [4] NOVOS NÚMEROS
    [5]SAIR DO PROGRAMA''')
    sleep(1)
    opcao = int(input('Qual é sua opção?:'))
    if opcao == 1:
        soma = n1 + n2
        print('O Resultado da opção SOMAR é de {}' .format(soma))
    elif opcao == 2:
        produto = n1 * n2
        print('O Resultado da opção MULTIPLICAR é de {}' .format(produto))
    elif opcao == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('O Resultado da opção MAIOR é de {}' .format(maior))
    elif opcao == 4:
        print('Informe os Novos Números: ')
        n1 = int(input('Primeiro Valor: '))
        n2 = int(input('Segundo Valor: '))
    elif opcao == 5:
        print('Finalizando...')

    else:
        print('Opção Inválida, Tente Novamente')
print('\033[31m-=-\033[m' * 10)
print(emoji.emojize(':fox:'))
