class Clientes:
    def __init__(self, nombre, apellido, correo, telefono):
        self.nombre = nombre
        self.apellido = apellido
        self.correo = correo
        self.telefono = telefono

    def __str__(self):
        return f"cliente: {self.nombre} {self.apellido}"