import turtle
from yogi import read

a = read(int)
b = read(int)
turtle.speed(100)
turtle.ht()

#circle
turtle.right(90)
turtle.penup()
turtle.forward(200)
turtle.left(90)
turtle.pendown()
turtle.circle(200)
turtle.left(90)
turtle.penup()

#rallas
turtle.forward(200)
turtle.right(90)
for i in range(12):
    turtle.forward(150)
    turtle.pendown()
    turtle.forward(50)
    turtle.penup()
    turtle.right(180)
    turtle.forward(200)
    turtle.right(180)

    turtle.right(360/12)

turtle.left(90)

# Minutos
turtle.right((b/60)*360)
turtle.pendown()
turtle.forward(140)

turtle.right(150)
turtle.forward(25)
turtle.right(120)
turtle.forward(25)
turtle.right(120)
turtle.forward(25)
turtle.right(150)

turtle.forward(140)
turtle.left((b/60)*360+180)


# Horas

turtle.right((a*30)+(b/60)*30)
turtle.forward(90)

turtle.right(150)
turtle.forward(25)
turtle.right(120)
turtle.forward(25)
turtle.right(120)
turtle.forward(25)
turtle.right(150)

turtle.done()