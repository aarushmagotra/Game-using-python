###################
# IMPORTED MODULES
###################

import turtle as tr
import random as r


########################
#   OBJECTS ON SCREEN
########################

# The main game screen
win = tr.Screen()
win.bgcolor("black")
win.setup(height=800, width=1000)
win.title("Pong")
win.tracer(0)

# For Full Screen
box = tr.Turtle("classic")
box.hideturtle()
box.color("white")
box.penup()
box.goto(-500, -400)
box.pendown()
box.goto(500, -400)
box.goto(500, 400)
box.goto(-500, 400)
box.goto(-500, -400)


# left paddle
lPaddle = tr.Turtle("square")
lPaddle.color("blue")
lPaddle.shapesize(6, 1)
lPaddle.speed(0)
lPaddle.penup()
lPaddle.goto(-450, 0)

# right paddle
rPaddle = tr.Turtle("square")
rPaddle.color("blue")
rPaddle.shapesize(6, 1)
rPaddle.speed(0)
rPaddle.penup()
rPaddle.goto(450, 0)

# ball
ball = tr.Turtle("circle")
ball.shapesize(1.2, 1.2)
ball.color("red")
ball.speed(1)
ball.penup()
ball_dir = r.choice([-150, -60, -45, -30, 30, 45, 60, 150])
ballx = r.choice([0.5, -0.5])
bally = r.choice([0.5, -0.5])
# ball.setx(-428)
# ball.sety(0)
# ball.left(ball_dir)


#######################
#   EVENT FUNCTIONS
#######################

def rightUp():
    rightY = rPaddle.ycor()
    if(rightY <= 328):
        rPaddle.sety(rightY+30)


def rightDown():
    rightY = rPaddle.ycor()
    if(rightY >= -328):
        rPaddle.sety(rightY-30)


def leftUp():
    leftY = lPaddle.ycor()
    if(leftY <= 328):
        lPaddle.sety(leftY+30)


def leftDown():
    leftY = lPaddle.ycor()
    if(leftY >= -328):
        lPaddle.sety(leftY-30)


def bounceX():
    global ballx
    ball.shapesize(0.8, 1.2)
    ballx *= -1
    ball.shapesize(1.2, 1.2)


def bounceY():
    global bally
    ball.shapesize(1.2, 0.8)
    bally *= -1
    ball.shapesize(1.2, 1.2)


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

    # Border Collision
    if ball.ycor() > 388:
        ball.sety(388)
        bounceY()

    if ball.ycor() < -388:
        ball.sety(-388)
        bounceY()

    # if ball.xcor() < 485:
    #     # ball.goto(0, 0)
    #     bounceX()

    # if ball.xcor() < -485:
    #     # ball.goto(0, 0)
    #     bounceX()

    # Paddle Collisions
    if (ball.xcor() > 428 and (ball.ycor() < rPaddle.ycor()+65 and ball.ycor() > rPaddle.ycor()-65)):
        bounceX()

    if ball.xcor() < -428 and (ball.ycor() < lPaddle.ycor()+65 and ball.ycor() > lPaddle.ycor()-65):
        bounceX()

    # Ball Movement
    ball.setx(ball.xcor() + ballx)
    ball.sety(ball.ycor() + bally)
