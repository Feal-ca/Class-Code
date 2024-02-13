from yogi import tokens, read
from dataclasses import dataclass
from typing import Optional


@dataclass
class Puzzle:
    letters: list[list[str]]
    points: list[list[int]]


@dataclass
class Word:
    name: str
    points: int


def horitzontally(p: Puzzle, w: Word, i: int, j: int) -> bool:
    c = len(p.letters[0])
    n = len(w.name)

    if c < j+n:
        return False
    else:
        for k in range(n):
            if w.name[k] != p.letters[i][j+k]:
                return False
        return True


def vertically(p: Puzzle, w: Word, i: int, j: int) -> bool:
    c = len(p.letters[0])
    n = len(w.name)

    if c < i+n:
        return False
    else:
        for k in range(n):
            if w.name[k] != p.letters[i+k][j]:
                return False
        return True


def valid_position(p: Puzzle, w: Word, i: int, j: int) -> bool:
    c = len(p.letters[0])
    n = len(w.name)
    v_points = 0
    h_points = 0

    if c < i+n:
        return False
    else:
        for k in range(n):
            if w.name[k] != p.letters[i+k][j]:
                return False
        return True


def award_points(p: Puzzle, w: list[Word]) -> None:
    r = len(p.letters)
    c = len(p.letters[0])

    for i in range(r):
        for j in range(c):
            if vertically(p, w)


def main() -> None:
    for r in tokens(int):
        c = read(int)
        puzzle = Puzzle(letters=[[read(str)
                        for _ in range(c)]for _ in range(r)]), points = [[read(int) for _ in range(c)]for _ in range(r)])


    n= read(int)
    words: list[Word]= [Word(read(str), -1) for _ in range(n)]
    award_points(puzzle, words)

    for w in words:
        if w.points == -1:
            print("no")
        else:
            print(w.points)

if __name__ == "__main__":
    main()
