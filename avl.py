"""
Este módulo contiene la implementación del árbol AVL, un algoritmo de "árbol" binario balanceado. Por un lado, 
la clase NodoAVL representa un nodo en el árbol, que almacena un objeto asiento, junto con su altura y apunta a 
sus nodos hijo izquierdo y derecho.
Por otro lado, la clase ArbolAVL gestiona la estructura del árbol cuyo constructor inicializa la raíz con None. 
El método insertar permite agregar nuevos asientos al árbol, utilizando una función interna "_insertar". Esta función
coloca el nuevo nodo en la posición correcta según el id del asiento (asiento.id), de forma que el árbol mantenga su orden.
Después de insertar un nuevo nodo, se actualiza la altura del nodo y se llama al método "_balancear" para verificar y corregir 
el balance del árbol. El balance se calcula como la diferencia entre las alturas de los subárboles izquierdo y derecho. 
Si el balance es mayor que 1 o menor que -1, se realizan rotaciones hacia la izquierda o derecha para restaurar el equilibrio del árbol, 
para que la búsqueda, inserción y eliminación de nodos sigan siendo eficientes. Por último, el método "buscar_disponible" permite buscar 
un asiento que esté disponible en el árbol, recorriendo los nodos en un orden determinado y devolviendo el primer asiento que encuentre 
en estado "disponible". Como conclusión, este módulo contiene el algoritmo de busqueda binaria, ideal para mi proyecto ya que
gracias al algoritmo, puedo gestionar un sistema perfecto para reservar asientos, y poder clasificarlos en función de su posición
en la sala. sobre todo, para poder buscar asientos en función de su disponibilidad con una buena eficiencia a nivel de optimizción de
espacio y de recursos
"""
class NodoAVL:
    def __init__(self, asiento):
        self.asiento = asiento
        self.altura = 1 
        self.izq = None 
        self.der = None

class ArbolAVL:
    def __init__(self):
        self.raiz = None

    def insertar(self, asiento):
        def _insertar(nodo, asiento):
            if not nodo:
                return NodoAVL(asiento)
            if asiento.id < nodo.asiento.id:
                nodo.izq = _insertar(nodo.izq, asiento)
            else:
                nodo.der = _insertar(nodo.der, asiento)

            nodo.altura = 1 + max(self._altura(nodo.izq), self._altura(nodo.der))
            return self._balancear(nodo)

        self.raiz = _insertar(self.raiz, asiento)

    def _altura(self, nodo):
        return nodo.altura if nodo else 0

    def _balancear(self, nodo):
        balance = self._altura(nodo.izq) - self._altura(nodo.der)
        if balance > 1:
            if self._altura(nodo.izq.izq) >= self._altura(nodo.izq.der):
                return self._rotar_derecha(nodo)
            else:
                nodo.izq = self._rotar_izquierda(nodo.izq)
                return self._rotar_derecha(nodo)
        if balance < -1:
            if self._altura(nodo.der.der) >= self._altura(nodo.der.izq):
                return self._rotar_izquierda(nodo)
            else:
                nodo.der = self._rotar_derecha(nodo.der)
                return self._rotar_izquierda(nodo)
        return nodo

    def _rotar_derecha(self, y):
        x = y.izq
        T2 = x.der
        x.der = y
        y.izq = T2
        y.altura = 1 + max(self._altura(y.izq), self._altura(y.der))
        x.altura = 1 + max(self._altura(x.izq), self._altura(x.der))
        return x

    def _rotar_izquierda(self, x):
        y = x.der
        T2 = y.izq
        y.izq = x
        x.der = T2
        x.altura = 1 + max(self._altura(x.izq), self._altura(x.der))
        y.altura = 1 + max(self._altura(y.izq), self._altura(y.der))
        return y

    def buscar_disponible(self):
        def _buscar(nodo):
            if not nodo:
                return None
            if nodo.asiento.estado == "disponible":
                return nodo.asiento
            izquierda = _buscar(nodo.izq)
            return izquierda if izquierda else _buscar(nodo.der)
        
        return _buscar(self.raiz)