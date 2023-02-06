lista = [] #Void List
for c in range(1, 6):
    weight = float(input(f'Informe o peso da {c}ª pessoa: '))
    lista += [weight] #Adding values to list
print(f'O maior peso informado é {max(lista)}kg') #Max Weight
print(f'O menor peso informado é {min(lista)}kg') #Min Weight
