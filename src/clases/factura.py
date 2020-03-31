import time

class Factura:

    def __init__(self, nroFactura, cliente, estado, items):

        self._nroFactura = nroFactura
        self._fechaFactura = time.strftime("%c")
        self._cliente = cliente
        self._totalFactura = sum( item.getValorUnidad() for item in items )
        self._estado = estado
        self._items = items

    #Getters
    def getNroFactura(self):
        return self._nroFactura
    def getFechaFactura(self):
        return self._fechaFactura
    def getCliente(self):
        return self._cliente
    def getTotalFactura(self):
        return self._totalFactura
    def getEstado(self):
        return self._estado
    def getItems(self):
        return self._items

    #Setters
    def setNroFactura(self, nroFactura):
        self._nroFactura = nroFactura
    def setFechaFactura(self, fechaFactura):
        self._fechaFactura = fechaFactura
    def setCliente(self, cliente):
        self._cliente = cliente
    def setTotalFactura(self, totalFactura):
        self._totalFactura = totalFactura
    def setEstado(self, estado):
        self._estado = estado
    def setItems(self, items):
        self._items = items