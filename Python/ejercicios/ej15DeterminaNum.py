
#! Crea un algoritmo que determine si un número es positivo, negativo o cero.

def determinaNum():
    op = "si"
    while op == "si":
        try:
            num = int(input("Introduce un numero "))
            if num > 0:
                print(f"El numero {num} es: positivo")
            elif num < 0:
                print(f"El numero {num} es: negativo")

            else:
                print(f"El numero {num} es: cero")

        except:
            print("No has introducido un numero")
        
        choose = input("Si quieres continuar teclea 'si', sino pulse cualquier otra tecla: ")
        op = choose.lower()
    print("¡Hasta luego!")

#determinaNum()