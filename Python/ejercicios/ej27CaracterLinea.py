 #!7. Crea un programa que le pida al usuario una cadena de caracteres y luego imprima cada carácter en una línea separada. El programa debe utilizar un bucle `for` para recorrer la cadena.


def CadenaCar():
    op = "s"
    while op == "s":

        cadena = input("Escribe una cadena: ")
        for caracter in cadena:
            print(caracter)
            print()

        choose =  input("Si quieres continuar teclea 's', sino pulse cualquier otra tecla: ")
        op = choose.lower()

