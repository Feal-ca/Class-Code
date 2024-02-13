from yogi import read
import turtle


def kochLine(n: int, s: int):
    if n==1:
        turtle.forward(s)
        turtle.left(60)

        turtle.forward(s)
        turtle.right(120)

        turtle.forward(s)
        turtle.left(60)

        turtle.forward(s)

    if n>0:
        kochLine(n-1,s/3)
        turtle.left(60)
        kochLine(n-1,s/3)
        turtle.right(120)
        kochLine(n-1,s/3)
        turtle.left(60)
        kochLine(n-1,s/3)

def KochSnow(n,s):
    for i in range(3):
        kochLine(n,s)
        turtle.right(120)

n = read(int)
s = read(int)

turtle.speed(0)

KochSnow(n,s)

turtle.done()
