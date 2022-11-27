from Python.gestorAplicacion.usuario.cuenta import Cuenta


class CuentaCorriente(Cuenta):
     def __int__(self, titular, saldo):
          super.__init__(titular, saldo, "Corriente")

     def __str__(self): #Incompleto, falta el id
          if self.estado:
               return f'Cuenta (Corriente) -> ID = ... :\n' \
                      'Saldo total = {self.saldoTotal} ' \
                      ', Saldo disponible = {self.saldoDisponible}' \
                      ', Número de cuenta {self.numero}' \
                      ', Estado = Activo'

          else:
               return f'Cuenta (Ahorro) -> ID = ... :\n' \
                      'Saldo total = {self.saldoTotal} ' \
                      ', Saldo disponible = {self.saldoDisponible}' \
                      ', Número de cuenta {self.numero}' \
                      ', Estado = Inactivo'


