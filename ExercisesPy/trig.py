from yogi import read
from math import sin, cos, radians

while True:
    a = read(float)

    print("{:.6f}".format(sin(radians(a))),"{:.6f}".format(cos(radians(a))))