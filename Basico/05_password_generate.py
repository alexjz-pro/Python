import random
import string

def menu_opciones():
    while True:
        print("Generador de Contraseñas")
        print("1- Alfanumerica \n2- Numerica \n3- Mixta \n4- Alfabetica" \
        "\n5- Letras y Simbolos \n6- Salir")

        try:
            usuario_opc = int(input("Elija una opcion: "))
        except ValueError:
            print("Debe escribir un numero, no otro valor.")
            continue

            
        if usuario_opc == 6:
            print("Cerrando programa...")
            break

        if not 1 <= usuario_opc <= 5:
            print("Elija un número válido.")
            continue

# Pedimos la longitud de la contraseña
        try:
            longitud = int(input(
                "Elija la longitud de la contraseña: "))
        except ValueError:
            print("No puede escoger otro valor que no sea un número.")

        if 1 <= longitud <= 20:
            print("Creando su contraseña...")
            return usuario_opc, longitud
        else:
            print("Debe escoger un numero entre 1 y 20.")

def caracteres(usuario_opc, longitud):
    if usuario_opc == 1:
        caracter = string.ascii_letters + string.digits
    elif usuario_opc == 2:
        caracter = string.digits
    elif usuario_opc == 3:
        caracter = string.ascii_letters + string.punctuation + string.digits
    elif usuario_opc == 4:
        caracter = string.ascii_letters
    elif usuario_opc == 5:
        caracter = string.ascii_letters + string.punctuation

    contraseña =  ''.join(random.choice(caracter)for i in range(longitud))

    return contraseña

usuario_opc, longitud = menu_opciones()

resultado = caracteres(usuario_opc, longitud)

print("contraseña creada con Exito: \n" + resultado)