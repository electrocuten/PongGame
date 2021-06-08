from turtle import Turtle

# El cuadrado inicial tiene unas medidas de 20x20, como lo queremos de 100x20, debemos multiplicar su altura por 5 y la
# anchura por 1

ALTURA = 5
ANCHURA = 1

UP = 0
DOWN = 180

class Pala(Turtle):

    def __init__(self, posicion):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(stretch_wid=ALTURA, stretch_len=ANCHURA)
        self.color("white")
        self.goto(posicion[0],posicion[1])

    def up(self):
        y = self.ycor()
        new_y = y + 20
        self.goto(self.xcor(), new_y)

    def down(self):
        y = self.ycor()
        new_y = y - 20
        self.goto(self.xcor(), new_y)