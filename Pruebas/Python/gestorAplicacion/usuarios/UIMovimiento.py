from cliente import Cliente
from uiMenu import UiMenu
from movimiento import Movimiento

class UIMovimiento:

    @classmethod
    def movimiento(cls, cliente):
        print("""Elija el tipo de transaccion
        1. Ver Pagos realizadas
        2. Ver transferencias realizados  
        """)

        tipo = int(input())
        print("Elija una cuenta:")
        UiMenu.traerCuentasAhorro()
        cuenta = int(input())
        if tipo == 1:
            movPago(cuenta)
        else:
            movTransferencia(cuenta)


        def movPago(id):
            movimiento = Movimiento.movimientoPago(Cliente.buscarCuenta(cliente, id))
            if len(movimiento) == 0:
                print("Usted no cuenta con Transferencias actualmente")
                return 
            if len(Cliente.buscarCuenta(cls, id).misBolsillos)==0:
                    print("Usted no cuenta con bolsillos actualmente")
            for i in movimiento:
                print(i)

        def movTransferencia(id):
            movimiento = Movimiento.movimientoTransferencia(Cliente.buscarCuenta(cliente, id))
            if len(movimiento) == 0:
                print("Usted no cuenta con pagos actualmente")
                return
            if (len((Cliente.buscarCuenta(cliente, id).getPrestamos())) == 0) :
                print("Usted no cuenta con prestamos actualmente")
            if (((Cliente.buscarCuenta(cls, id).getMultas())) == 0) :
                print("Usted no tiene multas actualmente")
            for i in movimiento:
                print(i)
                
