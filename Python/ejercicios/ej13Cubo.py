

def CalCubo():
    op = "si"
    while op == "si":
        try: 
            lado = int(input("Intoduce un lado(numero): "))
            area = 6 * lado^2
            volumen = lado^3
            print(f"El área del cubo: {area}")
            print(f"El volumen del cubo: {volumen}")

        except:
            print("No has introducido un numero")
        
        choose = input("Si quieres continuar teclea 'si', sino pulse cualquier otra tecla: ")
        op = choose.lower()
    print("¡Hasta luego!")

#CalCubo()