from datetime import datetime as dt
from gestorAplicacion.usuario import cuenta

class Multa :

    plazoPago = 30
    Multas = []

    def __init__(self, cuenta= None, monto = 50000, fecha = dt.now().strftime("%d/%m/%Y"), Estado = True):
        self.monto = monto
        self.cuenta = cuenta
        self.fecha = fecha
        self.Estado = Estado
        #static SimpleDateFormat formato = new SimpleDateFormat("yyyy-MM-dd")
        Multa.Multas.append(self)

    def pagarMulta(self, monto=None):
        if monto is None:
            self.cuenta.getMultas().remove(self)
            self.cuenta.setSaldoTotal(self.cuenta.getSaldoTotal()-self.monto)
            self.cuenta.setSaldoDisponible(self.cuenta.getSaldoDisponible()-self.monto)
        else:
            self.monto-=monto
            self.cuenta.setSaldoTotal(self.cuenta.getSaldoTotal()-monto)
            self.cuenta.setSaldoDisponible(self.cuenta.getSaldoDisponible()-monto)
            self.cuenta.getMultas().set(self.cuenta.getMultas().indexOf(self),self)
        
    def multarCuenta(cls, cuenta):
        cuenta.getMultas().add(Multa(cuenta))

    

    ''' Metodo usado para calcular el monto por mora despues de no haber cumplido el
    plazoPago. Si la cantidad de dias despues de haber pasado Plazopago
    es mayor a 90 se Bloquea la cuenta pasando Estado:a false
    '''
    def moraMulta(cls, pago, multa):
        fechaMulta = dt.strptime(multa.getFecha())
        fechaPago = dt.strptime(pago.getFecha())
        discriminante =  (fechaPago-fechaMulta).days()

        if (discriminante > cls.plazoPago):
            diasMora = discriminante- cls.plazoPago
            (pago.getCuenta()).setDeuda((pago.getCuenta()).getDeuda()*(1.01**diasMora)) #aplicar un mora del 1% por dia de mora
            if (diasMora > 90):                 # esto deberia de compararse por ultima fecha de pago y no por los dias de mora
                Multa.multarCuenta(pago.getCuenta())
            
        
    
    ''' Metodo usado para calcular el monto por mora despues de no haber cumplido el
    fechaPago del prestamo. Si la cantidad de dias despues de haber pasado fechaPago
    es mayor a 90 se multa la cuenta pasando Multa:a true y generando una nueva multa
    '''
    def moraPrestamo(cls, pago, cuenta, prestamo):
        fechaMulta = dt.strptime(prestamo.getFechaPago())
        fechaPago = dt.strptime(pago.getFecha())
        discriminante =  (fechaPago-fechaMulta).days()

        if (discriminante > cls.plazoPago) :
            diasMora = discriminante - cls.plazoPago
            cuenta.setDeuda(cuenta.getDeuda()*(1.01**diasMora)) #aplicar un mora del 1% por dia de mora

            if (diasMora > 90):                 # esto deberia de compararse por ultima fecha de pago y no por los dias de mora
                Multa.multarCuenta(cuenta)
            
    def ___str__(self) :

            return f'{self.getId()}: multa de {self.getMonto()} desde {self.getFecha()}'

    

    #Setters getters
    def getCuenta(self): return self.cuenta

    def setCuenta(self, cuenta): self.cuenta = cuenta

    def getMonto(self): return self.monto

    def setMonto(self, monto): self.monto = monto

    def getFecha(self): return self.fecha

    def setFecha(self, fecha): self.fecha = fecha

    def isEstado(self): return self.Estado

    def setEstado(self, estado): self.Estado = estado

    def getMultas(self) :return Multa.Multas

    def setMultas(self, multas): self.Multas = multas

    def getId(self) :return self.cuenta.getMultas().index(self)
    
