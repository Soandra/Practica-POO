from datetime import datetime as dt
from datetime import timedelta
class Prestamo:
    TOPEMAX = 7000000
    TOPEMIN = 500000

    def __int__(self, valor, cuenta, tipoPrestamo):
        self.cuenta = cuenta
        self.valor = valor
        self.tipoPrestamo = tipoPrestamo
        self.valorPrestamo = 0
        self.diasMora = ""
        self.fechaPrestamo = dt.now().strftime("%d/%m/%Y")
        self.fechaPago = self.fechaPrestamo + timedelta(days= 30)
        self.interes = 0.0

        self.cuotasDePago = 24
        self.valorCuota = 0
        self.estado = True
        self.generarPrestamo(valor, tipoPrestamo)

    def generarPrestamo(self, valorPrestamo, tipoPrestamo):
        if tipoPrestamo == "universitario":
            self.interes = 0.06
        elif tipoPrestamo == "hobbie":
            self.interes == 0.04
        elif tipoPrestamo == "libre":
            self.interes == 0.1
        else:
            print("El tipo de prestamo ingresado no existe. Por favor ingrese un tipo de prestamo válido (universitario, hobbie, libre)")

        valorTotalPrestamo = valorPrestamo + valorPrestamo * self.interes
        self.cuenta.setDeuda(valorTotalPrestamo + self.cuenta.getDeuda())
        self.cuenta.setSaldoTotal(self.cuenta.getSaldoTotal() + valorPrestamo)
        self.cuenta.setSaldoDisponible(self.cuenta.getSaldoDisponible() + valorPrestamo)
        self.valorCuota = round(valorTotalPrestamo / self.cuotasDePago )
        self.valorPrestamo = valorPrestamo;
        self.tipoPrestamo = tipoPrestamo;

    def saldarCuota(self, cantidadCuota):
        valor = self.valorCuota * self.cantidadCuotas
        self.cuenta.setDeuda(self.cuenta.getDeuda() - valor)
        self.cuenta.setSaldoTotal(self.cuenta.getSaldoTotal() - valor)
        self.cuenta.setSaldoDisponible(self.cuenta.getSaldoDisponible() - valor)
        self.cuotasDePago -= self.cantidadCuotas
        self.valorPrestamo -= self.valorCuota

    def saldarPrestamo(self):
        valorTotal = self.valorPrestamo + self.valorPrestamo * self.interes
        print(valorTotal)
        self.cuenta.setDeuda(valorTotal - self.cuenta.getDeuda())
        self.cuenta.setSaldoTotal(self.cuenta.getSaldoTotal() - valorTotal)
        self.cuenta.setSaldoDisponible(self.cuenta.getSaldoDisponible() - valorTotal)
        self.cuenta.getPrestamos().remove(self);
        if self.cuenta.getPrestamos().isEmpty():
            self.cuenta.setDeuda(0);


    #Getters y setters
    def getValorPrestamo(self):
        return self.valorPrestamo

    def setValorPrestamo(self, valorPrestamo):
        self.valorPrestamo = valorPrestamo;

    def getDiasMora(self):
        return self.diasMora;

    def setDiasMora(self, diasMora):
        self.diasMora = diasMora

    def getValorCuota(self):
        return self.valorCuota;

    def setValorCuota(self, valorCuota):
        self.valorCuota = valorCuota;

    def getFechaPago(self):
        return self.fechaPago;

    def setFechaPago(self, fechaPago):
        self.fechaPago = fechaPago;

    def getInteres(self):
        return self.interes;

    def setInteres(self, interes):
        self.interes = interes

    def getTipoPrestamo(self):
        return self.tipoPrestamo;

    def setTipoPrestamo(self, tipoPrestamo):
        self.tipoPrestamo = tipoPrestamo;

    def getFechaPrestamo(self):
        return self.fechaPrestamo;

    def isEstado(self):
        return self.estado

    def setEstado(self, estado):
        self.estado = estado

    def getId(self):
        return self.cuenta.getPrestamos().indexOf(self)

    def mensajePrestamo(self):
        return f"Ha sido aprobado tu prestamo" \
               f"con un valor de {self.valorPrestamo}" \
               f"en la fecha " \
               f"De tipo {self.tipoPrestamo}" \
               f"con una tasa de interes del {self.interes}, " \
               f"fue desembolsado en la cuenta {self.cuenta.getNumero()}" \
               f"La cuota a pagar será de {self.valorCuota}" \
               f"para una deuda total de {self.cuenta.getDeuda()}"

    def __str__(self):
        return self.getId() + ": Prestamo con una deuda pendiente de " + self.cuenta.getDeuda() + " de tipo " + self.tipoPrestamo + " La cuota a pagar es " + self.valorCuota;


