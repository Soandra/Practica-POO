from cuenta import Cuenta

class CuentaAhorro(Cuenta):
    def __int__(self, titular, saldo):
        super.__init__(titular, saldo, "Ahorro")
        self._deuda = 0
        self.multas = []
        self.prestamos = []

    #Función para verificar si la cuenta tiene multas
    def tieneMulta(self):
        return self.multas != None

    def __str__(self): #Incompleto, falta el id
        if self.estado:
            return f'Cuenta (Ahorro) -> ID = ... :\nSaldo total = {self.saldoTotal} ' \
                   f', Saldo disponible = {self.saldoDisponible}' \
                   f', Número de cuenta {self.numero}' \
                   f', Deuda = {self._deuda}' \
                   f', Estado = Activo'

        else:
            return f'Cuenta (Ahorro) -> ID = ... :\nSaldo total = {self.saldoTotal} ' \
                   f', Saldo disponible = {self.saldoDisponible}' \
                   f', Número de cuenta {self.numero}' \
                   f', Deuda = {self._deuda}' \
                   f', Estado = Inactivo'

    #Getters y setters
    def getDeuda(self):
        return self._deuda

    def setDeuda(self, deuda):
        self._deuda = deuda

    def getMultas(self):
        return self.multas

    def setMultas(self, multas):
        self.multas = multas

    def getPrestamos(self):
        return self.prestamos

    def setPrestamos(self, prestamos):
        self.prestamos = prestamos
