from tkinter import *
import random
from tkinter import messagebox

window = Tk()
window.title("pingpong game")
window.geometry("800x600")
canvas = Canvas(window,width=800,height=600)
canvas.config(bg="black")
canvas.pack()

player1_score = 0
player2_score = 0
score = canvas.create_text(401,20,text= f"{player1_score} {player2_score}",font=("Aerial",20),fill="white")
canvas.create_line(400,0,400,600,fill="white")
window.update()

class Paddle1:
    def __init__(self,canvas,color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0,200,20,300,fill="white")

class Paddle2:
    def __init__(self,canvas,color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(780,200,820,300,fill="white")



player1 = Paddle1(canvas,"white")
player2 = Paddle2(canvas,"white")
        

window.mainloop()
