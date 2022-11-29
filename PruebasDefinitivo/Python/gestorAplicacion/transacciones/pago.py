from datetime import datetime as dt
from gestorAplicacion.transacciones.multa import Multa
from gestorAplicacion.transacciones.movimiento import Movimiento

class Pago:
    pagos = []
    aux = 0
    def __init__(self, monto, cuenta, multaOPrestamo,tipo): #multaOPrestamo hace referencia a si el objeto es de clase multa o prestamo
        self.monto = monto
        self.id = Pago.aux +1
        Pago.aux = Pago.aux + 1
        self.fecha = dt.now().strftime("%d/%m/%Y")
        self.cuenta = cuenta 
        self.tipo = tipo
        Pago.pagos.append(self)
        self.multaOPrestamo = multaOPrestamo



    ''' Este metodo calcula la diferencia del monto a la hora de pagar una multa
    * separa casos dependiendo si es mayor menor o igual
    * retorna un mensaje dependiendo del caso
    * '''
    def realizarPagoMulta(self, multa, monto=None):
        Multa.moraMulta(self, multa)
        if (not self.cuenta.isEstado()):return "su cuenta está bloqueada" #en caso de que el metodo anterior haya dado false evitar problemas de consola
        
        if monto is None: #Pago total
            multa.pagarMulta()
            Movimiento(self.cuenta,self,multa.getMonto(),"Pago de multa",dt.now().strftime("%d/%m/%Y"))
            return f"su multa fue pagada con exito\nEste es su nuevo Saldo: {multa.getCuenta().getSaldoDisponible()}"
            
            
        if (self.cuenta.getSaldoDisponible()< monto):
            
            return "Saldo insuficiente"

        else:
            multa.pagarMulta(monto)
            Movimiento(self.cuenta,self,monto,"Pago de multa",dt.now().strftime("%d/%m/%Y"))
            return f"Este es su nuevo monto: {multa.getMonto()}" #Pago parcial
    

    ''' Este metodo realiza el pago de prestamo a travez de la consulta del
    estado saldo y prestamo de cuenta y la consulta de cuotas fechas de pago y los dias de mora de prestamo
    para al final calcular el nuevo saldo y el estado del prestamo
    '''
    def RealizarPagoPrestamo(self,cuotas=None): #opcion 1 para pagar un prestamo (pago total del prestamo)
        Multa.moraPrestamo(self, self, self.cuenta, self.multaOPrestamo)
        if(not self.cuenta.isEstado()):
            return "Su cuenta está bloqueada"

        if(self.cuenta.getDeuda()!= self.multaOPrestamo.getValorPrestamo()):
            self.cuenta.setDeuda(0)
            
        if (self.multaOPrestamo.getValorPrestamo() >= self.cuenta.getSaldoDisponible()):
            return "Saldo insuficiente"

        if cuotas is None: #Pago total
            Movimiento(self.cuenta,self,self.multaOPrestamo.getValorPrestamo(),"Pago de prestamo",dt.now().strftime("%d/%m/%Y"))

            self.multaOPrestamo.saldarPrestamo()
            return f"Su deuda ha sido saldada\nNuevo saldo: {self.cuenta.getSaldoDisponible()}"

        if (cuotas is None and cuotas > self.multaOPrestamo.cuotasDePago):
            return "Valor de cuotas es excedente"

        #pago parcial
        if (cuotas == self.multaOPrestamo.cuotasDePago):
            Movimiento(self.cuenta,self,self.multaOPrestamo.getValorPrestamo(),"Pago de prestamo",dt.now().strftime("%d/%m/%Y"))
            self.multaOPrestamo.saldarPrestamo()
            return f"Su deuda ha sido saldada\nNuevo saldo: {self.cuenta.getSaldoDisponible()}"

        else:
            Movimiento(self.cuenta,self,self.multaOPrestamo.getValorCuota(),"Pago de prestamo",dt.now().strftime("%d/%m/%Y"))
            self.multaOPrestamo.saldarCuota(cuotas)
            return f"Nuevo saldo: {self.cuenta.getSaldoDisponible()} \
            \nDeuda actual: {self.cuenta.getDeuda()} \
            \nTe Faltan {self.multaOPrestamo.cuotasDePago} cuotas"

    #setters getters

    def getFecha(self): return self.fecha

    def setFecha(self, fecha): self.fecha = fecha

    def getCuenta(self):return self.cuenta

    def setCuenta(self, cuenta):self.cuenta = cuenta

    # def getId(self):
    #     return self.id

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