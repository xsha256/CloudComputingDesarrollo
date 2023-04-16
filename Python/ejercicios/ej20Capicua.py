    #! Crea un algoritmo que determine si un número es capicúa o no.

def Capicua():
    op = "si"
    while op == "si":
        try: 
            num=int(input("Introduce un numero entero "))
            numReverso = str(num)[::-1]
            if str(numReverso) == str(num):
                print(f"El número {num} es capicúa")
            else:
                print(f"El número {num} no es capicúa")

        except:
            print("No has introducido un numero")
        
        choose = input("Si quieres continuar teclea 'si', sino pulse cualquier otra tecla: ")
        op = choose.lower()
    print("¡Hasta luego!")


#Capicua()