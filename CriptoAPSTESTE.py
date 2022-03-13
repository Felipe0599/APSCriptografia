print(r"Bem-vindo à Criptografia de César")
MODE_ENCRYPT = 1
MODE_DECRYPT = 0

def caesar(data, chave, modo):
    alfabeto = 'abcdefghijklmnopqrstuvwyzàáãâéêóôõíúçABCDEFGHIJKLMNOPQRSTUVWYZÀÁÃÂÉÊÓÕÍÚÇ'
    conversao = ''
    for c in data:
        caracter = alfabeto.find(c)
        if caracter == -1:
            conversao += c
        else:
            posiçao = caracter + chave if modo == MODE_ENCRYPT else caracter - chave
            posiçao = posiçao % len(alfabeto)
            conversao += alfabeto[posiçao:posiçao+1]
    return conversao

# Tests
chave = int(input('Digite o valor da chave:'))
original = input('Digite a mensagem a ser criptografada:')
print('  Original:', original)
cifrado = caesar(original, chave, MODE_ENCRYPT)
print('Encriptada:', cifrado)
decifrado = caesar(cifrado, chave, MODE_DECRYPT)
print('Decriptada:', decifrado)