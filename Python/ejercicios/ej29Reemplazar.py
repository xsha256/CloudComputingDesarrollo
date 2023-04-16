 #! 9. Crea un programa en Python donde la entrada sean una cadena de caracteres, una palabra y una palabra de reemplazo ,el resultado debe ser la cadena con todas las ocurrencias de la palabra reemplazadas por otra palabra. El programa debe utilizar un bucle `while` para buscar todas las ocurrencias de la palabra y reemplazarlas.

def reempCadena():
    op = "s"
    while op == "s":

        lista = input("introduce una lista de palabras separadas con espacios: ")
        print(lista)
        palabra = input("Escribe la palabra que va a ser reemplazada: ")
        palabraRee = input("Escribe la palabra que va a reemplazar: ")
        lista = lista.replace(palabra, palabraRee)
        
    choose =  input("Si quieres continuar teclea 's', sino pulse cualquier otra tecla: ")
    op = choose.lower()
    
