from yogi import read
import turtle

n=read(int)
m=read(int)

turtle.ht()
turtle.speed(100)

for i in range(n):
    turtle.forward(m*(i+1))
    turtle.left(90)
    turtle.forward(m*(i+1))
    turtle.left(90)

turtle.done()