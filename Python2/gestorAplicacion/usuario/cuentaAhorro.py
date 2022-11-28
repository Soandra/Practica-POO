import random

from Python.gestorAplicacion.usuario.cuenta import Cuenta


class CuentaAhorro(Cuenta):

    #i = 1000
    def __int__(self, titular, saldo, tipoCuenta="Ahorro"):
        super.__init__(titular, saldo, tipoCuenta)
        self._deuda = 0
        self.multas = []
        self.prestamos = []
        self.id = random.randint(1,100)


    #Función para verificar si la cuenta tiene multas
    def tieneMulta(self):
        return self.multas != None

    def __str__(self): #Incompleto, falta el id

        return f'Cuenta (Ahorro) -> ID = {self.getId()} :\n' \
                'Saldo total = {self.saldoTotal} ' \
                ', Saldo disponible = {self.saldoDisponible}' \
                ', Número de cuenta {self.numero}' \
                ', Deuda = {self._deuda}' \
                ', Estado = Activo'



    #Getters y setters
    def getId(self):
        return self.id
    #@classmethod
    #def getId(cls):
        #return CuentaAhorro.i

        #from Python.gestorAplicacion.usuario.cliente import Cliente
        #if cls in Cliente.listaCuentas:
            #return Cliente.listaCuentas.index(cls)
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
