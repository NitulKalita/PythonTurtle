import turtle as t
t.bgcolor('black')
t.speed(60)
t.pensize(1)
colors = ('magenta')
for i in range (200):
    t.forward(i*4)
    t.right(91)
    t.color(colors)
    for x in range (3):
        t.forward(x*4)
        t.right(91)
        for a in range (2):
            t.forward(a*4)
            t.right(91)
            for m in range (739):
                t.forward(m*4)
                t.right(891)