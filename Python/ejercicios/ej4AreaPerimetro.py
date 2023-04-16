def CalcularAreaPer():
    op = "si"
    while op == "si":
        radio = input("Escribe el radio: ")
        #! π = 3.14159
        pi = 3.14159
        area = 0
        perimetro = 0

        if str(radio).isnumeric():

            #! Área = π × radio²
            area = pi * int(radio) ** 2

            #! Perímetro = 2 × π × radio
            perimetro = 2 * pi * int(radio)

            print(f"  El área es: {area:.2f}")
            print(f"  El perímetro es: {perimetro:.2f}")

            choose = input("Si quieres continuar teclea 'si', sino pulse cualquier otra tecla: ")
            op = choose.lower()

        else:
            print("Radio inválido")
    print("¡Hasta luego!")

# CalcularAreaPer()