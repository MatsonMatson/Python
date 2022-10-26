num1 = int(input('Primeiro Número'))
num2 = int(input('Segundo Numero'))
soma = num1 + num2
#se o tipo de variavel for float ela serve para numeros reais
#print('A Soma entre', num1, 'e', num2, 'é de', soma)
print('A Soma entre {} e {} é de {}' .format(num1, num2, soma))
# o .format melhora a sintaxe do código, deixando ele mais dinámico e colocando o resultado das váriaveis no seus lugares definidos.
