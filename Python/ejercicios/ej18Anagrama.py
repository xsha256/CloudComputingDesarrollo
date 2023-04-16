#! Crea un algoritmo que determine si una cadena de texto es un anagrama de otra cadena de texto.

def Anagrama():
    op = "si"
    while op == "si":

        palabra1 = input("Escribe la primera palabra: ").lower()
        palabra2 = input("Escribe la seguna palabra: ").lower()

        if len(palabra1) != len(palabra2):
            print("Las palabras no son anagramas")

        else:

            if sorted(palabra1) == sorted(palabra2):
                print("Las palabras son anagramas")
            else:
                print("Las palabras no son anagramas")
        
        choose = input("Si quieres continuar teclea 'si', sino pulse cualquier otra tecla: ")
        op = choose.lower()
    print("¡Hasta luego!")

#Anagrama()