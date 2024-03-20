from yogi import read
import turtle as tl

def draw_square(s: int):
    """
    Dibuixa per pantalla un cuadrat de mida (s)
    """
    for i in range(4):
        tl.forward(s)
        tl.left(90)
    
def draw_fractal(m: int, n: int)-> None:
    """
    Dibuixa el 'fractal del poder' de mida (m) i de (n)  per pantalla 
    """
    """
    Fa una volta capa (sense pintar) mes del
    necesari, por como esta la recursion
    """
    if n > 0:

        draw_square(m)

        # Cuadrat 1
        tl.penup()
        tl.backward(2*(m/3))
        tl.left(90)
        tl.backward(2*(m/3))
        tl.right(90)
        tl.pendown()

        draw_fractal(m/3,n-1)

        # Cuadrat 2
        tl.penup()
        tl.forward(2*m)
        tl.pendown()
        
        draw_fractal(m/3,n-1)
        
        # Cuadrat 3
        tl.penup()
        tl.left(90)
        tl.forward(2*m)
        tl.right(90)
        tl.pendown()
        
        draw_fractal(m/3,n-1)
        
        # Cuadrat 4
        tl.penup()
        tl.backward(2*m)
        tl.pendown()
        
        draw_fractal(m/3,n-1)

        # Reposicionar
        tl.penup()
        tl.forward(2*(m/3))
        tl.right(90)
        tl.forward(4*(m/3))
        tl.left(90)
        tl.pendown()
        
if __name__ == "__main__":
    m = read(int)
    n = read(int)
    
    tl.speed(0)
    tl.hideturtle()
    
    tl.backward(m//6) # centrar el dibuix

    draw_fractal(m/3,n)

    tl.done()
