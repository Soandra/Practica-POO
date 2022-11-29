from gestorAplicacion.usuarios.cuenta import Cuenta

class CuentaCorriente(Cuenta):

    def __init__(self, titular, saldo, tipoCuenta):
        super().__init__(titular, saldo, tipoCuenta)


    def __str__(self):
        if self.estado:
            return f'Cuenta (Corriente) -> ID = {self.getId()} :\nSaldo total = {self.saldoTotal}, Saldo disponible = {self.saldoDisponible}, Número de cuenta {self.numero}, Estado = activo' 
        else:
           return f'Cuenta (Corriente) -> ID = {self.getId()} :\nSaldo total = {self.saldoTotal}, Saldo disponible = {self.saldoDisponible}, Número de cuenta {self.numero}, Estado = inactivo'  