class TipoItem:

    def __init__(self, idDescripcion, descripcion):

        self.__idDescripcion = idDescripcion
        self.__descripcion = descripcion

    def __str__(self):
        return "----Id de descripcion: "+str(self.__idDescripcion)+"\n----Descripcion: "+str(self.__descripcion)

    #Getters
    def getIdDescripcion(self):
        return self.__idDescripcion
    def getDescripcion(self):
        return self.__descripcion

    #Setters
    def setIdDescripcion(self, idDescripcion):
        self.__idDescripcion = idDescripcion
    def setDescripcion(self, descripcion):
        self.__descripcion = descripcion