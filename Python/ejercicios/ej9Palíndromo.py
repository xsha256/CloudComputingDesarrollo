
def Palindromo():
    op = "si"
    while op == "si":
        cadena = input("Introduce una cadena de palabras: ")
        #! lower(): para convertir a minúsculas
        #! replace(): para eliminar espacios en blanco
        cadenaOri = cadena.lower().replace(" ", "")

        #! invertir la cadena
        cadenaReversa = cadenaOri[::-1]

        if cadenaOri == cadenaReversa:
            print(f"La cadena {cadenaOri} es un palíndromo")
        else:
            print(f"La cadena {cadenaOri} no es un palíndromo")
        
        choose = input("Si quieres continuar teclea 'si', sino pulse cualquier otra tecla: ")
        op = choose.lower()
    print("¡Hasta luego!")

#Palindromo()