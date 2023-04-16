
def parImpar():
    op = "si"
    while op == "si":
        try:
                num = int(input("Escribe un número: "))

                if num%2 == 0:
                        print(f"{num} es par")
                else:
                        print(f"{num} es impar")
        except:
            print("No has introducido un numero")
        
        choose = input("Si quieres continuar teclea 'si', sino pulse cualquier otra tecla: ")
        op = choose.lower()
    print("¡Hasta luego!")

#parImpar()

