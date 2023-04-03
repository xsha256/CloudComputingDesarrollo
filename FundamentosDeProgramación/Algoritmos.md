> > # **Algoritmos**


+ ## Ejercicio 1:

Calcular la letra del DNI Español

+ **Paso 1:** Definir el problema

¿Cómo calcular la letra del DNI?

Para calcular la letra del DNI hay que dividir los 8 dígitos del DNI entre 23 y asignar a cada uno de los posibles 33 restos una letra del siguiente conjunto:

| **Numero** | **Letra** |
| ---------- | --------- |
| 0          | T         |
| 1          | R         |
| 2          | W         |
| 3          | A         |
| 4          | G         |
| 5          | M         |
| 6          | Y         |
| 7          | F         |
| 8          | P         |
| 9          | D         |
| 10         | X         |
| 11         | B         |
| 12         | N         |
| 13         | J         |
| 14         | Z         |
| 15         | S         |
| 16         | Q         |
| 17         | V         |
| 19         | H         |
| 20         | L         |
| 21         | C         |
| 22         | K         |
| 23         | E         |

+ **Paso 2:** Poner la entrada, el proceso y la salida

**Entrada**:

`DNI`, `letrasDNI`, `resto`, `letra`

**Proceso:**

Escribir los 8 dígitos del `DNI`

dividimos los digitos del `DNI` entre 23 y el resto lo asignamos a `resto`

buscamos la posición de `resto` en `letrasDNI` y asignamos la letra que esta en la posición a `letra`

**Salida**:

Escribir(`letra`)

+ **Paso 3**: Escribe el pseudocódigo

```cpp
Algoritmo LetraDNI
  # Entrada
  DNI <- leer()
  letraDNI <- "TRWAGMYFPDXBNJZSQVHLCKE"
  resto = 0
  letra = ""

  # Proceso
  Si DNI es válido entonces
    resto <- DNI mod 23
    letra <- letraDNI[resto]
  Si no 
    escribir("DNI no Válido")
  Fin Si

  #Salida
    Escribir(letra)

Fin algoritmo
```

+ ## Ejercicio 2:

Calcular el salario de un empleado

+ **Paso 1:** Definir el problema

¿Cómo calcular el salario de un empleado?

Sumar el pago por horas trabajadas al sueldo base y restar los descuentos por seguridad social y las retenciones de impuestos para obtener el salario neto del empleado

+ **Paso 2:** Poner la entrada, el proceso y la salida

**Entrada**:

`salarioBase` , `horasTrabajadas` , `percentajeSSocial`, `percentajeImpuestos` , `sueldoBruto`, `descuentoSS` , `descuentoIm`  , `sueldoNeto`

**Proceso:**

Multiplicamos el  `salarioBase` por `horaTrabajadas` y lo asignamos a `sueldoBruto`

multiplicamos el `sueldoBase` por `percentajeSSocial` y lo asignamos a `descuentoSS`

multiplicamos el `sueldoBase` por `percentajeImpuestos` y lo asignamos a `descuentoIm`

restamos del `sueldoBruto` `descuentoSS` y `descuentoIM` y lo asignamos a `sueldoNeto`

**Salida**:

escribir(`sueldoNeto`)

+ **Paso 3**: Escribe el pseudocódigo

```cpp
Algoritmo salario
  # Entrada
  salarioBase  <- leer()
  horasTrabajadas <- leer()
  percentajeSSocial <- leer()
  percentajeImpuestos <- leer()
  sueldoBruto = 0
  descuentoSS = 0
  descuentoIm = 0
  sueldoNeto = 0

  # Proceso
    sueldoBruto igual a salarioBase multiplicado por horasTrabajadas
    descuentoSS igual a sueldoBruto por (percentajeSSocial entre 100)
    descuentoIm igual a sueldoBruto por (percentajeImpuestos ente 100)
    sueldoNeto igual a sueldoBruto - descuentoSS - descuentoIm

  #Salida
    Escribir(sueldoNeto)
Fin algoritmo
```

+ ## Ejercicio 3:

Determinar la ruta para llegar a una ciudad por avión.

+ **Paso 1:** Definir el problema

Para llegar a una ciudad por avión:

1. Elegir el destino
2. Elegir la fecha
3. Comprar Vuelo
4. Ir al aeropuerto
5. Hacer check-in
6. Embarcar
   + **Paso 2:** Poner la entrada, el proceso y la salida

