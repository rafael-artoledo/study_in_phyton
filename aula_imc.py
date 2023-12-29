nome = 'Rafael Toledo'
altura = 1.7
peso = 70
imc = peso / altura ** 2
# print(nome + ' tem ' + str(altura) + ' de altura,' +
#      ' pesa ' + str(peso) + ' quilos e seu IMC é ' + str(int(imc)) + '.')
# formatação de strings
linha_1 = f'{nome} tem {altura:.2f} de altura, pesa {peso} quilos e seu IMC é {imc:.2f}.'
print(linha_1)
