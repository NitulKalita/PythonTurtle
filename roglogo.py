import turtle as t

t.speed(0)

def curve1():
    t.begin_fill()
    t.fillcolor("red")
    t.right(50)
    t.forward(100)
    t.right(150)
    for i in range(30):
        t.forward(2)
        t.right(1)
    t.end_fill()

def curve2():
    t.begin_fill()
    t.fillcolor("red")
    for i in range(20):
        t.right(1)
        t.forward(3)
    t.right(130)
    t.forward(50)
    t.left(80)
    for i in range(200):
        t.forward(1)
        t.right(0.1)
    t.right(20)
    for i in range(150):
        t.forward(1)
        t.right(0.1)
    t.right(164)
    for i in range(350):
        t.forward(1)
        t.left(0.1)
    t.left(80)
    t.forward(50)
    t.end_fill()

def curve3():
    t.begin_fill()
    t.fillcolor("red")
    t.left(80)
    t.forward(230)
    t.right(150)
    for i in range(200):
        t.forward(1)
        t.right(0.1)
    t.right(30)
    for i in range(170):
        t.forward(1)
        t.right(0.2)
    t.right(120)
    for i in range(164):
        t.forward(2)
        t.right(0.1)
    t.right(90)
    t.forward(14)
    t.right(90)
    for i in range(150):
        t.forward(2)
        t.left(0.1)
    t.left(134)
    for i in range(130):
        t.forward(1)
        t.left(0.1)
    t.left(50)
    for i in range(90):
        t.forward(1)
        t.left(0.1)
    t.left(140)
    t.forward(50)
    t.end_fill()
    t.hideturtle()

t.penup()
t.goto(-200,0)
t.pendown()
curve1()

t.penup()
t.goto(-140,-55)
t.pendown()
t.right(5)
curve2()

t.penup()
t.goto(0,-20)
t.pendown()
curve3()


t.done()