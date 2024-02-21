import random
import turtle

t = turtle.Turtle()

size = 50
t.forward(size)
t.left(120)
t.forward(size)
t.left(120)
t.forward(size)
t.left(120)
for _ in range(4):
    sizeF = 200
    sizeR = 90
    t.color("blue")
    t.forward(sizeF)
    t.right(sizeR)

turtle.done()


print("Hello World")

x = "awesome"


def myfunc():
    x = "fantastic"
    print("Python is " + x)


myfunc()
print("Python is " + x)
print(type(x))

print(random.randrange(1, 10))
