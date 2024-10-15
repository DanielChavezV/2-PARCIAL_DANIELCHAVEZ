from paciente import Paciente
from medico import Medico

class PersonaFactory:
    @staticmethod
    def crear_persona(tipo, *args):
        if tipo == "paciente":
            return Paciente(*args)
        elif tipo == "medico":
            return Medico(*args)
        else:
            raise ValueError("Tipo de persona no válido")
