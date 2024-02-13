from yogi import read, tokens
from math import sqrt, cbrt

solution = ""
no = True


def fermat1(a: int, b: int, c: int, d: int) -> str:
    for x in range(a, b + 1):
        for y in range(c, d + 1):
            if cbrt((x**3) + (y**3)) == int(cbrt((x**3) + (y**3))):
                z = int(cbrt((x**3) + (y**3)))
                return f"{x}^3 + {y}^3 = {z}^3"
    return ""


def fermat2(a: int, b: int, c: int, d: int) -> str:
    if a <= 0 and c <= 0:
        return "0^3 + 0^3 = 0^3"
    return ""


for a in tokens(int):
    b, c, d = read(int), read(int), read(int)
    if a <= 0 and c <= 0:
        print("0^3 + 0^3 = 0^3")
        no = False
        break
if no:
    print("No solution!")
