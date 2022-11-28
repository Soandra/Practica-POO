from cuenta import Cuenta
from cuentaAhorro import CuentaAhorro
from cuentaCorriente import CuentaCorriente
from prestamo import Prestamo
from bolsillo import Bolsillo
from multa import Multa
from pago import Pago
from cliente import Cliente

c = Cuenta("YO", 30000,"Ahorro")
c.aumentarSaldo(200)
print(c.saldoTotal)
print(c.titular)
print(c.getSaldoTotal())
print(c.getId())

d = Cuenta("Me", 1234, "Corriente")
print(d.getId())
print(d.saldoEnBolsillos())
print(d.getTipoCuenta())

ca = CuentaAhorro("Sofia", 1000, "Ahorro")
print(ca.getId())
print(ca.titular)
print(ca)
ca.aumentarSaldo(400)
print(ca)

cuentaCo = CuentaCorriente("Salome", 200, "Corriente")
print(cuentaCo)

cuenta = CuentaAhorro("anita", 2000, "Ahorro")
prestamo = Prestamo(500000, cuenta, "universitario")
print(prestamo)
print(cuenta.deuda)
#print(cuenta.getPrestamos())
#prestamo.saldarPrestamo()
#print(prestamo)

boldillo = Bolsillo(700000, 1, cuenta)
print(boldillo)
boldillo.cargarBolsillo(50000) #No se carga el bolsillo
print(boldillo)

multa = Multa(cuenta, 60000)
print(multa.fecha)
print(Multa.multas)
#print(multa)   !HAY UN ERROR AQUÍ!

#pago = Pago(2000,cuenta, prestamo, "Prestamo")
#print(pago.fecha)

cliente = Cliente("Jaimito", 123456)
print(cliente.listaCuentas) #las cuentas se añaden correctamente a la lista
print(cliente.listarCuentas())
