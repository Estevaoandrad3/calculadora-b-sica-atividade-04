opera_C3_A7ao_invalida = None
Primeiro_n_C3_BAmero = None
Segundo_n_C3_BAmero = None
Tipo_de_opera_C3_A7ao = None
Resultado = None

def text_prompt(msg):
  try:
    return raw_input(msg)
  except NameError:
    return input(msg)


opera_C3_A7ao_invalida = False
Primeiro_n_C3_BAmero = float(text_prompt('Qual é o primeiro número? '))
Segundo_n_C3_BAmero = float(text_prompt('Qual é o segundo número? '))
Tipo_de_opera_C3_A7ao = text_prompt('Qual a operação desejada? ').lower()
if Tipo_de_opera_C3_A7ao == 'soma':
  Resultado = Primeiro_n_C3_BAmero + Segundo_n_C3_BAmero
elif Tipo_de_opera_C3_A7ao == 'subtração':
  Resultado = Primeiro_n_C3_BAmero - Segundo_n_C3_BAmero
elif Tipo_de_opera_C3_A7ao == 'multiplicação':
  Resultado = Primeiro_n_C3_BAmero * Segundo_n_C3_BAmero
elif Tipo_de_opera_C3_A7ao == 'divisão':
  Resultado = Primeiro_n_C3_BAmero / Segundo_n_C3_BAmero
else:
  Resultado = 'Não é possivel realizar a operação!'
  opera_C3_A7ao_invalida = True
if opera_C3_A7ao_invalida:
  print(Resultado)
else:
  print(''.join([str(x) for x in ['O Resultado da ', Tipo_de_opera_C3_A7ao.title(), ' dos números é: ', Resultado]]))