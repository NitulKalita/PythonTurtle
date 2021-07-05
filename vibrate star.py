import turtle as t
import random

t.speed('fastest')

def draw(n, x, angle):
	for i in range(n):
		t.colormode(255)
		a = random.randint(0, 255)
		b = random.randint(0, 255)
		c = random.randint(0, 255)
		t.pencolor(a, b, c)
		t.fillcolor(a, b, c)
		t.begin_fill()
		for j in range(5):
			t.forward(5 * n-5 * i)
			t.right(x)
			t.forward(5 * n-5 * i)
			t.right(72 - x)
		t.end_fill()
		t.rt(angle)
n = 30
x = 144
angle = 18

draw(n, x, angle)
t.done()