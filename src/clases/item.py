class Item:

    def __init__(self, id, tipoItem, descripcion, valorUnidad):

        self.__id = id
        self.__tipoItem = tipoItem
        self.__descripcion = descripcion
        self.__valorUnidad = valorUnidad

    def __str__(self):
        return "--Id del item: "+str(self.__id)+"\n--Tipo de item: "+str(self.__tipoItem)+"\n--Descripcion: "+str(self.__descripcion)+"\n--Valor unitario: "+str(self.__valorUnidad)

    #Getters
    def getId(self):
        return self.__id
    def getTipoItem(self):
        return self.__tipoItem
    def getDescripcion(self):
        return self.__descripcion
    def getValorUnidad(self):
        return self.__valorUnidad

    #Setters
    def setId(self, id):
        self.__id = id
    def setTipoItem(self, tipoItem):
        self.__tipoItem = tipoItem
    def setDescripcion(self, descripcion):
        self.__descripcion = descripcion
    def setValorUnidad(self, valorUnidad):
        self.__valorUnidad = valorUnidad