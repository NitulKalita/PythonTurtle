import turtle as t

l = 200

def triangle():
    for i in range(3):
       t.forward(l)
       t.right(120)

def triangle2(l):
    for i in range(3):
       t.forward(l)
       t.right(120)

def polygon(l, n):
   angle = 360 / n
   for i in range(n):
       t.forward(l)
       t.right(angle)

def five_star(l):
    for i in range(5):
       t.forward(l)
       t.right(144)
def circle():
    for i in range(36):
       t.forward(10)
       t.right(15)

def square(x, y, l):
   t.penup()
   t.goto(x, y)
   t.pendown()
   for i in range(4):
       t.forward(l)
       t.right(90)
def setpen(x, y):
   t.penup()
   t.goto(x, y)
   t.pendown()
   t.setheading(0)

def square(x, y, l):
   setpen(x, y)
   for i in range(4):
       t.forward(l)
       t.right(90)

def square_line(x, y, l, n, dis):
    for i in range(n):
       inner_x = x + (l + dis) * i
       square(inner_x, y, l)

def square_matrix(x, y, l, n, dis, m):
    for i in range(m):
       inner_y = y - (l + dis) * i
       square_line(x, inner_y, l, n, dis)

def five_star(l):
   t.fillcolor('yellow')
   t.begin_fill()
   for i in range(5):
       t.forward(l)
       t.right(144)
   t.end_fill()
colors = ['red', 'yellow', 'darkblue', 'green']

def circle(x, y, r, color):
   n = 36
   angle = 360 / n
   pi = 3.1415926
   c = 2 * pi * r
   l = c / n
   start_x = x - l / 2
   start_y = y + r
   setpen(start_x, start_y)
   t.pencolor(color)
   t.fillcolor(color)
   t.begin_fill()

   for i in range(n):
       t.forward(l)
       t.right(angle)
   t.end_fill()

def five_star(l):
   setpen(0, 0)
   t.setheading(162)
   t.forward(150)
   t.setheading(0)
   t.fillcolor('WhiteSmoke')
   t.begin_fill()
   t.hideturtle()
   t.penup()

   for i in range(5):
       t.forward(l)
       t.right(144)
   t.end_fill()

def sheild():
   circle(0, 0, 300, 'red')
   circle(0, 0, 250, 'white')
   circle(0, 0, 200, 'red')
   circle(0, 0, 150, 'darkblue')
   five_star(284)

sheild()
t.done()