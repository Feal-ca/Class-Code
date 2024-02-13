from yogi import read, tokens
from dataclasses import dataclass
from functools import cmp_to_key


@dataclass
class Rectangle:
    width: int
    height: int
    # area: float
    # perimeter: int


def compare(r1: Rectangle, r2: Rectangle) -> int:
    a1 = r1.width * r1.height
    a2 = r2.width * r2.height
    if a1 != a2:
        return a1 - a2

    p1 = r1.width + r1.height
    p2 = r2.width + r2.height
    if p1 != p2:
        return p2 - p1

    return r1.width - r2.width


def show(rects: list[Rectangle]) -> None:
    for r in rects:
        print(r.width, end=" ")
        print(r.height)
    print("----------")


def main():
    for n in tokens(int):
        rectangles = [Rectangle(read(int), read(int)) for _ in range(n)]

        show(sorted(rectangles, key=cmp_to_key(compare)))


if __name__ == "__main__":
    main()
