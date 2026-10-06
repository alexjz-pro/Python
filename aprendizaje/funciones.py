"""
Guía práctica: aprendizaje de funciones en Python

Este archivo reúne ejemplos ejecutables, organizados desde lo básico hasta
conceptos intermedios. Lee cada bloque, ejecútalo y modifica los valores para
practicar.
"""

# ================================================================
# 1. FUNCIONES BÁSICAS
# ================================================================

def saludar():
    """Muestra un saludo en consola."""
    print("Hola, ¡bienvenido a las funciones en Python!")


# Llamar (ejecutar) una función:
saludar()


# ================================================================
# 2. PARÁMETROS Y ARGUMENTOS
# ================================================================

def saludar_persona(nombre):
    """Recibe un nombre y muestra un saludo personalizado."""
    print(f"Hola, {nombre}")


saludar_persona("Carlos")


def presentar(nombre, edad, ciudad):
    print(f"Me llamo {nombre}, tengo {edad} años y vivo en {ciudad}.")


# Argumentos posicionales: importa el orden.
presentar("Ana", 22, "Caracas")

# Argumentos por nombre: el orden deja de importar.
presentar(ciudad="Caracas", nombre="Luis", edad=25)


# ================================================================
# 3. VALORES POR DEFECTO
# ================================================================

def crear_saludo(nombre, mensaje="Hola"):
    """Construye y retorna un saludo; mensaje tiene valor por defecto."""
    return f"{mensaje}, {nombre}"


print(crear_saludo("María"))
print(crear_saludo("Pedro", "Buenas tardes"))


# ================================================================
# 4. RETURN: DEVOLVER RESULTADOS
# ================================================================

def sumar(a, b):
    return a + b


def restar(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    if b == 0:
        return None
    return a / b


resultado = sumar(8, 4)
print(f"8 + 4 = {resultado}")
print(f"8 / 0 = {dividir(8, 0)}")

# print muestra un valor; return permite reutilizarlo.
def cuadrado(numero):
    return numero ** 2

print(f"El cuadrado de 5 es {cuadrado(5)}")


# ================================================================
# 5. RETORNAR VARIOS VALORES
# ================================================================

def operaciones(a, b):
    """Devuelve una tupla con suma, resta y producto."""
    return a + b, a - b, a * b


suma, diferencia, producto = operaciones(10, 3)
print(suma, diferencia, producto)


# ================================================================
# 6. *args Y **kwargs
# ================================================================

def sumar_todos(*numeros):
    """Recibe cualquier cantidad de números posicionales."""
    return sum(numeros)


print(sumar_todos(1, 2, 3, 4, 5))


def mostrar_perfil(**datos):
    """Recibe datos nombrados en forma de diccionario."""
    for clave, valor in datos.items():
        print(f"{clave}: {valor}")


mostrar_perfil(nombre="Sofía", rol="Estudiante", ciudad="Caracas")


# ================================================================
# 7. ÁMBITO DE VARIABLES (SCOPE)
# ================================================================

mensaje_global = "Soy una variable global"

def demostrar_scope():
    mensaje_local = "Solo existo dentro de esta función"
    print(mensaje_global)
    print(mensaje_local)


demostrar_scope()
# print(mensaje_local)  # Esto produciría un error: no existe fuera de la función.


# ================================================================
# 8. FUNCIONES COMO VALORES
# ================================================================

def doble(numero):
    return numero * 2


def aplicar(funcion, valor):
    """Recibe una función y la ejecuta usando valor."""
    return funcion(valor)


print(aplicar(doble, 6))


# ================================================================
# 9. FUNCIONES LAMBDA
# ================================================================

triplicar = lambda numero: numero * 3
print(triplicar(4))

productos = [
    {"nombre": "Teclado", "precio": 25},
    {"nombre": "Mouse", "precio": 10},
    {"nombre": "Monitor", "precio": 120},
]

# Ordenar una lista usando una lambda como criterio (key).
productos_ordenados = sorted(productos, key=lambda producto: producto["precio"])
print(productos_ordenados)


# ================================================================
# 10. VALIDACIÓN Y MANEJO DE ERRORES
# ================================================================

def calcular_promedio(notas):
    """Calcula el promedio de una lista no vacía de notas numéricas."""
    if not notas:
        raise ValueError("La lista de notas no puede estar vacía.")
    return sum(notas) / len(notas)


try:
    print(f"Promedio: {calcular_promedio([15, 18, 20]):.2f}")
except ValueError as error:
    print(f"Error: {error}")


# ================================================================
# 11. EJERCICIOS PARA PRACTICAR
# ================================================================

# Ejercicio 1: crea una función es_par(numero) que devuelva True o False.
def es_par(numero):
    return numero % 2 == 0


# Ejercicio 2: crea una función convertir_celsius_a_fahrenheit(celsius).
def convertir_celsius_a_fahrenheit(celsius):
    return celsius * 9 / 5 + 32


# Ejercicio 3: crea una función contar_vocales(texto).
def contar_vocales(texto):
    vocales = "aeiouáéíóú"
    return sum(letra.lower() in vocales for letra in texto)


# Ejercicio 4: crea una función que reciba una lista y devuelva el mayor valor.
def mayor_numero(numeros):
    if not numeros:
        return None
    return max(numeros)


print(es_par(10))
print(convertir_celsius_a_fahrenheit(25))
print(contar_vocales("Funciones en Python"))
print(mayor_numero([4, 12, 7, 9]))


# ================================================================
# 12. MINI-PROYECTO: CALCULADORA POR FUNCIONES
# ================================================================

def calculadora(a, b, operacion):
    """Ejecuta una operación básica según el texto recibido."""
    operaciones_disponibles = {
        "sumar": sumar,
        "restar": restar,
        "multiplicar": multiplicar,
        "dividir": dividir,
    }

    funcion = operaciones_disponibles.get(operacion.lower())
    if funcion is None:
        return "Operación no válida. Usa sumar, restar, multiplicar o dividir."

    resultado = funcion(a, b)
    if resultado is None:
        return "No es posible dividir entre cero."
    return resultado


print(calculadora(20, 5, "dividir"))
print(calculadora(20, 0, "dividir"))


# Reto final:
# Crea un archivo llamado utilidades.py, mueve algunas funciones allí
# e impórtalas desde otro archivo usando:
# from utilidades import sumar, calcular_promedio