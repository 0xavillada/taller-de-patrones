from src.clases.factura import Factura

class FacturaSinIva(Factura):

    def __init__(self, nroFactura, cliente, estado, items):

        Factura.__init__(self, nroFactura, cliente, estado, items)

    def __str__(self):
        itemsStr=""
        for x in self._items:
            itemsStr+=str(x)

        return "\nFactura Nro: "+str(self._nroFactura)+"\nFecha de factura: "+str(self._fechaFactura)+"\nCliente: "+str(self._cliente)+"\nValor total: "+str(self._totalFactura)+"\nEstado: "+str(self._estado)+"\nItems: "+itemsStr+"\n\n"