from Python.gestorAplicacion.transacciones.bolsillo import Bolsillo
from Python.gestorAplicacion.transacciones.pago import Pago
from Python.gestorAplicacion.transacciones.prestamo import Prestamo
from Python.gestorAplicacion.transacciones.transferencia import Transferencia
from cuentaAhorro import CuentaAhorro
from cuentaCorriente import CuentaCorriente

import random

class Cliente:
    def __init__(self, nombre, cedula):
        self.nombre = nombre
        self.cuenta = None
        self.listaCuentas = []
        self.cedula = cedula
        self.trasnferencia = None

        var_random = random.randint(2,3)
        for i in range(0, var_random):
            self.listaCuentas.append(CuentaAhorro(self, random.randint(500000, 9000000)))
            self.listaCuentas.append(CuentaCorriente(self, random.randint(500000, 9000000)))

    def buscarCuenta(self, idCuenta):
        for cuenta in self.listaCuentas:
            if idCuenta == cuenta.id:
                return cuenta
        return None

    def listarCuentas(self):
        for cuenta in self.listaCuentas:
            return cuenta
        return None

    def buscarBolsillo(self, idCuenta, idBolsillo):
        cuenta = self.buscarCuenta(idCuenta);
        return cuenta.getMisBolsillos().get(idBolsillo)

    def buscarMulta(self,idCuenta, idMulta):
        cuenta = self.buscarCuenta(idCuenta);
        return cuenta.getMultas().get(idMulta);

    def buscarPrestamo(self, idCuenta, idPrestamo):
        cuenta = self.buscarCuenta(idCuenta)
        return cuenta.getPrestamos().get(idPrestamo)

    def hacerTransferencia(self, idCuentaOrigen, idCuentaDestino, valor):
        cuentaOrigen = self.buscarCuenta(idCuentaOrigen)
        cuentaDestino = self.buscarCuenta(idCuentaDestino)
        trasnfer = Transferencia(cuentaOrigen, cuentaDestino, valor)
        return trasnfer.enviarDinero()

    def solicitarPrestamo(self, valor, tipoPrestamo, idCuenta):
        if (valor >= Prestamo.TOPEMIN and valor <= Prestamo.TOPEMAX):
            (self.buscarCuenta(idCuenta)).getPrestamos().add(Prestamo(valor, self.buscarCuenta(idCuenta)), tipoPrestamo)


    def generarAhorro(self, valor, categoria, idCuenta):
        self.buscarCuenta(idCuenta).getMisBolsillos().add(Bolsillo.crearBolsillo(valor,self.buscarCuenta(idCuenta),categoria))

    def cargarAhorro(self, idCuenta, idBolsillo):
        return self.buscarBolsillo(idCuenta, idBolsillo).cargarBolsillo()

    # creo que debe haber un bolsillo que descargue totalmente y otro parcial
    def descargarAhorro(self, valor, idCuenta, idBolsillo):
        return self.buscarBolsillo(idCuenta, idBolsillo).descargarBolsillo(valor)

    def hacerPagoPrestamo(self, idCuenta, idPrestamo, cuota):
        pago = Pago((self.buscarPrestamo(idCuenta, idPrestamo).getValorCuota() * cuota), self.buscarCuenta(idCuenta), self.buscarPrestamo(idCuenta, idPrestamo), "Prestamo");
        return pago.RealizarPagoPrestamo(cuota)

    def hacerPagoMulta(self, idCuenta, idMulta, monto):
        pago = Pago(monto, self.buscarCuenta(idCuenta), self.buscarMulta(idCuenta, idMulta), "Multa");
        return pago.realizarPagoMulta(Cliente.buscarMulta(idCuenta, idMulta), monto)


    #Getters y setters
    def getNombe(self):
        return self.nombre

    def setNombre(self, nombre):
        self.nombre = nombre

    def getCuenta(self):
        return self.cuenta

    def setCuenta(self, cuenta):
        self.cuenta = cuenta

    def getListaCuentas(self):
        return self.listaCuentas

    def setListaCuentas(self, listaCuentas):
        self.listaCuentas = listaCuentas

    def getCedula(self):
        return self.cedula

    def setCecula(self, cedula):
        self.cedula = cedula

    def getTransferencia(self):
        return self.trasnferencia

    def setTransferencia(self, tranferencia):
        self.trasnferencia = tranferencia