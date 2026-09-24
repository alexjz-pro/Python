from pathlib import Path
import shutil

ruta = Path.home() # Le indicamos que va a buscar en nuestro disco 

print("="*53)
print("=|"*9 , "P O L A R I S", "|="*10)
print("="*53)
print(" "*13,"¡Bienvenido a Polaris!")

print("-"*8 + "Para buscar una carpeta escriba 'C'" + "-"*10)
print("-"*9 + "Para buscar un Archivo escriba 'A'" + "-"*10)
print("="*53)
flecha = str.upper(input("Que elemento desea buscar?: "))
print("="*53)

def buscar():
    print("="*53)
    if flecha == "C":
        print(" "*15 + "Buscando tu Carpeta...")
    elif flecha == "A":
        print(" "*15 + "Buscando tu Archivo...")
    print("-"*53)

def nota():
    print("Si no conoces el nombre exacto del archivo puedes \nbuscarlo colocando entre '*' una parte que recuerdes" \
    "\n(ejemplo: *tech*, *.py*, *01_*)")
    print("-"*53)
    print("Atencion: ten en cuenta que pueden existir miles \n" \
    "de archivos con ese aspecto en su nombre, asi que")
    print(" "*15 + "USALO CON CUIDADO")
    print("-"*53)

i = 0

def accion():
    print("-"*53)
    print(f"Cantidad de archivos encontrados: {i}")
    print("-"*53)

while flecha != "":
    if flecha == "C":
        src_carpeta = Path(input("Introduzca el nombre de la carpeta: "))
        buscar()
        break

    elif flecha == "A":
        nota()
        src_archive = Path(input("Introduzca el nombre del archivo: "))
        buscar()
        break

cl_carpeta = None

if flecha == "C":
    for carpeta in ruta.rglob(src_carpeta):
        if carpeta.is_dir():
            cl_carpeta = carpeta
            break

    if cl_carpeta:
        print("¡Encontramos tu carpeta!")
        print(f"Ruta: {cl_carpeta}")
        print(f"Contenido de: {src_carpeta}")
        opcion = str.upper((input("Desea reubicar sus archivos Y/N: ")))
        while opcion != "":
            if opcion == "Y":
                for archivo in cl_carpeta.iterdir():
                    if archivo.is_file():
                        print(f"\t>{archivo.name}")
                        i = i + 1
                accion()

                prototype = Path(input("Ingrese el nombre de nueva la carpeta: "))
                new_carpeta = Path(cl_carpeta / prototype)
                new_carpeta.mkdir(exist_ok=True)
                sufijo = str(input("Que tipos de archivos desea mover a esa carpeta?: "))
                
                for archivo in cl_carpeta.iterdir():
                    if archivo.is_file() and archivo.suffix == (f"{sufijo}"):
                        shutil.move(archivo, new_carpeta)
                        print(f"{archivo.name} Exito")
                
                        print(f"Archivos transferidos a {new_carpeta}")
                        print(f"Tipo de archivos: '{sufijo}'")
                break
            elif opcion == "N":
                print("Cerrando...")
                break      
    else:
        print("Error al buscar la carpeta... Intentalo de nuevo")

elif flecha == "A":
    for file in ruta.rglob(src_archive):
        try:
            if file.is_file():
                print("="* 53)
                print(f"{file.name} Encontrado")
                print(f"Ruta: {file}")
                i = i + 1    
            accion()

        except PermissionError:
            continue
    print("="*53)