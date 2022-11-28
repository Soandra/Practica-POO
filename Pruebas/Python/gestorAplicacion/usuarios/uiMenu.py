from cliente import Cliente

class UiMenu:
    @classmethod
    def traerCuentas(cls):
        
        for i in Cliente.listaCuentas:
            print(i)

    @classmethod
    def traerBolsillos(cls, idCuenta):
        
        cuenta = Cliente.buscarCuenta(idCuenta)
        for bolsillo in cuenta.misBolsillos:
            print(bolsillo.__str__())

    @classmethod
    def traerMultas(cls, idCuenta):
       
        cuenta = Cliente.buscarCuenta(idCuenta)
        for multa in cuenta.getMultas():
            if multa.isEstado():
                print(multa)

    @classmethod
    def traerPrestamos(cls, idCuenta):
        
        cuenta = Cliente.buscarCuenta(idCuenta)
        for prestamo in cuenta.getPrestamos():
            if prestamo.isEstado():
                print(prestamo)


if __name__ == "__main__":
    
    cliente = Cliente("Jaimito", 20192121)
    while True:
        print("""Bienvenido a PiggyBank\n¿Qué operación desea realizar?'\n
        1. Solicitar Prestamo
        2. Realizar Pagos
        3. Bolsillos
        4. Transferencias
        5. Movimientos
        6. Salir
        """)

        opcion = int(input("Ingrese una opción: "))

        if opcion == 1:
            from Python.uiMain.UIPrestamo import UIPrestamo
            UIPrestamo.prestamo(cliente)
        elif opcion == 2:
            from Python.uiMain.UIPago import UIPago
            UIPago.pago(cliente)
        elif opcion == 3:
            #UIBolsillos.bolsillo(cliente)
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
