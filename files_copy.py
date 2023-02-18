import os
import psutil
import shutil
import serial
import usb.core

origem = "C:\\Users\\seu_usuario\\Music\\"
destino1 = "E:\\Music\\"
destino2 = "F:\\Music\\"

discos = psutil.disk_partitions()
dispositivos = []
for disco in discos:
    if "removable" in disco.opts:
        dispositivos.append(disco.device)

for dispositivo in dispositivos:
    destino = destino1 if dispositivo == "E:\\" else destino2
    shutil.copytree(origem, destino)

vid = 0x1234
pid = 0x5678
arquivos = os.listdir(destino)
for arquivo in arquivos:
    with open(destino + arquivo, "rb") as f:
        data = f.read()
    dev = usb.core.find(idVendor=vid, idProduct=pid)
    if dev is not None:
        dev.set_configuration()
        ep = dev[0][(0, 0)][0]
        ep.write(data)
