from src.clases.cliente import Cliente

class ClienteCorriente(Cliente):

    def __init__(self, id, nombre, apellidos, genero, fechaNacimiento, estadoCivil):

        Cliente.__init__(self, id, nombre, apellidos, genero, fechaNacimiento, estadoCivil)

        self.__descuento = 0.0

    def __str__(self):
        
        return "--Id del cliente: "+str(self._id)+"\n--Nombre: "+str(self._nombre)+"\n--Apellido: "+str(self._apellidos)+"\n--Genero: "+str(self._genero)+"\n--Fecha de nacimiento: "+str(self._fechaNacimiento)+"\n--Estado civil: "+str(self._estadoCivil)+"\n--Descuento por cliente preferencial: "+str(self.__descuento)

    def getDescuento(self):
        return self.__descuento

    def setDescuento(self, descuento):
        self.__descuento = descuento