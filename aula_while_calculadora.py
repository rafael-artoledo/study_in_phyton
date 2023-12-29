while True:
  num_1 = input('Digite o primeiro número: ')
  num_2 = input('Digite o segundo número: ')
  operador = input('A operação desejada é(+, -, / ou *): ')
  
  # FLAG
  numeros_validos = None
  
  num_1_float = 0
  num_2_float = 0

  try: # má pratica de programação da forma que esta disposta
    num_1_float = float(num_1)
    num_2_float = float(num_2)
    # FLAG
    numeros_validos = True
  except:
    # FLAG
    numeros_validos = None

  if numeros_validos is None:
    print('Um ou ambos os números digitados são invalidos.')
    continue
  
  operadores_permitidos = '+-/*'
  
  if operador not in operadores_permitidos:
    print('Operador invalido')
    continue
  if len(operador) >1:
    print('Digite apenas um operador')
    continue

  print('Realizando sua conta: Confira o resultado abaixo.')
  if operador == '+':
    print(f'{num_1_float} + {num_2_float} = ', num_1_float + num_2_float)
  elif operador == '-':
    print(f'{num_1_float} - {num_2_float} = ', num_1_float - num_2_float)
  elif operador == '/':
    print(f'{num_1_float} / {num_2_float} = ', num_1_float / num_2_float)
  elif operador == '*':
    print(f'{num_1_float} * {num_2_float} = ', num_1_float * num_2_float)
  else:
    print('Nunca deveria ter chegado aqui.')

  sair = input('Quer sair? [s]im: ').lower().startswith('s')
  if sair is True:
    break  
  