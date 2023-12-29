"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""

import os

palavra_secreta = 'paralelepipedo'
letra_descoberta = ''
# palavra_descoberta = ''
numero_tentativas = 0

# while palavra_secreta != palavra_descoberta:
while True:
    if numero_tentativas < 1:
            print(f'A palavra secreta contém {len(palavra_secreta)} letras, decubra.')
    letra_palpite = input('digite uma letra: ')
    
    if len(letra_palpite) > 1:
        print('Digite apenas uma letra.')
        continue
    if letra_palpite in palavra_secreta:
        letra_descoberta += letra_palpite

    palavra_descoberta = ''    
    for letra_secreta in palavra_secreta:
        if letra_secreta in letra_descoberta:
            #print(letra_secreta)
            palavra_descoberta += letra_secreta
        else:
            palavra_descoberta += '*'
            #print('*')
    print('Palavra descoberta: ', palavra_descoberta)
    numero_tentativas += 1
    print(f'Tentativa {numero_tentativas}.')
    if palavra_descoberta == palavra_secreta:
        os.system('cls')
        print(f'Parabéns, com {numero_tentativas} tentativas você descobriu a palavra que é {palavra_secreta}.')    
        letra_descoberta = ''
        numero_tentativas = 0
        sair = input('Quer sair? [s]im: ').lower().startswith('s')
        if sair is True:
            break  