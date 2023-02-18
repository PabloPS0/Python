def cifra_de_cezar(mensagem, deslocamento):
    cifra = ''
    for letra in mensagem:
        if letra.isalpha():
            letra_cifrada = chr((ord(letra) - 97 + deslocamento) % 26 + 97)
        elif letra.isnumeric():
            letra_cifrada = str((int(letra) + deslocamento) % 10)
        else:
            letra_cifrada = letra
        cifra += letra_cifrada
    return cifra

mensagem = input('Digite a mensagem a ser criptografada: ')
deslocamento = int(input('Digite o deslocamento desejado (um número inteiro): '))

mensagem_cifrada = cifra_de_cezar(mensagem, deslocamento)

print(f'A mensagem criptografada é: {mensagem_cifrada}')