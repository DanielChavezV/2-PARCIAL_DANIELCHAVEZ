# Mejoras Realizadas - Proyecto de Gestión de Citas Médicas

Este documento detalla las mejoras implementadas en el sistema de gestión de citas médicas. A continuación, se describen las modificaciones realizadas en las diferentes clases y características del proyecto.

## 1. Aplicación Principal (`main.py`)

Se ha ampliado significativamente la lógica de la aplicación principal para mejorar la funcionalidad y la experiencia del usuario.

* **Carga de datos iniciales**: Se han añadido funciones para cargar los datos desde archivos CSV y JSON al inicio de la aplicación.
* **Interfaz enriquecida**: Se ha implementado una interfaz de usuario basada en menús utilizando la biblioteca [Rich](https://rich.readthedocs.io/en/stable/) para mejorar la experiencia visual.
* **Operaciones principales**:
  * `agendar_cita`: Permite agendar nuevas citas médicas.
  * `cancelar_cita`: Permite cancelar una cita programada.
  * `mover_cita`: Permite reprogramar una cita existente.
  * `ver_citas`: Muestra todas las citas agendadas.
  * `generar_reporte_citas`: Permite generar un reporte de las citas programadas.

## 2. Clase Hospital (`hospital.py`)

Se han añadido nuevos métodos para gestionar los pacientes y médicos dentro del hospital.

* **Gestión de pacientes y médicos**:
  * `agregar_paciente`: Añade un paciente al sistema.
  * `agregar_medico`: Añade un médico al sistema.
* **Métodos de búsqueda**:
  * `buscar_paciente`: Permite buscar pacientes por su identificador.
  * `buscar_medico`: Permite buscar médicos por su identificador.
  * `buscar_medicos_por_especialidad`: Permite buscar médicos por especialidad médica.

## 3. Clase Agenda (`agenda.py`)

Se ha implementado el método `mover_cita` que permite la reprogramación de citas ya agendadas.

## 4. Clase Medico (`medico.py`)

Se ha agregado el método `obtener_info` para proporcionar información formateada sobre el médico.

## 5. Clase Paciente (`paciente.py`)

Se han añadido nuevos métodos para gestionar el historial médico de los pacientes.

* **Gestión del historial médico**:
  * `agregar_historial`: Permite agregar registros al historial médico de un paciente.
  * `obtener_historial`: Permite obtener el historial médico completo de un paciente.
* **Método de información**:
  * `obtener_info`: Proporciona información formateada sobre el paciente.

## 6. Nuevas Clases y Características

* **Clase Persona (**`persona.py`): Se ha añadido una clase base abstracta `Persona` que sirve como padre para las clases `Paciente` y `Medico`. Esta clase gestiona atributos comunes como nombre, identificación, etc.
* **Sistema de Notificación (**`notificacion.py`): Se ha implementado un sistema de notificaciones con opciones para enviar alertas por **email**, **SMS** y **WhatsApp**.
* **Clase PersonaFactory (**`persona_factory.py`): Se ha creado una clase `PersonaFactory` que facilita la creación de objetos de tipo `Paciente` y `Medico` de manera centralizada.
* **Clase Reporte (**`reporte.py`): Se ha añadido una clase `Reporte` para generar informes detallados de las citas médicas programadas.

## 7. Integración de Rich Library

Se ha utilizado la biblioteca [Rich](https://rich.readthedocs.io/en/stable/) para enriquecer la interfaz de usuario. Esta biblioteca permite mostrar menús, tablas y textos con formato colorido y estilizado, mejorando la experiencia interactiva.