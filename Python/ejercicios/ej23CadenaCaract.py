 #! 3. Crea un programa en Python que tome una cadena de caracteres y devuelva el número de palabras que contiene. El programa debe utilizar un bucle `while` para recorrer la cadena y contar las palabras.


def CadenaCar():
    op = "s"
    while op == "s":
        cadena = input("Escribe una frase: ").split()

        count = 0
        while(count < len(cadena)):
            count += 1
        print(count)

        choose = input("Si  quieres continuar teclea 's', sino pulse cualquier otra tecla: ")
        op = choose.lower()
    print("¡Hasta luego!")


CadenaCar()