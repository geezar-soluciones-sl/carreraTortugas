# Carrera de Tortugas para ver uso de objetos
# Obligamos a que haya 4 corredores

import turtle # Que tiene también su propio lienzo. Lo usaremos (tipo Screen)
import random

class Circuito():
    corredores = []
    posStartY = (-30,-10,10,30)
    coloresT = ("red", "blue", "green", "orange")

    def __init__(self, ancho, alto):
        self.__screen = turtle.Screen()
# Ponemos la pantalla de módulo turtle. La hacemos privada.
# o se podrían cambiar cosas a mitad de partida desde cualquier sitio fácilmente
# En Python siempre se puede con miCirc._Circuito__screen
        self.__screen.setup(ancho,alto)
        self.__screen.bgcolor("lightgray")
        self.__lineaSalida = 20-ancho/2
        self.__lineaLlegada = ancho/2 -20
        
        self.__crearCorredores()
    
    def __crearCorredores(self):
        for i in range(4):
            newTurtle = turtle.Turtle()
            newTurtle.shape("turtle")
            newTurtle.penup() #"Levanta el boli" para que no se vean las lineas
            newTurtle.setpos(self.__lineaSalida, self.posStartY[i])
            newTurtle.color(self.coloresT[i])
            
            self.corredores.append(newTurtle)
            
    def competir(self):
        
        hayGanador = False
        while not hayGanador:
            for tortuga in self.corredores:
                avance = random.randint(1,6)
                tortuga.forward(avance)
                if tortuga.position()[0] >= self.__lineaLlegada:
                    hayGanador=True
                    print("La tortuga de color {} ha ganado".format(tortuga.color()[0]))

# Ejecutamos algo en __main__ para ver cómo va

if __name__ == "__main__":
    circuito=Circuito(640,480)
    circuito.competir()
    

        
    
    