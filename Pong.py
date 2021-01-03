#imports:
from time import sleep
import turtle
import winsound
################################################################
Window = turtle.Screen()
Window.title("Pong")
Window.bgcolor("black")
Window.setup(width=800, height=600)
Window.tracer(0)
################################################################
#Score
Score_A = 0
Score_B = 0
################################################################
#Paddle A
Paddle_A = turtle.Turtle()
Paddle_A.speed(0)
Paddle_A.shape("square")
Paddle_A.color("white")
Paddle_A.shapesize(stretch_wid= 5, stretch_len= 1)
Paddle_A.penup()
Paddle_A.goto(-350, 0)
################################################################
#Padle B
Paddle_B = turtle.Turtle()
Paddle_B.speed(0)
Paddle_B.shape("square")
Paddle_B.color("white")
Paddle_B.shapesize(stretch_wid= 5, stretch_len= 1)
Paddle_B.penup()
Paddle_B.goto(350, 0)
#################################################################
#ball
Ball = turtle.Turtle()
#Ball.speed(0)
Ball.shape("circle")
Ball.color("white")
Ball.penup()
Ball.goto(0, 0)
Ball.dy = -0.5
Ball.dx = 0.5
################################################################
#Pen
Pen = turtle.Turtle()
Pen.speed(0)
Pen.color("white")
Pen.penup()
Pen.hideturtle()
Pen.goto(0, 260)


################################################################
#functions:
#paddle A functions:
def Paddle_A_Up():
    y = Paddle_A.ycor()
    y += 20
    Paddle_A.sety(y)
def Paddle_A_Down():
    y = Paddle_A.ycor()
    y -= 20
    Paddle_A.sety(y)
#Paddle B Functions:
def Paddle_B_Up():
    y = Paddle_B.ycor()
    y += 20
    Paddle_B.sety(y)
def Paddle_B_Down():
    y = Paddle_B.ycor()
    y -= 20
    Paddle_B.sety(y)
################################################################
#keyword bimding:
Window.listen()
Window.onkeypress(Paddle_A_Up, "w")
Window.onkeypress(Paddle_A_Down, "s")
####
Window.onkeypress(Paddle_B_Up, "Up")
Window.onkeypress(Paddle_B_Down, "Down")

################################################################
#Main loop:
while True:
    Window.update()
    Pen.clear()
    Pen.write(f"Player A: {Score_A}  Player B: {Score_B}", align = "center", font =("Courier", 24) )
    #Ball Movment:
    Ball.setx(Ball.xcor() + Ball.dx )
    Ball.sety(Ball.ycor() + Ball.dy )

    #Border Setup
    if Ball.ycor() > 290:
        Ball.sety(290)
        Ball.dy *= -1
        winsound.PlaySound("pongbip.wav", winsound.SND_ASYNC)
    if Ball.ycor() < -290:
        Ball.sety(-290)
        Ball.dy *= -1
    if Ball.xcor() > 390:
        Ball.dx *= -1
        Ball.goto(0, 0)
        Score_A += 1     
        sleep(1)

    if Ball.xcor() < -390:
        Ball.dx *= -1
        Ball.goto(0, 0)
        Score_B += 1 
        sleep(1)
    #paddle and Ball Collisions
    if (Ball.xcor() > 340 and Ball.xcor() < 350 ) and (Ball.ycor() < Paddle_B.ycor() + 40 and Ball.ycor() > Paddle_B.ycor() -40):
        Ball.dx *= -1
    if (Ball.xcor() < -340 and Ball.xcor() > -350 ) and (Ball.ycor() < Paddle_A.ycor() + 40 and Ball.ycor() > Paddle_A.ycor() -40):
        Ball.dx *= -1


    