**Entrada:**

`salidaAeropuerto`  `destino` `fecha` `vuelo` `llegadaAeropuerto` `checkIn` `embarcar`

**proceso**:

+ Buscar si hay vuelos desde tu aeropuerto `salidaAeropuerto` al aeropuerto del `destino` .
+ Buscar si hay vuelo disponible para la `fecha`  elegida
   + Si no hay vuelos al aeropuerto del destino:

cambia el `destino` o el aeropuerto de salida.

+ Si no hay vuelo en la `fecha` elegida:

cambia la `fecha` de salida

+ Compra el `vuelo`
+ Ir al aeropuerto en la fecha del vuelo `llegadaAeropuerto`
+ Llegar 2 horas antes para hacer el `checkIn`
+ `embarcar` al avión

**Salida**:

Escribir la ruta (`salidaAeropuerto`, `destino`)

+ **Paso 3**: Escribe el pseudocódigo

```cpp
Algoritmo rutaAvionAlgoritmo rutaAvion

  # Entrada
      destino <- leer()
      fecha <- leer()
      vuelo <- leer()
      llegadaAeropuerto <- leer()
      checkIn <- leer()
      embarcar <- leer()
      llegada = ""
      
  # Proceso 
Repetir: 
      Si destino es válido: 

        Repetir: 
          si fecha es válida:
              compra vuelo

              si llegadaAeropuerto >= 2 horas:
                  hacer checkIn
                  escribir("Has llegado con tiempo")
              sino:
                  hacer checkIn
                  escribir("No has llegado con tiempo")
        
              Si hora de terminar checkIn >= la ultima llamada:
                  puedes embarcar
                  haEmbarcado = True
              sino:
                  el avión sale en 15 minutos las puertas están cerradas
                  haEmbarcado = False

              Si el avión haLlegadoSinProblemas entonces 
                  haLlegadoSinProblemas = True
              Sino:
                  haLlegadoSinProblemas = False

              Si haEmbarcado y el avión haLlegadoSinProblemas entonces:
                  llegada = verdadero 
              sino:
                  llegada = falso

          sino:
              opción <- ¿Queres elegir otra fecha si/no?
              si opción = "no" entonces
                  Break
        hasta que opción = "no"

      sino:
         opción <- ¿Queres elegir otro destino o aeropuerto de salida si/no?
          
hasta que opción = "no"
          
  # Salida
      Si llegada = verdadero:
        escribir("La ruta: ", salida, destino)
      Sino:
        escribir("No ha salido, no se puede calcular la ruta")

Fin algoritmo
```

+ ## Ejercicio 4:

Calcula el área y perímetro de un círculo dado su radio

+ **Paso 1:** Definir el problema

¿Cómo calcular el área y perímetro de un círculo dado su radio?

El área y el perímetro de un círculo se pueden calcular a partir de su radio utilizando las siguientes fórmulas:

Área = π × radio²
Perímetro = 2 × π × radio

Donde π (pi) es una constante matemática aproximadamente igual a 3.14159.

+ **Paso 2:** Poner la entrada, el proceso y la salida

**Entrada**:

`radio area` `perímetro pi = 3.14159` `resultado = 0`

**Proceso:**
`radio` <- lee()

validar si el `radio` es un numero

Si no es numero  da error

asignamos al `area` el resultado de `pi` * `radio` al cuadrado

asignamos al `perímetro` el resultado de 2 * `pi` * `radio`

asignamos al `resultado` el valor del `area` y `perímetro`

**Salida**:

Escribir resultado

+ **Paso 3**: Escribe el pseudocódigo

```cpp
Algoritmo rutaAvionCalcula el area y perímetro
  # Entrada
    radio <- leer()
    pi <- 3.14159
    area <- 0
    perímetro <- 0
    resultado <- 0

  # Proceso
      Si radio es numero:
        area = pi * radio ^ 2
        perímetro = 2 * pi * radio
        resultado = ("el area es: ", area, "el perímetro es: ". perímetro)
      Sino 
        radio no es un numero

  #Salida
    escrib

Fin algoritmo
```

+ ## Ejercicio 5:

Dada una lista de números enteros, determina cuál es el mayor y cuál es el menor.

+ **Paso 1:** Definir el problema

a partir de una lista de números tenemos que determinar cuando es  mayor y cuando es menor

+ **Paso 2:** Poner la entrada, el proceso y la salida

**Entrada**:

