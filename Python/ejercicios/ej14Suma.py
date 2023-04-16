def CalNumPares():

    op = "si"
    while op == "si":
        numeros = input("Introduce una lista de números separados por espacios: ").split()
        pares = 0
        for num in numeros:
            if num.isdigit():
                if int(num) % 2 == 0:
                    pares = pares + int(num)

            else:
                print("Error: al menos uno de los valores introducidos no es número")
        print(f"La suma de todos los numeros pares: {pares}")
        choose = input("Si quieres continuar teclea 'si', sino pulse cualquier otra tecla: ")
        op = choose.lower()
    print("¡Hasta luego!")

#CalNumPares()