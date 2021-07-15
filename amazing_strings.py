import turtle as t

t.bgcolor("black")
t.speed(0)
t.pensize(2)

colors = ['red', 'orange', 'green', 'indigo', 'blue', 'yellow']

a=0

for i in range(36):
    t.color(colors[i%6])
    for i in range(6):
        t.circle(10,180)
        t.left(180)
        t.circle(10,-180)
        t.left(180)
    t.penup()
    t.setpos(0,0)
    t.pendown()
    a+=10
    t.seth(a)
t.done()