`listaNumeros` , `mayor` , `menor`

**Proceso:**

- Establecemos dos variables para el número mayor y el número menor
- Recorremos la lista de números enteros utilizando un bucle, empezando desde el segundo elemento hasta el último
- Vamos comparando el número actual con el número mayor y el número menor, actualizando dichas variables.

**Salida**:

Escribir(`mayor`)

Escribir(`menor`)

+ **Paso 3**: Escribe el pseudocódigo

```cpp
Algoritmo mayorMenor

  # Entrada
   lista_numeros <- leer()
   mayor <- lista_numeros[0]
   menor <- lista_numeros[0]

  # Proceso
    Para cada numero en lista_numeros hacer:
       Si numero > mayor entonces:
          mayor = numero
       Si numero < menor entonces:
          menor = numero

  #Salida
    Escribir("El número mayor es: ", mayor)
    Escribir("El número menor es: ", menor)

Fin algoritmo
```

+ ## Ejercicio 6:

Crea un algoritmo que convierta grados Celsius a Fahrenheit

+ **Paso 1:** Definir el problema

Para convertir grados Celsius a Fahrenheit, se utiliza la siguiente fórmula matemática:

$$
°F = (°C * 1.8) + 32 
$$

+ **Paso 2:** Poner la entrada, el proceso y la salida

**Entrada**:

`C, F`

**Proceso:**

`F` ← multiplicamos C por 1.8 más 32

**Salida**:

Escribir(F)

+ **Paso 3**: Escribe el pseudocódigo

```cpp
Algoritmo conviertaGrados 
  # Entrada
    C <- leer()
    F <- 0

  # Proceso
    F = C * 1.8 + 32

  #Salida
    Escribir(F)

Fin algoritmo
```

+ ## Ejercicio 7:

Dado un número entero, crea un algoritmo que determine si es par o impar.

+ **Paso 1:** Definir el problema

Saber si un numero es par o impar.

- Si el número es divisible entre 2, entonces es par.
- Si el número no es divisible entre 2, entonces es impar.
   + **Paso 2:** Poner la entrada, el proceso y la salida

**Entrada**:

`numero` `resultado`

**Proceso:**

Dividimos el `numero` entre 2:

Si el resto de la división = 0:

`resultado` ← Es par

Sino:

`resultado` ← es impar

**Salida**:

Escribe(`resultado`)

+ **Paso 3**: Escribe el pseudocódigo

```cpp
Algoritmo parOImpar
  # Entrada
    numero <- leer()
    resultado <- 0

  # Proceso
    Si numero%2 = 0: 
      devuelve resultado = "Es par"
    Si no:
      devuelve resultado = "Es impar"
  

  #Salida
    escribe(resultado)

Fin algoritmo
```

+ ## Ejercicio 8:

Crea un algoritmo que determine si un año es bisiesto o no.

+ **Paso 1:** Definir el problema

Un año es bisiesto si es divisible entre 4, excepto en el caso de los años que son divisibles entre 100. En este último caso, solo son bisiestos si también son divisibles entre 400.

+ **Paso 2:** Poner la entrada, el proceso y la salida

**Entrada**:

`año` , `resultado`

**Proceso:**

dividimos el año entre 4

Si es divisible entre 4 y no es divisible entre 100 es bisiesto

Si es divisible entre 4 y entre 100 en este caso tiene que ser divisible entre 400 para ser bisiesto

**Salida**:

escribir(resultado)

+ **Paso 3**: Escribe el pseudocódigo

```cpp
Algoritmo añoBisiesto
  # Entrada
     año <- leer()
    resultado <- ""

  # Proceso
    Si año % 4 = 0 y año % 100 != 0 entonces
      resultado = "El año ", año " bisiesto"
    Si no Si año % 4 = 0 y año % 100 = 0 y año % 400 = 0 entonces
      resultado = "El año ", año " bisiesto"
    Si no:
      resultado = "El año ", año " no bisiesto"
    FinSi

  #Salida
    Escribir(resultado)

Fin algoritmo
```

+ ## Ejercicio 9:

Crea un algoritmo que determine si una cadena de texto es un palíndromo o no.

+ **Paso 1:** Definir el problema

Para determinar si una cadena de texto es un palíndromo o no, es necesario verificar si la cadena es igual al revés.

+ **Paso 2:** Poner la entrada, el proceso y la salida

**Entrada**:

`cadenaOriginal` , `cadenaReversa` , `Resultado`

