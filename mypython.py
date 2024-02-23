import turtle


turtle.color("blue")


def back(len):
    turtle.penup()
    turtle.backward(len)
    turtle.pendown()


"""
def triangle(size):
    for i in range(3):
        turtle.forward(size)
        turtle.left(120)
"""


def spiral(num_turns, init_length, increment, sides=5):
    # Iterate over the number of turns to draw the spiral
    for a in range(num_turns):
        # draw a polygon with 5 sides
        polygon(sides, init_length)
        init_length += increment


def polygon(sides, length):
    if (sides < 3):
        print("Error! You have to have at least 3 sides.")
        return

    angle = 360/sides
    for i in range(sides):
        turtle.forward(length)
        turtle.left(angle)


spiral(10, 50, 10)
back(500)
turtle.hideturtle()
turtle.done()

polygon(3, 50)
back(200)
polygon(2, 200)
back(50)
