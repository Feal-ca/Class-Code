from yogi import read, tokens


def read_map(n: int, m: int) -> list[list[str]]:
    return [
        ["X" for _ in range(m + 2)]
        if j == 0 or j == n + 1
        else [c for c in "X" + read(str) + "X"]
        for j in range(n + 2)
    ]


def dfs(map: list[list[str]], x: int, y: int) -> bool:
    c = map[x][y]
    if c == "t":
        return True

    map[x][y] = "X"

    return any(
        dfs(map, x - i, y - j)
        for i in range(-1, 2)
        for j in range(-1, 2)
        if (i * j == 0 and (i != 0 or j != 0)) and map[x - i][y - j] != "X"
    )


def main():
    n, m = read(int), read(int)
    map = read_map(n, m)
    x, y = read(int), read(int)

    if dfs(map, x, y):
        print("yes")
    else:
        print("no")


if __name__ == "__main__":
    main()
