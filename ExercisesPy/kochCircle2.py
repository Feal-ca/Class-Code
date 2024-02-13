from yogi import read
from turtle import *

def draw_koch(s: float, n: int, x: float, y: float) -> None:
    """
    Dibuja el fractal de Koch tamaño (s) de grado (n)
    """
    if n > 0:
        penup()
        goto(x,y)
        pendown()
        
        circle(s)
        
        draw_koch(s/2, n-1, x, y-s)
        draw_koch(s/2, n-1, x+(3/2)*s, y+(1/2)*s)
        draw_koch(s/2, n-1, x, y+2*s)
        draw_koch(s/2, n-1, x-(3/2)*s, y+(1/2)*s)

if __name__ == "__main__":
    s = read(float)
    n = read(int)
    speed(0)
    draw_koch(s,n,0,-s)

    done()
