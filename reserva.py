"""
Este módulo contiene la clase "Reserva" para que el usuario pueda hacer una reserva de un asiento según su preferencia.
La clase contiene el metodo constructor para poder inicializar los atributos que necesita el usuario a la hora de reservar
un asiento, además de la posibilidad de cancelar la reserva y cambiar el estado del asiento de reservado a disponible.
Por último el método __repr__ muestra los datos de la reserva.
"""
from asiento import Asiento

class Reserva:
    def __init__(self, id_reserva, asiento, usuario):
        self.id_reserva = id_reserva
        self.asiento = asiento
        self.usuario = usuario
        self.estado = "activa"
        asiento.estado = "reservado"

    def cancelar(self):
        self.estado = "cancelada"
        self.asiento.estado = "disponible"

    def __repr__(self):
        return f"Reserva {self.id_reserva} - {self.usuario} - {self.asiento}"