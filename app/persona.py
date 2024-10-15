from abc import ABC, abstractmethod

class Persona(ABC):
    def __init__(self, id, nombre, apellido, fecha_nacimiento, genero, direccion, telefono, email):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.fecha_nacimiento = fecha_nacimiento
        self.genero = genero
        self.direccion = direccion
        self.telefono = telefono
        self.email = email

    @abstractmethod
    def obtener_info(self):
        pass
