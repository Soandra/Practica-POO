import random
class Cuenta:
    id = 1000

    def __int__(self, titular, saldo, tipoCuenta):
        self.titular = titular
        self.tipoCuenta = tipoCuenta
        self.saldoTotal = saldo
        self.saldoDisponible = saldo
        self.misBolsillos = []
        self.estado = True
        self.numero = random.randint(1000,10000)
        #Cuenta.id = getId() + 1
        """
        if len(misBolsillos) == 0:
            self.saldoDisponible = saldoTotal
        else:
            self.saldoDisponible = saldoTotal - saldoEnBolsillos()
        """

        #Función para disminuir el saldo total de la cuenta
        def aumentarSaldo(self, cantidad):
            if self.estado:
                setSaldoTotal(getSaldoTotal() + cantidad)


        #Función para disminuir el saldo total de la cuenta
        def disminuirSaldo(self, cantidad):
            if self.estado and (getSaldoDisponibles() >= cantidad):
                setSaldoTotal(getSaldoTotal() - cantidad)

        #Función que retorna el saldo de los bolsillos
        def saldoEnBolsillos(self):
            pass

        #Getters y setters
        def getId(self):
            pass
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

        def getSaldoDisponibles(self):
            return self.saldoDisponible

        def setSaldoDisponible(self, saldoDisponible):
            self.saldoDisponible= saldoDisponible

        def getMisBolsillos(self):
            return self.misBolsillos

        def setMisBolsillos(self, misBolsillos):
            self.misBolsillos = misBolsillos

        def getEstado(self):
            return self.estado

        def setEstado(self, estado):
            self.estado = estado

        def getNumero(self):
            return self.numero

        def setNumero(self, numero):
            self.numero = numero















