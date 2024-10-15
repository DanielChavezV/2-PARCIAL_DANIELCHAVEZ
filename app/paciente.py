from persona import Persona

class Paciente(Persona):
    def __init__(self, id, nombre, apellido, fecha_nacimiento, genero, direccion, telefono, email):
        super().__init__(id, nombre, apellido, fecha_nacimiento, genero, direccion, telefono, email)
        self.historial_medico = []

    def agregar_historial(self, entrada):
        self.historial_medico.append(entrada)

    def obtener_historial(self):
        return self.historial_medico

    def obtener_info(self):
        return f"Paciente: {self.nombre} {self.apellido}, ID: {self.id}"