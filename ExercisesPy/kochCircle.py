import turtle
from yogi import read

n = read(int)
s = read(float)

turtle.speed(0)

def four_circles(n,s):
    if n != 0:
        turtle.right(90)
        turtle.penup()
        turtle.forward(2*s)
        turtle.pendown()
        turtle.left(90)

        turtle.circle(s)
        four_circles(n-1,s/2)

        turtle.left(90)
        turtle.penup()
        turtle.forward(3*s)
        turtle.right(90)
        turtle.forward(3*s)
        turtle.pendown()

        turtle.circle(s)
        four_circles(n-1,s/2)

        turtle.left(90)
        turtle.penup()
        turtle.forward(3*s)
        turtle.left(90)
        turtle.forward(3*s)
        turtle.pendown()
        turtle.right(180)

        turtle.circle(s)
        four_circles(n-1,s/2)

        turtle.left(180)
        turtle.penup()
        turtle.forward(3*s)
        turtle.left(90)
        turtle.forward(3*s)
        turtle.pendown()
        turtle.left(90)

        turtle.circle(s)
        four_circles(n-1,s/2)

        turtle.penup()
        turtle.forward(3*s)
        turtle.right(90)
        turtle.forward(1*s)
        turtle.left(90)

turtle.right(90)
turtle.penup()
turtle.forward(s)
turtle.pendown()
turtle.left(90)
turtle.circle(s)

four_circles(n-1,s/2)

turtle.done()