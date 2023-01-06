from time import sleep
primeiro = int(input('Digite o primeiro termo: ')) 
razao = int(input('Digite a razão: '))
n = int(input('Quantos elementos exibir: '))

# a(n) = a(1) + (n-1).r
ultimo = primeiro + (n-1) * razao
ultimo = ultimo + 1

for pa in range(primeiro, ultimo, razao):
    print(f'\033[33mA progressão aritmética de \033[35m{primeiro} \033[33mé \033[32m{pa}.')
    sleep(1)