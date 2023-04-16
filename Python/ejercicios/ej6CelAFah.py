
def celAfah():
    op = "si"
    while op == "si":
        try:
            cel = int(input("Introduce grados Celsius: "))
            fah = cel * 1.8 + 32
            print(f"{cel} Celsius en Fahrenheit = {fah} ")
        except:
            print("No has introducido un numero")
        choose = input("Si quieres continuar teclea 'si', sino pulse cualquier otra tecla: ")
        op = choose.lower()
    print("¡Hasta luego!")

#celAfah()