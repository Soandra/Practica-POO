from uiMenu import UiMenu
from cliente import Cliente

class UITranferencia:

    @classmethod
    def trasnfer(cls, cliente):
        UiMenu.traerCuentas()
        print("Ingrese el numero de cuenta de origen")
        cOrigen = int(input())
        print("Ingrese el numero de cuenta destino")
        cDestino = int(input())

        if cOrigen >= 0 and cOrigen < len(Cliente.listaCuentas) and cDestino < len(Cliente.listaCuentas):
            print("Ingrese valor a transferir")
            valor = int(input())
            print(cliente.hacerTransferencia(cOrigen, cDestino, valor))