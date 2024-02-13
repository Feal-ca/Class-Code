from yogi import read
import turtle as tl

def sierpinskuy(s: float, n: int) -> None:
    """
    Dibuixa un triangle de sierpinsky de n nivells y costat de mida s
    """
    if n == 0:
        tl.forward(s)
        tl.left(120)
        tl.forward(s)
        tl.left(120)
        tl.forward(s)
        tl.left(120)

    else:
        sierpinskuy(s/2,n-1)
        tl.forward(s/2)
        
        sierpinskuy(s/2,n-1)

        tl.backward(s/2)
        tl.left(60)
        tl.forward(s/2)
        tl.right(60)

        sierpinskuy(s/2,n-1)
        tl.left(60)
        tl.bk(s/2)
        tl.right(60)

if __name__ == "__main__":
    tl.speed(0)

    s = read(float)
    n = read(int)

    sierpinskuy(s,n-1)

    tl.done()
