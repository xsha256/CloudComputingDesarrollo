# Ejercicios Python

## Ejercicio 1:

### Calcular la letra del DNI Español:

```cpp
        letraDNI = "TRWAGMYFPDXBNJZSQVHLCKE"

        op = "si"
        while op == "si":

            numero = input("Pon el número de tu DNI: ")
            if len(str(numero)) == 8 and str(numero).isnumeric():

                resto = int(numero) % 23
                print(f"La letra del DNI introducido es: {letraDNI[resto]}")
                choose = input("Quieres buscar otra letra del DNI 'si' o 'no': ")
                op = choose.lower()


            else:
                print("DNI inválido")

        print("¡Hasta luego!")
```


## Ejercicio 2:

### Calcular el salario de un empleado:

```cpp
        op = "si"
        while op == "si":

            salarioBase = int(input("Introduce tu salario base: "))
            horasTrabajadas = int(input("Introduce las horas trabajadas: "))
            percentajeSSocial = int(
                input("Introduce el percentaje de la seguridad social: "))
            percentajeImpuestos = int(
                input("Introduce el percentaje de la impuestos: "))

            sueldoBruto = salarioBase * horasTrabajadas
            descuentoSS = (sueldoBruto * percentajeSSocial) / 100
            descuentoIm = (sueldoBruto * percentajeImpuestos) / 100
            sueldoNeto = sueldoBruto - descuentoIm - descuentoSS
            print(f"Tu sueldo neto es: {sueldoNeto: .2f}")

            choose = input("Quieres calcular otro sueldo 'si' o 'no': ")
            op = choose.lower()
```

## Ejercicio 3:

### Determinar la ruta para llegar a una ciudad por avión. 

```cpp

```

## Ejercicio 4:
###  Calcula el área y perímetro de un círculo dado su radio

```cpp
    #todo: Op: 1
    # #! π = 3.14159
    # pi = 3.14159
    # area = 0 
    # perimetro = 0

    # op = "si"
    # while op == "si":

    #     radio = input("Introduce el radio del círculo: ")
    #     if str(radio).isnumeric():

    #         #! Área = π × radio²
    #         area = pi * int(radio) ** 2

    #         #! Perímetro = 2 × π × radio
    #         perimetro = 2 * pi * int(radio)

    #         print(f"El área es: {area:.2f} ")
    #         print(f"El perímetro es: {perimetro:.2f} ")
    #         choose = input("Quieres calcular otra vez el área y perímetro de un círculo 'si' o 'no': ")
    #         op = choose.lower()

    #     else:
    #         print("Radio inválido")

    # print("¡Hasta luego!")

    #todo: Op: 2
    def CalcularAreaPer(radio):
        #! π = 3.14159
        pi = 3.14159
        area = 0 
        perimetro = 0

        if str(radio).isnumeric():

            #! Área = π × radio²
            area = pi * int(radio) ** 2

            #! Perímetro = 2 × π × radio
            perimetro = 2 * pi * int(radio)

            print(f"+------------------------------+")
            print(f"  El área es: {area:.2f}")
            print(f"  El perímetro es: {perimetro:.2f}")
            print(f"+------------------------------+")

        else:
            print("Radio inválido")
        


    CalcularAreaPer(5)
    CalcularAreaPer(0)
    CalcularAreaPer(1)
```
   

## Ejercicio 5:
### Dada una lista de números enteros, determina cuál es el mayor y cuál es el menor.

```cpp
    def CalcularMayMen():
            numeros = input("Introduce una lista de numeros separados por espacios: ").split()
            mayor = float("-inf")
            menor =  float("inf")

            for numero in numeros:
                    if int(numero) >  mayor:   
                            mayor = int(numero) 
                    if int(numero) < menor:
                            menor = int(numero)

            print(f"El numero mayor es: {mayor}")
            print(f"El numero menor es: {menor}")


    CalcularMayMen()
```

## Ejercicio 6:
### Crea un algoritmo que convierta grados Celsius a Fahrenheit

```cpp
    def celAfah(cel):
        fah = cel * 1.8 + 32
        print(f"{cel} Celsius en Fahrenheit = {fah} ")

    celAfah(50)
```

