
###################
# IMPORTED MODULES
###################

import turtle as tr
import tkinter as tk
import time
import random as r



######################
# IMPORTANT VARIABLES
######################


pause = 0



############################
#   START MENU FOR THE GAME
############################

start_screen = tk.Tk(className=" PONG MENU")
# start_screen.title("PONG MENU ;)")
start_screen.configure(bg="grey")
start_screen.geometry("600x400")
start_screen.minsize(600, 400)
start_screen.maxsize(600, 400)

head = tk.Label(start_screen, text = "PONG MENU", bg="grey", pady=50) 
head.config(font =("Courier", 35)) 
head.pack()



button1 = tk.Button(start_screen, text='Play', width=40, height=2, bg='white', fg='#000000', activebackground='#66ff66', font=("",10, "italic bold underline"))
button1.pack()

button2 = tk.Button(start_screen, text='Difficulty', width=40, height=2, bg='white', fg='#000000', activebackground='#ff9933', font=("",10, "italic bold underline"))
button2.pack(pady=10)

button3 = tk.Button(start_screen, text='Exit', width=40, height=2, bg='white', fg='#000000', activebackground='#ff355e', font=("",10, "italic bold underline"))
button3.pack()

foot = tk.Label(start_screen, text = "Made by~ Muteen, Aarush & Arjun", bg='grey', font=("",9,'underline'))
foot.pack(side="bottom", anchor='e')

start_screen.mainloop()


########################
#   OBJECTS ON SCREEN
########################

# The main game screen
win = tr.Screen()
win.bgcolor("black")
win.setup(height=1000, width=1200)
win.title("PONG")
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
# PLAYERS INFO
####################

player1 = tr.Turtle()
player1.hideturtle()
player1.color("white")
player1.penup()
player1.goto(-450, 410)
player1.write("Player1: 0", font=("Arial", 20, "italic"))
player1_score = 0

player2 = tr.Turtle()
player2.hideturtle()
player2.color("white")
player2.penup()
player2.goto(50, 410)
player2.write("Player2: 0", font=("Arial", 20, "italic"))
player2_score = 0


#####################
# CREDITS
#####################

credit = tr.Turtle()
credit.hideturtle()
credit.color("white")
credit.penup()
credit.goto(0, -450)
credit.write("MADE BY~ MUTEEN, AARUSH, ARJUN", font=("Arial", 20, "italic"))


#####################
# PAUSE SCREEN
#####################

pause_txt = tr.Turtle()
pause_txt.hideturtle()
pause_txt.color("white")
pause_txt.penup()
pause_txt.goto(-168, -50)

####################
#   Components
####################

# ball
ball = tr.Turtle("circle")
ball.shapesize(1.2, 1.2)
ball_colour = ["#8a2be2", "#9955ee", "cyan", "#66ff66", "#ffff66", "#ff9933", "#ff355e", "#7cfc00", "#ff3399" , "#50bfe6", "#c8c8cd"]
prevColor = r.choice(ball_colour)
ball.color(prevColor)
ball.speed(1)
ball.penup()
speed_lst = [0.1, -0.1]
ballx = r.choice(speed_lst)
bally = r.choice(speed_lst)
# ball.goto(474, 0)

# left paddle
lPaddle = tr.Turtle("square")
lPaddle.color("#50bfe6")
lPaddle.shapesize(6, 0.3)
lPaddle.speed(0)
lPaddle.penup()
lPaddle.goto(-450, 0)

# right paddle
rPaddle = tr.Turtle("square")
rPaddle.color("#50bfe6")
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


# Ball colour change on bouncing
def colorChange():
    global ball_colour
    global prevColor
    clr = r.choice(ball_colour)
    while clr == prevColor:
        clr = r.choice(ball_colour)
    ball.color(clr)
    return clr

