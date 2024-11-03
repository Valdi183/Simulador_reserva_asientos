"""
Esta es mi otra versión de simulador de reserva de asientos. Cuya mayor diferencia. es que no importa ningún modulo, si no 
que está todo completamente organizado en un solo archivo, para evitar problemas de importación.
"""

# La clase nodo inicializa los atributos de cada nodo del árbol, definiendo su valor (clave), altura, y los nodos hijos izquierdo y derecho
class NodoAVL:
    def __init__(self, clave):
        self.clave = clave
        self.altura = 1
        self.izquierdo = None
        self.derecho = None

"""
Esta clase contiene los métodos necesarios para gestionar el árbol AVL, como insertar nodos y mantener el arbol balanceado.
Con el metodo de insertar, se insertan nodos en el arbol, cuyo funcionamiento es el siguiente:
Hay dos posibilidades, el caso de que el nodo raiz este vacio (devuelve None), para lo cual se crea un nuevo nodo (haciendo
uso de la clase NodoAVL), y de lo contrario, se inserta en los subarbol izquierdo o derecho según si el valor es mayor
o menor que el valor de la raiz (raiz.clave).
Para la inserción, también utilizo (dependiendo del valor del balance) rotaciones para mantener el árbol balanceado.
Rotación a la derecha Si el árbol está inclinado hacia la izquierda, y a la izquierda si está inclinado hacia la derecha.
Encima de los metodos de rotación, explico brevemente como funcionan
"""

class ArbolAVL:
    # Inserta los nodos segun corresponda
    def insertar(self, raiz, clave):
        if not raiz:
            return NodoAVL(clave)
        elif clave < raiz.clave:
            raiz.izquierdo = self.insertar(raiz.izquierdo, clave)
        else:
            raiz.derecho = self.insertar(raiz.derecho, clave)

        raiz.altura = 1 + max(self.obtener_altura(raiz.izquierdo), self.obtener_altura(raiz.derecho))

        balance = self.obtener_balance(raiz)

        # Rotaciones para balancear el árbol
        if balance > 1:
            if clave < raiz.izquierdo.clave:
                return self.rotacion_derecha(raiz)
            else:
                raiz.izquierdo = self.rotacion_izquierda(raiz.izquierdo)
                return self.rotacion_derecha(raiz)

        if balance < -1:
            if clave > raiz.derecho.clave:
                return self.rotacion_izquierda(raiz)
            else:
                raiz.derecho = self.rotacion_derecha(raiz.derecho)
                return self.rotacion_izquierda(raiz)

        return raiz
    """
    Los metodos de rotación, se utilizan como he mencionado anteriormente, para balancear el árbol:
    Si el arbol está desbalanceado hacia la derecha la rotación ajusta el subárbol derecho "y" para 
    que el nodo "z" se convierta en su hijo izquierdo. Y posteriormente actualizar las alturas de "y" y "z"
    después de la rotación. Si el arbol esta desbalanceado hacia la izquierda hace lo mismo pero al revés
    """
    def rotacion_izquierda(self, z):
        y = z.derecho
        T2 = y.izquierdo

        y.izquierdo = z
        z.derecho = T2

        z.altura = 1 + max(self.obtener_altura(z.izquierdo), self.obtener_altura(z.derecho))
        y.altura = 1 + max(self.obtener_altura(y.izquierdo), self.obtener_altura(y.derecho))

        return y

    def rotacion_derecha(self, z):
        y = z.izquierdo
        T3 = y.derecho

        y.derecho = z
        z.izquierdo = T3

        z.altura = 1 + max(self.obtener_altura(z.izquierdo), self.obtener_altura(z.derecho))
        y.altura = 1 + max(self.obtener_altura(y.izquierdo), self.obtener_altura(y.derecho))

        return y

    # Metodo que devuelve la altura del nodo
    def obtener_altura(self, nodo):
        if not nodo:
            return 0
        return nodo.altura
    # Metodo que devuelve el balance del nodo
    def obtener_balance(self, nodo):
        if not nodo:
            return 0
        return self.obtener_altura(nodo.izquierdo) - self.obtener_altura(nodo.derecho)
    # 
    def recorrido_preorden(self, raiz):
        if not raiz:
            return
        print(raiz.clave, end=' ')
        self.recorrido_preorden(raiz.izquierdo)
        self.recorrido_preorden(raiz.derecho)

"""
La clase asiento, representa el objeto asiento, cuyos atributos son su id (para iderntificar el asiento), la zona donde se encuentra, su 
precio y si esta disponible o reservado. Además, el metodo __lt__ que define el criterio para comparar asientos (por precio en este caso)
y el metodo __rpr__ que como indican el nombre del propio metodo, es una representación en texto de un asiento, mostrando sus atributos basicos
"""

class Asiento:
    def __init__(self, id_asiento, zona, precio, disponible=True):
        self.id_asiento = id_asiento
        self.zona = zona
        self.precio = precio
        self.disponible = disponible

    def __lt__(self, otro):
        return self.precio < otro.precio  

    def __repr__(self):
        return f"Asiento(ID: {self.id_asiento}, Zona: {self.zona}, Precio: {self.precio}, Disponible: {self.disponible})"

# La clase reserva maneja la acción para que el usuario pueda reservar su asiento en función de su disponibilidad, y las preferencias del usuario
class Reserva:
    def __init__(self):
        self.asientos_reservados = []

    def reservar_asiento(self, asiento):
        if asiento.disponible:
            asiento.disponible = False
            self.asientos_reservados.append(asiento)
            print(f"Asiento {asiento.id_asiento} reservado.")
        else:
            print(f"Asiento {asiento.id_asiento} no está disponible.")

# Muestra los asientos y sus atributos, para el usuario
def mostrar_asientos(asientos):
    for asiento in asientos:
        print(asiento)


"""
Con la función main, hago un ejmplo de uso del programa, para lo que creo objetos de el arbol AVL y de reserva, además de iniciar la raíz con None,
para que el algoritmo de arbol empiece en ese punto. Después, pongo algunos asientos de ejemplo y los inserto en el arbol. (Para ver un mejor ejemplo
del funcionamiento del arbol, lo ideal sería crear muchos mas asientos, para hacer que el algoritmo "trabaje mucho mas", pero este es un simple ejemplo
de funcionamiento)  
"""
def main():
    arbol_avl = ArbolAVL()
    reserva = Reserva()
    raiz = None

    # Creo algunos asientos de ejemplo
    asientos = [
        Asiento(1, "VIP", 100),
        Asiento(2, "Regular", 50),
        Asiento(3, "Económico", 30)
    ]

    # Insertar asientos en el árbol AVL
    for asiento in asientos:
        raiz = arbol_avl.insertar(raiz, asiento)

    while True:
        print("\n1. Mostrar asientos")
        print("2. Reservar asiento")
        print("3. Salir")
        eleccion = input("Seleccione una opción: ")

        if eleccion == "1":
            mostrar_asientos(asientos)
        elif eleccion == "2":
            id_asiento = int(input("Ingrese el ID del asiento a reservar: "))
            asiento_a_reservar = next((asiento for asiento in asientos if asiento.id_asiento == id_asiento), None)
            if asiento_a_reservar:
                reserva.reservar_asiento(asiento_a_reservar)
            else:
                print("Asiento no encontrado.")
        elif eleccion == "3":
            break
        else:
            print("Opción no válida.")

# Ejecuta el codigo solo si realiza desde el archivo original, es decir, desde este archivo
if __name__ == "__main__":
    main()