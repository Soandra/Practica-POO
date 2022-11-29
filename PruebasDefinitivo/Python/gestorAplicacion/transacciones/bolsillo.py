from gestorAplicacion.transacciones.movimiento import Movimiento
from datetime import datetime as dt

class Bolsillo():
    CATEGORIA = ["VIAJES", "EDUCACION", "SALUD", "ALIMENTACION", "TRANSPORTE", "HOGAR", "IMPREVISTOS", "OTROS"]
    aux = 0
    def __init__(self, metaAhorro,opcion, cuenta) :
        self.cuenta = cuenta
        self.categoria = Bolsillo.CATEGORIA[opcion]
        self.metaAhorro = metaAhorro
        self.id = Bolsillo.aux +1
        Bolsillo.aux = Bolsillo.aux +1
        self.valorCargaBolsillo = 0
        #cuenta.getMisBolsillos().append(self)
    
    @classmethod
    def crearBolsillo(cls, metaAhorro, opcion, cuenta) :
        cuenta.setSaldoDisponible(cuenta.getSaldoTotal())
        return Bolsillo(metaAhorro, opcion, cuenta)


    def cargarBolsillo(self, valor=None):
        if valor == None:
            if (self.cuenta.getSaldoDisponible() < self.metaAhorro):
                return "No tienes saldo suficiente en la cuenta para cargar el bolsillo"

            elif (self.valorCargaBolsillo == self.metaAhorro):
                return "La meta de ahorro ya fue alcanzada"

            elif (self.cuenta.misBolsillos == []):
                return "No existe un bolsillo, por favor cree uno"

            self.valorCargaBolsillo = self.metaAhorro
            self.cuenta.setSaldoDisponible(self.cuenta.getSaldoTotal() - self.cuenta.saldoEnBolsillos())
            Movimiento(self.cuenta,self,self.metaAhorro,"Hacia mis bolsillos",dt.now().strftime("%d/%m/%Y"))
            return "Felicitaciones, alcanzaste tu meta de ahorro"

        else:
            if (self.cuenta.getSaldoDisponible() < valor):
                return "No tienes saldo suficiente en la cuenta para cargar el bolsillo"

            elif (len(self.cuenta.misBolsillos)==0):
                return "No existe un bolsillo, por favor cree uno"

            elif (valor + self.valorCargaBolsillo == self.metaAhorro):
                return "La meta de ahorro ya fue alcanzada"

            elif (valor + self.valorCargaBolsillo > self.metaAhorro):
                return "Verifica tu saldo en el bolsillo, es posible que excedas el valor posible a recargar "

            self.valorCargaBolsillo += valor
            Movimiento(self.cuenta,self,valor,"Hacia mis bolsillos",dt.now().strftime("%d/%m/%Y"))
            self.cuenta.setSaldoDisponible(self.cuenta.getSaldoTotal() - self.cuenta.saldoEnBolsillos())
            return f"El bolsillo fue cargado con {self.getValorCargaBolsillo()}"


    def descargarBolsillo(self, valor=None):
        
        if valor == None:
            if (len(self.cuenta.misBolsillos) == 0 or self.valorCargaBolsillo == 0):
                return "Debe crear o cargar el bolsillo para poder descargarlo"

            self.cuenta.setSaldoTotal(self.cuenta.getSaldoDisponible() + self.cuenta.saldoEnBolsillos())
            self.cuenta.setSaldoDisponible(self.cuenta.getSaldoTotal())
            self.valorCargaBolsillo -= self.valorCargaBolsillo
            self.cuenta.misBolsillos.set(self.cuenta.misBolsillos.indexOf(self), self)
            Movimiento(self.cuenta,self,self.valorCargaBolsillo,"Desde mis bolsillos",dt.now().strftime("%d/%m/%Y"))
            return "Se ha descargado el bolsillo completamente."
        else:
            if (self.valorCargaBolsillo == 0):
                return "Su bolsillo no cuenta con saldo"

            elif (len(self.cuenta.misBolsillos) == 0 or self.valorCargaBolsillo == 0):
                return "Debe crear o cargar el bolsillo para poder descargarlo"
            Movimiento(self.cuenta,self,valor,"Desde mis bolsillos",dt.now().strftime("%d/%m/%Y"))
            self.valorCargaBolsillo -= valor
            self.cuenta.setSaldoTotal(self.cuenta.getSaldoDisponible() + self.cuenta.saldoEnBolsillos())
            return f"Se ha descargado el valor del bolsillo a tu cuenta, quedas con un saldo de ahorro de: {self.getValorCargaBolsillo()}"


    def getCuenta(self) :
        return self.cuenta

    def setCuenta(self, cuenta) :
        self.cuenta = cuenta

    def getCategoria(self) :
        return self.categoria

    def setCategoria(self, categoria) :
        self.categoria = categoria

    def getId(self) :
        return self.cuenta.getMisBolsillos().index(self)

    def setId(self, id) :
        self.id = id

    def getValorCargaBolsillo(self) :
        return self.valorCargaBolsillo

    def setValorCargaBolsillo(self, valorCargaBolsillo) :
        self.valorCargaBolsillo = valorCargaBolsillo

    def mensajeBolsillo(self) :
        return f"Has iniciado un nuevo ahorro: \
Número de bolsillo = {self.getId()}\
, se asoció a la cuenta = {self.cuenta.getNumero()}\
                \nestableciste una meta de ahorro de = {self.metaAhorro}\
, para ser usado en = {self.categoria}\
                \nHasta el momento has ahorrado = {self.valorCargaBolsillo}"

    def __str__(self) :
        return f"Bolsillo {self.getId()}: en la cuenta {self.cuenta.getNumero()} con una meta de ahorro {self.metaAhorro} hasta el momento has ahorrado {self.valorCargaBolsillo}"