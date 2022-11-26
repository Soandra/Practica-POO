from datetime import datetime as dt
from gestorAplicacion.usuario import cuenta
from multa import Multa
import random

class Pago:
    id = 1000 + random.randint(8999)
    pagos = []
    def __init__(self, monto, cuenta, tipo, tipo_clase=None):
        self.monto = monto
        self.fecha = dt.now().strftime("%d/%m/%Y")
        self.cuenta = cuenta
        self.tipo = tipo
        self.tipo_clase = tipo_clase # aqui se deberia de almacenar objetos tipo multa o prestamo
        Pago.pagos.add(self)

    
    # Este metodo filtra los pagos de prestamos y le añade los pagos de multas
    def separarPagos():
        multas = []
        prestamos = []
        for pago in Pago.pagos:
            if (pago.getTipo().equals("Multa")):
                multas.add(pago)
            else:
                prestamos.add(pago)
            
        
        prestamos.addAll(multas)
        return prestamos
    

    ''' Este metodo calcula la diferencia del monto a la hora de pagar una multa
    * separa casos dependiendo si es mayor menor o igual
    * retorna un mensaje dependiendo del caso
    * '''
    def realizarPagoMulta(self, multa, monto=None):

        Multa.moraMulta(self, multa)

        if (not self.cuenta.isEstado()):return "su cuenta está bloqueada" #en caso de que el metodo anterior haya dado false evitar problemas de consola

        if (self.cuenta.getSaldoDisponible()< monto):return "Saldo insuficiente"

        if monto is None:
            multa.pagarMulta()
            return f"su multa fue pagada con exito\nEste es su nuevo Saldo: {multa.getCuenta().getSaldoDisponible()}"
        else:
            multa.pagarMulta(monto)
            return "Este es su nuevo monto: "+ multa.getMonto()
    

    ''' Este metodo realiza el pago de prestamo a travez de la consulta del
    estado saldo y prestamo de cuenta y la consulta de cuotas fechas de pago y los dias de mora de prestamo
    para al final calcular el nuevo saldo y el estado del prestamo
    '''
    def RealizarPagoPrestamo(self,cuotas=None): #opcion 1 para pagar un prestamo (pago total del prestamo)
        Multa.moraPrestamo(self,self.cuenta,self.tipo_clase)

        if(not self.cuenta.isEstado()): return "Su cuenta está bloqueada"

        if(self.cuenta.getDeuda()!= self.tipo_clase.getValorPrestamo()): self.cuenta.setDeuda(0)
            
        if (self.tipo_clase.getValorPrestamo() >= self.cuenta.getSaldoDisponible()): return "Saldo insuficiente"

        if cuotas is None:
            self.tipo_clase.saldarPrestamo()
            return f"Su deuda ha sido saldada\nNuevo saldo: {self.cuenta.getSaldoDisponible()}"

        if ( cuotas is None and cuotas > self.tipo_clase.cuotasDePago): return "Valor de cuotas es exedente"

        if (cuotas == self.tipo_clase.cuotasDePago):
            self.tipo_clase.saldarPrestamo()
            return f"Su deuda ha sido saldada\nNuevo saldo: {cuenta.getSaldoDisponible()}"

        else :
            self.tipo_clase.saldarCuota(cuotas)
            return f"Nuevo saldo: {self.cuenta.getSaldoDisponible()} \
            \nDeuda actual: {self.cuenta.getDeuda()} \
            \nTe Faltan {self.prestamo.cuotasDePago} cuotas"

    #setters getters

    def getFecha(self): return self.fecha

    def setFecha(self, fecha): self.fecha = fecha

    def getCuenta(self):return cuenta

    def setCuenta(self, cuenta):self.cuenta = cuenta

    def getId(self):return id

    def getMonto(self):return self.monto

    def setMonto(self, monto):self.monto = monto

    def getPagos(cls):return cls.pagos

    def setPagos(cls, pagos) :Pago.pagos = pagos

    def getTipo(self):return self.tipo

    def setTipo(self, tipo):self.tipo = tipo

    def __str__(self) :
        return f"Pago \
                \nmonto= {self.monto} \
                \nid= {self.pagos.index(self)} \
                \nfecha= {self.fecha} \
                \ncuenta= {self.cuenta.getNumero()} \
                \ntipo= {self.tipo}"
