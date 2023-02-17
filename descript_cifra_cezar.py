def decrypt(ciphertext, key):
    plaintext = ""
    for char in ciphertext:
        if char.isalpha():
            shift = key % 26
            if char.isupper():
                plaintext += chr((ord(char) - shift - 65) % 26 + 65)
            else:
                plaintext += chr((ord(char) - shift - 97) % 26 + 97)
        else:
            plaintext += char
    return plaintext

ciphertext = input("Digite a mensagem cifrada: ")
key = int(input("Digite o valor da chave: "))

plaintext = decrypt(ciphertext, key)
print("Mensagem original: " + plaintext)