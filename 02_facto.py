#Estos son los datos asignados para las cajas con sus respectivos cajeros
cajeros = { 
    "241024": {"nombre": "Eliannis", "box": "1"},
    "121212": {"nombre": "Jesus", "box": "2"},
    "311005": {"nombre": "Alejandro", "box": "3"},
    "1": {"nombre": "KRONNOS", "box": "PROGRAMADOR"}
}

# Estos son los productos disponibles en el sistema cada uno con un codigo y precio preestablecido
items = {
    "001":{"nombre": "Arroz La siembra 1kg", "precio": 2.4, "cod": "001"},
    "002":{"nombre": "Pasta Horizonte 1kg", "precio": 2.5, "cod": "002"},
    "003":{"nombre": "Azucar La Pastora 900g", "precio": 3, "cod": "003"},
    "004":{"nombre": "Leche La Campiña 400g", "precio": 5.47, "cod": "004"},
    "005":{"nombre": "Mantequilla Mavesa 250g", "precio": 2.25, "cod": "005"},
    "006":{"nombre": "Aceite Vatel 1lt", "precio": 4, "cod": "006"},
    "007":{"nombre": "Salsa Pampero 397ml", "precio": 1.27, "c": "007"},
    "008":{"nombre": "Harina Pan 1kg", "precio": 0.87, "cod": "008"},
    "009":{"nombre": "Sal Cristal 1kg", "precio": 0.5, "cod": "009"},
    "010":{"nombre": "Sardina en aceite Peñero", "precio": 0.4, "cod": "010"},
}

factura = []

list_i = ("001: arroz", "002: pasta", "003: azucar", 
          "004: leche", "005: mantequilla", "006: aceite",
          "007: salsa", "008: harina", "009: sal", "010: sardina")

# Inicio del sistema con un modelo de login predeterminado
atemps = 0 # Numero de intentos admitidos 
veriy_c = False # Validacion por boolean
veriy_p = False # Validacion de lista de productos
total_n = 0
empresa = "\t    Inversiones Shaddai C.A""\n\t         " \
"J-89570221024\n\t    " \
"San Juan  de los Morros""\n\t         " \
"Edo.  Guárico"
saludo = "¡Gracias por su Compra!"

# Bucle de Validacion de usuario
while(atemps < 3 and veriy_c == False): # Mientras los intentos sean menores a 3 y la verificacion se mantenga en false
    key = input("Password: ") # Recibe la contraseña 
    if key in cajeros: # Condiciona y valida la residencia de la misma en el diccionario
        dato = cajeros[key] # Si esta, guarda los datos en otra variable 
        veriy_c = True # Verificacion es admitida
        atemps = False # Se usara como boolean en el siguiente bucle
        name = dato['nombre']
        caja = dato['box']
        if(key == "1"):
            print(f"SISTEM ON \nBienvenido: Mr.{dato['nombre']}")
        else:
            print(f"SISTEM ON \nCaja: {dato['box']}") # Publica que el sistema esta encendido y que caja esta trabajando
    elif(key != cajeros):
        atemps += 1
        if(atemps < 3):
            print(f"Contraseña Inválida \n {atemps}/3")
        elif(atemps == 3):
            print("Has alcanzado el limite de intentos permitidos \nSISTEM OFF")

print("Si desea verificar el inventario presione: I \nSi desea publicar factura presione: F")
# Bucle de validacion productos 
while(atemps == False):
    code = input("Codigo del producto: ")
    if (code == "i" or code == 'I'):
        print(list(list_i))

    if (code == 'f' or code == 'F'):
        break

    if code in items:
        dato = items[code]
        print("="*50)
        print(dato["nombre"], dato["precio"], "$")
        print("="*50)
        print("="*10 + "Presione 0 para cancelar" + "="*16)
        cant = int(input("Cantidad: "))
        total_p = 0

        if (cant > 0): 
            total_p = float(dato["precio"] * cant)
            total_n = total_n + total_p
            producto = {
                "nombre" : {dato['nombre']},
                "precio" : {dato['precio']},
                "cantidad" : {cant},
                "total" : {total_p}
            }

        elif(cant == 0):
            producto = ""

        if(producto != ""):
            factura.append(producto)

iva = total_n * 0.16
tni = total_n + iva
# print(f"Total neto: {total_n:.2f}$   +   IVA(16%) = {iva:.2f}$ \nTotal + IVA: {tni:.2f}$")
def imprimir():
    print("="*50)                 
    print("="*19,"Factura","="*22)
    print("="*50)                 
    print("="*50)
    print("="*19,"Factura","="*22)
    print("="*50)
    print("="*50)
    print("="*19,"Factura","="*22)
    print("="*50)
    print(f" {empresa}")
    print(f"-"*50)
    if(key == "1"):
        print(f"{name} : {caja}")
    else:
        print(f"Cajero: {name} \nCaja: #{caja}")
    print("-"*50)

    for producto in factura:
        print(f"{producto['cantidad']} x {producto['nombre']}          {producto['precio']}$")

    print("-"*50)
    print(f"SUBTOTAL: {total_n:.2f}$")
    print(f"I.V.A (16%): {iva:.2f}$")
    print(f"TOTAL A PAGAR: {tni:.2f}$")
    print(f"="*50)
    print("="*19,"Factura","="*22)
    print(f"="*50)
    print("="*19,"Factura","="*22)
    print("="*50)
    print("="*11,f"{saludo}","="*14)
    print("="*50)


imprimir()
total_n = 0
iva = 0
tni = 0