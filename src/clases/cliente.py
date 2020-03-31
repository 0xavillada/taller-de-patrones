class Cliente:

    def __init__(self, id, nombre, apellidos, genero, fechaNacimiento, estadoCivil):

        self._id = id
        self._nombre = nombre
        self._apellidos = apellidos
        self._genero = genero
        self._fechaNacimiento = fechaNacimiento
        self._estadoCivil = estadoCivil

    # Geters
    def getId(self):
        return self._id
    def getNombre(self):
        return self._nombre
    def getApellidos(self):
        return self._apellidos
    def getGenero(self):
        return self._genero
    def getFechaNacimiento(self):
        return self._fechaNacimiento
    def getEstadoCivil(self):
        return self._estadoCivil

    # Seters
    def setId(self, id):
        self._id = id
    def setNombre(self, nombre):
        self._nombre = nombre
    def setApellidos(self, apellidos):
        self._apellidos = apellidos
    def setGenero(self, genero):
        self._genero = genero
    def setFechaNacimiento(self, fechaNacimiento):
        self._fechaNacimiento = fechaNacimiento
    def setEstadoCivil(self, estadoCivil):
        self._estadoCivil = estadoCivil