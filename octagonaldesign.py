import turtle as t
t.speed(10)
t.bgcolor("black")
t.color("yellow")
t.pensize(5)
for i in range(8):
    t.left(45)
    for i in range(8):
        t.forward(100)
        t.right(45)

t.done()