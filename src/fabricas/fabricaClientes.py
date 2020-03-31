from src.clases.clienteCorriente import ClienteCorriente
from src.clases.clientePremiun import ClientePremium

class FabricaClientes:

    def crearCliente(self, id, nombre, apellidos, genero, fechaNacimiento, estadoCivil, cliente, descuento):

        if cliente == "corriente":
            return ClienteCorriente(id, nombre, apellidos, genero, fechaNacimiento, estadoCivil)
        elif cliente == "premium":
            return ClientePremium(id, nombre, apellidos, genero, fechaNacimiento, estadoCivil, descuento)
        else:
            raise Exception("La fabrica no puede crear ese cliente!")