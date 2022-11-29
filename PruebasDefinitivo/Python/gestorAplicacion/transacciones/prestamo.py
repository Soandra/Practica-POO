from datetime import datetime as dt
from datetime import timedelta
from gestorAplicacion.transacciones.movimiento import Movimiento


class Prestamo:
    TOPEMAX = 7000000
    TOPEMIN = 500000

    def __init__(self, valor, cuenta, tipoPrestamo, fechaPrestamo=dt.now().strftime("%d/%m/%Y")): 
        self.cuenta = cuenta
        self.valor = valor
        self.tipoPrestamo = tipoPrestamo
        self.valorPrestamo = 0
        self.diasMora = ""
        self.interes = 0.0
        self.cuotasDePago = 24
        self.valorCuota = 0
        self.estado = True
        self.generarPrestamo(valor, tipoPrestamo)
        self.fechaPrestamo = fechaPrestamo
        self.fechaPago = (dt.strptime(self.fechaPrestamo,"%d/%m/%Y") + timedelta(days=30)).strftime("%d/%m/%Y")


    def generarPrestamo(self, valorPrestamo, tipoPrestamo):
        if tipoPrestamo == "universitario":
            self.interes = 0.06
        elif tipoPrestamo == "hobbie":
            self.interes == 0.04
        elif tipoPrestamo == "libre":
            self.interes == 0.1
        else:
            return "El tipo de prestamo ingresado no existe. Por favor ingrese un tipo de prestamo válido (universitario, hobbie, libre)"

        Movimiento(self.cuenta,self,valorPrestamo,"Prestamo",dt.now().strftime("%d/%m/%Y"))
        valorTotalPrestamo = valorPrestamo + valorPrestamo * self.interes
        self.cuenta.setDeuda(valorTotalPrestamo + self.cuenta.getDeuda())
        self.cuenta.setSaldoTotal(self.cuenta.getSaldoTotal() + valorPrestamo)
        self.cuenta.setSaldoDisponible(self.cuenta.getSaldoDisponible() + valorPrestamo)
        self.valorCuota = round(valorTotalPrestamo / self.cuotasDePago)
        self.valorPrestamo = valorPrestamo
        self.tipoPrestamo = tipoPrestamo

    def saldarCuota(self, cantidadCuota):
        valor = self.valorCuota * cantidadCuota
        self.cuenta.setDeuda(self.cuenta.getDeuda() - valor)
        
        self.cuenta.setSaldoTotal(self.cuenta.getSaldoTotal() - valor)
        self.cuenta.setSaldoDisponible(self.cuenta.getSaldoDisponible() - valor)
        self.cuotasDePago -= cantidadCuota
        self.valorPrestamo -= self.valorCuota

    def saldarPrestamo(self):
        valorTotal = self.valorPrestamo + self.valorPrestamo * self.interes
        print(valorTotal)
        self.cuenta.setDeuda(valorTotal - self.cuenta.getDeuda())
        self.cuenta.setSaldoTotal(self.cuenta.getSaldoTotal() - valorTotal)
        self.cuenta.setSaldoDisponible(self.cuenta.getSaldoDisponible() - valorTotal)
        self.cuenta.getPrestamos().remove(self)
        if len(self.cuenta.getPrestamos()) == 0:
            self.cuenta.setDeuda(0)


    #Getters y setters
    def getValorPrestamo(self):
        return self.valorPrestamo

    def setValorPrestamo(self, valorPrestamo):
        self.valorPrestamo = valorPrestamo

    def getDiasMora(self):
        return self.diasMora

    def setDiasMora(self, diasMora):
        self.diasMora = diasMora

    def getValorCuota(self):
        return self.valorCuota

    def setValorCuota(self, valorCuota):
        self.valorCuota = valorCuota

    def getFechaPago(self):
        return self.fechaPago

    def setFechaPago(self, fechaPago):
        self.fechaPago = fechaPago

    def getInteres(self):
        return self.interes

    def setInteres(self, interes):
        self.interes = interes

    def getTipoPrestamo(self):
        return self.tipoPrestamo

    def setTipoPrestamo(self, tipoPrestamo):
        self.tipoPrestamo = tipoPrestamo

    def getFechaPrestamo(self):
        return self.fechaPrestamo

    def isEstado(self):
        return self.estado

    def setEstado(self, estado):
        self.estado = estado

    def getId(self):
        if self in self.cuenta.getPrestamos():
            return (self.cuenta.getPrestamos()).index(self)
        return None

    def mensajePrestamo(self):
        return f"Ha sido aprobado tu prestamo \
               \ncon un valor de {self.valorPrestamo} \
               \nen la fecha {self.fechaPrestamo}\
               \nDe tipo {self.tipoPrestamo} \
               \ncon una tasa de interes del {self.interes}, \
               \nfue desembolsado en la cuenta {self.cuenta.getNumero()}\
               \nLa cuota a pagar será de {self.valorCuota} \
               \npara una deuda total de {self.cuenta.getDeuda()}"

    def __str__(self):
        return f"{self.getId()}: Prestamo con una deuda pendiente de {self.cuenta.getDeuda()} de tipo {self.tipoPrestamo}. La cuota a pagar es {self.valorCuota}" 
        
'''cuenta = CuentaAhorro("Sofia", 2000, "Ahorro")
prestamo = Prestamo(500000, cuenta, "universitario")
print(prestamo)
print(cuenta.deuda)'''