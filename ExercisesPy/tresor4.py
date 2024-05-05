from yogi import read, tokens
from collections import deque


def read_map(n: int, m: int) -> list[list[str]]:
    return [
        [*"X" * (m + 2)] if j == 0 or j == n +
        1 else ["X"] + [*read(str)] + ["X"]
        for j in range(n + 2)
    ]


def neighbours(x, y):
    return [(x + i, y + j) for i, j in [(-1, 0), (1, 0), (0, -1), (0, 1)]]


def bfs(map, x, y):
    queue = deque([(x, y, 0)])
    visited = [[False for _ in range(len(map[0]) + 2)]
               for _ in range(len(map) + 2)]
    final = -1

    while queue:
        x, y, d = queue.popleft()
        c = map[x][y]

        if c == "t":
            final = d

        for x1, y1 in neighbours(x, y):
            if not visited[x1][y1] and map[x1][y1] != "X":
                visited[x1][y1] = True
                queue.append((x1, y1, d + 1))

    return final


def main():
    n, m = read(int), read(int)
    map = read_map(n, m)
    x, y = read(int), read(int)
    s = bfs(map, x, y)

    if s != -1:
        print(f"maximum distance: {s}")
    else:
        print("no treasure can be reached")


if __name__ == "__main__":
    main()
