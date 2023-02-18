import os # Módulo que traz informações sobre o sistema operacional
import shutil # Módulo útil para mexer com arquivos (copiar e colar)
import psutil # Módulo útil para implementar ferramentas de monitoramento de sistema e otimização de desempenho em programas

folder_path = "EsteComputador/S.O(E:)/Music"
temp_folder_path = "EsteComputador/S.O(E:)/temp_folder_path"

def get_files(folder_path): # Função para listar os arquivos do diretório
    files = os.listdir(folder_path)
    return [os.path.join(folder_path, f) for f in files]

def copy_files(files, temp_folder_path): # Função para copiar os arquivos do diretório para a pasta temporária
    for f in files:
        shutil.copy(f, temp_folder_path)
def get_external_drives(): # Função para detectar dispositivos externos ou removíveis conectados ao computador
    drives = []