**Proceso:**

Asignamos la `cadenaOriginal` invertida a la `cadenaReversa`

Si la `cadenaReversa` igual a  `cadenaOriginal` entonces:

`Resultado` ← la cadena es un palíndromo

Si no:

`Resultado` ← la cadena no es un palíndromo

**Salida**:

escribir(`resultado`)

+ **Paso 3**: Escribe el pseudocódigo

```cpp
Algoritmo Palindromo
   # Entrada
   cadena <- leer()
   #Proceso
   #cadena <- Convertir a minúsculas y eliminar espacios en blanco
   reversa <- depuracionCadena(cadena)
   Si cadena es igual a reversa entonces
     resultado <- "La cadena es un palíndromo"
   Sino
     resultado <- "La cadena no es un palíndromo"
   Fin Si
   # Salida
   escribir resultado
Fin Algoritmo

SubAlgoritmo depuracionCadena (cadena)
    #quita los espacios en blanco, otros caracteres y convierte todo a minusculas
    i<-0
    Mientras cadena[i] sea diferente de findecadena Haga
        caracter<-""
        Si  el ASCII de cadena[i]  mayor que 64 y ASCII de cadena[i] menor que 91 Entonces
            caracter<-cadena[i] en minusculas
        Fin Si
        Si  el ASCII de cadena[i]  mayor que 96 y ASCII de cadena[i] menor que 123 Entonces
            caracter<-cadena[i]
        End Si
        temporal <- temporal + caracter
        Si caracter es diferente "" Entonces
            i<-i+1
        Fin Si
    Fin Mientras
    L<-i
    reversa<-""
    Para N = 0 Hasta L-1 Con Paso 1 Haga
        reversa    <-reversa+ temporal[i-1]
        i<-i-1
    Fin Para
    devuelva reversa
Fin SubAlgoritmo
```

+ ## Ejercicio 10:

Dada una lista de nombres, crea un algoritmo que ordene la lista alfabéticamente

+ **Paso 1:** Definir el problema

El problema consiste en ordenar alfabéticamente una lista de nombres, es decir, crear un algoritmo que organice los elementos de la lista en orden ascendente o descendente según su posición en el alfabeto.

+ **Paso 2:** Poner la entrada, el proceso y la salida

**Entrada**:

`nombresDesordenados` , `nombresOrdenados, nombrePrimero`

**Proceso:**

- Recorremos la lista de `nombresDesordenados` utilizando un bucle
- Encontramos el nombre que esté primero en orden alfabético en la lista desordenada.
- Añadimos el nombre a la lista de`nombresOrdenados` y lo eliminamos de la lista de `nombresDesordenados`

**Salida**:

Escribir(`nombresOrdenados`)

+ **Paso 3**: Escribe el pseudocódigo

```cpp
Algoritmo listaOrdenadaAlfabéticamente
#Entrada
    nombresDesordenados <- leer()
    nombresOrdenados <- " "
    nombrePrimero <- " "

#Proceso
    Mientras nombresDesordenados no esté vacía repetir:
       nombrePrimero = lista_nombres[0]
       Para cada nombre en nombrePrimero hacer: 
           Si nombre < nombrePrimero entonces:
              nombrePrimero = nombre
       Agregar nombrePrimero a nombresOrdenados
       Eliminar nombrePrimero de nombresDesordenados

  #Salida
    Escribir(nombresOrdenados)

Fin algoritmo
```

+ ## Ejercicio 11:

Crea un algoritmo que calcule el factorial de un número entero.

+ **Paso 1:** Definir el problema

El factorial de un número se calcula multiplicando ese número por todos los números enteros positivos menores que él. Por ejemplo, el factorial de 5 se calcula así: 
          $$
          5! = 5 x 4 x 3 x 2 x 1 = 120 
          $$

+ **Paso 2:** Poner la entrada, el proceso y la salida

**Entrada**:

`numero` , `factorial` , `resultado`

**Proceso:**

multiplicamos el factorial actual por cada número entero positivo desde 1 hasta el número deseado.

**Salida**:

escribir(resultado)

+ **Paso 3**: Escribe el pseudocódigo

```cpp
Algoritmo factorial
  # Entrada
  numero <- leer()
  factorial <- 1
  resultado <- 0

  # Proceso
    Para i desde 1 hasta numero: 
        factorial = factorial * i
  
    Fin Para
  #Salida
    Escribir(factorial)

Fin algoritmo
```

