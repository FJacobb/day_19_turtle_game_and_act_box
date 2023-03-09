import random
from turtle import Screen,Turtle
from playernames import name
from tkinter import messagebox

def players(color):
   player_name = Turtle()
   player_name.color(color)
   player_name.shape("turtle")
   player_name.penup()
   return player_name


list_color = ["red", "yellow", "blue", "orange", "green", "brown", "gray"]

race = []
screen = Screen()
screen.bgpic("image/Asset 3.png")
for x in list_color:
    race.append(players(x))
y = -90
for x in race:
    x.goto(-270,y)
    y+=30

play =True
while play:
    rr = random.choice(race)
    rr.forward(5)
    for x in race:
        if x.position() >= (237,x.ycor()):
            messagebox.showinfo("game result",f"The winner is {x.color()[0].upper()}")
            play = False

screen.exitonclick()