

def bisiestoONo():
    op = "si"
    while op == "si":
        try:
            anyo = int(input("Intoduce un año: "))

            if anyo % 4 == 0 and anyo % 100 != 0:
                print(f"{anyo} es bisiesto")
            elif anyo % 400 == 0:
                print(f"{anyo} es bisiesto")
            else:
                print(f"{anyo} no es bisiesto")
        except:
            print("No has introducido un año")

        choose = input("Si quieres continuar teclea 'si', sino pulse cualquier otra tecla: ")
        op = choose.lower()
    print("¡Hasta luego!")

#bisiestoONo()