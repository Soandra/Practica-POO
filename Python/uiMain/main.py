from UIPrestamo import *
from Python.gestorAplicacion.usuario.cliente import Cliente

def traerCuentas():
    for i in cliente.listaCuentas:
        print(i)

def traerBolsillos(idCuenta):
    cuenta = cliente.buscarCuenta(idCuenta)
    for bolsillo in cuenta.misBolsillos:
        print(bolsillo.__str__())

def traerMultas(idCuenta):
    cuenta = cliente.buscarCuenta(idCuenta)
    for multa in cuenta.getMultas():
        if multa.isEstado():
            print(multa)

def traerPrestamos(idCuenta):
    cuenta = cliente.buscarCuenta(idCuenta)
    for prestamo in cuenta.getPrestamos():
        if prestamo.isEstado():
            print(prestamo)

if __name__ == "__main__":
    cliente = Cliente("Jaimito", 20192121)
    while True:
        print("""
        Bienvenido a PiggyBank\n¿Qué operación desea realizar?'\n
        1. Solicitar Prestamo
        2. Realizar Pagos
        3. Bolsillos
        4. Transferencias
        5. Movimientos
        6. Salir
        """)

        opcion = int(input("Ingrese una opción: "))

        if opcion == 1:
            prestamo(cliente)
        elif opcion == 2:
            pass
        elif opcion == 3:
            pass
        elif opcion == 4:
            pass
        elif opcion == 5:
            pass
        elif opcion == 6:
            print("Vuelva pronto")
            break
        else:
            print("Por favor ingrese una opción valida")





