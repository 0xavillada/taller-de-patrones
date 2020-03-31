from src.persistencia.CrudImp import CrudImp
from src.clases.tipoItem import TipoItem
from src.clases.item import Item

crud = CrudImp.getInstance()

def menu0():
    return input("> Seleccione una accion:\n1. Ver todas las facturas\n2. Nueva factura\n3. Modificar una factura\n4. Eliminar factura\n5. Buscar factura\n0. Salir\n\n> ")

def mostrarFacturas(facturas):
    for x in facturas:
        print("Nro. Factura: " + str(x.getNroFactura()) + " Fecha: " + x.getFechaFactura())

def tomarDatos():

    idCliente = input("> Ingresa el id del cliente:\n> ")
    nombre = input("> Ingresa el nombre del cliente:\n> ")
    apellidos = input("> Ingresa los apellidos del cliente:\n> ")
    genero = input("> Ingresa el genero del cliente:\n> ")
    fechaNacimiento = input("> Ingresa fecha de nacimiento del cliente:\n> ")
    estadoCivil = input("> Ingresa el estado civil del cliente:\n> ")
    clienteElegido = input("> Escoja tipo de cliente:\n1. Corriente\n2. Premium\n\n> ")
    cliente = ""
    if clienteElegido == "1":
        cliente = "corriente"
    elif clienteElegido == "2":
        cliente = "premium"
    else:
        print("> Error: Valor invalido!")
        return -1

    itemsSeleccionados = input("\n> Seleccione los productos separados por espacio:\n1. perro\n2. gaseosa\n\n> ").split()
    print()
    items = []
    for x in itemsSeleccionados:
        if int(x) == 1:
            items.append(Item(x, TipoItem("1", "solidos"), "Perro sencillo con queso", 5000))
            print("> Agregado perro sencillo x1")
        elif int(x) == 2:
            items.append(Item(x, TipoItem("2", "bebidas"), "Gaseosa en lata", 2000))
            print("> Agregado gaseosa lata x1")
        else:
            print("> Error: "+x+" Producto invalido!")
            return -1

    tipoFacturaElegido = input("> Escoja tipo de factura:\n1. Con iva\n2. Sin iva\n\n> ")
    if tipoFacturaElegido == "1":
        return [idCliente, nombre, apellidos, genero, fechaNacimiento, estadoCivil, cliente, items, "conIva"]
    elif tipoFacturaElegido == "2":
        return [idCliente, nombre, apellidos, genero, fechaNacimiento, estadoCivil, cliente, items, "sinIva"]
    else:
        print("> Error: Valor invalido!")
        return -1

while True:

    resMenu0 = menu0()
    print()

    if resMenu0 == "1":
        mostrarFacturas(crud.getAllFacturas())

    elif resMenu0 == "2":
        datosLeidos = tomarDatos()
        if datosLeidos == -1:
            continue
        else:
            crud.createFactura(datosLeidos[0], datosLeidos[1], datosLeidos[2], datosLeidos[3], datosLeidos[4], datosLeidos[5], datosLeidos[6], datosLeidos[7], datosLeidos[8])

    elif resMenu0 == "3":
        idEditar = input("> Digite el Nro de la factura a editar:\n ")
        datosLeidos = tomarDatos()
        crud.updateFactura(idEditar, datosLeidos[0], datosLeidos[1], datosLeidos[2], datosLeidos[3], datosLeidos[4], datosLeidos[5], datosLeidos[6], datosLeidos[7], datosLeidos[8])

    elif resMenu0 == "4":
        resMenu4 = input("> Digite el Nro de la factura a eliminar:\n ")
        crud.removeFactura(resMenu4)
    elif resMenu0 == "5":
        resMenu5 = input("> Digite el Nro de la factura a buscar:\n ")
        print(crud.getById(resMenu5))
    elif resMenu0 == "0":
        break
    else:
        continue