import random
import string

def generador():
    print("Generador de contraseñas")

    longitud = int(input("Ingrese la longitud de su contraseña: "))

    caracter = string.ascii_letters + string.digits + string.punctuation

    contraseña = ''.join(random.choice(caracter)for i in range(longitud))

    print("contraseña creada:", contraseña)

generador()