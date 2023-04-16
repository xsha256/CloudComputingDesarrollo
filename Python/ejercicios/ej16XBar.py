# ! Dada una lista de números enteros, crea un algoritmo que calcule la media de la lista

def XBar():
    op = "si"
    while op == "si":
        try: 
            lista = input("Introduce una lista de números separados por espacios: ").split()
            print(lista)
            n = 0
            suma = 0
            for num in lista:
                        suma = int(num) + suma
                        n = n + 1
            xbar = suma/n
            print(f"x̄  = {suma} / {n}")
            print(f"La media de la lista: {xbar:.2f}")

        except:
            print("No has introducido un numero")
        
        choose = input("Si quieres continuar teclea 'si', sino pulse cualquier otra tecla: ")
        op = choose.lower()
    print("¡Hasta luego!")

#XBar()


