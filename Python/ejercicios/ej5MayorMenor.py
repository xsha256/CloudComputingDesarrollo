

def CalcularMayMen():
    op = "si"
    while op == "si":
        try:
                numeros = input("Introduce una lista de números separados por espacios: ").split()
                mayor = float("-inf")
                menor = float("inf")

                for numero in numeros:
                        if int(numero) > mayor:
                                mayor = int(numero)
                        if int(numero) < menor:
                                menor = int(numero)

                print(f"El numero mayor es: {mayor}")
                print(f"El numero menor es: {menor}")
        except:
                print("No has introducido numeros")

        choose = input("Si quieres continuar teclea 'si', sino pulse cualquier otra tecla: ")
        op = choose.lower()
    print("¡Hasta luego!")

# CalcularMayMen()