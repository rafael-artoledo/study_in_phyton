"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
# num_1 = input('Digite um número inteiro(numero sem decimais): ')
# try:
#   if int(num_1) % 2 == 0:
#      print('O numero é par.')
#   else:
#      print('O número é impar.')
# except:     
#   print('O dado inserido não é número inteiro.')

#Solução do professor

# entrada = input('Digite um número: ')
# if entrada.isdigit():
#    entrada_int = int(entrada)
#    par_impar = entrada_int % 2 == 0
#    par_impar_texto = 'impar'
#    if par_impar:
#       par_impar_texto = 'par'
#    print(f'O número {entrada_int} é {par_impar_texto}.')
# else:
#    print('Você não digitou um numero inteiro.')

   #OU
# try:
#    entrada_int = int(entrada)
#    par_impar = entrada_int % 2 == 0
#    par_impar_texto = 'impar'
#    if par_impar:
#       par_impar_texto = 'par'
#    print(f'O número {entrada_int} é {par_impar_texto}.')
# except:
#    print('Você não digitou um numero inteiro.')      

#Solução do professor   
   
"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
# nome = input('Olá, digite seu nome: ')
# hora = input(f'{nome}, que horas são agora ? Entre 0 e 23: ')
# hora_int = int(hora)

# if hora_int >= 0 and hora_int <= 11:
#    print( f'Bom dia, {nome}!')
# elif hora_int >= 12 and hora_int <= 17:
#    print( f'Boa tarde, {nome}!')
# elif hora_int >= 18 and hora_int <= 23:
#    print( f'Boa noite, {nome}!')
# else:
#    print( f'{nome}, este não é um valor válido.') 

#Solução do professor 
 
#entrada = input('Digite a hora em números inteiros: ')

# try:
#     hora = int(entrada)

#     if hora >= 0 and hora <= 11:
#         print('Bom dia')
#     elif hora >= 12 and hora <= 17:
#         print('Bom tarde')
#     elif hora >= 18 and hora <= 23:
#         print('Bom noite')
#     else:
#         print('Não conheço essa hora')
# except:
#     print('Por favor, digite apenas números inteiros')

#Solução do professor      
"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""
print('Descubra se seu nome é curto, normal ou longo.')
nome = input('Digite seu primeiro nome: ')
tamanho_nome = len(nome)

if tamanho_nome <= 4 and tamanho_nome >1:
   print('Seu nome é curto.')
elif tamanho_nome >= 5 and tamanho_nome <= 6:
   print('Seu nome é normal.')
elif tamanho_nome > 6:
   print('Seu nome é longo.')
else:
   print('Digite ao menos duas letras')


# Solução do professor

nome = input('Digite seu nome: ')
tamanho_nome = len(nome)

if tamanho_nome > 1:
    if tamanho_nome <= 4:
        print('Seu nome é curto')
    elif tamanho_nome >= 5 and tamanho_nome <= 6:
        print('Seu nome é normal')
    else:
        print('Seu nome é muito grande')
else:
    print('Digite mais de uma letra.')
    
# Solução do professor
