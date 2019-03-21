import datetime

class Persona:
    def __init__(self, nombre, fechaNacimiento):
        self.nombre = nombre
        self.fechaNacimiento = fechaNacimiento
    def __str__(self):
        return self.nombre + " [" + self.fechaNacimiento.strftime("%d/%m/%Y") + "]"