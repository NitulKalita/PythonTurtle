import turtle as t

t.penup()
t.goto(0,-190)
t.pendown()
t.speed(0)

def curve1():
    for i in range(180):
        t.right(1)
        t.forward(3)

def curve2():
    for i in range(180):
        t.left(1)
        t.forward(1.2)

def curve():
    t.begin_fill()
    t.fillcolor("red")
    curve1()
    t.right(90)
    t.forward(106)
    t.right(90)
    curve2()
    t.right(90)
    t.forward(102)
    t.end_fill()

def curve3():
    t.begin_fill()
    t.fillcolor("white")
    curve1()
    t.right(90)
    t.forward(106)
    t.right(90)
    curve2()
    t.right(90)
    t.forward(102)
    t.end_fill()


t.begin_fill()
t.fillcolor("black")
t.circle(200)
t.end_fill()

t.pencolor("white")
t.penup()
t.goto(0,-40)
t.pendown()
t.begin_fill()
t.fillcolor("white")
t.circle(50)
t.end_fill()

t.pencolor("black")
t.penup()
t.goto(0,-10)
t.pendown()
t.circle(20)

t.penup()
t.goto(-170,20)
t.pendown()
t.left(90)
curve()

t.penup()
t.goto(171.2,0)
t.pendown()
t.left(90)
curve3()
t.hideturtle()

t.done()