from datetime import datetime as dt
from gestorAplicacion.transacciones.movimiento import Movimiento
import random 

class Transferencia:
	id = 0
	lista= []

	def __init__(self, cuentaOrigen,  cuentaFinal, valor):
		self.fecha = dt.now().strftime("%d/%m/%Y")
		self.cuentaOrigen = cuentaOrigen
		self.cuentaFinal = cuentaFinal
		self.valor = valor
		Transferencia.id = 1000 + random.randint(1,100)
		Transferencia.lista.append(self)
		self.enviarDinero()
		Movimiento(self.cuentaOrigen,self,self.valor,"Transferencia",dt.now().strftime("%d/%m/%Y"))
		

	def enviarDinero(self):
		if (self.cuentaOrigen.isEstado()==False):
			return "cuenta inactiva"
			
		if (self.cuentaOrigen.getSaldoDisponible()<self.valor) :
			return "saldo insuficiente"
		
		self.cuentaOrigen.disminuirSaldo(self.valor)
		self.cuentaFinal.aumentarSaldo(self.valor)
		self.cuentaOrigen.setSaldoDisponible(self.cuentaOrigen.getSaldoDisponible() - self.valor)
		self.cuentaFinal.setSaldoDisponible(self.cuentaFinal.getSaldoDisponible() + self.valor)
		return f"La transferencia por un valor de {self.getValor()} fue exitosa."
	
	def __str__(self) :
		return  f"Transferencia {self.getId()}:\
				se realizo: {self.getFecha()}\
				desde: {self.getCuentaOrigen().getId()}\
				hacia: {self.getCuentaDestino().getId()}\
				con valor de: {self.getValor()}"
	
	
	@classmethod
	def getId(cls) :return  Transferencia.id

	@classmethod
	def setId(cls, id): Transferencia.id = id

	def getCuentaOrigen(self): return self.cuentaOrigen

	def setCuentaOrigen(self, cuenta): self.cuentaOrigen = cuenta

	def getCuentaFinal(self): return self.cuentaFinal

	def setcuentaFinal(self, cuentaFinal): self.cuentaFinal = cuentaFinal

	def getFecha(self): return self.fecha

	def setFecha(self, fecha): self.fecha = fecha

	def getValor(self): return self.valor

	def setValor(self, valor): self.valor = valor

	@classmethod
	def getLista(cls): return Transferencia.lista
	@classmethod
	def setLista(cls, lista): Transferencia.lista = lista