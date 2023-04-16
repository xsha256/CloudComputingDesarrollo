
#! Crea un algoritmo que calcule el factorial de un número entero.
def Factorial():
    op = "si"
    while op == "si":
        try:
            n = int(input("Introduce un número: "))
            fac = 1
            for i in range(1, n+1):
                fac = fac * i

            print(fac)
        except:
             print("No has introducido un numero")

        choose = input("Si quieres continuar teclea 'si', sino pulse cualquier otra tecla: ")
        op = choose.lower()
    print("¡Hasta luego!")

#Factorial()