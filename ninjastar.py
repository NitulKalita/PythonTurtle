import turtle as t

t.bgcolor("black")
t.speed(0)
t.pensize(2)
colors = ['yellow','red', 'green', 'blue', 'orange', 'violet', 'green']

distance = 170

for color in colors:
    t.color(color)
    for j in range(8):
        t.left(45)
        for i in range(2):
            t.forward(distance)
            t.left(60)
            t.forward(distance)
            t.left(120)
    distance = distance - 20

t.hideturtle()
t.done()