import turtle
turtle.bgcolor('black')
turtle.speed(60)
turtle.pensize(1)
colors = ('blue','red')
for i in range (200):
    turtle.forward(i*4)
    turtle.right(91)
    turtle.color(colors[i%5])
    for x in range (3):
        turtle.forward(x*4)
        turtle.right(91)
        for a in range (2):
            turtle.forward(a*4)
            turtle.right(91)
            for m in range (739):
                turtle.forward(m*4)
                turtle.right(899)