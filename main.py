"""
En este módulo, se ejecuta el programa donde se simula la creación de un estadio teatro o cine. Para ello importo la clase de
Recinto y así poder crear el objeto correspondiente e inicializar el entorno (para este caso he creado una instancia en forma
de teatro con el numero de filas y columnas indicados). En la función main también se hace una prueba donde se reserva un asiento
a nombre de "Juan", y se muestran posteriormente los asientos, para ver como queda registrada la reserva.
"""
"""
Por problemas de importación que no consigo averigiuar, los modulos de este programa no funcionan correctamente. Por ello,
dejo aquí la idea inicial de proyecto, y a continuación, se puede ver en el archivo "simulación.py" Un sistema parecido 
que también cubre con las bases de mi proyecto, solo que he programado el algoritmo de otra forma, y sin importar modulos para
evitar este problema. En el archivo mencionado, logro hacer un simulador de reserva de asientos en salas como teatros o cines
funcional, aunque haciendo uso de otras herramientas sobre todo a la hora de elaborar el arbol AVL. Para ver su funcionamiento,
queda explicado en dicho módulo
"""

from recinto import Recinto
from interfaz_usuario import mostrar_asientos, reservar_asiento

def main():
    teatro = Recinto(nombre="Teatro Principal", tipo_recinto="Teatro", filas=5, columnas=10)

    print("Asientos disponibles:")
    mostrar_asientos(teatro.arbol_asientos)

    print("\nReservando un asiento para el usuario 'Juan'")
    reserva = reservar_asiento(teatro.arbol_asientos, usuario="Juan")

    print("\nAsientos después de la reserva:")
    mostrar_asientos(teatro.arbol_asientos)

# Ejecuta la función, solo si se hace desde este archivo, "main.py"
if __name__ == "__main__":
    main()
