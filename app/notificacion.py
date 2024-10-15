from abc import ABC, abstractmethod

class Notificacion(ABC):
    @abstractmethod
    def enviar_notificacion(self):
        pass

class NotificacionCorreo(Notificacion):
    def __init__(self, destinatario, asunto, mensaje):
        self.destinatario = destinatario
        self.asunto = asunto
        self.mensaje = mensaje
    
    def enviar_notificacion(self):
        print(f"Enviando correo a {self.destinatario}")
        print(f"Asunto: {self.asunto}")
        print(f"Mensaje: {self.mensaje}")

class NotificacionSMS(Notificacion):
    def __init__(self, numero, mensaje):
        self.numero = numero
        self.mensaje = mensaje
    
    def enviar_notificacion(self):
        print(f"Enviando SMS al número {self.numero}")
        print(f"Mensaje: {self.mensaje}")

class NotificacionWhatsapp(Notificacion):
    def __init__(self, numero, mensaje):
        self.numero = numero
        self.mensaje = mensaje
    
    def enviar_notificacion(self):
        print(f"Enviando WhatsApp al número {self.numero}")
        print(f"Mensaje: {self.mensaje}")
