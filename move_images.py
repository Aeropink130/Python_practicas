import os
import shutil


downloads = r"C:\Users\aeropink\Downloads"
images =  r"C:\Users\aeropink\Pictures"

archivos = os.listdir(downloads)

moved = False

for archivo in archivos:

    if archivo.lower().endswith((".png", ".jpg", ".jpeg", ".gif")):

        origen = os.path.join(downloads, archivo)
        destino =os.path.join(images, archivo)

        shutil.move(origen, destino)
        moved = True

if moved:
    print("Archivos movidos correctamente")
else:
    print("No se encontro/movio ningún archivo")