## Ejercicio 7:
### Dado un número entero, crea un algoritmo que determine si es par o impar.

```cpp
    def parImpar(num):
        if num%2 == 0:
                print(f"{num} es par")
        else:
            print(f"{num} es impar")

    parImpar(2)
    parImpar(3)
    parImpar(6)
    parImpar(13)
```

## Ejercicio 8:
### Crea un algoritmo que determine si un año es bisiesto o no.

```cpp
    def bisiestoONo(anyo):
        if anyo % 4 == 0 and anyo % 100 != 0:
            print(f"{anyo} es bisiesto")
        elif anyo % 4 == 0 and anyo % 100 == 0 and anyo%400 == 0 :
            print(f"{anyo} es bisiesto")
        else:
            print(f"{anyo} no es bisiesto")

    bisiestoONo(2000)
    bisiestoONo(2024)
    bisiestoONo(2023)
    bisiestoONo(2010)   
```

## Ejercicio 9:
### Crea un algoritmo que determine si una cadena de texto es un palíndromo o no.

```cpp
    
    def Palindromo(cadena):
        #! lower(): para convertir a minúsculas
        #! replace(): para eliminar espacios en blanco
        cadenaOri = cadena.lower().replace(" ", "")

        #! invertir la cadena
        cadenaReversa = cadenaOri[::-1]

        if cadenaOri == cadenaReversa:
            print(f"La cadena {cadenaOri} es un palíndromo")
        else:
            print(f"La cadena {cadenaOri} no es un palíndromo")

    Palindromo("Radar")
    Palindromo("lol")
    Palindromo("Ojo")
    Palindromo("hola")
    Palindromo("A Santa at NASA")
```

## Ejercicio 10:
### Dada una lista de nombres, crea un algoritmo que ordene la lista alfabéticamente

```cpp
    def Ordenar(lista):
        lista.sort()
        print(lista)


    lista = ["hola", "test", "adios", "aa", "zz"]
    Ordenar(lista)
```

## Ejercicio 11
### Crea un algoritmo que calcule el factorial de un número entero.

```cpp
    def Factorial(n):
        fac = 1

        for i in range(1, n+1):
            fac = fac * i

        print(fac)


    Factorial(5)
    Factorial(6)
    Factorial(7)
    Factorial(8)
```

## Ejercicio 12
### Dado un número entero, crea un algoritmo que determine si es primo o no

```cpp
import math
#! Dado un número entero, crea un algoritmo que determine si es primo o no

    def EsPrimo(n):
        if n < 2:
            return False
        for i in range(2, int(math.sqrt(n))+1):
            if n % i == 0:
                return False
            
        return True

    def Primo(n):
        if EsPrimo(n):
            print(f"{n}: es primo")
        else:
            print(f"{n}: no es primo")

    Primo(2)
    Primo(4)
    Primo(5)
    Primo(59)
    Primo(10)
    Primo(21)
    Primo(97)
```

## Ejercicio 13
### Crea un algoritmo que calcule el área y volumen de un cubo dado su lado.

```cpp
    def CalCubo(lado):
        area = 6 * lado^2
        volumen = lado^3
        print(f"El área del cubo: {area}")
        print(f"El volumen del cubo: {volumen}")


    CalCubo(10)
    CalCubo(11)
    CalCubo(4)
```

## Ejercicio 14
### Dada una lista de números enteros, crea un algoritmo que calcule la suma de todos los números pares de la lista.

```cpp
    def CalNumPares(lista):
        pares = 0 
        for num in lista:
            if num % 2 == 0:
                pares = pares + num
        print(f"La suma de todos los numeros pares: {pares}")


    lista = [1, 2, 4, 5, 6, 10, 10]
    CalNumPares(lista)

```

## Ejercicio 15
### Crea un algoritmo que determine si un número es positivo, negativo o cero.

```cpp
    def determinaNum(num):
        if num > 0:
            print(f"El numero {num} es: positivo")
        elif num < 0:
            print(f"El numero {num} es: negativo")

        else:
            print(f"El numero {num} es: cero")


    determinaNum(1)
    determinaNum(2)
    determinaNum(20)
    determinaNum(-12)
    determinaNum(0)
    determinaNum(-1)

```

