import turtle
import random

DIS=float(input("Size?  "))

turtle.speed(1000)

while True:
    w = random.randint(1,10)
    ang = random.randint(1,360) 

    color = hex(random.randint(1118481,16777216))
    turtle.width(11-w)
    turtle.color("#"+color[2:].upper())

    turtle.forward(DIS*w)
    turtle.right(ang)
    
turtle.done()