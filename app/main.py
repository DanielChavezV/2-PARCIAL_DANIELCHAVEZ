import csv
import json
from datetime import datetime
from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt
from rich.panel import Panel
from rich.text import Text
from rich.align import Align
from hospital import Hospital
from paciente import Paciente
from medico import Medico
from notificacion import NotificacionCorreo, NotificacionSMS, NotificacionWhatsapp
from reporte import Reporte

console = Console()

def mostrar_logo():
    logo = """
            ██████╗██╗     ██╗███╗   ██╗██╗ ██████╗ █████╗ 
            ██╔════╝██║     ██║████╗  ██║██║██╔════╝██╔══██╗
            ██║     ██║     ██║██╔██╗ ██║██║██║     ███████║
            ██║     ██║     ██║██║╚██╗██║██║██║     ██╔══██║
            ╚██████╗███████╗██║██║ ╚████║██║╚██████╗██║  ██║
            ╚═════╝╚══════╝╚═╝╚═╝  ╚═══╝╚═╝ ╚═════╝╚═╝  ╚═╝

                                [bold yellow]CLÍNICA DCH[/bold yellow]
             [italic cyan]"Transformando tu salud con cuidado y dedicación"[/italic cyan]
    """
    console.print(Align.center(logo, vertical="middle"), style="bold green")


def cargar_datos_iniciales(hospital):
    # Cargar pacientes desde CSV
    with open('datos//pacientes.csv', 'r', encoding='utf-8') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            paciente = Paciente(
                row['identificación'], row['nombre_completo'].split()[0], 
                ' '.join(row['nombre_completo'].split()[1:]),
                '1990-01-01', 'No especificado',  
                'No especificada', row['celular'], row['correo']
            )
            hospital.agregar_paciente(paciente)

    # Cargar médicos desde JSON
    with open('datos/medicos.json', 'r', encoding='utf-8') as file:
        medicos_data = json.load(file)
        for medico_data in medicos_data:
            medico = Medico(
                medico_data['id'], medico_data['nombre'], medico_data['apellido'],
                medico_data['fecha_nacimiento'], medico_data['genero'],
                medico_data['direccion'], medico_data['telefono'],
                medico_data['email'], medico_data['especialidad']
            )
            hospital.agregar_medico(medico)

    # Cargar citas desde CSV
    with open('datos/citas.csv', 'r', encoding='utf-8') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            paciente = hospital.buscar_paciente(row['paciente'])
            medico = hospital.buscar_medico(row['medicos'])
            if paciente and medico:
                fecha_hora = datetime.strptime(row['fecha_hora'], '%Y-%m-%d %H:%M:%S')
                hospital.agendar_cita(paciente, medico, fecha_hora.date(), fecha_hora.time())

def mostrar_menu_principal():
    mostrar_logo()
    console.print(Panel("Sistema de Gestión de Citas Médicas", style="bold green on grey15"))
    table = Table(show_header=False, box=None)
    table.add_row("1. Agendar cita")
    table.add_row("2. Cancelar cita")
    table.add_row("3. Mover cita")
    table.add_row("4. Ver citas")
    table.add_row("5. Generar reportes")
    table.add_row("6. Salir")
    console.print(table)

def agendar_cita(hospital):
    console.print(Panel("Agendar nueva cita", style="bold green on grey15"))
    id_paciente = Prompt.ask("[bold white]ID del paciente[/]")
    paciente = hospital.buscar_paciente(id_paciente)
    if not paciente:
        console.print("[bold red]Paciente no encontrado[/]")
        return

    especialidad = Prompt.ask("[bold white]Especialidad requerida[/]")
    medicos_disponibles = hospital.buscar_medicos_por_especialidad(especialidad)
    if not medicos_disponibles:
        console.print("[bold red]No hay médicos disponibles para esa especialidad[/]")
        return

    console.print("[bold green]Médicos disponibles:[/]")
    for i, medico in enumerate(medicos_disponibles, 1):
        console.print(f"[bold white]{i}.[/] {medico.obtener_info()}")

    seleccion = int(Prompt.ask("[bold white]Seleccione un médico (número)[/]")) - 1
    medico = medicos_disponibles[seleccion]

    fecha = Prompt.ask("[bold white]Fecha de la cita (YYYY-MM-DD)[/]")
    hora = Prompt.ask("[bold white]Hora de la cita (HH:MM)[/]")

    if hospital.agendar_cita(paciente, medico, fecha, hora):
        console.print("[bold green]Cita agendada con éxito[/]")
        notificacion = NotificacionCorreo(paciente.email, "Cita Agendada", f"Su cita con Dr. {medico.nombre} ha sido agendada para el {fecha} a las {hora}")
        notificacion.enviar_notificacion()
    else:
        console.print("[bold red]No se pudo agendar la cita[/]")

