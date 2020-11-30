import turtle as tr
import tkinter as tk

while True:
    win = tr.Screen()
    win.bgcolor("light green")
    win.title("Pong")

    ball = tr.Turtle("circle", 20, True)
    ball.color("red")
    
