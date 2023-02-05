String = str(input('Digite uma Frase: '))
StringSemEspaços = String.replace(' ', '')
StringCaseFold = StringSemEspaços.casefold()
Inverso = ""

for letra in range(len(StringCaseFold)-1, -1, -1): #Ex: palavra com 15 letras = 15-1 = 14, -1, -1 -> conta da letra 14 até a 0
    Inverso += StringCaseFold #Inverso = Inverso + StringCaseFold

if Inverso == StringCaseFold:
    print(f"A frase ({String.upper()}) é um Palíndromo.")
else: 
    print(f"A frase ({String.upper()}) Não é um Palíndromo.")