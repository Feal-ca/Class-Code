from yogi import read
import turtle
turtle.ht()
shp=read(str)
a = read(int)

if shp=="rectangle":
    b = read(int)
    turtle.forward(a)
    turtle.left(90)
    turtle.forward(b)
    turtle.left(90)
    turtle.forward(a)
    turtle.left(90)
    turtle.forward(b)
    turtle.left(90)

if shp=="cercle":
    turtle.circle(a)
if shp=="quadrat":
    for i in range(4):
        turtle.forward(a)
        turtle.left(90)

turtle.done()