def cancelar_cita(hospital):
    console.print(Panel("Cancelar cita", style="bold white on green"))
    citas = hospital.obtener_citas()  # Suponemos que este método devuelve las citas activas
    if not citas:
        console.print("[bold red]No hay citas agendadas[/]")
        return

    for i, cita in enumerate(citas, 1):
        console.print(f"[bold white]{i}.[/] {cita}")

    seleccion = int(Prompt.ask("[bold white]Seleccione la cita a cancelar (número)[/]")) - 1
    cita = citas[seleccion]

    motivo_cancelacion = Prompt.ask("[bold white]Motivo de cancelación[/]")  # Solicitar el motivo
    if hospital.cancelar_cita(cita, motivo_cancelacion):  # Llamar al método para cancelar la cita
        console.print("[bold green]Cita cancelada con éxito[/]")
        notificacion = NotificacionSMS(cita.paciente.telefono, f"Su cita del {cita.fecha} a las {cita.hora} ha sido cancelada")
        notificacion.enviar_notificacion()
    else:
        console.print("[bold red]No se pudo cancelar la cita[/]")


def mover_cita(hospital):
    console.print(Panel("Mover cita", style="bold white on green"))
    citas = hospital.obtener_citas()
    if not citas:
        console.print("[bold red]No hay citas agendadas[/]")
        return

    for i, cita in enumerate(citas, 1):
        console.print(f"[bold white]{i}.[/] {cita}")

    seleccion = int(Prompt.ask("[bold white]Seleccione la cita a mover (número)[/]")) - 1
    cita_original = citas[seleccion]

    nueva_fecha = Prompt.ask("[bold white]Nueva fecha (YYYY-MM-DD)[/]")
    nueva_hora = Prompt.ask("[bold white]Nueva hora (HH:MM)[/]")

    if hospital.mover_cita(cita_original, nueva_fecha, nueva_hora):
        console.print("[bold green]Cita movida con éxito[/]")
        notificacion = NotificacionWhatsapp(cita_original.paciente.telefono, f"Su cita ha sido movida al {nueva_fecha} a las {nueva_hora}")
        notificacion.enviar_notificacion()
    else:
        console.print("[bold red]No se pudo mover la cita[/]")

def ver_citas(hospital):
    console.print(Panel("Citas agendadas", style="bold green on grey15"))
    citas = hospital.obtener_citas()
    if not citas:
        console.print("[bold red]No hay citas agendadas[/]")
        return

    table = Table(title="[bold yellow]Citas Agendadas[/]", header_style="bold green")
    table.add_column("[bold yellow]Paciente[/]", style="white")
    table.add_column("[bold yellow]Médico[/]", style="green")
    table.add_column("[bold yellow]Fecha[/]", style="red")
    table.add_column("[bold yellow]Hora[/]", style="red")

    for cita in citas:
        table.add_row(
            f"{cita.paciente.nombre} {cita.paciente.apellido}",
            f"Dr. {cita.medico.nombre} {cita.medico.apellido}",
            str(cita.fecha),
            str(cita.hora)
        )

    console.print(table)

def mostrar_menu_reportes():
    console.print(Panel("Menú de Reportes", style="bold cyan"))
    table = Table(show_header=False, box=None)
    table.add_row("1. Reporte de demanda de médicos")
    console.print(table)

def generar_reportes(hospital):
    while True:
        mostrar_menu_reportes()
        opcion = Prompt.ask("Seleccione una opción", choices=["1", "2"])

        if opcion == "1":
            Reporte.generar_reporte_demanda_medicos(hospital)
            
            break

        input("\nPresione Enter para continuar...")

def main():
    hospital = Hospital("Hospital Central")
    cargar_datos_iniciales(hospital)

    while True:
        mostrar_menu_principal()
        opcion = Prompt.ask("Seleccione una opción", choices=["1", "2", "3", "4", "5", "6"])

        if opcion == "1":
            agendar_cita(hospital)
        elif opcion == "2":
            cancelar_cita(hospital)
        elif opcion == "3":
            mover_cita(hospital)
        elif opcion == "4":
            ver_citas(hospital)
        elif opcion == "5":
            generar_reportes(hospital)
        elif opcion == "6":
            console.print("Gracias por usar el sistema. ¡Hasta luego!", style="bold")
            break

if __name__ == "__main__":
    main()