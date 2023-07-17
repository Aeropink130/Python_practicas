import os
import shutil

# replace with your own folders route
downloads = r"C:\Users\aeropink\Downloads"
comp = r"C:\Users\aeropink\Documents\comprimidos"

archivos = os.listdir(downloads)

moved = False

cont = 0

for archivo in archivos:

    if archivo.lower().endswith((".zip", ".rar")):

        origen = os.path.join(downloads, archivo)
        destino = os.path.join(comp, archivo)

        shutil.move(origen, destino)
        cont = cont + 1
        moved = True

if moved:
    print("Archivos movidos correctamente")
    print(f"{cont} archivos movidos")
else:
    print("No se encontro/movio ningún archivo")
