#Exercícios
# Ex.1:
#Com o nome completo do usuário, adicione um caractere entre as letras do nome do usuário.
#Lembre sobre fatiamento e indice dos caracteres.
nome = input('Digite seu nome: ')
nome_size = len(nome)
indice = 0
novo_nome= ''
while indice < nome_size:
    letra = nome[indice]
    novo_nome += f'*{letra}'
    indice += 1
novo_nome += '*'
print(novo_nome)    