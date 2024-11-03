"""
Esta clase hereda de reserva y de avl, contiene 2 metodos. El primero, muestra los asientos disponibles y recorre los nodos del arbol
para ello. Por otro lado, el método de resera_asientos que permitirá al usuario interactuar con los datos de los asientos disponibles
para poder reservarlos.
"""
from reserva import Reserva
from avl import ArbolAVL

def mostrar_asientos(arbol):
    asientos = []
    
    def _recorrer(nodo):
        if nodo:
            asientos.append(nodo.asiento)
            _recorrer(nodo.izq)
            _recorrer(nodo.der)
    
    _recorrer(arbol.raiz)
    for asiento in asientos:
        print(asiento)

def reservar_asiento(arbol, usuario):
    asiento = arbol.buscar_disponible()
    if asiento:
        nueva_reserva = Reserva(asiento.id, asiento, usuario)
        print(f"Reserva realizada: {nueva_reserva}")
        return nueva_reserva
    else:
        print("No hay asientos disponibles")
        return None