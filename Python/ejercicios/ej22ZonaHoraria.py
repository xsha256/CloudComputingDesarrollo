 #! 2. Crea un programa que le pregunte al usuario su zona horaria y le muestre la hora actual en esa zona. El programa debe manejar excepciones en caso de que la zona horaria ingresada no sea válida.

from datetime import datetime, timedelta
from pytz import timezone  
import pytz 

def ZonaHoraria():
    op = "s"
    while op == "s":
        print("Zonas Horarias Disponibles:")
        print (*pytz.all_timezones,sep='\n')
        zona = input("Pon tu zona horaria(continente/ciudad): ")
        try:
            print( datetime.now(timezone(zona)).strftime("%H:%M"))
        except: 
            print("No has puesto la zona corretamente")

        choose = input("Si  quieres continuar teclea 's', sino pulse cualquier otra tecla: ")
        op = choose.lower()
    print("¡Hasta luego!")


ZonaHoraria()