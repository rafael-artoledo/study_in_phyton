"""
Exercício
Exiba os índices da lista
0 Maria
1 Helena
2 Luiz
"""
lista_nome = ['Nome:','Maria','Helena','Luiz']
lista_idade = ['Idade:', 31,46,18]
lista_nome.append('jorge')
lista_idade.append(0)

indices = range(len(lista_nome))
for indice in indices:
    print(indice, lista_nome[indice], lista_idade[indice])