import turtle
from yogi import read

n = read(int)
s = read(float)

turtle.speed(0)
def square(size):
    for i in range(4):
        turtle.forward(size)
        turtle.left(90)

def three_squares(n,s):
    if n != 0:
        turtle.backward(s)
        turtle.right(90)
        turtle.forward(s)
        turtle.left(90)
        square(s)
        three_squares(n-1, s/2)

        turtle.penup()
        turtle.left(90)
        turtle.forward(3*s)
        turtle.right(90)
        turtle.pendown()
        square(s)
        three_squares(n-1, s/2)

        turtle.penup()
        turtle.forward(3*s)
        turtle.pendown()
        square(s)
        three_squares(n-1,s/2)

        turtle.penup()
        turtle.backward(2*s)
        turtle.right(90)
        turtle.forward(2*s)
        turtle.left(90)
        turtle.pendown()


turtle.backward(s/2)
square(s)
three_squares(n-1, s/2)

turtle.done()