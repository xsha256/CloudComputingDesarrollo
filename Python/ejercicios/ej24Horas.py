 #! 4. Crea un programa que le pida al usuario una hora en formato "hh:mm" y luego calcule y muestre la hora en 24 horas (por ejemplo, "19:30" se convertiría en "19:30"). La hora debe ser validada para asegurarse de que esté en el formato correcto y de que las horas y los minutos sean números enteros.


from datetime import datetime

def convertir_hora():
    op = "s"
    while op == "s":
        hora = input("escribe una hora (hh:mm): ")
        pmAm = input("La hora es pm o am? ").lower()
        try: 
            hora = (f"{hora}  {pmAm}")
            dt = datetime.strptime(hora, '%I:%M %p')
            dt.strftime('%H:%M')
            print(dt.strftime('%H:%M'))
        except:
            print("Formato incorrecto")

        choose = input("Si  quieres continuar teclea 's', sino pulse cualquier otra tecla: ")
        op = choose.lower()
    print("¡Hasta luego!")


convertir_hora()