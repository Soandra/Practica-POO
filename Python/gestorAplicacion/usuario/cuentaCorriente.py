from gestorAplicacion.usuario.cuenta import Cuenta

class CuentaCorriente(Cuenta):
     def __int__(self, titular, saldo):
          super.__init__(titular, saldo, "Corriente")

     def __str__(self): #Incompleto, falta el id
          if self.estado:
               return f'Cuenta (Corriente) -> ID = ... :\nSaldo total = {self.saldoTotal} ' \
                      f', Saldo disponible = {self.saldoDisponible}' \
                      f', Número de cuenta {self.numero}' \
                      f', Estado = Activo'

          else:
               return f'Cuenta (Ahorro) -> ID = ... :\nSaldo total = {self.saldoTotal} ' \
                      f', Saldo disponible = {self.saldoDisponible}' \
                      f', Número de cuenta {self.numero}' \
                      f', Estado = Inactivo'


