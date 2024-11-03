"""
Este módulo hereda de los modulos asiento y avl. En recinto, se define una clase para poder contruir el obhjeto que representa el recinto,
ya sea estadio, teatro, cine... En el, se inicializan los atributos del recinto, como el nombre, el tipo de recinto (para diferenciar un
tetaro de un cine por ejemplo) además de la construcción de los asientos en función de
"""
from asiento import Asiento
from avl import ArbolAVL

class Recinto:
    def __init__(self, nombre, tipo_recinto, filas, columnas):
        self.nombre = nombre
        self.tipo_recinto = tipo_recinto
        self.filas = filas
        self.columnas = columnas
        self.asientos = self.generar_asientos()
        self.arbol_asientos = ArbolAVL()
        for asiento in self.asientos:
            self.arbol_asientos.insertar(asiento)

    def generar_asientos(self):
        asientos = []
        id_counter = 1
        for fila in range(self.filas):
            for numero in range(self.columnas):
                zona = "VIP" if fila < 2 else "General"
                vista = 10 - fila
                asiento = Asiento(id=id_counter, zona=zona, fila=fila, numero=numero, VIP=(zona == "VIP"), vista=vista)
                asientos.append(asiento)
                id_counter += 1
        return asientos