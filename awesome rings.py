import turtle as t

COLORS = ['black', 'magenta', 'pink', 'blue', 'green', 'yellow', 'orange', 'red']

t.width(6)
t.speed(0)

for color in COLORS:
    t.fillcolor(color)
    t.begin_fill()
    t.circle(145)
    t.circle(130, -360)
    t.circle(115)
    t.circle(100, -360)
    t.end_fill()
    t.right(45)

t.hideturtle()
t.done()