import turtle as tr
import tkinter as tk

########################
#   OBJECTS ON SCREEN
########################

# The main game screen
win = tr.Screen()
win.bgcolor("black")
win.setup(height=800, width=1000)
win.title("Pong")
win.tracer(0)

# left paddle 
lPaddle = tr.Turtle("square")
lPaddle.color("blue")
lPaddle.shapesize(6, 1.3)
lPaddle.speed(0)
lPaddle.penup()
lPaddle.goto(-450, 0)

# right paddle
rPaddle = tr.Turtle("square")
rPaddle.color("blue")
rPaddle.shapesize(6, 1.3)
rPaddle.speed(0)
rPaddle.penup()
rPaddle.goto(450, 0)

# ball
ball = tr.Turtle("circle")
ball.shapesize(1.2, 1.2)
ball.color("red")
ball.penup()
    


#######################
#   EVENT FUNCTIONS
#######################

def rightUp():
    rightY = rPaddle.ycor()
    if(rightY <= 350):
        rPaddle.sety(rightY+20)

def rightDown():
    rightY = rPaddle.ycor()
    if(rightY >= -350):
        rPaddle.sety(rightY-20)

def leftUp():
    leftY = lPaddle.ycor()
    if(leftY <= 350):
        lPaddle.sety(leftY+20)

def leftDown():
    leftY = lPaddle.ycor()
    if(leftY >= -350):
        lPaddle.sety(leftY-20)



#######################
# KEYBOARD INPUT
#######################

win.listen()
win.onkeypress(rightUp, "Up")
win.onkeypress(rightDown, "Down")
win.onkeypress(leftUp, "w")
win.onkeypress(leftDown, "s")


# The main game loop
while True:
    win.update()

    
