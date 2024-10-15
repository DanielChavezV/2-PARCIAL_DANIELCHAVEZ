# PARCIAL 2 PROGRAMACION I

## Proyecto: Sistema de Gestión de Citas Médicas

 ![Fondo](https://d2lcsjo4hzzyvz.cloudfront.net/blog/wp-content/uploads/2022/05/13100505/Por-que%CC%81-ofrecer-citas-me%CC%81dicas-virtuales-a-tus-pacientes-.jpg)

## Descripción

Este es un sistema de gestión de citas médicas que permite a los pacientes agendar, cancelar y mover citas con médicos, además de consultar el listado de citas agendadas. Los médicos pueden pertenecer a distintas especialidades, y los pacientes pueden seleccionar un médico en función de su especialidad. El sistema incluye notificaciones a través de correo electrónico, celular y WhatsApp, utilizando una interfaz de texto basada en la librería **Rich** para mejorar la experiencia de usuario.

# Requerimientos:

### Requerimientos Funcionales

#### 1. Gestión de Pacientes:

El sistema debe permitir agregar nuevos pacientes con los campos: nombre, apellido, cédula, correo y celular.
Debe ser posible buscar pacientes por su cédula.

#### 2. Gestión de Médicos:

El sistema debe permitir agregar médicos con los campos: nombre, apellido, cédula, correo, celular y especialidad.
El usuario debe poder buscar médicos por su cédula o filtrar por especialidad.

#### 3. Agendar Citas:

Los pacientes deben poder agendar una cita seleccionando la especialidad médica y luego eligiendo un médico disponible de esa especialidad.
Las citas deben tener una fecha y hora con intervalos de 20 minutos.
El sistema debe permitir ingresar el motivo de la cita.

#### 4. Cancelar Citas:

Debe ser posible cancelar una cita seleccionando la misma desde un listado de citas agendadas.

#### 5. Mover Citas:

El sistema debe permitir modificar la fecha y hora de una cita ya agendada, respetando la disponibilidad del médico.

#### 6. Ver Citas:

Los usuarios deben poder visualizar todas las citas agendadas, con la información del paciente, médico, fecha, hora y motivo.

#### 7. Notificaciones:

El sistema debe notificar a los pacientes y médicos sobre citas a través de tres medios:
Correo electrónico.
Mensaje de texto (SMS).
WhatsApp.
Las notificaciones deben ser enviadas automáticamente cuando una cita es agendada, cancelada o movida.

#### 8. Carga de Datos Iniciales:

El sistema debe poder cargar datos de pacientes desde un archivo CSV y médicos desde un archivo JSON.

### Requerimientos No Funcionales

#### 1. Interfaz de Usuario:

La interfaz de texto debe ser clara y sencilla, utilizando la librería Rich para mostrar menús, tablas y paneles interactivos.

#### 2. Persistencia de Datos:

Los datos de pacientes, médicos y citas deben ser cargados desde archivos de entrada y almacenados en memoria durante la ejecución del programa.

#### 3. Eficiencia:

El sistema debe permitir el manejo eficiente de citas y médicos, filtrando por especialidad y mostrando citas en intervalos de 20 minutos.

#### 4. Flexibilidad:

Los usuarios deben poder modificar y cancelar citas de forma sencilla, y el sistema debe ajustarse a la disponibilidad del médico al mover citas.

#### 5. Notificaciones:

El sistema debe heredar el método enviar_notificación() de una clase base para los diferentes tipos de notificación (Correo, SMS, WhatsApp).

#### 5. Soporte de Archivos:

El sistema debe ser compatible con archivos CSV para pacientes y JSON para médicos para la carga masiva de datos.

# 

# Instalación


1. Clona el Repositorio:

   Si estás utilizando Git, clona el repositorio a tu máquina local:

```bash
git clone  https://github.com/DanielChavezV/Parcial_Programacion_I.git
```


2. Crear y activar el entorno virtual:

```bash
python -m venv venv
source venv/bin/activate  # Linux/MacOS
venv\Scripts\activate  # Windows
```


3. Instalar las dependencias:

```bash
pip install -r requirements.txt
```

# Ejecución

Para ejecutar el proyecto, usa el siguiente comando:

```bash
python main.py
```

# Autor

**Daniel Steven Chavez Valdes**
**Ingeniería de Sistemas 4 Semestre**
**Universidad Libre Seccional Cali**