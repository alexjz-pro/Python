from rpython import resolver
from pteory import quiz
from exercices import ejercicio
from programar import programa

def menu():
    i = 0
    while True:
        print("="*64)
        print("   P r i o r i t y \n1: Resuelve Python \n2: Preguntas teóricas \n3: Ejercicios Básicos \n4: A Programar" \
        "\n5: Salir")
        select = input("Elije una opcion: ").strip()

        if select == "1":
            print("="*64)
            print("resolver()")

        elif select == "2":
            print("="*64)
            print("quiz()")

        elif select == "3":
            print("="*64)
            print("ejercicio()")  

        elif select == "4":
            print("="*64)
            print("programa()") 

        elif select == "5":
            print("="*15, "C e r r a n d o  P r i o r i t y","="*15)
            break
        
        else:
            i = i + 1
            if i < 3:
                print("="*64)
                print("Elija una Opcion Válida.")
            elif i == 3:
                print("="*64)
                print("Demasiados intentos fallidos...")
                print("="*15, "C e r r a n d o  P r i o r i t y","="*15)
                break

menu()

