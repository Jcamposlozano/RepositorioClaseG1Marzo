


class Empleado:
    
    def __init__(self):
        self.nombre = None
        self.apellido = None
        self.cargo = None
        self.salario = None


    def __str__(self):
        return str("nombre: {} \n"
            "apellido: {} \n"
            "cargo: {} \n"
            "salario: {}").format(
                self.nombre,
                self.apellido,
                self.cargo,
                self.salario)

