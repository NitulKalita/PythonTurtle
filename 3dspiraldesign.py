import turtle as t
from random import  randint

t.bgcolor("black")
t.speed(0)

x=1

while x<400:
    r=randint(0,255)
    g=randint(0,255)
    b=randint(0,255)
    t.colormode(255)
    t.pencolor(r,g,b)

    t.forward(x+5)
    t.right(90.99)
    x=x+1

t.done()