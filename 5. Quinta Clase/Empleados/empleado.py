
class Empleado:
    
    def __init__(self):
        self.__nombre = None
        self.__apellido = None
        self.__cargo = None
        self.__salario = None

    def getNombre(self):
        return self.__nombre

    def setNombre(self, nombre):
        self.__nombre = nombre

    def getApellido(self):
        return self.__apellido

    def setApellido(self, apellido):
        self.__apellido = apellido

    def getCargo(self):
        return self.__cargo

    def setCargo(self, cargo):
        self.__cargo = cargo

    def getSalario(self):
        return self.__salario
    
    def setSalario(self, salario):
        self.__salario = salario


    def __str__(self):
        return str("nombre: {} \n"
            "apellido: {} \n"
            "cargo: {} \n"
            "salario: {}").format(
                self.__nombre,
                self.__apellido,
                self.__cargo,
                self.__salario)