## Ejercicio 16
### Dada una lista de números enteros, crea un algoritmo que calcule la media de la lista.

```cpp
    def XBar(lista):
        n = 0
        suma = 0
        for num in lista:
            suma = num + suma
            n = n + 1
        xbar = suma/n
        print(f"x̄  = {suma} / {n}")
        print(f"La media de la lista: {xbar:.2f}")


    lista = [1, 2, 3, 4, 5, 6, 10]
    XBar(lista)

```

## Ejercicio 17
### Crea un algoritmo que genere un número aleatorio entre 1 y 100, y le pida al usuario adivinarlo. El algoritmo deberá indicar si el número introducido es mayor o menor que el número aleatorio, hasta que el usuario adivine el número correcto.

```cpp
import random

    def Aleatorio():
        numAleatorio = random.randint(1, 100)
        num = int(input("Adivina el número aleatorio: "))
        while num != numAleatorio:             
            if num > numAleatorio:
                print("El número introducido mayor que el número aleatorio")
                num = int(input("Introduce un numero menor: "))
                
            elif num < numAleatorio:
                print("El número introducido menor que el número aleatorio")
                num = int(input("Introduce un numero mayor: "))
                
        print(f"Has adivinado el número correctamente")
        
    Aleatorio()
```

## Ejercicio 18
### Crea un algoritmo que determine si una cadena de texto es un anagrama de otra cadena de texto.

```cpp
    def Anagrama():
        palabra1 = input("Escribe la primera palabra: ").lower()
        palabra2 = input("Escribe la seguna palabra: ").lower()

        if len(palabra1) != len(palabra2):
            print("Las palabras no son anagramas")

        else:

            if sorted(palabra1) == sorted(palabra2):
                print("Las palabras son anagramas")
            else:
                print("Las palabras no son anagramas")


    Anagrama()


```

## Ejercicio 19
### Dada una lista de números enteros, crea un algoritmo que elimine los números duplicados de la lista.

```cpp

    def Duplicados(lista):
        nuevaLista = []
        for num in lista:
            if num not in nuevaLista:
                nuevaLista.append(num)

        print(f"La nueva lista: {nuevaLista}")


    lista = [1, 2, 3, 3, 4, 5, 6, 1, 2]
    Duplicados(lista)

```

## Ejercicio 20
### Crea un algoritmo que determine si un número es capicúa o no.

```cpp
    def Capicua(num):
        numReverso = str(num)[::-1]
        if str(numReverso) == str(num):
            print(f"El número {num} es capicúa")
        else:
            print(f"El número {num} no es capicúa")

    Capicua(111)
    Capicua(220)
    Capicua(331)
    Capicua(221122)

```

## Ejercicio 21
### 1. Crea un programa en Python que acepte una fecha como cadena de caracteres en formato `"dd/mm/aaaa"` y devuelva la fecha en formato `"aaaa-mm-dd"`, con el año primero. El programa debe manejar excepciones en caso de que la cadena no tenga el formato correcto.


```cpp
    def Fecha(fechaStr):
        try:
            fecha = datetime.strptime(fechaStr, '%d/%m/%Y').date()
            print(fecha)
        except:
            print("No has puesto la fecha corretamente")


    fechaStr = input("Pon una fecha en formato 'dd/mm/aaaa': ")
    Fecha(fechaStr)


```

## Ejercicio 22
### 2. Crea un programa que le pregunte al usuario su zona horaria y le muestre la hora actual en esa zona. El programa debe manejar excepciones en caso de que la zona horaria ingresada no sea válida.

```cpp

    from datetime import datetime, timedelta
    from pytz import timezone  
    import pytz 

    def ZonaHoraria(zona):
        try:
            print(datetime.now(pytz.timezone(zona)))
        except: 
            print("No has puesto la zona corretamente")


    zona = input("Pon tu zona horaria(continente/ciudad): ")
    ZonaHoraria(zona)

```

## Ejercicio 23
###  3. Crea un programa en Python que tome una cadena de caracteres y devuelva el número de palabras que contiene. El programa debe utilizar un bucle `while` para recorrer la cadena y contar las palabras.


```cpp

    def CadenaCar(cadena):
        count = 0
        while(count < len(cadena)):
            count += 1
        return count

    cadena = input("Escribe una frase: ").split()
    print(CadenaCar(cadena))

```

