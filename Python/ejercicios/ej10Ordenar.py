
def Ordenar():
    op = "si"
    while op == "si":
        lista = input("Introduce una lista separados con espacios: ")
        lista = lista.split()
        lista.sort()
        print(lista)

        choose = input("Si quieres continuar teclea 'si', sino pulse cualquier otra tecla: ")
        op = choose.lower()
    print("¡Hasta luego!")

# Ordenar()