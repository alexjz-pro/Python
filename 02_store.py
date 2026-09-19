#Estos son los datos asignados para las cajas con sus respectivos cajeros
cajeros = { 
    "102938": {"nombre": "User1", "box": "1"},
    "001199": {"nombre": "User2", "box": "2"},
    "123456": {"nombre": "User3", "box": "3"},
    "1": {"nombre": "Admin", "box": "PROGRAMADOR"}
}

# Estos son los productos disponibles en el sistema cada uno con un codigo y precio preestablecido
items = {
    "001":{"nombre": "Producto 1", "precio": 1},
    "002":{"nombre": "Producto 2", "precio": 2},
    "003":{"nombre": "Producto 3", "precio": 3},
    "004":{"nombre": "Producto 4", "precio": 4},
    "005":{"nombre": "Producto 5", "precio": 5},
    "006":{"nombre": "Producto 6", "precio": 4.1},
    "007":{"nombre": "Producto 7", "precio": 3.25},
    "008":{"nombre": "Producto 8", "precio": 2.5},
    "009":{"nombre": "Producto 9", "precio": 1.75},
    "010":{"nombre": "Producto 10", "precio": 5.3},
}

factura = []

# Inicio del sistema con un modelo de login predeterminado
atemps = 0 # Numero de intentos admitidos 
veriy_c = False # Validacion por boolean
veriy_p = False # Validacion de lista de productos
total_n = 0
empresa = "\t    Inversiones ------- C.A""\n\t         " \
"J-***********\n\t    " \
"Ciudad que quiera int""\n\t         " \
"Edo.  *******"
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
        contador = 1
        while contador <= 10:
            impre = f"{contador:03d}"
            print("-"*10, "Lista de Productos", "-"*10)
            for impre in items:
                flash = items[impre]
                print(f"{impre} --- {flash['nombre']} --- {flash['precio']}")
                contador += 1
        print("-"*40)
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
                "nombre" : f"{dato['nombre']}",
                "precio" : f"{dato['precio']}",
                "cantidad" : f"{cant}",
                "total" : f"{total_p}"
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