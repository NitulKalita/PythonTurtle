import turtle

turtle.bgcolor("black")
colors=['violet', '#4b0082', 'green', 'blue', 'yellow', 'orange', 'red']
turtle.speed(0)

for i in range(280):
    turtle.pencolor(colors[i%7])
    turtle.pensize(2)
    turtle.forward(i)
    turtle.left(59)

turtle.done()

