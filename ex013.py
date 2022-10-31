salario = float(input('Qual é o Salário do Funcionário? R$: '))
newsa = salario + (salario * 15 / 100)
print('Um Funcionário que ganhava R${}, com o aumento de 15%, passa a receber R${:.2f}' .format(salario, newsa))
