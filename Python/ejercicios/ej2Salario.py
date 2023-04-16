

def salarioBase():
    op = "si"
    while op == "si":
        try:
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
        except:
            print("No has introducido un numero")

        choose = input("Si quieres continuar teclea 'si', sino pulse cualquier otra tecla: ")
        op = choose.lower()
        
    print("¡Hasta luego!")

#salarioBase()