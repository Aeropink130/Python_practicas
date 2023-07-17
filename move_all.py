'''
Este programa une los modulos anteriormente
programados con la funcionalidad de clasificar y
mover los archivos a las carpetas correspondientes
'''

import os
import shutil

# replace with your own folders route
downloads = r"C:\Users\aeropink\Downloads"
inst = r"C:\Users\aeropink\Documents\instaladores"
vids = r"C:\Users\aeropink\Videos"
comp = r"C:\Users\aeropink\Documents\comprimidos"
images = r"C:\Users\aeropink\Pictures"
musica = r"C:\Users\aeropink\Music"

archivos = os.listdir(downloads)

moved = False

cont = 0

# movemos imagenes
for archivo in archivos:

    if archivo.lower().endswith((".png", ".jpg", ".jpeg", ".gif")):

        origen = os.path.join(downloads, archivo)
        destino = os.path.join(images, archivo)

        shutil.move(origen, destino)
        cont = cont + 1
        moved = True

# movemos archivos comprimidos
for archivo in archivos:

    if archivo.lower().endswith((".zip", ".rar")):

        origen = os.path.join(downloads, archivo)
        destino = os.path.join(comp, archivo)

        shutil.move(origen, destino)
        cont = cont + 1
        moved = True

# movemos videos
for archivo in archivos:

    if archivo.lower().endswith((".mp4", ".avi", ".mov", ".mkv", ".wmv",
                                 ".flv", ".mpeg", ".mpg", ".webm")):

        origen = os.path.join(downloads, archivo)
        destino = os.path.join(vids, archivo)

        shutil.move(origen, destino)
        cont = cont + 1
        moved = True

# movemos videos
for archivo in archivos:

    if archivo.lower().endswith((".mp3")):

        origen = os.path.join(downloads, archivo)
        destino = os.path.join(musica, archivo)

        shutil.move(origen, destino)
        cont = cont + 1
        moved = True

# movemos instaladores
for archivo in archivos:

    if archivo.lower().endswith((".exe", ".msi")):

        origen = os.path.join(downloads, archivo)
        destino = os.path.join(inst, archivo)

        shutil.move(origen, destino)
        cont = cont + 1
        moved = True

# comprobamos si se movieron archivos
if moved:
    print("Archivos movidos correctamente")
    print(f"{cont} archivos movidos")
else:
    print("No se encontro/movio ningún archivo")
