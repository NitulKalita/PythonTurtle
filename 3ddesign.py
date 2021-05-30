import turtle as t

t.bgcolor("black")
colors = ['red','purple','blue','green']
t.speed(0)

x=30
y=0

while True:
    t.circle(x)
    t.pencolor(colors[y % 4])
    t.forward(x)
    t.right(90)

    x+=1
    y+=1

    if y == 100:
        break
t.done()