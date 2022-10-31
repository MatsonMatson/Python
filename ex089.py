import emoji

ficha = list()
while True:
    nome = str(input('Qual é o Seu Nome?: '))
    n1 = float(input('Digite sua Primeira Nota: '))
    n2 = float(input('Digite sua Segunda Nota: '))
    media = (n1 + n2) / 2
    ficha.append([nome, [n1, n2], media])
    resp = str(input('Quer Continuar?: [S/N]'))
    if resp in 'N/n':
        break
print('-=-' * 20)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-' * 25)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('-' * 30)
    opc = int(input('Mostra Notas de qual Aluno? (999 Interrompe): '))
    if opc == 999:
        print('FINALIZANDO...')
        break
    if opc <= len(ficha) - 1:
        print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')
print('<<< VOLTE SEMPRE >>>')
print(emoji.emojize(':fox:'))
