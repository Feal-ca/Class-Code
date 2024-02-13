from yogi import read
from math import pi
n = read(int)

for case in range(n):
    shp=read(str)
    a = read(float)

    if shp=="rectangle":
        b = read(float)
        print("{:.6f}".format(a*b))
    if shp=="circle":
        print("{:.6f}".format(pi*a*a))