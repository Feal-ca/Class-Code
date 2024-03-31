from yogi import read

from yogi import read
from typing import TypeAlias


class Point:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y


Skyline: TypeAlias = list[Point]


def read_skyline() -> Skyline:
    return [Point(read(int), read(int)) for _ in range(read(int))]


def print_skyline(s: Skyline) -> None:
    print(len(s), end="")
    for p in s:
        print("", p.x, p.y, end="")
    print()


def skyline_superposition(a: Skyline, b: Skyline) -> Skyline:
    result = []
    h1, h2 = 0, 0
    i, j = 0, 0

    while i < len(a) and j < len(b):
        if a[i].x < b[j].x:
            x, h1 = a[i].x, a[i].y
            i += 1

        elif a[i].x > b[j].x:
            x, h2 = b[j].x, b[j].y
            j += 1

        else:
            x, h1 = a[i].x, a[i].y
            h2 = b[j].y
            i += 1
            j += 1

        height = max(h1, h2)

        if not result or height != result[-1].y:
            result.append(Point(x, height))

    return result + b[j::] + a[i::]


def main() -> None:
    for _ in range(read(int)):
        s1 = read_skyline()
        s2 = read_skyline()
        ss = skyline_superposition(s1, s2)
        print_skyline(ss)


main()
