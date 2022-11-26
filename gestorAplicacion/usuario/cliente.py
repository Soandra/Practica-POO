from cuenta import Cuenta
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
        pass

    def buscarMulta(self,idCuenta, idMulta):
        cuenta = self.buscarCuenta(idCuenta)
        return cuenta.getMultas().get(idMulta)

    def buscarPrestamo(self, id, idPrestamo):
        pass

    def hacerTransferencia(self, idCuentaOrigen, idCuentaDestino, valor):
        pass

    def solicitarPrestamo(self, valor, tipoPrestamo, idCuenta):
        pass

    def generarAhorro(self, valor, categoria, idCuenta):
        pass

    def cargarAhorro(self, idCuenta, idBolsillo):
        pass

    def descargarAhorro(self, valor, idCuenta, idBolsillo):
        pass

    def hacerPagoPrestamo(self, idCuenta, idPrestamo, cuota):
        pass

    def hacerPagoMulta(self, idCuenta, idMulta):
        pass


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