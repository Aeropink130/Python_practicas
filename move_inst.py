import os
import shutil

# replace with your own folders route
downloads = r"C:\Users\aeropink\Downloads"
inst = r"C:\Users\aeropink\Documents\instaladores"

archivos = os.listdir(downloads)

moved = False

cont = 0

for archivo in archivos:

    if archivo.lower().endswith((".exe", ".msi")):

        origen = os.path.join(downloads, archivo)
        destino = os.path.join(inst, archivo)

        shutil.move(origen, destino)
        cont = cont + 1
        moved = True

if moved:
    print("Archivos movidos correctamente")
    print(f"{cont} archivos movidos")
else:
    print("No se encontro/movio ningún archivo")
