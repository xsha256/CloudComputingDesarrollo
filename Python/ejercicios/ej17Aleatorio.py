 #! Crea un algoritmo que genere un número aleatorio entre 1 y 100, y le pida al usuario adivinarlo. El algoritmo deberá indicar si el número introducido es mayor o menor que el número aleatorio, hasta que el usuario adivine el número correcto.

import random

def Aleatorio():
    op = "si"
    while op == "si":
        try: 
            numAleatorio = random.randint(1, 100)
            print(numAleatorio)
            num = int(input("Adivina el número aleatorio: "))
            while num != numAleatorio:             
                if num > numAleatorio:
                    print("El número introducido mayor que el número aleatorio")
                    num = int(input("Introduce un numero menor: "))
                    
                elif num < numAleatorio:
                    print("El número introducido menor que el número aleatorio")
                    num = int(input("Introduce un numero mayor: "))
                    
            print(f"Has adivinado el número correctamente")

        except:
            print("No has introducido un numero")
        
        choose = input("Si quieres continuar teclea 'si', sino pulse cualquier otra tecla: ")
        op = choose.lower()
    print("¡Hasta luego!")

#Aleatorio()
    
