import os
import psutil
import shutil
import tkinter as tk
from tkinter import filedialog

# Função para copiar arquivos de música
def copiar_musicas(origem, destino1, destino2):
    # Verificar se a pasta de origem existe
    if not os.path.isdir(origem):
        return "A pasta de origem não existe."

    # Verificar se as pastas de destino existem
    for destino in [destino1, destino2]:
        if not os.path.isdir(destino):
            return f"A pasta de destino {destino} não existe."

    # Encontrar dispositivos externos conectados
    discos = psutil.disk_partitions()
    dispositivos = []
    for disco in discos:
        if "removable" in disco.opts:
            dispositivos.append(disco.device)

    # Copiar arquivos de música para cada dispositivo
    for dispositivo in dispositivos:
        destino = destino1 if dispositivo == "E:\\" else destino2
        shutil.copytree(origem, destino)

    return "Arquivos de música copiados com sucesso!"

# Função para exibir uma janela de seleção de pasta
def selecionar_pasta():
    pasta = filedialog.askdirectory()
    pasta_var.set(pasta)

# Função para iniciar a cópia de arquivos
def iniciar_copia():
    origem = pasta_var.get()
    destino1 = pasta_var2.get()
    destino2 = pasta_var3.get()
    resultado = copiar_musicas(origem, destino1, destino2)
    resultado_var.set(resultado)

# Criar a janela principal
janela = tk.Tk()
janela.title("Bot de cópia de músicas")

# Criar as variáveis de controle
pasta_var = tk.StringVar()
pasta_var2 = tk.StringVar()
pasta_var3 = tk.StringVar()
resultado_var = tk.StringVar()

# Criar os widgets
tk.Label(janela, text="Selecione a pasta de origem:").grid(row=0, column=0, padx=5, pady=5)
tk.Entry(janela, textvariable=pasta_var, width=50).grid(row=0, column=1, padx=5, pady=5)
tk.Button(janela, text="Selecionar pasta", command=selecionar_pasta).grid(row=0, column=2, padx=5, pady=5)
tk.Label(janela, text="Selecione a pasta de destino 1:").grid(row=1, column=0, padx=5, pady=5)
tk.Entry(janela, textvariable=pasta_var2, width=50).grid(row=1, column=1, padx=5, pady=5)
tk.Label(janela, text="Selecione a pasta de destino 2:").grid(row=2, column=0, padx=5, pady=5)
tk.Entry(janela, textvariable=pasta_var3, width=50).grid(row=2, column=1, padx=5, pady=5)
tk.Button(janela, text="Começar", command=iniciar_copia).grid(row=3, column=1, padx=5, pady=10)
tk.Label(janela, textvariable=resultado_var).grid(row=4, column=1, padx=5, pady=5)

# Iniciar a janela principal
janela.mainloop()