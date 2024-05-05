from yogi import read, tokens
from collections import deque


def read_map(n: int, m: int) -> list[list[str]]:
    return [
        ["X" for _ in range(m + 2)]
        if j == 0 or j == n + 1
        else [c for c in "X" + read(str) + "X"]
        for j in range(n + 2)
    ]


def neighbours(x, y):
    return [
        (x + i, y + j)
        for i in range(-1, 2)
        for j in range(-1, 2)
        if (i * j == 0 and (i != 0 or j != 0))
    ]


def bfs(map, x, y):
    queue = deque([(x, y, 0)])

    while queue:
        x, y, d = queue.popleft()
        c = map[x][y]
        """
        map[x][y] = "O"
        print()
        for line in map:
            print(line)
        print(x, y)
        """
        map[x][y] = "X"
        if c == "t":
            return d

        for x1, y1 in neighbours(x, y):
            if map[x1][y1] != "X":
                queue.append((x1, y1, d + 1))

    return -1


def main():
    n, m = read(int), read(int)
    map = read_map(n, m)
    x, y = read(int), read(int)
    s = bfs(map, x, y)

    if s != -1:
        print(f"minimum distance: {s}")
    else:
        print("no treasure can be reached")


if __name__ == "__main__":
    main()
