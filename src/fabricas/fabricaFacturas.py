from src.clases.facturaConIva import FacturaConIva
from src.clases.facturaSinIva import FacturaSinIva

class FabricaFacturas:

    def crearFactura(self, nroFactura, cliente, estado, items, tipoFactura):

        if tipoFactura == "conIva":
            return FacturaConIva(nroFactura, cliente, estado, items, 0.19)
        elif tipoFactura == "sinIva":
            return FacturaSinIva(nroFactura, cliente, estado, items)
        else:
            raise Exception("La fabrica no puede crear esa factura!")