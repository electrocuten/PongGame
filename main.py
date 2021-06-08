from turtle import Screen, Turtle
from palas import Pala
from pelota import Pelota
from marcador import Marcador
import time
PO_INICIAL_DER = (350, 0)
PO_INICIAL_IZQ = (-350, 0)

pantalla = Screen()


# Configuramos la pantalla, medidas, color de fondo y titulo
pantalla.setup(width=800, height=600)
pantalla.bgcolor("black")
pantalla.title("Pong Game. Developed by Daniel R")
pantalla.tracer(0)                          # Apagamos la animacion de la pantalla


palaDer = Pala(PO_INICIAL_DER)
palaIzq = Pala(PO_INICIAL_IZQ)
pelota = Pelota()
marcador = Marcador()

pantalla.listen()
pantalla.onkey(key="Up", fun=palaDer.up)
pantalla.onkey(key="Down", fun=palaDer.down)

pantalla.onkey(key="w", fun=palaIzq.up)
pantalla.onkey(key="s", fun=palaIzq.down)



game_on = True

while game_on:
    time.sleep(pelota.velocidad)
    pantalla.update()
    pelota.move()

    # Si la pelota pasa de 280 o de -280 (limite de la pantalla superior e inferior), debe rebotar
    if pelota.ycor() > 280 or pelota.ycor() < -280:
        pelota.rebote_y()
    # Si la pelota está a menos de 60 de las palas, y en el eje de las palas, debe rebotar
    if (pelota.distance(palaDer) < 60 and pelota.xcor() > 320) or (pelota.distance(palaIzq) < 60 and pelota.xcor() < -320):
        pelota.rebote_x()

    # Si la pelota se va por la derecha
    if pelota.xcor() > 400:
        pelota.reset_posicion()
        marcador.puntos_Izquierda()
        pantalla.update()
        time.sleep(2)

    #Si la pelota se va por la izquierda
    if pelota.xcor() < -400:
        pelota.reset_posicion()
        marcador.puntos_Derecha()
        pantalla.update()
        time.sleep(2)

    if marcador.puntos_Der == 5 or marcador.puntos_Izq == 5:
        marcador.gameOver()
        game_on = False


#Cerramos con click en pantalla
pantalla.exitonclick()