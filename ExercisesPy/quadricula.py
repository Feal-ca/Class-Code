from yogi import read
import turtle

n=read(int)
m=read(int)
turtle.ht()
turtle.speed(100)
for i in range(n+1):
    turtle.pendown()
    turtle.forward(n*m)
    turtle.penup()
    turtle.left(180)
    turtle.forward(n*m)
    turtle.right(90)
    turtle.forward(m)
    turtle.right(90)
turtle.right(90)
turtle.forward(m)
for i in range(n+1):
    turtle.pendown()
    turtle.forward(n*m)
    turtle.penup()
    turtle.left(180)
    turtle.forward(n*m)
    turtle.right(90)
    turtle.forward(m)
    turtle.right(90)

turtle.done()