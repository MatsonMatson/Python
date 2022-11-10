def aumentar(preco=0, taxa=0, formato=False):
    res = preco + (preco * taxa / 100)
    return res if formato is False else moeada(res)


def diminuir(preco=0, taxa=0, formato=False):
    res = preco - (preco * taxa / 100)
    return res if formato is False else moeada(res)


def dobro(preco=0, formato=False):
    res = preco * 2
    return res if formato is False else moeada(res)


def metade(preco=0, formato=False):
    res = preco / 2
    return res if formato is False else moeada(res)


def dolar(preco=0, formato=False):
    res = preco / 5.20
    return res if formato is False else moeada(res)


def moeada(preco=0, moeda='R$'):
    return f'{moeda}{preco:>.2f}'.replace('.', ',')


def resumo(preco=0, taxaa=10, taxar=5):
    print('-=-' * 15)
    print('RESUMO DO VALOR'.center(30))
    print('-=-' * 15)
    print(f'Preço Analisando: \t{moeada(preco)}')
    print(f'Dobro do Preço: \t{dobro(preco, True)}')
    print(f'Metade do Preço: \t{metade(preco, True)}')
    print(f'{taxaa}% de aumento: \t{aumentar(preco, taxaa, True)}')
    print(f'{taxar}% de redução: \t\t{diminuir(preco, taxar, True)}')
    print('-=-' * 15)
