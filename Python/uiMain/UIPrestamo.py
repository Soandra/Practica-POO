from main import *
def prestamo(cliente):
    print("Ingresa el ID de la cuenta que deseas aplicar el prestamo")
    traerCuentas()
    opcion = int(input())
    if opcion >= 0 and opcion < len(cliente.listaCuentas):
        # falta validación de si es corriente o no
        print("Puedes solicitar un prestamo entre 500.000 y 7'000.000 a 24 cuotas\n Ingresa el valor a solicitar")
        valor = int(input())
        if valor < 500000 or valor > 7000000:
            print("Valor fuera del rando permitido")
        else:
            print("Elige el tipo de prestamo (universitario,hobbie,libre)")
            tipoPrestamo = input()

            if tipoPrestamo != "universitario" and tipoPrestamo != "hobbie" and tipoPrestamo != "libre":
                print("El tipo de prestamo ingresado no existe")
            else:
                cliente.solicitarPrestamo(valor, tipoPrestamo, opcion)
                prestamos = cliente.listaCuentas.get(opcion).getprestamos() #organizar

