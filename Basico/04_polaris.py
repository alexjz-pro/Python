from pathlib import Path
import shutil

ruta = Path.home()

respuestas = {
    "buscar" : "Buscando...",
    "encontrado" : "¡Encontramos tu archivo!",
    "cerrar" : "___Cerrando Sesion___"
}

def buscar_carpeta():
    nombre_carpeta = input("Introduzca el nombre de la carpeta: ").strip()

    if not nombre_carpeta:
        print("El nombre no puede estar vacio.")
        return
    
    print(respuestas["buscar"])

    carpetas = [ carpeta for carpeta in ruta.rglob(nombre_carpeta) if carpeta.is_dir()]

    if not carpetas:
        print("No se encontro la carpeta.")
        return

    carpeta = carpetas[0]
    print(f"Carpeta encontrada en: {carpeta}")

def mover_archivo():
    send_to = Path(input("introduzca la direccion: ").strip())

    if not send_to:
        print("Introduzca un valor en direccion.")
        return
    
    new_direccion = Path(f"{send_to}")
    new_direccion.mkdir(exist_ok=True)
    archive = input("Nombre del archivo: ").strip()

    if not archive:
        print("El nombre de la carpeta no puede estar vacio.")
        return

    busqueda = [archivo for archivo in ruta.rglob(archive) if archivo.is_file()]

    if not busqueda:
        print("No encontramos tu archivo.")
        return

    if busqueda:
        for archivo in busqueda:
            shutil.move(archivo, new_direccion)
            print(f"{archive} movido con exito a {new_direccion}")
    

def buscar_archivo():
    nombre_archivo = input("Introduzca el nombre del archivo: ").strip()

    if not nombre_archivo:
        print("El nombre no puede estar vacio.")
        return
    print(respuestas["buscar"])

    encontrado = [ archivo for archivo in ruta.rglob(nombre_archivo) if archivo.is_file()]

    if encontrado:
        for archivo in encontrado:
            print(f"Archivo encontrado en: {archivo}")
    else:
        print("Archivo no econtrado.")



def menu():
    while True:
        print("="*20, "POLARIS", "="*20)
        print("'MENU DE OPCIONES' \n1: Buscar arpeta \n2: Buscar archivo \n3: Mover un Archivo \n4: Salir")
        menu_option = input("Elije tu Opcion: ").strip()

        if menu_option == "1":
            buscar_carpeta()
        elif menu_option == "2":
            buscar_archivo()
        elif menu_option == "3":
            mover_archivo()
        elif menu_option == "4":
            print(respuestas["cerrar"])
            break
        else:
            print("Opcion no válida.")

if __name__ == "__menu__":
    menu()

menu()