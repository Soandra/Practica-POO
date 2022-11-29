from cliente import Cliente
from prestamo import Prestamo
from multa import Multa
from cuentaAhorro import CuentaAhorro
from bolsillo import Bolsillo


class UiMenu:
    @classmethod
    def traerCuentas(cls):
        
        for i in Cliente.listaCuentas:
            print(i)

    @classmethod
    def traerCuentasAhorro(cls):
        
        for i in Cliente.listaCuentas:
            if i.getTipoCuenta() == "Ahorro":
                print(i)

    @classmethod
    def traerBolsillos(cls, idCuenta):
        
        cuenta = Cliente.buscarCuenta(cls, idCuenta)
        for bolsillo in cuenta.getMisBolsillos():
            print(bolsillo.__str__())

    @classmethod
    def traerMultas(cls, idCuenta):
       
        cuenta = Cliente.buscarCuenta(cls, idCuenta)
        for multa in cuenta.getMultas():
            if multa.isEstado():
                print(multa)

    @classmethod
    def traerPrestamos(cls, idCuenta):
        
        cuenta = Cliente.buscarCuenta(cls, idCuenta)
        for prestamo in cuenta.getPrestamos():
            if prestamo.isEstado():
                print(prestamo)



def crearObjetos(cliente):
    #(self, valor, cuenta, tipoPrestamo, fechaPrestamo=None)
    #(self, cuenta= None, monto = 50000, fecha = dt.now().strftime("%d/%m/%Y")):
    #(self, titular, saldo, tipoCuenta)
    #(self, metaAhorro,opcion, cuenta)
    c1= CuentaAhorro(cliente, 23484578, "Ahorro")
    cliente.getListaCuentas().append(c1)
    p1 = Prestamo(12311,c1,"hobbie")
    p2 = Prestamo(1211,c1,"universitario")
    m1 = Multa(c1)
    m2 = Multa(c1,1231213)
    c1.getPrestamos().append(p1)
    c1.getPrestamos().append(p2)
    c1.getMultas().append(m1)
    c1.getMultas().append(m2)
    b1 = Bolsillo(1231, 0, c1)
    c1.getMisBolsillos().append(b1)


if __name__ == "__main__":
    
    cliente = Cliente("Jaimito", 20192121)
    crearObjetos(cliente)
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
            from uiPrestamo import UIPrestamo
            UIPrestamo.prestamo(cliente)
        elif opcion == 2:
            from uiPago import UIPago
            UIPago.Pagar(cliente)
        elif opcion == 3:
            from UIBolsillos import UIBolsillos
            UIBolsillos.bolsillo(cliente)
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

