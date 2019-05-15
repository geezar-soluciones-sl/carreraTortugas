# Carrera de Tortugas para ver uso de objetos
# Obligamos a que haya 4 corredores

import turtle # Que tiene también su propio lienzo. Lo usaremos (tipo Screen)

class Circuito():
    corredores = []
#    lienzo =

    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto

# Ponemos la pantalla de módulo turtle. La hacemos privada.
        self.__screen = turtle.Screen()
    
    