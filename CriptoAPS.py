print(r"Bem-vindo à Criptografia de César")

chave = int(input("Digite a chave de criptografia (ate 26): "))
while chave > 26 or chave < 0:  
    print(" ")
    chave = input("Chave inválida, tente novamente.")

char = 'abcdefghijklmnopqrstuvwxyz'

#escolhe o modoQueer
modo = str(input("Deseja encriptar ou descriptar:"))

#insere e formata o texto
text= input("Digite o texto a ser criptografado:")
text = text.lower()


#insere o texto final
cripto =''

    #escolhe o modo
if (modo == 'e' or 'E' or modo == 'encriptar') :
    for word in text:
                #encontra o numero da posição dp word na base
        posicion = char.find(word)

            #soma a chave á posição
        posicion += chave

            # se a posição for maior que a base ira calcular a diferença
        if(posicion > len(char)):
            posicion = posicion - len(char)

    #concatena a o word encontrado           
        cripto = cripto + char[posicion]

elif (modo == 'd' or 'D' or modo == 'decriptar'):
        # contador do texto
            # recebe o word da posição
            #condição se o word estiver contido na base
    for word in text:
            #encontra a posição1
        posicion = char.find(word)
            #subtrai a chave
        posicion -= chave
            #condicional se a posição foi menor que 0
        if posicion < 0:
                # subtrai o valor absoluto da base para encontrar a posição
            posicion = len(char)- abs(posicion)

    #resultado            
        cripto = cripto + char[posicion]

print("sua mensagem" + cripto)