###################
# IMPORTED MODULES
###################

import turtle as tr
import time
import random as r



########################
#   OBJECTS ON SCREEN
########################

# The main game screen
win = tr.Screen()
win.bgcolor("black")
win.setup(height=1000, width=1200)
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



#################
# Designs
#################

#center line
cLine = tr.Turtle("square")
cLine.hideturtle()
cLine.color("white")
cLine.penup()
cLine.goto(0, -400)
cLine.pendown()
cLine.goto(0, 400)


#center circle
cCircle = tr.Turtle()
cCircle.hideturtle()
cCircle.color("white")
cCircle.penup()
cCircle.goto(0, -100)
cCircle.pendown()
cCircle.circle(100)



####################
#   Components
####################

# ball
ball = tr.Turtle("circle")
ball.shapesize(1.2, 1.2)
ball.color("red")
ball.speed(1)
ball.penup()
speed_lst = [0.1, -0.1]
ballx = r.choice(speed_lst)
bally = r.choice(speed_lst)
# ball.goto(474, 0)

# left paddle
lPaddle = tr.Turtle("square")
lPaddle.color("blue")
lPaddle.shapesize(6, 0.3)
lPaddle.speed(0)
lPaddle.penup()
lPaddle.goto(-450, 0)

# right paddle
rPaddle = tr.Turtle("square")
rPaddle.color("blue")
rPaddle.shapesize(6, 0.3)
rPaddle.speed(0)
rPaddle.penup()
rPaddle.goto(450, 0)



#######################
#   EVENT FUNCTIONS
#######################

# Right paddle movement up
def rightUp():
    rightY = rPaddle.ycor()
    if(rightY <= 328):
        rPaddle.sety(rightY+30)


# Right paddle movement down
def rightDown():
    rightY = rPaddle.ycor()
    if(rightY >= -328):
        rPaddle.sety(rightY-30)


# Left paddle movement up
def leftUp():
    leftY = lPaddle.ycor()
    if(leftY <= 328):
        lPaddle.sety(leftY+30)


# Left paddle movement down
def leftDown():
    leftY = lPaddle.ycor()
    if(leftY >= -328):
        lPaddle.sety(leftY-30)


# Bounce ball on X-axis
def bounceX():
    global ballx
    ball.shapesize(0.8, 1.2)
    ballx *= -1
    ball.shapesize(1.2, 1.2)


# Bounce ball on Y-axis
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



#####################
# The main game loop
#####################

while True:
    win.update()



    # Border Collisions
    ###################

    # Border Collision for top
    if ball.ycor() > 388:
        ball.sety(388)
        bounceY()

    # Border Collision for bottom
    if ball.ycor() < -388:
        ball.sety(-388)
        bounceY()

    # Border Collision for right
    if ball.xcor() > 485:
        ball.goto(0, 0)
        time.sleep(1)
        ballx = r.choice(speed_lst)
        bally = r.choice(speed_lst)

    # Border Collision for left
    if ball.xcor() < -485:
        ball.goto(0, 0)
        time.sleep(1)
        ballx = r.choice(speed_lst)
        bally = r.choice(speed_lst)



    # Paddle Collisions
    ###################

    # Paddle Collision for right paddle
    if ((ball.xcor() >= 438 and ball.xcor()<=439) and (ball.ycor() <= rPaddle.ycor()+75 and ball.ycor() >= rPaddle.ycor()-75)):
        bounceX()

    # Paddle Collision for left paddle
    if (ball.xcor() <= -438 and ball.xcor()>=-439) and (ball.ycor() <= lPaddle.ycor()+75 and ball.ycor() >= lPaddle.ycor()-75):
        bounceX()



    # Ball Movement
    ################

    # Ball movement X-axis
    ball.setx(ball.xcor() + ballx)

    # Ball movement Y-axis
    ball.sety(ball.ycor() + bally)
