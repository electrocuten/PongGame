from turtle import Turtle

class Marcador(Turtle):

    def __init__(self):
        super().__init__()

        self.color("white")
        self.penup()
        self.hideturtle()
        self.puntos_Der = 0
        self.puntos_Izq = 0
        self.actualizar_Marcador()

    def actualizar_Marcador(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.puntos_Izq, align="center", font=("Courier", 80, "normal"))
        self.goto(100, 200)
        self.write(self.puntos_Der, align="center", font=("Courier", 80, "normal"))

    def puntos_Izquierda(self):
        self.puntos_Izq += 1
        self.actualizar_Marcador()

    def puntos_Derecha(self):
        self.puntos_Der += 1
        self.actualizar_Marcador()

    def gameOver(self):
        self.goto(50, 100)
        self.write("GAME OVER", align="center", font=("Courier", 80, "normal"))
        if self.puntos_Izq == 5:
            self.goto(50, 50)
            self.write("El jugador de la izquierda gana", align="center", font=("Courier", 30, "normal"))
        else:
            self.goto(50, 50)
            self.write("El jugador de la derecha gana", align="center", font=("Courier", 30, "normal"))
