 #! 1. Crea un programa en Python que acepte una fecha como cadena de caracteres en formato `"dd/mm/aaaa"` y devuelva la fecha en formato `"aaaa-mm-dd"`, con el año primero. El programa debe manejar excepciones en caso de que la cadena no tenga el formato correcto.
from datetime import datetime 


def Fecha():
    op = "s"
    while op == "s":
        fechaStr = input("Pon una fecha en formato 'dd/mm/aaaa': ")
        try:
            fecha = datetime.strptime(fechaStr, '%d/%m/%Y').date()
            print(fecha)
        except:
            print("No has puesto la fecha corretamente")
        choose = input("Si  quieres continuar teclea 's', sino pulse cualquier otra tecla: ")
        op = choose.lower()
    print("¡Hasta luego!")



Fecha()
