from yogi import read, tokens
from math import sqrt


class Point:
    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    def distance(self, p: "Point") -> float:
        return sqrt((self.x - p.x) ** 2 + (self.y - p.y) ** 2)

def closest(xs, ys, l, r) -> float:
    minim = float("inf")

    if l < r:
        m = (r + l) // 2

        left = closest(xs, [y for y in ys if (xs[l].x <= y.x <= xs[m].x)], l, m)
        right = closest(xs, [y for y in ys if (xs[m + 1].x <= y.x <= xs[r].x)], m + 1, r)

        d = min(left, right)

        band = [p for p in ys if abs(p.x - xs[m].x) <= d]

        minim = d

        for i in range(len(band)):
            for j in range(i + 1, min(i + 8, len(band))):
                if (band[j].y - band[i].y) < d:
                    minim = min(minim, band[i].distance(band[j]))

    return minim


def main():
    ps: list[Point] = [Point(p, read(float)) for p in tokens(float)]
    
    sorted_x = sorted(ps, key=lambda p: (p.x, p.y))
    sorted_y = sorted(ps, key=lambda p: (p.y, p.x))

    d = closest(sorted_x, sorted_y, 0, len(sorted_x) - 1)
    print(f"{d:.5f}")


if __name__ == "__main__":
    main()
