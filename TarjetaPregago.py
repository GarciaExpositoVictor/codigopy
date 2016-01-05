#~Programa que representa una tarjeta prepago de un teléfono con la cual podemos enviar mensajes, llamar e ingresar saldo
#~Importamos estos módulos para poder heredar sus métodos
from dni import *
from Hora import * 

#~Clase

class TarjetaPrepago ():

	hora.__init__
	dni.__init__

#~Bloque de los constructores
	
	def __init__ (self):

		self.numeroTelefono = ""
		self.NIF = NIF ()
		self.saldo = float
		self.consumo = Hora()

	def __init__ (self, numeroTelefono = "", NIF = "", saldo = 0.0, consumo = Hora()):

		self.numeroTelefono = numeroTelefono
		self.NIF = NIF
		self.saldo = saldo
		self.consumo = Hora ()

#~Seters y getters
	
	def setNumeroTelefono (self, numeroTelefono):
		self.numeroTelefono = numeroTelefono

	def getNumeroTelefono (self):
		return self.numeroTelefono

	def setNIF (self, NIF):
		self.NIF = NIF

	def getNIF (self):
		return NIF

	def setSaldo (self, saldo):
		self.saldo = saldo

	def getSaldo (self):
		return saldo

	def setConsumo (self, consumo):
		self.consumo = consumo

	def getConsumo (self):
		return consumo

#Funciones del programa

"""Esta función recibe como dato un numero e incrementa el saldo en la cantidad deseada"""
	def ingresarSaldo (self, ingresoSaldo):

		saldoActualizado = self.saldo() + ingresoSaldo
		self.getSaldo(dineroActualizado)
		return (ingresoSaldo, saldoActualizado)
		
"""Esta función reduce nuestro saldo en función de los mensajes que deseemos enviar"""
	def enviarMensaje (self, cantidadMensajes, precioMensaje):

		while self.saldo() >= 0:
			consumo = self.getSaldo - (cantidadMensajes * precioMensaje)
			self.getSaldo(consumo)
			return (consumo, cantidadMensajes)
		else:
			print ("Tu saldo es insuficiente para realizar el mensaje")
			
"""Esta función reduce nuestro saldo en función de la duración de la llamada, su coste y el establecimiento de llamada"""
	def realizarLlamada (self, establecimientoLlamada, duracionLlamada, tarifaLlamada):

		while saldo >= 0:
			consumo = self.getSaldo() - ((duracionLlamada * tarifaLlamada) + establecimientoLlamada)
			self.getSaldo (consumo)
			return (consumo)

		else:
			print ("Saldo insuficiente para realizar la llamada")
			
"""Esta función nos permite ver los datos relacionados a la tarjeta"""
	def consultarTarjeta (self):

		print ("Su numero es: ", self.numeroTelefono)
		print ("Su NIF es: ", self.NIF)
		print ("Su saldo es: ", self.saldo)
		
"""Esta función nos permite cambiar la duración de la llamada a segundos para así poder calcular su coste"""
	def cambiaraSegundos (self):

		segundos = (self.horas * 3600) + (self.minutos * 60) + self.segundos

#~Casos test

if __name__ == '__main__':
	tarjetaPrepago = TarjetaPrepago()
	tarjetaPrepago.setNumeroTelefono("564564654")
	tarjetaPrepago.setNif("45610975C")
	tarjetaPrepago.setSaldo(100)
	tarjetaPrepago.consultarTarjeta()

	print ("\n")

	ingresoSaldo, saldoActualizado = tarjetaPrepago.ingresarSaldo(100)
	consumo, cantidadMensajes = tarjetaPrepago.enviarMensaje(10)
	duracionLlamada, consumo = tarjetaPrepago.realizarLlamada(200)

	print ("Se ha ingresado:",str(cantidadIngresada),"euros del saldo disponible, tu saldo actual es de:", str(self.getSaldo(saldoActualizado)), "euros")
	print ("Por la cantidad de:",str(cantidadMensajes),"Mensajes, se ha descontado:",str(consumo), " euros del saldo disponible, tu saldo actual es de:", str(saldoRestante), "euros")
	print ("La duracion de la llamada es:",str(segundosHablados),"segundos, se ha descontado:",str(consumo), "euros del saldo disponible, tu saldo actual es de:", str(self.getSaldo(consumo)), "euros")


 