+ ## Ejercicio 12:

Dado un número entero, crea un algoritmo que determine si es primo o no

+ **Paso 1:** Definir el problema

    determinar si un numero es primo o no. El número primo es un número entero mayor que 1 que solo es divisible exactamente por 1 y por sí mismo. 

    Utilizamos la raíz cuadrada porque si un número no es primo, necesariamente tiene un divisor que es menor o igual que su raíz cuadrada. Si no hay ningún divisor en el rango de 2 a la raíz cuadrada del número, no habrá ningún divisor en el rango de la raíz cuadrada del número a su valor máximo.

+ **Paso 2:** Poner la entrada, el proceso y la salida

**Entrada**:

`numero` , `esPrimo`

**Proceso:**

Hay que comprobar si el numero es menor que 2, si lo es no es primo

utilizamos un bucle para iterar desde 2 hasta la raíz cuadrada del numero ingresado si es divisible por algún numero en este rango, si lo es no es primo

**Salida**:

Escribir si es primo o no

+ **Paso 3**: Escribe el pseudocódigo

```cpp
Algoritmo numeroPrimo
  # Entrada
    numero <- leer()
    esPrimo <- True

  # Proceso
    Si 2 > numero entonces:
      esPrimo = False
    Fin Si
    Para i desde 2 hasta raizCuadrada(numero) hacer:
        Si % i == 0 entonces
            esPrimo = False
            salir del bucle
        Fin si
    Fin para

  #Salida
  Si esPrimo entonces:
      Escribir(numero, "Es primo")
  Si no 
      Escribir(numero, "No es primo")

Fin algoritmo
```

+ ## Ejercicio 13:

Crea un algoritmo que calcule el área y volumen de un cubo dado su lado.

+ **Paso 1:** Definir el problema

Calcular el área y volumen de un cubo dado su lado.

El área de un cubo se puede calcular utilizando la fórmula:

$$
area = 6 x (lado)^2
$$

El volumen de un cubo se puede calcular utilizando la fórmula:

$$
Volumen = (lado)^3
$$

+ **Paso 2:** Poner la entrada, el proceso y la salida

**Entrada**:

`lado` , `area` , `volumen`

**Proceso:**

para calcular el `area` del cubo, tenemos que multiplicar el `lado` por el numero de caras que tiene el cubo, 6,  elevado al cuadrado 

Para calcular el `volumen` del cubo, tenemos que elevar al cubo la medida del `lado`

**Salida**:

escribir(`area`, `volumen`)

+ **Paso 3**: Escribe el pseudocódigo

```cpp
Algoritmo areaVolumenCubo
  # Entrada
    lado <- leer()
    area <- 0
    volumen <- 0

  # Proceso
    area = lado^2 * 6
    Volumen = lado^3

  #Salida
    Escribir(area)
    Escribir(volumen)

Fin algoritmo
```

+ ## Ejercicio 14:

Dada una lista de números enteros, crea un algoritmo que calcule la suma de todos los números pares de la lista.

+ **Paso 1:** Definir el problema

Hay que sumar los números pares de una lista. Un número es par si es divisible exactamente por 2, lo que significa que su resto es 0 al dividirlo por 2.

+ **Paso 2:** Poner la entrada, el proceso y la salida

**Entrada**:

`listaNumeros` , `sumaPares`

**Proceso:**

- Recorremos la lista de `listaNumeros` utilizando un bucle
- vamos verificando si el número actual es par utilizando el operador módulo
- Si el número actual es par, lo sumamos a la variable `sumaPares`

**Salida**:

Escribir(`sumaPares`)

+ **Paso 3**: Escribe el pseudocódigo

```cpp
Algoritmo sumaPares
  # Entrada
     listaNumeros <- leer()
     sumaPares <- 0

  # Proceso
     Para cada numero en listaNumeros:
       Si numero % 2 == 0 entonces:
          sumaPares += numero

  #Salida
    Escribir(sumaPares)
            
Fin algoritmo
```

+ ## Ejercicio 15:

Crea un algoritmo que determine si un número es positivo, negativo o cero.

+ **Paso 1:** Definir el problema
   + Hay que determinar si un numero es positivo, negativo o cero.
   + **Paso 2:** Poner la entrada, el proceso y la salida

**Entrada**:

`numero`

**Proceso:**

- Si el número es mayor que cero, el número es positivo
- Si el número es menor que cero, el número es negativo
- Si el número es igual a cero, el número es cero

