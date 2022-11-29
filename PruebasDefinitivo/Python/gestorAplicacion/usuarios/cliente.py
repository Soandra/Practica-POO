import random
from gestorAplicacion.usuarios.cuentaAhorro import CuentaAhorro
from gestorAplicacion.usuarios.cuentaCorriente import CuentaCorriente
from gestorAplicacion.transacciones.transferencia import Transferencia
from gestorAplicacion.transacciones.prestamo import Prestamo
from gestorAplicacion.transacciones.multa import Multa
from gestorAplicacion.transacciones.pago import Pago
from gestorAplicacion.transacciones.bolsillo import Bolsillo
from gestorAplicacion.transacciones.movimiento import Movimiento

class Cliente:
    listaCuentas = []

    def __init__(self, nombre, cedula):
        self.nombre = nombre
        self.cuenta = None
        self.cedula = cedula
        self.trasnferencia = None

        var_random = random.randint(2,3)
        for i in range(0, var_random):
            Cliente.listaCuentas.append(CuentaAhorro(self, random.randint(100000, 600000), "Ahorro"))
            Cliente.listaCuentas.append(CuentaCorriente(self, random.randint(100000, 600000), "Corriente"))


    def buscarCuenta(self, idCuenta):
        for cuenta in Cliente.listaCuentas:
            if idCuenta == cuenta.id:
                return cuenta
        return None

    @classmethod
    def listarCuentas(cls):
        for cuenta in Cliente.listaCuentas:
            return cuenta
        return None


    @classmethod
    def buscarBolsillo(cls, idCuenta, idBolsillo):
        cuenta = Cliente.buscarCuenta(cls, idCuenta)
        return cuenta.getMisBolsillos()[idBolsillo]


    @classmethod
    def buscarMulta(cls,idCuenta, idMulta):
        cuenta = Cliente.buscarCuenta(cls, idCuenta)
        return cuenta.getMultas()[idMulta]


    @classmethod
    def buscarPrestamo(cls, idCuenta, idPrestamo):
        cuenta = Cliente.buscarCuenta(cls, idCuenta)
        return cuenta.getPrestamos()[idPrestamo]

    
    def hacerTransferencia(self, idCuentaOrigen, idCuentaDestino, valor):
        cuentaOrigen = Cliente.buscarCuenta(self, idCuentaOrigen)
        cuentaDestino = Cliente.buscarCuenta(self, idCuentaDestino)
        
        trasnfer = Transferencia(cuentaOrigen, cuentaDestino, valor)
        return trasnfer.enviarDinero()


    def solicitarPrestamo(self, valor, tipoPrestamo, idCuenta):
        if (valor >= Prestamo.TOPEMIN and valor <= Prestamo.TOPEMAX):
            (Cliente.buscarCuenta(self,idCuenta)).getPrestamos().append(Prestamo(valor, Cliente.buscarCuenta(self,idCuenta),tipoPrestamo))


    def generarAhorro(self, valor, categoria, idCuenta):
        Cliente.buscarCuenta(self, idCuenta).getMisBolsillos().append(Bolsillo.crearBolsillo(valor, categoria, Cliente.buscarCuenta(self, idCuenta)))


    def cargarAhorro(self,idCuenta, idBolsillo, valor= None):
        if valor == None:
            return Cliente.buscarBolsillo(idCuenta, idBolsillo).cargarBolsillo() #Recarga total
        else:
            return Cliente.buscarBolsillo(idCuenta, idBolsillo).cargarBolsillo(valor) #Recarga parcial


    def descargarAhorro(self, idCuenta, idBolsillo, valor=None):
        if valor == None:
            return Cliente.buscarBolsillo(idCuenta, idBolsillo).descargarBolsillo() #Recarga total
        else:
            return Cliente.buscarBolsillo(idCuenta, idBolsillo).descargarBolsillo(valor) #Recarga parcial


    def hacerPagoPrestamo(self, idCuenta, idPrestamo, cuota=None):   
        if cuota == None:
            pago = Pago((Cliente.buscarPrestamo(idCuenta, idPrestamo).getValorCuota()), Cliente.buscarCuenta(self, idCuenta),
                        Cliente.buscarPrestamo(idCuenta, idPrestamo), "Prestamo")
            return pago.RealizarPagoPrestamo()
        else:
            pago = Pago((Cliente.buscarPrestamo(idCuenta, idPrestamo).getValorCuota() * cuota), Cliente.buscarCuenta(self, idCuenta), Cliente.buscarPrestamo(idCuenta, idPrestamo), "Prestamo")
            return pago.RealizarPagoPrestamo(cuota)#cambiarnombre en pago


    def hacerPagoMulta(self, idCuenta, idMulta, monto=None):   
        if monto == None:
            pago = Pago(monto, Cliente.buscarCuenta(self, idCuenta), Cliente.buscarMulta(idCuenta, idMulta), "Multa")
            return pago.realizarPagoMulta(Cliente.buscarMulta(idCuenta, idMulta))  # cambiarnombre en pago
        else:
            pago = Pago(monto, Cliente.buscarCuenta(self, idCuenta), Cliente.buscarMulta(idCuenta, idMulta), "Multa")
            return pago.realizarPagoMulta(Cliente.buscarMulta(idCuenta, idMulta), monto)#cambiarnombre en pago

    def movPago(self, id):
        movimiento = Movimiento.movimientoPago(Cliente.buscarCuenta(self, id))
        lista = []
        if len(movimiento) == 0:
            return "Usted no cuenta con Transferencias actualmente"
        if len(Cliente.buscarCuenta(self, id).misBolsillos)==0:
                lista.append("Usted no cuenta con bolsillos actualmente")
        for i in movimiento:
            lista.append(i)
        return lista

    def movTransferencia(self, id):
        movimiento = Movimiento.movimientoTransferencia(Cliente.buscarCuenta(self, id))
        lista = []
        if len(movimiento) == 0:
            lista.append("Usted no cuenta con pagos actualmente")
        if (len((Cliente.buscarCuenta(self, id).getPrestamos())) == 0) :
            lista.append("Usted no cuenta con prestamos actualmente")
        if (((Cliente.buscarCuenta(self, id).getMultas())) == 0) :
            lista.append("Usted no tiene multas actualmente")
        for i in movimiento:
            lista.append(i)
        return lista

    #Getters y setters
    @classmethod
    def getListaCuentas(cls):
        return Cliente.listaCuentas

    @classmethod
    def setListaCuentas(self, listaCuentas):
        Cliente.listaCuentas = listaCuentas

    def getNombe(self):
        return self.nombre

    def setNombre(self, nombre):
        self.nombre = nombre

    def getCuenta(self):
        return self.cuenta

    def setCuenta(self, cuenta):
        self.cuenta = cuenta

    def getCedula(self):
        return self.cedula

    def setCecula(self, cedula):
        self.cedula = cedula

    def getTransferencia(self):
        return self.trasnferencia

    def setTransferencia(self, tranferencia):
        self.trasnferencia = tranferencia


    """
    Otros métodos
    """

    def movimientoTransferencia(self):
        pass

    def movimientoPago(self):
        pass