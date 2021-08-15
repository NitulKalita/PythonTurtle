import turtle as t

t.speed(10)
t.bgcolor("black")
colors = ("cyan", "blue", "yellow", "green")
c=0
for i in range(110):
    t.pensize(2)
    t.forward(i*5)
    t.right(144)
    t.color(colors[c])
    if c==3:
       c=0
    else:
       c+=1
t.done()