# SIMULADOR DE RESERVA DE ASIENTOS:
Este Repositorio contiene la primera entrega de Estructura de datos y algorítmos II.
Para la entrega voy realizar un simulador de reserva de asientos que sirva para teatros, cines y estadios. A continuación procedo a explicar resumidamente cual es el objetivo del proyecto, 
herramientas a utilizar y posibles retos que abordar.

### Objetivo del programa:
El objetivo del programa es simular un sistema de reserva de asientos para teatros, cines y estadios. Además, el programa permitirá a los usuarios seleccionar los asientos disponibles
en función de criterios como la mejor vista, zona VIP o proximidad a la salida.

### Organización de código:
El codigo estará organizado en distintos módulos, de forma que se puedan programar de forma indpendiente distintas partes y así probar mejor su funcionamiento individualmente.
Para ello destinaré un módulo a la estructura de datos (en donde programaré el árbol AVL), un módulo para crear objetos con los distintos tipos de asientos, un módulo de reservas,
otro módulo para la interacción de los usuarios con el sistema y ,por último, un módulo para gestionar el teatro, cine o estadio.

### Gestión de cada módulo:
Implementaré el árbol AVL desde cero o quizá importe un módulo de estructuras de datos balanceadas como base. Adaptaré las funciones de inserción y eliminación para que respeten 
los atributos de los asientos, de forma que el árbol según los criterios seleccionados.
Definiré una clase "Asiento" que contendrá los atributos necesarios para crearlos según los criterios.
Utilizaré el sistema AVL creado para buscar asientos disponibles y que cumplan con los requisitos del usuario.
Optaré por la consola de vs code como interfaz que permita al usuario interactuar con el sistema mediante comandos.
Crearé una estructura que represente la disposición física del recinto, inicializando asientos y asignándolos al árbol AVL en función de sus atributos.

### Retos a enfrentar:
Crear de 0 un  algorítmo AVL para ordenar según múltiples criterios podría resultar bastante complejo. Además, su optimización para evitar una gran cantidad
de gasto de espacio y tiempo, podría resultar también en algo realmente difícil de manejar

### Librerías y lenguaje:
Para realizar este proyecto utilizaré como lenguaje python fundamentalmente debido a que es el con el que más he estado trabajando.
Valoraré el uso de la librería pygame, para una mejor interfaz gráfica, así como el uso de NumPy para un manejo de gran cantidad de datos.

## Link del repositorio: [Simulador de reserva de asientos](
