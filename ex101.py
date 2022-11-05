import emoji


def voto(ano):
    from datetime import datetime
    atual = datetime.today().year
    idade = atual - ano
    if idade < 16:
        return f'Com {idade} anos: NÃO VOTA!'
    elif idade >= 65:
        return f'Com {idade} anos: VOTO OPCIONAL!'
    else:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO!'

nasc = int(input('Ano de Nascimento: '))
print(voto(nasc))
