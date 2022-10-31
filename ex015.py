dias = int(input('Quantos Dias Alugado?: '))
km = float(input('Quantos KM Rodado?: '))
total = (dias * 60) + (km * 0.15)
print('O total a pagar é de R${:.2f}' .format(total))
