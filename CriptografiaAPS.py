# Solicitando o texto a ser encriptado ou decriptado


texto = input('Digite a mensagem a ser criptogrfada ou descriptografada: ')
# Chave a ser utilizada
chave = int(input('Entre com o valor da chave (deslocamento): '))
chave_arm = chave
tent=0
CARACTERES = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
convertido = ''
texto = texto.upper()

modo = input('Deseja Criptografar? : ')
if modo == 's' or modo == 'S' or modo == 'Sim' or modo == 'SIM': 

  for caractere in texto:
    if caractere in CARACTERES:
            # Obter o número criptografado ou decriptado do caractere
            num = CARACTERES.find(caractere)
            # Obter o número do caractere
            if modo == 'E':
                num = num + chave
            elif modo == 'D':
                num = num - chave
         # Manipulando a rotação se o valor de num for maior do que o comprimento de CARACTERES ou menor que 0
            if num >= len(CARACTERES):
              num = num - len(CARACTERES)
            elif num < 0:
              num = num + len(CARACTERES)
         # Adicionar (concatenar) o caractere correspondente a num na variável convertido
            convertido = convertido + CARACTERES[num] 
    else:
          # Concatenado o caractere sem efetuar criptografia ou decifragem
          convertido = convertido + caractere

if modo == 'E':
  print('O texto criptografado é ', convertido)
  desc = input('Deseja descriptografar? ')
  if desc == 's' or desc == 'S' or desc == 'sim' or desc == 'Sim' or desc == 'SIM' or desc == 'SiM':
    chav = int(input('Entre com o valor da chave de deslocamento: '))
    while chav != chave_arm:
      chav = int(input('Chave incorreta, digite novamente: '))
      tent=tent+1
      if tent == 3:
                 exit()
if modo == 'D':
  print('O texto Descriptografado é: ' , convertido)

   
