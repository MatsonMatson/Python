import emoji

time = list()
jogador = {}
partidas = list()

while True:
    jogador.clear()
    jogador ['Nome'] = str(input('Nome do Jogador: '))
    tot = int(input(f'Quantas Partidas o {jogador["Nome"]} Jogou?: '))
    partidas.clear()
    for c in range(0, tot):
        partidas.append(int(input(f'Quantos Gol na partida {c+1}?: ')))
    jogador ['Gols'] = partidas[:]
    jogador ['Total'] = sum(partidas)
    while True:
        resp = str(input('Quer Continuar?: [S/N]')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda Apenas S ou N.')
    if resp == 'N':
        break
print('-=-' * 30)
print('cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('--' * 20)
for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-' * 40)
while True:
    busca = int(input('Mostra dados de qual Jogador? (999 para Parar) '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO! Não existe jogador com esse Código {busca}!')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {time[busca]["Nome"]}:')
        for i, g in enumerate(time[busca]["Gols"]):
            print(f'  No Jogo {i+1} fez {g} Gols.')
    print('-' * 40)
print('<< VOLTE SEMPRE >>')
print(emoji.emojize(':fox:'))
