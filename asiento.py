"""
Este módulo se encarga de crear el objeto de asiento, para lo cual creo la clase "Asiento" con un constructorpara inicializar
los atributos del objeto asiento, tales como un id, si es vip, o la cercania a la salida para identificarlo, asi como su
disponibilidad. Por último he creado el método __repr__ para mostrar algunos de los atributos, aquellos necesarios para
que el usuario pueda reservarlo según su preferencia.
"""
from avl import ArbolAVL
class Asiento:
    def __init__(self, id, zona, fila, numero, VIP=False, vista=0, distancia_salida=0, estado="disponible"):
        self.id = id
        self.zona = zona
        self.fila = fila
        self.numero = numero
        self.VIP = VIP
        self.vista = vista
        self.distancia_salida = distancia_salida
        self.estado = estado  # Inicialización con valor del argumento

    def __repr__(self):
        return f"Asiento {self.id} - {self.zona} - {self.estado} (VIP: {self.VIP})"