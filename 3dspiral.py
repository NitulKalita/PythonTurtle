import turtle
turtle = turtle.Turtle()

turtle.bgcolor("black")

turtle.speed(0)

turtle.penup()
turtle.goto(0,200)
turtle.pendown()

a=0
b=0

while True:
    turtle.forward(a)
    turtle.right(b)
    turtle.pencolor("green")
    a+=3
    b+=1
    if b == 210:
        break
turtle.hideturtle()
turtle.done