import emoji

jogador = {}
partidas = list()
jogador ['Nome'] = str(input('Nome do Jogador: '))
tot = int(input(f'Quantas Partidas o {jogador["Nome"]} Jogou?: '))
for c in range(0, tot):
    partidas.append(int(input(f'Quantos Gol na partida {c+1}?: ')))
jogador ['Gols'] = partidas[:]
jogador ['Total'] = sum(partidas)
print('-=-' * 20)
print(f'O jogador {jogador["Nome"]} Jogou {len(jogador["Gols"])} Partidas')
for i, v in enumerate(jogador['Gols']):
    print(f'    => Na Partida {i}, fez {v} Gols')
print(f'Foi um total de {jogador["Total"]} Gols')
print(emoji.emojize(':fox:'))
