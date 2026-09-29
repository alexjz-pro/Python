import random

preguntas = [
    {"pregunta" : "¿Que funcion se utiliza para mostrar informacion en pantalla?",
    "opciones" : ["show()", "print()", "display()", "write()"], "respuesta" : "print()"},
    {"pregunta" :"¿Que simbolo se utiliza para asignar un valor a una variable?",
    "opciones" : ["==",":","=","=>"], "respuesta" : "="},
    {"pregunta" :"¿Cual de los siguientes valores es un numero entero?", 
    "opciones" : ["'25'","25.5","true","25"], "respuesta" : "25"},
    {"pregunta" :"¿Que tipo de dato representa los valores 'True' y 'False'?", 
    "opciones" : ["boolean","bool","logic","bit"], "respuesta" : "boolean"},
    {"pregunta" :"¿Que estructura se utiliza para almacenar varios valores ordenados y modificables?", 
    "opciones" : ["tupla","diccionario","lista","conjunto"], "respuesta" : "lista"},
    {"pregunta" :"¿Cual es el indice del primer elemento de una lista?", 
    "opciones" : ["0","1","-1","first"], "respuesta" : "0"},
    {"pregunta" :"¿Como se escribe correctamente una lista en Python?", 
    "opciones" : ["{1, 2, 3}","[1, 2, 3]","(1, 2, 3)","<1, 2, 3>"], "respuesta" : "[1, 2, 3]"},
    {"pregunta" :"¿Que estructura almacena datos mediante pares clave-valor?", 
    "opciones" : ["lista","diccionario","tupla","cadena"], "respuesta" : "diccionario"},
    {"pregunta" :"¿Que palabra reservada se utiliza para crear una condicion?", 
    "opciones" : ["when","if","check","condition"], "respuesta" : "if"},
    {"pregunta" :"¿Que metodo agrega un elemento al final de una lista?", 
    "opciones" : ["add()","append()","insertEnd()","push()"], "respuesta" : "append()"},
    {"pregunta" :"¿Que metodo elimina y devuelve el ultimo elemento de una lista?", 
    "opciones" : ["delete()","remove()","pop()","clear()"], "respuesta" : "pop()"},
    {"pregunta" :"¿Que estructura de datos es inmutable?", 
    "opciones" : ["lista","diccionario","conjunto","tupla"], "respuesta" : "tupla"},
    {"pregunta" :"¿como se crea una tupla con varios elementos?", 
    "opciones" : ["[1, 2, 3]","{1, 2, 3}","(1, 2, 3)","<1, 2, 3>"], "respuesta" : "(1, 2, 3)"},
    {"pregunta" :"¿Que caracteristica principal tiene un conjunto (set)?", 
    "opciones" : ["permite elementos repetidos","no permite elementos repetidos","solo almacena texto","siempre ordena sus elementos"], "respuesta" : "no permite elementos repetidos"},
    {"pregunta" :"¿Como se crea un conjunto vacio?", 
    "opciones" : ["{}","[]","set()","empty()"], "respuesta" : "set()"},
    {"pregunta" :"¿Que operador se utiliza para comprobar si dos valores son diferentes?", 
    "opciones" : ["<>","!=","!==","not="], "respuesta" : "!="},
    {"pregunta" :"¿Que bloque se utiliza para capturar errores o excepciones?", 
    "opciones" : ["try y except","check y error","test y catch","error y handle"], "respuesta" : "try y except"},
    {"pregunta" :"¿Que funcion devuelve la cantidad de elementos de una coleccion?", 
    "opciones" : ["count()","size()","length()","len()"], "respuesta" : "len()"},
    {"pregunta" :"¿Que produce range(5)?", 
    "opciones" : {"los numeros del 1 al 5","los numeros del 0 al 5","los numeros del 0 al 4","solo el numero 5"}, "respuesta" : "los numeros del 0 al 4"},
    {"pregunta" :"¿Que palabras se utiliza cuando se desea comprobar otra condicion?", 
    "opciones" : ["else if","elseif","elif","otherwise"], "respuesta" : "elif"},
    {"pregunta" : "¿Que palabra se ejecuta cuando ninguna condicion anterior se cumple?", 
    "opciones" : ["finally","default","else","last"], "respuesta" : "else"},
    {"pregunta" : "¿Que ciclo se utiliza normalmente para recorrer los elementos de una coleccion?", 
    "opciones" : ["repeat","loop","for","each"], "respuesta" : "for"},
    {"pregunta" : "¿Que ciclo se repite mientras una condicion sea verdadera?", 
    "opciones" : ["while","during","repeat","until"], "respuesta" : "while"},
    {"pregunta" : "¿Que palabra se utiliza para definir una funcion?", 
    "opciones" : ["function","define","def","func"], "respuesta" : "def"},
    {"pregunta" : "¿Que palabra se utiliza para devolver el resultado desde una funcion?", 
    "opciones" : ["send","return","output","back"], "respuesta" : "return"},
    {"pregunta" : "¿Que palabra se utiliza para importar una libreria o modulo?", 
    "opciones" : {"import","include","require","using"}, "respuesta" : "import"},
    {"pregunta" : "¿Que simbolo se utiliza para escribir un comentario de una linea?", 
    "opciones" : ["//","<!--","#","--"], "respuesta" : "#"},
    {"pregunta" : "¿Que funcion permite conocer el tipo de dato de un valor?", 
    "opciones" : ["typeof()","type()","datatype()","classof()"], "respuesta" : "type()"},
    {"pregunta" : "¿Que instruccion se utiliza normalmente para capturar datos escritos por el usuario?", 
    "opciones" : ["get()","scan()","input()","read()"], "respuesta" : "input()"},
    {"pregunta" : "Como se contruye un bucle infinito", "opciones" : ["while true:", "while true():", "loop()", "for of:"],
     "respuesta" : "while true:"}
]

textos = ["Valla estuviste cerca.", "Por poco aciertas...", "Venga le estas pillando el rollo", "Ups... Esa no era.", "Intentemozlo de nuevo"]

# opcion con funcion
# def aleatorio():
#     i = random.randint(0, len(textos) -1)
#     publico = textos[i]
#     print(publico)

def quiz():
    puntaje = 0

    random.shuffle(preguntas)

    for pregunta in preguntas:
        print(f"{pregunta['pregunta']}")
        print("="*64)

        for opc in pregunta['opciones']:
            print(f"==>   {opc} \n")
        
        error = random.choice(textos)

        while True:
            user = str(input("Ingrese la respuesta: ").strip().lower())
            if not user:
                print("="*64)
                print("La respuesta no puede estar Vacia.")
                print("="*64)
    
            if user == pregunta['respuesta']:
                puntaje = puntaje + 35
                print("="*64)
                print("correcto +35 pts")
                print("="*64)
                break
            else:
                puntaje = puntaje - 25
                print("="*64)
                # aleatorio()
                print(f"{error} -25")
                print("-"*64)
                print(f"R: {pregunta['respuesta']}")
                print("="*64)
                break

    print(f"E N D   G A M E \nPuntaje: {puntaje}")