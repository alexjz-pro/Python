# Calculadora sencilla de la ley de Ohm 
print("Calculadora (ley de ohm)")
print("------------------------")
cuestion = input("¿Que necesitas calcular? (V, A, R=Ω):")

def any (cuestion):
    if(cuestion == "v" or cuestion == "V"): #Aca validamos que sea el dato V o v  
        print("Vamos a calcular Voltaje...") #Damos un mensaje al usuario para orientacion
        a = float(input("dame el valor de A: ")) #Aca recibimos el valor de A para la ecuacion
        b = float(input("dame el valor de Ω: ")) #Aca recibimos el segundo

        if(a != 0 and b != 0):           #Hacemos una validacion para que no sea 0
            c = str(a * b)                         #Aca calculamos y convertimos a str
            print(f"El resultado es: {c}V") #Publicamos al usuario el resultado en un solo str 
        else:
            print("El valor indicado NO puede ser 0")  #Que pasa si es 0

    elif(cuestion == "a" or cuestion == "A"): #Validacion
        print("Vamos a calcular Corriente...") #Orientacion
        a = float(input("dame el valor de V: ")) #Elemento a
        b = float(input("dame el valor de Ω: ")) #Elemento b

        if(a != 0 and b != 0):
            c = str(a / b)                         #Calculo, conversion 
            print(f"El resultado es: {c}A") #Resultado
        else:
            print("El valor indicado NO puede ser 0")  #Que pasa si es 0

    elif(cuestion == "r" or cuestion == "R"): #Validacion
        print("Vamos a calcular Resistencia...") #Orientacion
        a = float(input("dame el valor de V: ")) #Elemento 1
        b = float(input("dame el valor de A: ")) #Elemento 2

        if(a != 0 and b != 0):
            c = str(a / b)                         #Calculo, conversion 
            print(f"El resultado es: {c}Ω") #Resultado
        else:
            print("El valor indicado NO puede ser 0")  #Que pasa si es 0

    else:                                      #En esta parte ejecutamos una sintaxis de validacion de termino valido
        print("Dato Inválido")   #Si el usuario elije otra letra que no sea v,a ó r da este mensaje
        print(f"'{cuestion}' no es una opcion valida") #Hacemos saber el problema
        print("Las opciones validas son V= Voltaje, A= Corriente (Amperaje) y R= Resistencia") #Correccion de errores

any(cuestion)