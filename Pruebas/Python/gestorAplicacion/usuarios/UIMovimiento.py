from cliente import Cliente
from uiMenu import UiMenu

class UIMovimiento:

    @classmethod
    def movimiento(cls, cliente):
        print("""Elija el tipo de transaccion
        1. Ver todas tus transacciones disponibles
        2. Ver transferencias realizadas
        3. Ver Pagos realizados  
        """)

        tipo = int(input())
        if tipo == 1:
            print("Elija una cuenta:")
            UiMenu.traerCuentasAhorro()
            id = int(input())
            if id >= 0 and id <= len(Cliente.listaCuentas):
                print("Estas son tus transacciones disponibles")
                UiMenu.traerPrestamos(id)
                UiMenu.traerMultas(id)
                UiMenu.traerBolsillos(id)

        elif tipo == 2:
            print("Transferencias Realizadas:") #No está definida en cliente
            print(cliente.movimientoTransferencia())
        elif tipo == 3:
            print("Pagos realizados: ")
            print(cliente.movimientoPago) #No está definida en cliente