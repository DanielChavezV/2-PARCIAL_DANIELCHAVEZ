from datetime import datetime, timedelta
from cita import Cita

class Agenda:
    def __init__(self):
        self.citas = []

    def agendar_cita(self, cita):
        if self.verificar_disponibilidad(cita):
            self.citas.append(cita)
            return True
        return False

    def cancelar_cita(self, cita):
        if cita in self.citas:
            self.citas.remove(cita)
            return True
        return False

    def verificar_disponibilidad(self, nueva_cita):
        for cita in self.citas:
            if cita.fecha == nueva_cita.fecha and cita.hora == nueva_cita.hora:
                return False
        return True

    def obtener_citas(self):
        return self.citas

    def mover_cita(self, cita_original, nueva_fecha, nueva_hora):
        if cita_original in self.citas:
            nueva_cita = Cita(cita_original.paciente, cita_original.medico, nueva_fecha, nueva_hora)
            if self.verificar_disponibilidad(nueva_cita):
                self.citas.remove(cita_original)
                self.citas.append(nueva_cita)
                return True
        return False