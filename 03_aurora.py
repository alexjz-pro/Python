#calculadora 
### Este es el tercer proyecto que trataremos de realizar sin ayuda de la IA###

#recepcion de valores
"""La llamaremos Aurora, debido a que es una idea que se me ocurrio de la nada...
esperaba presentar un proyecto mas avanzado pero bueno... No se puede correr...
Si aun no sabemos caminar... Atte: Axdev"""

# Variables principales
val_1 = 0 # Primer valor
val_2 = 0 # Segundo valor

# Valores especiales
ruta = False # Usaremos un boolean en false ya veran mas adelante para que

# funciones suma, resta, multiplicacion, division, mayor menor o igual que
def suma():
    val_1 = int(input("introduzca el primer valor: \n"))
    val_2 = int(input("introduzca el segundo valor: \n"))
    print("-"*50)
    print(val_1 + val_2)

def resta():
    val_1 = int(input("introduzca el primer valor: \n"))
    val_2 = int(input("introduzca el segundo valor: \n"))
    print("-"*50)
    print(val_1 - val_2)

def multiplicacion():
    val_1 = int(input("introduzca el primer valor: \n"))
    val_2 = int(input("introduzca el segundo valor: \n"))
    print("-"*50)
    print(val_1 * val_2)

def division():
    val_1 = int(input("introduzca el primer valor: \n"))
    val_2 = int(input("introduzca el segundo valor: \n"))
    print("-"*50)
    print(f"{val_1 / val_2:.2f}")

def mmq():
    val_1 = float(input("introduzca el primer valor: \n"))
    val_2 = float(input("introduzca el segundo valor: \n"))
    if val_1 > val_2:
        print("-"*50)
        print(f"{val_1} es mayor que {val_2}")
    elif val_2 > val_1:
        print("-"*50)
        print(f"{val_2} es mayor que {val_1}")
    elif val_1 == val_2:
            print("-"*50)
            print(f"Los valores son iguales")

print("-"*50)
print("-"*18, "A U R O R A", "-"*19)

while ruta == False:
    print("-"*50)
    print("Suma = S \nResta = R \nMultiplicacion = M \nDivision = D \nMayor que = P \nCerrar = N")
    print("Recuerda que solo puedes escoger uno")
    respuesta = str.upper(input("Que quieres calcular?: ")) # Recibimos el dato y ejecutamos
    print("-"*50)

    if respuesta == "S":
        print("Sumar")
        print("-"*50)
        suma()

    elif respuesta == "R":
        print("Restar")
        print("-"*50)
        resta()

    elif respuesta == "M":
        print("Multiplicar")
        print("-"*50)
        multiplicacion()

    elif respuesta == "D":
        print("Dividir")
        print("-"*50)
        division()

    elif respuesta == "P":
        print("Mayor que")
        mmq()

    elif respuesta == "N":
        ruta = True
