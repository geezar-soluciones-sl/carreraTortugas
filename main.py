# Carrera de Tortugas para ver uso de objetos
# Obligamos a que haya 4 corredores

import turtle # Que tiene también su propio lienzo. Lo usaremos (tipo Screen)

class Circuito():
    corredores = []

    def __init__(self, ancho, alto):
        self.__screen = turtle.Screen()
# Ponemos la pantalla de módulo turtle. La hacemos privada.
# o se podrían cambiar cosas a mitad de partida desde cualquier sitio fácilmente
# En Python siempre se puede con miCirc._Circuito__screen
        self.__screen.setup(ancho,alto)
        self.__screen.bgcolor("lightgray")
        
        for i in range(4):
            newTurtle = turtle.Turtle()
            self.corredores.append(newTurtle)


# Ejecutamos algo en __main__ para ver cómo va

if __name__ == "__main__":
    circuito=Circuito(680,480)
    

        
    
    