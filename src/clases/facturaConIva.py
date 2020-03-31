from src.clases.factura import Factura

class FacturaConIva(Factura):

    def __init__(self, nroFactura, cliente, estado, items, valorIva=0.19):

        Factura.__init__(self, nroFactura, cliente, estado, items)

        self.__valorIva = valorIva
        self.__totalFacturaConIva = self.getTotalFactura() + (self.getTotalFactura() * self.__valorIva)

    def __str__(self):
        itemsStr=""
        for x in self._items:
            itemsStr+=str(x)

        return "\nFactura Nro: "+str(self._nroFactura)+"\nFecha de factura: "+str(self._fechaFactura)+"\nCliente: "+str(self._cliente)+"\nValo Subtotal: "+str(self._totalFactura)+"\nPorcentaje del IVA: "+str(self.__valorIva)+"\nValor total facturado: "+str(self.__totalFacturaConIva)+"\nEstado: "+str(self._estado)+"\nItems: "+itemsStr+"\n\n"

    #Getters
    def getTotalFacturaConIva(self):
        return self.__totalFacturaConIva

    #Setters
    def setTotalFacturaConIva(self, totalFacturaConIva):
        self.__totalFacturaConIva = totalFacturaConIva