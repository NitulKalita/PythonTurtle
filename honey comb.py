import turtle as t
from random import randint
size = 20
circles = 20
t.speed(100)

t.colormode(255)

def move(length, angle):
    t.right(angle)
    t.forward(length)

def hex():
    t.pendown()
    t.color( randint(0,255),randint(0,255),randint(0,255) )
    t.begin_fill()
    for i in range(6):
        move(size,-60)
    t.end_fill()
    t.penup()
t.penup()

for circle in range (circles):
    if circle == 0:
        hex()
        move(size,-60)
        move(size,-60)
        move(size,-60)
        move(0,180)
    for i in range (6):
        move(0,60)
        for j in range (circle+1):
            hex()
            move(size,-60)
            move(size,60)
        move(-size,0)
    move(-size,60)
    move(size,-120)
    move(0,60)

turtle.exitonclick()