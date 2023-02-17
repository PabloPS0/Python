def cifra_cesar(texto, chave, modo):
    alfabeto = 'abcdefghijklmnopqrstuvwxyz'
    texto_cifrado = ''
    for c in texto:
        if c in alfabeto:
            indice = alfabeto.index(c)
            if modo == 'cifrar':
                indice_cifrado = (indice + chave) % len(alfabeto)
            elif modo == 'decifrar':
                indice_cifrado = (indice - chave) % len(alfabeto)
            texto_cifrado += alfabeto[indice_cifrado]
        else:
            texto_cifrado += c
    return texto_cifrado

texto = input("Digite o texto a ser criptografado: ")
chave = int(input("Digite a chave de criptografia (um número inteiro): "))
modo = input("Digite 'cifrar' para criptografar ou 'decifrar' para descriptografar: ")

texto_cifrado = cifra_cesar(texto, chave, modo)
print("O texto", modo, "é:", texto_cifrado)
