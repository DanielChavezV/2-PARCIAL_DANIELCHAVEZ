from datetime import datetime

class Cita:
    def __init__(self, paciente, medico, fecha, hora, estado="agendada", motivo_cancelacion=None):
        self.paciente = paciente
        self.medico = medico
        self.fecha = fecha
        self.hora = hora
        self.estado = estado  # Atributo estado
        self.motivo_cancelacion = motivo_cancelacion  # Atributo motivo de cancelación

    def cancelar(self, motivo):
        self.estado = "cancelada"
        self.motivo_cancelacion = motivo  # Guardar el motivo de la cancelación

    def __str__(self):
        if self.estado == "cancelada":
            return f"Cita: {self.paciente.nombre} {self.paciente.apellido} con Dr. {self.medico.nombre} {self.medico.apellido} el {self.fecha} a las {self.hora}. Estado: {self.estado}. Motivo de cancelación: {self.motivo_cancelacion}"
        return f"Cita: {self.paciente.nombre} {self.paciente.apellido} con Dr. {self.medico.nombre} {self.medico.apellido} el {self.fecha} a las {self.hora}. Estado: {self.estado}"

