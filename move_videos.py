import os
import shutil

# replace with your own folders route
downloads = r"C:\Users\aeropink\Downloads"
vids = r"C:\Users\aeropink\Videos"

archivos = os.listdir(downloads)

moved = False

cont = 0

for archivo in archivos:

    if archivo.lower().endswith((".mp4", ".avi", ".mov", ".mkv", ".wmv", ".flv", ".mpeg", ".mpg", ".webm")):

        origen = os.path.join(downloads, archivo)
        destino = os.path.join(vids, archivo)

        shutil.move(origen, destino)
        cont = cont + 1
        moved = True

if moved:
    print("Archivos movidos correctamente")
    print(f"{cont} archivos movidos")
else:
    print("No se encontro/movio ningún archivo")
