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
    print(len(s), end='')
    for p in s:
        print('', p.x, p.y, end='')
    print()


def skyline_superposition(a: Skyline, b: Skyline) -> Skyline:
    ...


def main() -> None:
    for _ in range(read(int)):
        s1 = read_skyline()
        s2 = read_skyline()
        ss = skyline_superposition(s1, s2)
        print_skyline(ss)


main()
