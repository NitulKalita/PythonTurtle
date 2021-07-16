import turtle as t

colors = ['red', 'blue', 'indigo','green', 'yellow', 'violet', 'orange']
t.speed(0)
a = 300
for i in range(16):
    t.color(colors[i%7])
    t.begin_fill()
    for i in range(4):
        t.forward(a)
        t.right(90)
        t.forward(a)
        t.right(90)
        t.forward(a-10)
        t.right(90)
        t.forward(a)
    t.end_fill()
    a-=20
t.done()