**Salida**:

Escribir(n`umero)`

+ **Paso 3**: Escribe el pseudocódigo

```cpp
Algoritmo NumeroPositivoNegativo
  # Entrada
     numero <- leer()

  # Proceso
    Si numero > 0 entonces:
        escribir("El número es positivo")
    Si numero < 0 entonces:
        escribir("El número es negativo")
    Si numero == 0 entonces:
        escribir("El número es cero")
  #Salida

Fin algoritmo
```

+ ## Ejercicio 16:

Dada una lista de números enteros, crea un algoritmo que calcule la media de la lista.

+ **Paso 1:** Definir el problema
   Hay que calcular la media de una lista de números.
  la media se calcula de la siguiente forma:

  $$
  media = suma de todos los números en la lista / cantidad de números en la lista 
  $$

+ **Paso 2:** Poner la entrada, el proceso y la salida

**Entrada**:

`listaNumeros`  , `cantidadNumeros, sumaNumeros, media`

**Proceso:**

- Recorremos la lista de números enteros utilizando un bucle.
- En cada iteración del bucle, sumamos el número actual a la variable de la `sumaNumeros` y aumentar en uno `cantidadNumeros`en la lista.
- Al finalizar el bucle, dividimos `sumaNumeros` entre `cantidadNumeros`en la lista para obtener la media.

**Salida**:

Escribir(media)

+ **Paso 3**: Escribe el pseudocódigo

```cpp
Algoritmo media

  # Entrada
     listaNumeros <- leer()
     cantidadNumeros <- 0
     sumaNumeros <- 0
     media <- 0
  
  # Proceso
     Para cada numero en listaNumeros hacer:
       sumaNumeros += numero
       cantidadNumeros += 1
     media = sumaNumeros / cantidadNumeros

  #Salida
    Escribir(media)

Fin algoritmo
```

+ ## Ejercicio 17:

Crea un algoritmo que genere un número aleatorio entre 1 y 100, y le pida al usuario adivinarlo. El algoritmo deberá indicar si el número introducido es mayor o menor que el número aleatorio, hasta que el usuario adivine el número correcto.

+ **Paso 1:** Definir el problema

Hay que generar un número aleatorio entre 1 y 100, y pedir al usuario que adivine ese número. El algoritmo debe indicar si el número introducido por el usuario es mayor o menor que el número aleatorio generado, y seguir pidiendo al usuario que introduzca un nuevo número hasta que adivine el número correcto.

+ **Paso 2:** Poner la entrada, el proceso y la salida

**Entrada**:

`numeroAleatorio` , `numeroUsuario`

**Proceso:**

- pedimos un numero al usuario
- Recorremos la lista de números enteros utilizando un bucle.
- Si el número ingresado por el usuario es mayor que el número aleatorio, imprimimos El número ingresado es mayor que el número a adivinar
- Si el número ingresado por el usuario es menor que el número aleatorio, imprimimos El número ingresado es menor que el número a adivinar
- Si el número ingresado por el usuario es igual al número aleatorio, imprimimos ¡Felicitaciones! Adivinaste el número.

**Salida**:
  Escribir("¡Felicitaciones! Adivinaste el número.")

+ **Paso 3**: Escribe el pseudocódigo

```cpp
Algoritmo AdivinarElNumero
  # Entrada
     numeroAleatorio <- leer()
     numeroUsuario <- leer()

  # Proceso
      numeroAleatorio <- generarNumeroAleatorio(1, 100)
      numeroUsuario <- 0
      Mientras numeroUsuario != numeroAleatorio:
        numeroUsuario <- leer()     
        Si numeroUsuario > numeroAleatorio entonces:
            Escribir("El número ingresado es mayor que el número a adivinar")
        Si numeroUsuario < numeroAleatorio entonces:
            Escribir("El número ingresado es menor que el número a adivinar")
         Si numeroUsuario == numeroAleatorio entonces:
            Escribir("¡Felicitaciones! Adivinaste el número." y salir del bucle)
        Fin Mientras

  #Salida
      Escribir("¡Felicitaciones! Adivinaste el número.")

Fin algoritmo
```

+ ## Ejercicio 18:

Crea un algoritmo que determine si una cadena de texto es un anagrama de otra cadena de texto.

+ **Paso 1:** Definir el problema

Hay que crear un algoritmo que permita comprobar si dos palabras tienen las mismas letras pero en diferente orden. Si las dos palabras tienen las mismas letras y la misma cantidad de ellas, pero ordenadas de forma distinta, entonces se consideran "anagramas".

+ **Paso 2:** Poner la entrada, el proceso y la salida

**Entrada**:

`texto1` , `texto2`

**Proceso:**

- Pedimos al usuario que ingrese dos cadenas de texto
- Si la longitud de  `texto1` es diferente a la longitud de `texto2`, imprimimos: Las cadenas no son anagramas.
- Si las longitudes son iguales, continuar con el siguiente paso.
- Convertimos `texto1` y `texto2` a minúsculas (o mayúsculas) para eliminar diferencias en la capitalización de las letras.
- Convertimos `texto1` y `texto2` en listas de caracteres.
- Ordenar la lista de caracteres de `texto1` y`texto2` alfabéticamente.

**Salida**:

- Si las listas de caracteres de `texto1` y`texto2` son iguales, imprimimmos: Las cadenas son anagramas.
- Si las listas no son iguales, imprimimos:  Las cadenas no son anagramas
   + **Paso 3**: Escribe el pseudocódigo

```cpp
Algoritmo Anagramas
  # Entrada
     texto1 <- leer()
     texto2 <- leer()

  # Proceso
      si longi(texto1) != longi(texto2) entonces:
          escribir("Las cadenas no son anagramas.")
      Si no:
          text1 <- lista(texto1.minúscula())
          text2 <- lista(texto2.minúscula())

          texto1.ordenar()
          texto2.ordenar()
   

  #Salida
      si texto1 == texto2 entonces:
          escribir("Las cadenas son anagramas.")
      Si no:
          escribir("Las cadenas no son anagramas.")
            
Fin algoritmo
```

+ ## Ejercicio 19:

Dada una lista de números enteros, crea un algoritmo que elimine los números duplicados de la lista.

+ **Paso 1:** Definir el problema

Hay que escribir un algoritmo que reciba una lista de números enteros y elimine cualquier número que aparezca más de una vez en la lista, manteniendo solo una ocurrencia de cada número.

+ **Paso 2:** Poner la entrada, el proceso y la salida

**Entrada**:

`listaNumeros` , `listaSinDuplicados`

**Proceso:**

- Recorremos `listaNumeros` utilizando un bucle, para cada número en listaNumeros, hacer lo siguiente:
- Si el número no está en `listaSinDuplicados`, lo añadimos a la lista.

**Salida**:

Escribir(`listaSinDuplicados`)

+ **Paso 3**: Escribe el pseudocódigo

```cpp
Algoritmo eliminarNumerosDuplicados
  # Entrada
     listaNumeros <- leer()
     listaSinDuplicados <- []

  # Proceso
    Para cada numero en listaNumeros hacer:
      Si numero no esta en listaSinDuplicados entonces:
        listaSinDuplicados.añadir(numero)

  #Salida
    Escribir(numero)

Fin algoritmo
```

+ ## Ejercicio 20:

Crea un algoritmo que determine si un número es capicúa o no.

+ **Paso 1:** Definir el problema

El algoritmo debe comprobar si un número es capicúa o no. Un número es capicúa si se lee igual de izquierda a derecha que de derecha a izquierda.

+ **Paso 2:** Poner la entrada, el proceso y la salida

**Entrada**:

`numero` , `cadena` , `cadenaInvertida` ,

**Proceso:**

- Pedimos al usuario que ingrese un número entero y guardarlo en una variable llamada `numero`
- Convertimos el número en una cadena de caracteres y guardarla en una variable llamada `cadena`
- Invertimos la cadena y guardarla en una variable llamada `cadenaInvertida`

**Salida**:

- Si `cadena` es igual a `cadenaInvertida`, imprimimos El número es capicúa.
- Si `cadena` no es igual a `cadenaInvertida`, imprimimos El número no es capicúa.
   + **Paso 3**: Escribe el pseudocódigo

```cpp
Algoritmo Capicua
  # Entrada
     numero <- leer()
     cadena <- cadena(numero)
     cadenainvertida <- ""

  # Proceso
       Para i en rango(longi(cadena)) hacer:
          cadenainvertida <- cadena[i] + cadenainvertida

  #Salida
      Si cadena == cadenainvertida entonces: 
          Esribir("El número es capicúa")
      Si no:
          Esribir("El número nes capicúa")
Fin algoritmo
```

