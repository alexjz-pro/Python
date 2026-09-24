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
buscar = str.upper(input("Que elemento desea buscar?: "))
print("="*53)

# para usar un elemento de la lista iniciamos en "0"
textos = ["Buscando...", "Eureka!!!", "Bienvenido", "="*53, "Busquemos otra carpeta", "Cerrando P o l a r i s"]


def src_carpeta():
    c_e = None
    buscar_c = Path(input("Intoduzca el nombre de la Carpeta: "))
    print(textos[0])

    for carpeta in ruta.rglob(buscar_c):
        if carpeta.is_dir():
            c_e = carpeta
            break

    if c_e:
        print(f"Carpeta: {buscar_c} Encontrada en: {c_e}")
    else:
        print("Ups... no la encontre")
        src_carpeta()

    buscar = str.upper(input("Desea ver el contenido de la carpeta?(Y/N): "))
    if buscar == "Y":
    #mostrar contenido de la carpeta
        for archivo in c_e.iterdir():
            if archivo.is_file():
                print(f"\t*{archivo.name}")

        buscar = str.upper(input("Desea reubicar tus archivos a una nueva carpeta?(Y/N): "))
        if buscar == "Y":
            folio = Path(input("Como quieres que se llame la carpeta?: "))       
            new_c = Path(c_e / folio)
            new_c.mkdir(exist_ok=True)
            cart = str(input("Que archivos moveras?: "))

            for archivo in c_e.iterdir():
                if archivo.is_file() and archivo.suffix == (f"{cart}"): 
                    shutil.move(archivo, new_c)
                    print(textos[1])
                    src_carpeta()
                
        if buscar == "N":
            print(textos[4])
            src_carpeta()

    elif buscar == "N":
        print(textos[4])
        src_carpeta()
    elif buscar == "EXIT":
        print(textos[5])

def src_archivo():
    buscar_a = Path(input("Introduzca el nombre del Archivo: "))
    print(textos[3])
    print(textos[0])
    print(textos[3])

    for archivo in ruta.rglob(buscar_a):
        if archivo.is_file():
            print(f"{buscar_a} Encontrado en {archivo}")


# Bucle para la ejecucion de funciones dependiendo la seleccion en buscar
if buscar == "C":
    src_carpeta()
        
else:
    src_archivo()
