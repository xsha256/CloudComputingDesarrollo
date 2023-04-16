 #! Dada una lista de números enteros, crea un algoritmo que elimine los números duplicados de la lista.

def Duplicados():
    op = "si"
    while op == "si":
        try: 
            lista = input("Introduce una lista de números separados por espacios: ").split()
            nuevaLista = []
            for num in lista:
                if int(num) not in nuevaLista:
                    nuevaLista.append(int(num))

            print(f"La nueva lista sin repetidos es: {nuevaLista}")
        
        except:
            print("No has introducido un numero")
        
        choose = input("Si quieres continuar teclea 'si', sino pulse cualquier otra tecla: ")
        op = choose.lower()
    print("¡Hasta luego!")

#Duplicados()