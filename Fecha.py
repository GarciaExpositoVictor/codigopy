#~Programa que representa la fecha en cifras

#Nombre de la clase

class Fecha():

#~Bloque constructor
	
	def __init__ (self):
		year = 1900
		mes = 1
		dia = 1

	def __init__ (self, year = 1900, mes = 01, dia = 01):

		self.year = year
		self.mes = mes
		self.dia = dia

#~Setters y getters
	
	def setYear(self, year):
		self.year = year

	def getYear(self):
		return self.year

	def setMes(self, mes):
		self.mes = mes

	def	getMes(self):
		return self.mes

	def setDia(self, dia):
		self.dia = dia

	def getDia(self):
		return self.dia

	def setFecha(self, dia, mes, year):
		self.dia = dia if dia >= 1 and dia <= 31 else 1
		self.mes = mes if mes >= 1 and mes <= 12 else 1
		self.year = year if year >= 1900 and year <= 300 else 1900

	def getFecha(self):
		return str(self.getDia()) + "-" + str(self.getMes()) + "-" + str(self.getYear())

#~Funciones del programa

"""Esta función recibe un número y devuelve el mes al cual le corresponde dicho número"""
	def __mesLetra(self):
		mesesAnyo = ['enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio', 'julio', 'agosto', 'septiembre', 'octubre', 'noviembre', 'diciembre']
		return mesesAnyo[self.getMes() -1]

"""Esta función nos devuelve la fecha en formato dd/mes(con letras)/yyyy"""
	def imprimirFecha(self):

		print (self.getDia(),"-",self.__mesLetra(),"-",self.getYear())

#~Casos test

if __name__ == '__main__':

	hora = Hora()
	hora.setHora(20, 11, 23)
	print (hora.imprimirHora())
