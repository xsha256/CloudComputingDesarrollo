from termcolor import colored
import os 
import platform
# ## Enunciado

if platform.system() == "Windows":
    os.system("cls")
    print("Estás en Windows")
elif platform.system() == "Darwin" :
    os.system("clear")
    print("Estás en MacOS")
elif platform.system() == "Linux" :
    os.system("clear")
    print("Estás en Linux")

#todo: En una clase de programación hay dos alumnos, Ana y Luis, que han asistido a diferentes sesiones de clase. La información se encuentra en un diccionario donde las llaves son los nombres de los alumnos y los valores son tuplas con las sesiones a las que asistieron.


asistencias = {"Ana": (1, 2, 3, 5, 6), "Luis": (2, 3, 4, 6, 7)}


#! Se pide:

#! 1. Calcular la cantidad total de sesiones a las que asistieron Ana y Luis en conjunto.
print(colored("*---------------------------------------------------*", "red"))
for key, value in asistencias.items():
    key
    valueLeng = len(value)
    print(colored(f"{key} Asistió a: {valueLeng} sesiones", "red" ))

total = asistencias["Ana"] + asistencias["Luis"] 
print(colored(f"Ana y Luis Asistieron a: {len(total)} sesiones", "red" ))
print(colored("*---------------------------------------------------*", "red"))

#! 2. Mostrar las sesiones a las que asistieron ambos alumnos.
ana = asistencias.get("Ana", 0)
luis = asistencias.get("Luis", 0)
numSesionesAmbos= []
#todo: op1:
for sesion in ana:
    if sesion  in luis:
        numSesionesAmbos.append(sesion)

#todo: op2:
#* List Comprehension 
numSesionesAmbos = [sesion for sesion in ana if sesion in luis]

print(colored(f"Ana y Luis Asistieron a estas sesiones: {numSesionesAmbos}", "blue" ))
print(colored("*---------------------------------------------------*", "blue"))

#! 3. Mostrar las sesiones a las que asistió uno de los dos alumnos, pero no a las que asistieron ambos.
numSesionAna= []
numSesionLuis= []

#todo: op1:
for sesion in ana:
    if sesion not in luis:
        numSesionAna.append(sesion)
for sesion in luis:
    if sesion not in ana:
        numSesionLuis.append(sesion)

#todo: op2:
#* List Comprehension 
numSesionAna = [sesion for sesion  in ana if sesion not in luis]
numSesionLuis = [sesion for sesion  in luis if sesion not in ana]

SesionesDeCadaUno ={"Ana":numSesionAna, "Luis":numSesionLuis} 
print(colored(f"Las sesiones a las que asistó cada uno por separado: {SesionesDeCadaUno}", "yellow" ))
print(colored("*---------------------------------------------------*", "yellow"))

#! 4. Mostrar las sesiones a las que asistió Ana pero no Luis.
print(colored(f"Luis asistió a estas sesiones: {numSesionLuis}", "green" ))
print(colored("*---------------------------------------------------*", "green"))

#! 5. Mostrar las sesiones a las que asistió Luis pero no Ana.
print(colored(f"Ana asistió a estas sesiones: {numSesionAna}", "cyan"))
print(colored("*---------------------------------------------------*", "cyan"))

