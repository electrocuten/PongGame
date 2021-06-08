from turtle import Turtle

class Pelota(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto(0,0)
        self.xmov = 10
        self.ymov = 10
        self.velocidad = 0.1

    def move(self):
        new_x = self.xcor() + self.xmov
        new_y = self.ycor() + self.ymov
        self.goto(new_x, new_y)

    # Las funciones de rebote, invierte la direccion del movimiento de x o y
    def rebote_y(self):
        self.ymov *= -1
        self.velocidad *= 0.9

    def rebote_x(self):
        self.xmov *= -1
        self.velocidad *= 0.9

    def reset_posicion(self):
        self.goto(0,0)
        self.velocidad = 0.1
        self.rebote_x()