from gestorAplicacion.usuarios.cuenta import Cuenta

class CuentaAhorro(Cuenta):

    def __init__(self, titular, saldo, tipoCuenta):
        super().__init__(titular, saldo, tipoCuenta)
        self.deuda = 0
        self.multas = []
        self.prestamos =[]

    def tieneMulta(self):
        return self.multas != None

    def __str__(self): 
        if self.estado:
            return f'Cuenta (Ahorro) -> ID = {self.getId()} :\nSaldo total = {self.saldoTotal}, Saldo disponible = {self.saldoDisponible}, Número de cuenta {self.numero}, Deuda = {self.deuda}, Estado = activo' 
        else:
           return f'Cuenta (Ahorro) -> ID = {self.getId()} :\nSaldo total = {self.saldoTotal}, Saldo disponible = {self.saldoDisponible}, Número de cuenta {self.numero}, Deuda = {self.deuda}, Estado = inactivo'  
            
    def getDeuda(self):
        return self.deuda

    def setDeuda(self, deuda):
        self.deuda = deuda

    def getMultas(self):
        return self.multas

    def setMultas(self, multas):
        self.multas = multas

    def getPrestamos(self):
        return self.prestamos

    def setPrestamos(self, prestamos):
        self.prestamos = prestamos

        
