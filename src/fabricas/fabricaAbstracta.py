from src.fabricas.fabricaClientes import FabricaClientes
from src.fabricas.fabricaFacturas import FabricaFacturas

class FabricaAbstracta:

    __instance = None

    @staticmethod
    def getInstance():
        if FabricaAbstracta.__instance == None:
            FabricaAbstracta()
        else:
            return FabricaAbstracta.__instance

        return FabricaAbstracta.__instance

    def __init__(self):
        if FabricaAbstracta.__instance == None:
            FabricaAbstracta.__instance = self
        else:
            return self.__instance

    def crearFabrica(self, fabrica):

        if fabrica == "clientes":
            return FabricaClientes()
        elif fabrica == "facturas":
            return FabricaFacturas()
        else:
            raise Exception("La fabrica abstracta no puede crear esa fabrica!")
