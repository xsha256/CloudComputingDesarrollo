 #! 5. Crea un programa en Python que acepte una cadena de caracteres y devuelva la cadena invertida (por ejemplo, "hola" se convertiría en "aloh"). El programa debe utilizar un bucle `for` para recorrer la cadena y construir la cadena invertida.

def Convertir():
    op = "s"
    while op == "s":
        cadena = input("Escribe una cadena: ")
        cadenaReversa = ""
        for palabra in cadena:
            cadenaReversa = palabra + cadenaReversa 

        print(cadenaReversa)

        choose = input("Si  quieres continuar teclea 's', sino pulse cualquier otra tecla: ")
        op = choose.lower()
    print("¡Hasta luego!")



Convertir()