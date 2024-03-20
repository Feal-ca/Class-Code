from yogi import read
import turtle

n = read(int)
s = read(float)
a = read(float)
turtle.speed(0)
turtle.pensize(2)


def tree(n, s, r, g, b):
    if n > 0:
        r = r % 256
        g = g % 256
        b = b % 256

        turtle.color("#%02x%02x%02x" % (r, g, b))
        turtle.right(a)
        turtle.forward(s)
        tree(n - 1, (3 / 4) * s, r + 50, g, b)
        turtle.penup()
        turtle.backward(s)
        turtle.pendown()

        turtle.left(a)
        turtle.forward(s)
        tree(n - 1, (3 / 4) * s, r, g + 50, b)
        turtle.penup()
        turtle.backward(s)
        turtle.pendown()

        turtle.left(a)
        turtle.forward(s)
        tree(n - 1, (3 / 4) * s, r, g, b + 50)
        turtle.penup()
        turtle.backward(s)
        turtle.pendown()

        turtle.right(a)


turtle.left(90)
turtle.forward(2 * s)
(
    r,
    g,
    b,
) = 0, 0, 0
tree(n - 1, (3 / 4) * s, r, g, b)
turtle.done()
