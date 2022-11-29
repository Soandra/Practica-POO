import random
class Cuenta:
    aux = 0    

    def __init__(self, titular, saldo, tipoCuenta):
        self.titular = titular
        self.tipoCuenta = tipoCuenta
        self.estado = True
        self.numero = random.randint(1000, 10000)
        self.misBolsillos = []
        self.saldoTotal = saldo
        self.saldoDisponible = saldo
        self.id = Cuenta.aux +1
        Cuenta.aux = Cuenta.aux + 1

        if len(self.misBolsillos) == 0:
            self.saldoDisponible = self.saldoTotal
        else:
            self.saldoDisponible = self.saldoTotal - self.saldoEnBolsillos()


    def aumentarSaldo(self, cantidad):
        if self.estado:
            self.setSaldoTotal(self.getSaldoTotal() + cantidad)


    def disminuirSaldo(self, cantidad):
        if self.estado and (self.getSaldoDisponible() >= cantidad):
            self.setSaldoTotal(self.getSaldoTotal() - cantidad)


    def saldoEnBolsillos(self):
        valorEnBolsilos = 0
        for bolsillo in self.misBolsillos:
            valorEnBolsilos += bolsillo.getValorCargaBolsillo()
        return valorEnBolsilos
        
    
    def getId(self):
        return self.id
    
    def getTitular(self):
        return self.titular

    def setTitular(self, titular):
        self.titular = titular

    def getTipoCuenta(self):
        return self.tipoCuenta

    def setTipoCuenta(self, tipoCuenta):
        self.tipoCuenta = tipoCuenta

    def getSaldoTotal(self):
        return self.saldoTotal

    def setSaldoTotal(self, saldoTotal):
        self.saldoTotal = saldoTotal

    def getSaldoDisponible(self):
        return self.saldoDisponible

    def setSaldoDisponible(self, saldoDisponible):
        self.saldoDisponible= saldoDisponible

    def getMisBolsillos(self):
        return self.misBolsillos

    def setMisBolsillos(self, misBolsillos):
        self.misBolsillos = misBolsillos

    def isEstado(self):
        return self.estado

    def setEstado(self, estado):
        self.estado = estado

    def getNumero(self):
        return self.numero

    def setNumero(self, numero):
        self.numero = numero




