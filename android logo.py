import turtle as t

t.penup()
t.goto(-80,80)
t.pendown()

t.speed(0)
t.pencolor("#3DDC84")

def circle():
    t.begin_fill()
    t.fillcolor("white")
    t.circle(7)
    t.end_fill()

def android1():
    t.begin_fill()
    t.fillcolor("#3DDC84")
    t.forward(150)
    t.left(90)
    for i in range(238):
        t.left(0.76)
        t.forward(1)
    t.end_fill()

    t.penup()
    t.goto(-40, 120)
    t.pendown()
    circle()

    t.penup()
    t.goto(24, 120)
    t.pendown()
    circle()

    t.penup()
    t.goto(-34, 150)
    t.pendown()

    t.pensize(4)
    t.right(140)
    t.forward(40)

    t.penup()
    t.goto(34, 144)
    t.pendown()

    t.pensize(4)
    t.right(80)
    t.forward(46)

def android2():
    t.begin_fill()
    t.fillcolor("#3DDC84")
    t.pensize(1)
    t.right(141)
    t.forward(100)
    for i in range(20):
        t.forward(1)
        t.left(5)
    t.right(9.5)
    t.forward(127)
    for i in range(20):
        t.forward(1)
        t.left(5)
    t.right(9.5)
    t.forward(100)
    t.end_fill()

def android3():
    t.begin_fill()
    t.fillcolor("#3DDC84")
    for i in range(45):
        t.right(4)
        t.forward(1)
    t.forward(70)
    for i in range(45):
        t.right(4)
        t.forward(1)
    t.forward(70)
    t.end_fill()

def android4():
    t.begin_fill()
    t.fillcolor("#3DDC84")
    t.right(91)
    t.forward(30)
    t.right(90)
    t.forward(50)
    for i in range(45):
        t.right(4)
        t.forward(1)
    t.end_fill()


android1()

t.penup()
t.goto(-80,68)
t.pendown()

android2()

t.penup()
t.goto(80,68)
t.pendown()

android3()

t.penup()
t.goto(-124,70)
t.pendown()

android3()

t.penup()
t.goto(-50,-50)
t.pendown()

android4()

t.penup()
t.goto(14,-50)
t.pendown()
t.left(1.7)
android4()

t.hideturtle()

t.done()