## Ejercicio 24
###  Crea un programa que le pida al usuario una hora en formato "hh:mm" y luego calcule y muestre la hora en 24 horas (por ejemplo, "19:30" se convertiría en "19:30"). La hora debe ser validada para asegurarse de que esté en el formato correcto y de que las horas y los minutos sean números enteros.


```cpp

    from datetime import datetime

    def convertir_hora(hora, pmAm):
        hora = (f"{hora}  {pmAm}")
        dt = datetime.strptime(hora, '%I:%M %p')
        dt.strftime('%H:%M')
        print(dt.strftime('%H:%M'))


    hora = input("escribe una hora (hh:mm): ")
    pmAm = input("La hora es pm o am? ").lower()

    convertir_hora(hora, pmAm)

```

## Ejercicio 25
### Crea un programa en Python que acepte una cadena de caracteres y devuelva la cadena invertida (por ejemplo, "hola" se convertiría en "aloh"). El programa debe utilizar un bucle `for` para recorrer la cadena y construir la cadena invertida.


```cpp

    def Convertir(cadena):
        cadenaReversa = ""
        for palabra in cadena:
            cadenaReversa = palabra + cadenaReversa 

        print(cadenaReversa)


    cadena = input("Escribe una cadena: ")
    Convertir(cadena)

```

## Ejercicio 26
###  Crea un programa que le pida al usuario un número entero y luego calcule y muestre la suma de todos los números desde 1 hasta el número ingresado. El programa debe utilizar un bucle `for` para sumar los números.

```cpp

    def SumNum(num):
        sum = 0
        for num in range(1, num+1):
            sum = num + sum
        print(f"La suma de todos los números desde {num} hasta 1 = {sum}")


    num = int(input("Pone un número: "))
    SumNum(num)

```

## Ejercicio 27
###  Crea un programa que le pida al usuario una cadena de caracteres y luego imprima cada carácter en una línea separada. El programa debe utilizar un bucle `for` para recorrer la cadena.

```cpp

    def CadenaCar(cadena):
        for caracter in cadena:
            print(caracter)
            print()


    cadena = input("Escribe una cadena: ")
    CadenaCar(cadena)

```

## Ejercicio 28
### Crea un programa en Python que acepte una lista de cadenas de caracteres y devuelva una nueva lista que contenga solo las cadenas que tienen más de 5 caracteres. El programa debe utilizar un bucle `for` para recorrer la lista y una estructura de control de flujo para filtrar las cadenas.

```cpp

    def Cadena5Car(cadena):
        cadena = cadena.split()
        nuevaCad = []
        for palabra in cadena:
            if len(palabra) > 5:
                nuevaCad.append(palabra)
        print(nuevaCad)


    cadena = input("Escribe una cadena: ")
    Cadena5Car(cadena)

```

## Ejercicio 29
### 

```cpp

```

## Ejercicio 30
### Crea un un programa en Python que tome una lista de cadenas de caracteres y devuelva una nueva lista que contenga solo las cadenas que contienen al menos una vocal. La función debe utilizar un bucle `for` para recorrer la lista y una estructura de control de flujo para filtrar las cadenas.

```cpp

    def Vocal(cadena):
        cadena = cadena.split()
        vocal = ['a', 'o', 'e', 'u', 'i']
        nuevaLista = []
        
        for palabra in cadena:
            for car in vocal:        
                if car in palabra:
                    if palabra not in nuevaLista:
                        nuevaLista.append(palabra)
        print(nuevaLista)


    cadena = input("Escribe una cadena: ")
    Vocal(cadena)

```

## Ejercicio 31
###  Crea un programa en Python que tome una lista de números enteros y devuelva una nueva lista que contenga solo los números que son múltiplos de 3. El programa debe utilizar un bucle `for` para recorrer la lista y una estructura de control de flujo para filtrar los números.

```cpp

    def Multiplos3(numeros):
        nuevaLista = []
        for num in numeros:
            if num % 3 == 0:
                nuevaLista.append(num)
        print(nuevaLista)


    numeros = [1, 2, 5, 6, 7, 8, 10, 30, 23, 33]
    Multiplos3(numeros)

```