# Bounce ball on X-axis
def bounceX():
    global ballx
    ball.shapesize(0.8, 1.2)
    cColor = colorChange()
    credit.undo()
    credit.color(cColor)
    credit.write("MADE BY~ MUTEEN, AARUSH, ARJUN", font=("Arial", 20, "italic"))
    ballx *= -1
    ball.shapesize(1.2, 1.2)

    return cColor


# Bounce ball on Y-axis
def bounceY():
    global bally
    ball.shapesize(1.2, 0.8)
    cColor = colorChange()
    credit.undo()
    credit.color(cColor)
    credit.write("MADE BY~ MUTEEN, AARUSH, ARJUN", font=("Arial", 20, "italic"))
    bally *= -1
    ball.shapesize(1.2, 1.2)
    return cColor


# Game Pause
def pauseGame():
    global pause
   
    if pause == 1:
        pause -= 1
        pause_txt.undo()
    elif pause == 0:
        pause += 1
        pause_txt.write("PAUSED", font=("Arial", 60, "bold"))



#######################
# KEYBOARD INPUT
#######################

win.listen()
win.onkeypress(rightUp, "Up")
win.onkeypress(rightDown, "Down")
win.onkeypress(leftUp, "w")
win.onkeypress(leftDown, "s")
win.onkeypress(pauseGame, "p")



#####################
# The main game loop
#####################

while player1_score < 6 and player2_score < 6:

    # to update the screen
    win.update()

    # To Pause the main game loop
    if pause == 1:
        continue

    # Border Collisions
    ###################

    # Border Collision for top
    if ball.ycor() > 388:
        ball.sety(388)
        nColor = bounceY()
        prevColor = nColor

    # Border Collision for bottom
    if ball.ycor() < -388:
        ball.sety(-388)
        nColor = bounceY()
        prevColor = nColor

    # Border Collision for right
    if ball.xcor() > 485:
        ball.goto(0, 0)
        player1_score += 1
        player1.undo()
        player1.write("Player1: {0}".format(player1_score), font=("Arial", 20, "italic"))
        time.sleep(1)
        ballx = r.choice(speed_lst)
        bally = r.choice(speed_lst)

        

    # Border Collision for left
    if ball.xcor() < -485:
        ball.goto(0, 0)
        player2_score += 1
        player2.undo()
        player2.write("Player2: {0}".format(player2_score), font=("Arial", 20, "italic"))
        time.sleep(1)
        ballx = r.choice(speed_lst)
        bally = r.choice(speed_lst)
        


    # Paddle Collisions
    ###################

    # Paddle Collision for right paddle
    if ((ball.xcor() >= 438 and ball.xcor()<=439) and (ball.ycor() <= rPaddle.ycor()+75 and ball.ycor() >= rPaddle.ycor()-75)):
        nColor = bounceX()
        rPaddle.color(prevColor)
        player2.undo()
        player2.color(prevColor)
        player2.write("Player2: {0}".format(player2_score), font=("Arial", 20, "italic"))
        prevColor = nColor
        
        

    # Paddle Collision for left paddle
    if (ball.xcor() <= -438 and ball.xcor()>=-439) and (ball.ycor() <= lPaddle.ycor()+75 and ball.ycor() >= lPaddle.ycor()-75):
        nColor = bounceX()
        lPaddle.color(prevColor)
        player1.undo()
        player1.color(prevColor)
        player1.write("Player1: {0}".format(player1_score), font=("Arial", 20, "italic"))
        prevColor = nColor
        
        



    # Ball Movement
    ################

    # Ball movement X-axis
    ball.setx(ball.xcor() + ballx)

    # Ball movement Y-axis
    ball.sety(ball.ycor() + bally)


end_screen = tk.Tk()
end_screen.title("GAME OVER!!!")
end_screen.configure(bg="grey")
end_screen.geometry("600x400")
end_screen.minsize(600, 400)
end_screen.maxsize(600, 400)
end_screen.mainloop()
