from yogi import read, tokens
from typing import Optional
from math import sqrt
from functools import cmp_to_key

class Point:
    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self. y = y

    def distance(self, p: Optional["Point"]) -> float:
        dx, dy = self.x, self.y
        if p is not None:
            dx -= p.x
            dy -= p.y
        return sqrt(dx * dx + dy * dy)
    
def ordena_punts_x(p1: Point, p2: Point) -> int:
    if p1.x != p2.x:
        return int(p1.x - p2.x)
    return int(p1.y - p2.y)

def ordena_punts_y(p1: Point, p2: Point) -> int:

    if p1.y != p2.y:
        return int(p1.y - p2.y)
    return int(p1.x - p2.x)

def find_strip(p: list[Point], left:int, right: int, d: float) -> list[Point]:
    mid = (left + right) // 2
    pmid = p[mid].x
    return [p[i] for i in range(left, right + 1) if abs(p[i].x - pmid) < d]

def dist_in_middle(s: list[Point], d: float) -> float:
    s.sort(key=cmp_to_key(ordena_punts_y))
    for i in range(len(s)):
        for j in range(i + 1, len(s)):
            if abs(s[i].y - s[j].y) > d:
                break
            dist = s[i].distance(s[j])
            if dist< d:
                d = dist
    return d


def closest_distance_rec(p: list[Point], left: int, right: int) -> float:
    dist = float("inf")
    if left < right:
        mid = (left + right) // 2
        dist = min(closest_distance_rec(p, left, mid), 
                   closest_distance_rec(p, mid + 1, right))

        s = [p[i] for i in range(left, right + 1) if abs(p[i].x - p[mid].x) < dist]

        # distm = dist_in_middle(s, dist)
        d = dist
        s.sort(key=cmp_to_key(ordena_punts_y))
        for i in range(len(s)):
            for j in range(i + 1, len(s)):
                if abs(s[i].y - s[j].y) > d:
                    break
                dist = s[i].distance(s[j])
                if dist< d:
                    d = dist

        dist = (min(dist, d))
    return dist

def closest_distance(p: list[Point]) -> float:
    p.sort(key=cmp_to_key(ordena_punts_x))
    return closest_distance_rec(p, 0, len(p)-1)

def main() -> None:
    points= [Point(p_x, read(float)) for p_x in tokens(float)]
    print(f"{closest_distance(points):.5f}")

main()
