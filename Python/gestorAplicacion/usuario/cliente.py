

import random

from Python.gestorAplicacion.transacciones.bolsillo import Bolsillo
from Python.gestorAplicacion.transacciones.pago import Pago
from Python.gestorAplicacion.transacciones.prestamo import Prestamo
from Python.gestorAplicacion.transacciones.transferencia import Transferencia
from Python.gestorAplicacion.usuario.cuentaAhorro import CuentaAhorro
from Python.gestorAplicacion.usuario.cuentaCorriente import CuentaCorriente


class Cliente:
    listaCuentas = []
    def __init__(self, nombre, cedula):
        self.nombre = nombre
        self.cuenta = None
        self.cedula = cedula
        self.trasnferencia = None

        var_random = random.randint(2,3)
        for i in range(0, var_random):
            Cliente.listaCuentas.append(CuentaAhorro(self, random.randint(500000, 9000000)))
            Cliente.listaCuentas.append(CuentaCorriente(self, random.randint(500000, 9000000)))

    @classmethod
    def buscarCuenta(cls, idCuenta):
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
        cuenta = Cliente.buscarCuenta(idCuenta)
        return cuenta.getMisBolsillos().get(idBolsillo)


    @classmethod
    def buscarMulta(cls,idCuenta, idMulta):
        cuenta = Cliente.buscarCuenta(idCuenta);
        return cuenta.getMultas().get(idMulta);


    @classmethod
    def buscarPrestamo(cls, idCuenta, idPrestamo):
        cuenta = Cliente.buscarCuenta(idCuenta)
        return cuenta.getPrestamos().get(idPrestamo)


    def hacerTransferencia(self, idCuentaOrigen, idCuentaDestino, valor):
        cuentaOrigen = Cliente.buscarCuenta(idCuentaOrigen)
        cuentaDestino = Cliente.buscarCuenta(idCuentaDestino)
        trasnfer = Transferencia(cuentaOrigen, cuentaDestino, valor)
        return trasnfer.enviarDinero()


    def solicitarPrestamo(self, valor, tipoPrestamo, idCuenta):
        if (valor >= Prestamo.TOPEMIN and valor <= Prestamo.TOPEMAX):
            (Cliente.buscarCuenta(idCuenta)).getPrestamos().add(Prestamo(valor, Cliente.buscarCuenta(idCuenta)), tipoPrestamo)


    def generarAhorro(self, valor, categoria, idCuenta):
        Cliente.buscarCuenta(idCuenta).getMisBolsillos().add(Bolsillo.crearBolsillo(valor,Cliente.buscarCuenta(idCuenta),categoria))


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
            pago = Pago((Cliente.buscarPrestamo(idCuenta, idPrestamo).getValorCuota()), Cliente.buscarCuenta(idCuenta),
                        Cliente.buscarPrestamo(idCuenta, idPrestamo), "Prestamo");
            return pago.RealizarPagoPrestamo()
        else:
            pago = Pago((Cliente.buscarPrestamo(idCuenta, idPrestamo).getValorCuota() * cuota), Cliente.buscarCuenta(idCuenta), Cliente.buscarPrestamo(idCuenta, idPrestamo), "Prestamo");
            return pago.RealizarPagoPrestamo(cuota)#cambiarnombre en pago


    def hacerPagoMulta(self, idCuenta, idMulta, monto=None):
        if monto == None:
            pago = Pago(monto, Cliente.buscarCuenta(idCuenta), Cliente.buscarMulta(idCuenta, idMulta), "Multa");
            return pago.realizarPagoMulta(Cliente.buscarMulta(idCuenta, idMulta))  # cambiarnombre en pago
        else:
            pago = Pago(monto, Cliente.buscarCuenta(idCuenta), Cliente.buscarMulta(idCuenta, idMulta), "Multa");
            return pago.realizarPagoMulta(Cliente.buscarMulta(idCuenta, idMulta), monto)#cambiarnombre en pago


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