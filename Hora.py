class Hora():
# constructor    
    def __init__ (self):

        self.hora = 0
        self.minuto = 0
        self.segundo = 0

    def __init__ (self, hora = 0, minuto = 0, segundo =)
        
        modificarHora(hora, minuto, segundo)
        
# setters y getters

    def setHora (self, hora, minuto, segundo):
        self.__hora = hora % 24
        self.__minuto = minuto % 60
        self.__segundo = segundo % 60 

    def getHora (self):
        return str(self.__hora) + ":" + str(self.__minuto) + ":" + str(self.__segundo)

# funciones del programa

    def imprimirHora ():

        return print ("La hora que me has dado es: ", self.getHora())

#casos test

  if __name__ == '__main__':

    hora = Hora()
    hora.setHora(20, 11, 23)
    print (hora.imprimirHora())
