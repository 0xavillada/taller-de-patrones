from src.interfaces.dao import Dao
from src.fabricas.fabricaAbstracta import FabricaAbstracta

class CrudImp(Dao):

    __instance = None
    facturas = []
    contador = 0

    @staticmethod
    def getInstance():
        if CrudImp.__instance == None:
            CrudImp()
        else:
            return self.__instance

        return CrudImp.__instance 

    def __init__(self):
        if CrudImp.__instance == None:
            CrudImp.__instance = self
            CrudImp.facturas = []
            CrudImp.contador = 0
        else:
            raise Exception("Esta clase es un singleton!")

    def getAllFacturas(self):
        return self.facturas

    def getById(self, id):
        for x in self.facturas:
            if x.getNroFactura() == int(id):
                return x
        print("> Error: Factura con id: "+id+" no existe en el registro!\n")
        return None

    def createFactura(self, idCliente, nombre, apellidos, genero, fechaNacimiento, estadoCivil, cliente, items, tipoFactura):
        fabricaAbstracta = FabricaAbstracta.getInstance()
        fabricaClientes = fabricaAbstracta.crearFabrica("clientes")
        fabricaFacturas = fabricaAbstracta.crearFabrica("facturas")

        nuevoCliente = fabricaClientes.crearCliente(idCliente, nombre, apellidos, genero, fechaNacimiento, estadoCivil, cliente, 0.2)
        nuevaFactura = fabricaFacturas.crearFactura(self.contador, nuevoCliente, "activa", items, tipoFactura)
        self.facturas.append(nuevaFactura)
        print("> Factura con id: "+str(self.contador)+" fue creada exitosamente!\n")
        self.contador += 1

    def updateFactura(self, id, idCliente, nombre, apellidos, genero, fechaNacimiento, estadoCivil, cliente, items, tipoFactura):

        for i in range(len(self.facturas)):
            if self.facturas[i].getNroFactura() == int(id):

                fabricaAbstracta = FabricaAbstracta.getInstance()
                fabricaClientes = fabricaAbstracta.crearFabrica("clientes")
                fabricaFacturas = fabricaAbstracta.crearFabrica("facturas")

                nuevoCliente = fabricaClientes.crearCliente(idCliente, nombre, apellidos, genero, fechaNacimiento, estadoCivil, cliente, 0.2)
                nuevaFactura = fabricaFacturas.crearFactura(self.facturas[i].getNroFactura(), nuevoCliente, "activa", items, tipoFactura)
                self.facturas[i] = nuevaFactura
                print("> Factura con id: "+ str(id) +" fue modificado exitosamente!\n")
                return 0
        print("> Error: Factura con id: "+str(id)+" no existe en el registro!\n")
        return -1

    def removeFactura(self, id):
        for i in range(len(self.facturas)):
            if self.facturas[i].getNroFactura() == int(id):
                self.facturas.pop(i)
                print("> Factura con id: "+str(id)+" fue removida exitosamente!\n")
                return 0
        print("> Error: Factura con id: "+str(id)+" no existe en el registro!\n")
        return -1