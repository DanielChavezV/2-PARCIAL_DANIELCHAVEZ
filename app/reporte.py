from rich.console import Console
from rich.table import Table
from collections import Counter
from datetime import datetime, timedelta

class Reporte:
    @staticmethod
    def generar_reporte_citas(citas):
        console = Console()
        table = Table(title="Reporte de Citas")
        
        table.add_column("Paciente", style="cyan")
        table.add_column("Médico", style="magenta")
        table.add_column("Fecha", style="green")
        table.add_column("Hora", style="yellow")
        table.add_column("Estado", style="blue")
        
        for cita in citas:
            table.add_row(
                f"{cita.paciente.nombre} {cita.paciente.apellido}",
                f"Dr. {cita.medico.nombre} {cita.medico.apellido}",
                str(cita.fecha),
                str(cita.hora),
                cita.estado
            )
        
        console.print(table)

    @staticmethod
    def generar_reporte_demanda_medicos(hospital):
        console = Console()
        table = Table(title="Reporte de Demanda de Médicos")
        
        table.add_column("Médico", style="cyan")
        table.add_column("Especialidad", style="magenta")
        table.add_column("Número de Citas", style="green")
        
        demanda_medicos = Counter()
        for cita in hospital.obtener_citas():
            demanda_medicos[cita.medico] += 1
        
        for medico, num_citas in demanda_medicos.most_common():
            table.add_row(
                f"Dr. {medico.nombre} {medico.apellido}",
                medico.especialidad,
                str(num_citas)
            )
        
        console.print(table)

   