from persona import Persona

class Medico(Persona):
    def __init__(self, id, nombre, apellido, fecha_nacimiento, genero, direccion, telefono, email, especialidad):
        super().__init__(id, nombre, apellido, fecha_nacimiento, genero, direccion, telefono, email)
        self.especialidad = especialidad

    def obtener_info(self):
        return f"Dr. {self.nombre} {self.apellido}, Especialidad: {self.especialidad}, ID: {self.id}"
