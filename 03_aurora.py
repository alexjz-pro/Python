#calculadora 
### Este es el tercer proyecto que trataremos de realizar sin ayuda de la IA###

#recepcion de valores
"""La llamaremos Aurora, debido a que es una idea que se me ocurrio de la nada...
esperaba presentar un proyecto mas avanzado pero bueno... No se puede correr...
Si aun no sabemos caminar... Atte: Axdev"""

# Variables principales
val_1 = 0 # Primer valor
val_2 = 0 # Segundo valor
resultado = 0 # resultado

# Valores especiales
ruta = False # Usaremos un boolean en false ya veran mas adelante para que

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
        val_1 = int(input("ingrese el primer valor: \n"))
        val_2 = int(input("ingrese el segundo valor: \n"))
        resultado = val_1 + val_2
        print("-"*50)
        print(f"{resultado}")
        resultado = 0

    elif respuesta == "R":
        print("Restar")
        val_1 = int(input("ingrese el primer valor: \n"))
        val_2 = int(input("ingrese el segundo valor: \n"))
        resultado = val_1 - val_2
        print("-"*50)
        print(f"{resultado}")
        resultado = 0

    elif respuesta == "M":
        print("Multiplicar")
        val_1 = int(input("ingrese el primer valor: \n"))
        val_2 = int(input("ingrese el segundo valor: \n"))
        resultado = val_1 * val_2
        print("-"*50)
        print(f"{resultado}")
        resultado = 0

    elif respuesta == "D":
        print("Dividir")
        val_1 = int(input("ingrese el primer valor: \n"))
        val_2 = int(input("ingrese el segundo valor: \n"))
        resultado = val_1 / val_2
        print("-"*50)
        print(f"{resultado:.2f}")
        resultado = 0

    elif respuesta == "P":
        print("Mayor que")
        val_1 = float(input("ingrese el primer valor: \n"))
        val_2 = float(input("ingrese el segundo valor: \n"))
        if val_1 > val_2:
            print("-"*50)
            print(f"{val_1} es mayor que {val_2}")
        elif val_2 > val_1:
            print("-"*50)
            print(f"{val_2} es mayor que {val_1}")
        elif val_1 == val_2:
            print("-"*50)
            print(f"Los valores son iguales")

    elif respuesta == "N":
        ruta = True
