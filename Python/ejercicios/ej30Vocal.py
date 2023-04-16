 #! 10. Crea un un programa en Python que tome una lista de cadenas de caracteres y devuelva una nueva lista que contenga solo las cadenas que contienen al menos una vocal. La función debe utilizar un bucle `for` para recorrer la lista y una estructura de control de flujo para filtrar las cadenas.
 

def Vocal():
    op = "s"
    while op == "s":
        
        cadena = input("Escribe una cadena: ")
        cadena = cadena.split()
        vocal = ['a', 'o', 'e', 'u', 'i']
        nuevaLista = []
        
        for palabra in cadena:
            for car in vocal:        
                if car in palabra:
                    if palabra not in nuevaLista:
                        nuevaLista.append(palabra)
        print(nuevaLista)

    choose = input("Si quieres continuar teclea 's', sino pulse cualquier otra tecla: ")
    op = choose.lower()

