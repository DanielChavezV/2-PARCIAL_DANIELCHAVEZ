from agenda import Agenda
from cita import Cita
from collections import Counter

class Hospital:
    def __init__(self, nombre):
        self.nombre = nombre
        self.pacientes = []
        self.medicos = []
        self.agenda = Agenda()

    def agregar_paciente(self, paciente):
        self.pacientes.append(paciente)

    def agregar_medico(self, medico):
        self.medicos.append(medico)

    def buscar_paciente(self, id_paciente):
        for paciente in self.pacientes:
            if paciente.id == id_paciente:
                return paciente
        return None

    def buscar_medico(self, id_medico):
        for medico in self.medicos:
            if medico.id == id_medico:
                return medico
        return None

    def agendar_cita(self, paciente, medico, fecha, hora):
        cita = Cita(paciente, medico, fecha, hora)
        return self.agenda.agendar_cita(cita)

    def cancelar_cita(self, cita, motivo):
        cita.cancelar(motivo)
        return self.agenda.cancelar_cita(cita)

    def obtener_citas(self):
        return self.agenda.obtener_citas()

    def mover_cita(self, cita_original, nueva_fecha, nueva_hora):
        return self.agenda.mover_cita(cita_original, nueva_fecha, nueva_hora)

    def buscar_medicos_por_especialidad(self, especialidad):
        return [medico for medico in self.medicos if medico.especialidad == especialidad]

    def obtener_citas_canceladas(self):
        """Obtener las citas que han sido canceladas"""
        return [cita for cita in self.agenda.obtener_citas() if cita.estado == "cancelada"]