class Movimiento: # :(
	Movimientos = []

	def __init__(self,cuenta,clase,valor,tipo,fecha): #cuanta de origen,clase de origen, tipo de movimiento, fecha
		self.valor = valor
		self.cuenta = cuenta
		self.clase = clase
		self.tipo = tipo
		self.fecha = fecha
		Movimiento.Movimientos.append(self)

	@classmethod
	def movimientoPago(cls,cuenta): #muestra los pagos por multas y prestamos
		mov = []
		for i in Movimiento.Movimientos:
			if i.getCuenta() != cuenta:
				continue
			if i.getTipo() == "Pago de multa":
				mov.append(i) 
				continue
			if i.getTipo() == "Pago de prestamo": 
				mov.append(i) 
				continue
		return mov

	@classmethod
	def  movimientoTransferencia(cls,cuenta): #muestra los pagos por transferencias y bolsillos
		mov = []
		for i in Movimiento.Movimientos:
			if i.getCuenta() != cuenta:
				continue
			if i.getTipo() == "Desde mis bolsillos": 
				mov.append(i) 
				continue
			if i.getTipo() == "Hacia mis bolsillos": 
				mov.append(i) 
				continue
			if i.getTipo() == "Transferencia": 
				mov.append(i) 
				continue
			if i.getTipo() == "Prestamo": 
				mov.append(i) 
				continue

		return mov
	

	#Getters y setters

	def getValor(self): return self.valor
	def setValor(self,valor): self.valor = valor

	def getCuenta(self): return self.cuenta
	def setCuenta(self,cuenta): self.cuenta = cuenta

	def getClase(self): return self.clase
	def setClase(self,clase): self.clase = clase

	def getTipo(self): return self.tipo
	def setTipo(self,tipo): self.tipo = tipo

	def getFecha(self): return self.fecha
	def setFecha(self,fecha): self.fecha = fecha


	def __str__(self): return f"Movimiento de tipo {self.getTipo()} el dia {self.getFecha()} con un valor de {self.getValor()}"